"""Merge a staging batch into the databases.

Parallel agents never write to databases/ directly. Each writes a batch folder:

    staging/<batch>/batch.yaml      agent: <run id>   research_unit: RU-0007
    staging/<batch>/<db>.jsonl      new records, no "id"; optional "key" for local references
    staging/<batch>/updates.jsonl   {"id": "CO-0003", "set": {"field": value}}

Inside a batch, reference another new record as "@key"; reference existing
records by their real id. The merge assigns ids, resolves "@key" references,
de-duplicates sources/entities/companies/terms/claims, applies fact-checks,
recomputes confidence, validates the whole result, and writes only if the
result is valid. Nothing is written on error.
"""
import difflib
import json
import shutil
from pathlib import Path

from . import db
from .rules import TIER_BY_TYPE, VERDICT_TO_STATUS, compute_confidence, normalize_text, normalize_url
from .validate import latest_checks, validate

NEAR_DUP_RATIO = 0.88


def _name_keys(r: dict, field: str) -> set:
    # normalize_text keeps only ASCII; a non-Latin name (e.g. 中微公司) would become ""
    # and match every other non-Latin name, so fall back to the casefolded original.
    keys = {normalize_text(x) or x.strip().casefold() for x in [r.get(field, "")] + r.get("aliases", []) if x}
    keys.discard("")
    return keys


def _find_existing(name: str, rec: dict, rows: list):
    if name == "sources":
        u = normalize_url(rec["url"])
        return next((r["id"] for r in rows if normalize_url(r["url"]) == u), None)
    field = {"entities": "name", "companies": "name", "regulations": "name", "glossary": "term"}.get(name)
    if field:
        keys = _name_keys(rec, field)
        return next((r["id"] for r in rows if keys & _name_keys(r, field)), None)
    if name == "claims":
        t = normalize_text(rec["claim"])
        return next((r["id"] for r in rows if normalize_text(r["claim"]) == t), None)
    return None


def _resolve(obj, keymap: dict, batch: str):
    if isinstance(obj, str) and obj.startswith("@"):
        if obj[1:] not in keymap:
            raise SystemExit(f"batch {batch}: unresolved reference {obj}")
        return keymap[obj[1:]]
    if isinstance(obj, list):
        return [_resolve(v, keymap, batch) for v in obj]
    if isinstance(obj, dict):
        return {k: _resolve(v, keymap, batch) for k, v in obj.items()}
    return obj


def _read_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    out = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{n}: invalid JSON: {e}")
    return out


def apply_fact_checks(dbs: dict) -> None:
    """Set claim status/verified_by/last_verified from the latest fact-check."""
    checks = latest_checks(dbs["fact_checks"])
    for c in dbs["claims"]:
        fc = checks.get(c["id"])
        if not fc:
            continue
        c["status"] = VERDICT_TO_STATUS[fc["verdict"]]
        if fc["verdict"] in ("verified", "partially_verified"):
            c["verified_by"], c["last_verified"] = fc["checker"], fc["checked_at"]


def recompute(dbs: dict) -> int:
    sources, changed = db.index(dbs["sources"]), 0
    for c in dbs["claims"]:
        conf, why = compute_confidence(c, sources)
        if (c.get("confidence"), c.get("confidence_reason")) != (conf, why):
            c["confidence"], c["confidence_reason"] = conf, why
            changed += 1
    return changed


def merge_batch(ind: Path, batch_dir: Path, dry_run: bool = False) -> dict:
    meta = db.load_yaml(batch_dir / "batch.yaml")
    batch = batch_dir.name
    agent = meta.get("agent")
    if not agent:
        raise SystemExit(f"batch {batch}: batch.yaml needs 'agent'")
    ru, today = meta.get("research_unit"), db.today()
    dbs = db.load_all(ind)
    existing_claims = list(dbs["claims"])
    keymap, stats = {}, {"batch": batch, "agent": agent, "research_unit": ru, "date": today,
                         "added": {}, "reused": {}, "near_duplicate_claims": 0}

    for name, (prefix, _) in db.DBS.items():
        for rec in _read_jsonl(batch_dir / f"{name}.jsonl"):
            key = rec.pop("key", None)
            if "id" in rec:
                raise SystemExit(f"batch {batch}: new {name} record must not carry an id: {rec['id']}")
            rec = _resolve(rec, keymap, batch)
            found = _find_existing(name, rec, dbs[name])
            if found:
                stats["reused"][name] = stats["reused"].get(name, 0) + 1
                if key:
                    keymap[key] = found
                continue
            rec["id"] = db.next_id(dbs[name], prefix)
            if name == "claims":
                rec.setdefault("recorded_by", agent)
                rec.setdefault("recorded_at", today)
                rec.setdefault("status", "unknown" if rec.get("claim_type") == "unknown" else "unverified")
                if ru:
                    rec.setdefault("research_unit", ru)
                rec.setdefault("confidence", "low")
                rec.setdefault("confidence_reason", "")
                t = normalize_text(rec["claim"])
                for old in existing_claims:
                    if difflib.SequenceMatcher(None, t, normalize_text(old["claim"])).ratio() >= NEAR_DUP_RATIO:
                        rec["duplicate_of"] = old["id"]
                        stats["near_duplicate_claims"] += 1
                        break
            elif name == "sources":
                rec.setdefault("access_date", today)
                if rec.get("source_type") in TIER_BY_TYPE:
                    rec.setdefault("tier", TIER_BY_TYPE[rec["source_type"]])
            elif name == "fact_checks":
                rec.setdefault("checker", agent)
                rec.setdefault("checked_at", today)
            elif name == "research_units":
                rec.setdefault("status", "queued")
                rec.setdefault("created_at", today)
            elif name == "contradictions":
                rec.setdefault("recorded_by", agent)
            if ru and name in ("sources", "entities", "companies", "regulations", "glossary", "interview_queue"):
                rec.setdefault("research_units", [])
                if ru not in rec["research_units"]:
                    rec["research_units"].append(ru)
            dbs[name].append(rec)
            stats["added"][name] = stats["added"].get(name, 0) + 1
            if key:
                keymap[key] = rec["id"]

    all_ids = {r["id"]: r for rows in dbs.values() for r in rows}
    for up in _read_jsonl(batch_dir / "updates.jsonl"):
        target = all_ids.get(up.get("id"))
        if not target:
            raise SystemExit(f"batch {batch}: update targets missing id {up.get('id')}")
        target.update(_resolve(up.get("set", {}), keymap, batch))
        stats["added"]["updates"] = stats["added"].get("updates", 0) + 1

    apply_fact_checks(dbs)
    recompute(dbs)
    errors, _ = validate(ind, dbs)
    if errors:
        raise SystemExit(f"batch {batch}: merge rejected, nothing written. {len(errors)} error(s):\n  "
                         + "\n  ".join(errors[:40]))
    if not dry_run:
        db.save_all(ind, dbs)
        log = ind / "logs" / "merges.jsonl"
        log.parent.mkdir(exist_ok=True)
        with log.open("a") as f:
            f.write(json.dumps(stats, sort_keys=True) + "\n")
        done = ind / "staging" / "_merged" / batch
        done.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(batch_dir), str(done))
    return stats

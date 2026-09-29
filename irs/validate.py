"""Validation: schemas, referential integrity, evidence rules, ontology conformance, atlas lint.

Errors block a merge; warnings are reported for humans.
"""
import json
import re
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from . import db
from .rules import EVIDENCED_TYPES, TIER_BY_TYPE, VERDICT_TO_STATUS, compute_confidence, normalize_url

_validators = {}


def validator(schema_name: str) -> Draft202012Validator:
    if schema_name not in _validators:
        schema = json.loads((db.SCHEMA_DIR / f"{schema_name}.schema.json").read_text())
        _validators[schema_name] = Draft202012Validator(schema)
    return _validators[schema_name]


def _walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk_strings(v)


def latest_checks(fact_checks: list) -> dict:
    """claim_id -> most recent fact-check (by date, then id)."""
    out = {}
    for fc in sorted(fact_checks, key=lambda f: (f["checked_at"], db.id_num(f["id"]))):
        out[fc["claim_id"]] = fc
    return out


def validate(ind: Path, dbs: dict = None) -> tuple:
    dbs = dbs if dbs is not None else db.load_all(ind)
    cfg = db.load_yaml(ind / "config.yaml")
    onto = db.load_yaml(ind / "ontology.yaml")
    errors, warnings = [], []
    ids = {name: db.index(rows) for name, rows in dbs.items()}

    # 1. schema + id format + uniqueness
    for name, rows in dbs.items():
        prefix, schema = db.DBS[name]
        seen = set()
        for r in rows:
            rid = r.get("id", "?")
            for e in validator(schema).iter_errors(r):
                errors.append(f"{name} {rid}: {'/'.join(map(str, e.path)) or '(record)'}: {e.message}")
            if not str(rid).startswith(prefix + "-"):
                errors.append(f"{name} {rid}: id must start with {prefix}-")
            if rid in seen:
                errors.append(f"{name} {rid}: duplicate id")
            seen.add(rid)

    # 2. referential integrity: any string that is exactly an ID must exist
    for name, rows in dbs.items():
        for r in rows:
            for s in _walk_strings({k: v for k, v in r.items() if k != "id"}):
                m = db.ID_RE.match(s)
                if m and m.group(1) in db.PREFIX_TO_DB and s not in ids[db.PREFIX_TO_DB[m.group(1)]]:
                    errors.append(f"{name} {r['id']}: references missing {s}")

    # 3. sources: tier derived from type; no duplicate URLs
    urls = {}
    for s in dbs["sources"]:
        want = TIER_BY_TYPE.get(s.get("source_type"))
        if want is not None and s.get("tier") != want:
            errors.append(f"sources {s['id']}: tier {s.get('tier')} but source_type {s['source_type']} is tier {want}")
        u = normalize_url(s.get("url", ""))
        if u in urls:
            errors.append(f"sources {s['id']}: same URL as {urls[u]}")
        urls[u] = s["id"]

    # 4. claims: evidence, verification independence, computed confidence
    checks = latest_checks(dbs["fact_checks"])
    for c in dbs["claims"]:
        cid = c["id"]
        if c.get("claim_type") in EVIDENCED_TYPES and c.get("status") not in ("unknown",):
            if not c.get("source_ids"):
                errors.append(f"claims {cid}: {c['claim_type']} needs at least one source")
            if not c.get("evidence", "").strip():
                errors.append(f"claims {cid}: evidence passage is empty")
        fc = checks.get(cid)
        if c.get("status") in ("verified", "partially_verified", "refuted", "unsupported", "outdated"):
            if not fc:
                errors.append(f"claims {cid}: status {c['status']} requires a fact-check record")
            elif VERDICT_TO_STATUS[fc["verdict"]] != c["status"]:
                errors.append(f"claims {cid}: status {c['status']} disagrees with latest fact-check {fc['id']} ({fc['verdict']})")
        if fc and fc["checker"] == c.get("recorded_by"):
            errors.append(f"claims {cid}: fact-checked by its own author ({fc['checker']}); needs an independent checker")
        if "status" in c and "claim_type" in c:
            conf, _ = compute_confidence(c, ids["sources"])
            if c.get("confidence") != conf:
                errors.append(f"claims {cid}: confidence '{c.get('confidence')}' but rules give '{conf}' (run `irs recompute`)")
        m = c.get("metric")
        if m and c.get("claim_type") != "unknown" and m.get("value") is None and "value_low" not in m:
            errors.append(f"claims {cid}: metric has no value or range")
        if m and "value_low" in m and "value_high" in m and m["value_low"] > m["value_high"]:
            errors.append(f"claims {cid}: metric value_low > value_high")
    for c in dbs["contradictions"]:
        if c.get("more_defensible") and c["more_defensible"] not in c.get("claim_ids", []):
            errors.append(f"contradictions {c['id']}: more_defensible must be one of its claim_ids")

    # 5. ontology conformance
    types = {t["id"] for t in onto.get("entity_types", [])}
    preds = {p["id"] for p in onto.get("predicates", [])}
    dims = {d["id"] for d in onto.get("dimensions", [])}
    for e in dbs["entities"]:
        if e.get("entity_type") not in types:
            errors.append(f"entities {e['id']}: entity_type '{e.get('entity_type')}' not in ontology.yaml")
    for c in dbs["companies"]:
        for role in c.get("roles", []):
            if role not in types:
                errors.append(f"companies {c['id']}: role '{role}' not in ontology.yaml")
    for r in dbs["regulations"]:
        for p in r.get("affected_participants", []):
            if p not in types:
                errors.append(f"regulations {r['id']}: affected participant '{p}' not in ontology.yaml")
    for r in dbs["relations"]:
        if r.get("predicate") not in preds:
            errors.append(f"relations {r['id']}: predicate '{r.get('predicate')}' not in ontology.yaml")
    for u in dbs["research_units"]:
        if u.get("dimension") not in dims:
            errors.append(f"research_units {u['id']}: dimension '{u.get('dimension')}' not in ontology.yaml")

    # 6. research tree has no dependency cycles
    errors += [f"research_units: dependency cycle {' -> '.join(c)}" for c in _cycles(dbs["research_units"])]

    # 7. opportunities use exactly the configured criteria
    crit = {c["id"] for c in cfg.get("scoring", {}).get("criteria", [])}
    for o in dbs["opportunities"]:
        if set(o.get("inputs", {})) != crit:
            errors.append(f"opportunities {o['id']}: inputs {sorted(o.get('inputs', {}))} != criteria {sorted(crit)}")

    # 8. warnings: staleness and unverified backlog
    stale_days = cfg.get("stale_after_days", 365)
    stale = [c["id"] for c in dbs["claims"] if c.get("last_verified")
             and (date.today() - date.fromisoformat(c["last_verified"])).days > stale_days]
    if stale:
        warnings.append(f"{len(stale)} claims last verified > {stale_days} days ago (e.g. {', '.join(stale[:5])})")
    unverified = sum(1 for c in dbs["claims"] if c.get("status") == "unverified")
    if unverified:
        warnings.append(f"{unverified} claims awaiting fact-check")

    e2, w2 = lint_atlas(ind, ids["claims"])
    return errors + e2, warnings + w2


def _cycles(units: list) -> list:
    graph = {u["id"]: u.get("depends_on", []) for u in units}
    state, found = {}, []

    def visit(n, path):
        if state.get(n) == 1:
            found.append(path[path.index(n):] + [n])
            return
        if state.get(n) == 2 or n not in graph:
            return
        state[n] = 1
        for d in graph[n]:
            visit(d, path + [n])
        state[n] = 2

    for n in graph:
        visit(n, [])
    return found


CITE_RE = re.compile(r"\[(CLM-\d{4,})\]")
NUMBER_RE = re.compile(r"(\$\s?\d|\d[\d,.]*\s?(%|percent|bn|billion|million|mn|trillion|tn|nm\b|wafers|units))", re.I)


def lint_atlas(ind: Path, claims: dict) -> tuple:
    """Narrative pages must cite claims as [CLM-0001]; numbers need a citation in the same paragraph."""
    errors, warnings = [], []
    atlas = ind / "atlas"
    if not atlas.exists():
        return errors, warnings
    for md in sorted(atlas.rglob("*.md")):
        if "databases" in md.relative_to(atlas).parts:
            continue  # generated pages
        rel = md.relative_to(ind)
        uncited = 0
        for para in re.split(r"\n\s*\n", md.read_text()):
            cites = CITE_RE.findall(para)
            for cid in cites:
                if cid not in claims:
                    errors.append(f"{rel}: cites missing claim {cid}")
                elif claims[cid]["status"] in ("refuted", "unsupported"):
                    errors.append(f"{rel}: cites {cid}, which failed fact-check ({claims[cid]['status']})")
            if not cites and NUMBER_RE.search(para) and not para.lstrip().startswith(("#", "|", "```")):
                uncited += 1
        if uncited:
            warnings.append(f"{rel}: {uncited} paragraph(s) contain figures without a [CLM-] citation")
    return errors, warnings

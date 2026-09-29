"""Read-only reports: status, research queue, saturation, coverage audit."""
import json
from collections import Counter
from pathlib import Path

from . import db

DONE = {"researched", "fact_checked", "done"}


def status(ind: Path) -> str:
    dbs = db.load_all(ind)
    lines = ["Records: " + ", ".join(f"{n}={len(r)}" for n, r in dbs.items() if r)]
    claims = dbs["claims"]
    if claims:
        lines.append("Claims by status: " + _fmt(Counter(c["status"] for c in claims)))
        lines.append("Claims by confidence: " + _fmt(Counter(c["confidence"] for c in claims)))
        lines.append("Claims by type: " + _fmt(Counter(c["claim_type"] for c in claims)))
    if dbs["sources"]:
        lines.append("Sources by tier: " + _fmt(Counter(f"tier{s['tier']}" for s in dbs["sources"])))
    rus = dbs["research_units"]
    if rus:
        lines.append("Research units by status: " + _fmt(Counter(u["status"] for u in rus)))
        lines.append("Research units by wave: " + _fmt(Counter(f"w{u['wave']}" for u in rus)))
    return "\n".join(lines)


def _fmt(c: Counter) -> str:
    return ", ".join(f"{k}={v}" for k, v in sorted(c.items()))


def next_units(ind: Path, n: int = 10) -> list:
    """Queued units whose dependencies are all researched, in wave/priority order."""
    rus = db.load_db(ind, "research_units")
    st = {u["id"]: u["status"] for u in rus}
    ready = [u for u in rus if u["status"] == "queued" and all(st.get(d) in DONE for d in u.get("depends_on", []))]
    ready.sort(key=lambda u: (u["wave"], u["priority"], db.id_num(u["id"])))
    return ready[:n]


def set_unit_status(ind: Path, unit_ids: list, new_status: str, note: str = None) -> None:
    rus = db.load_db(ind, "research_units")
    idx = db.index(rus)
    for uid in unit_ids:
        if uid not in idx:
            raise SystemExit(f"no research unit {uid}")
        idx[uid]["status"] = new_status
        if note:
            idx[uid]["status_note"] = note
    db.save_db(ind, "research_units", rus)


def saturation(ind: Path, last: int = 10) -> str:
    """How much of what recent batches found was already known. High duplicate share = diminishing returns."""
    log = ind / "logs" / "merges.jsonl"
    if not log.exists():
        return "No merges yet."
    rows = [json.loads(l) for l in log.read_text().splitlines() if l.strip()][-last:]
    out = ["batch | new claims | exact dup | near dup | dup share | new entities+companies"]
    tot_new = tot_dup = 0
    for r in rows:
        new = r["added"].get("claims", 0)
        exact = r["reused"].get("claims", 0)
        near = r.get("near_duplicate_claims", 0)
        dup = exact + near
        share = dup / (new + exact) if (new + exact) else 0
        ents = r["added"].get("entities", 0) + r["added"].get("companies", 0)
        out.append(f"{r['batch']} | {new} | {exact} | {near} | {share:.0%} | {ents}")
        tot_new, tot_dup = tot_new + new + exact, tot_dup + dup
    if tot_new:
        out.append(f"Duplicate share over last {len(rows)} batches: {tot_dup / tot_new:.0%}")
    return "\n".join(out)


def coverage(ind: Path) -> str:
    """Deterministic half of the quality audit: which dimensions and ontology types are thin."""
    dbs = db.load_all(ind)
    onto = db.load_yaml(ind / "ontology.yaml")
    ru_by_id = db.index(dbs["research_units"])
    out = ["dimension | units | done | claims | verified claims"]
    for d in onto.get("dimensions", []):
        units = [u for u in dbs["research_units"] if u["dimension"] == d["id"]]
        cl = [c for c in dbs["claims"] if ru_by_id.get(c["research_unit"], {}).get("dimension") == d["id"]]
        ver = sum(1 for c in cl if c["status"] in ("verified", "partially_verified"))
        flag = "  <-- no units" if not units else ("  <-- no claims yet" if not cl else "")
        out.append(f"{d['id']} | {len(units)} | {sum(u['status'] in DONE for u in units)} | {len(cl)} | {ver}{flag}")
    used = Counter(e["entity_type"] for e in dbs["entities"])
    for c in dbs["companies"]:
        used.update(c["roles"])
    parents = {t.get("parent") for t in onto.get("entity_types", [])}
    empty = [t["id"] for t in onto.get("entity_types", []) if not used[t["id"]] and t["id"] not in parents]
    out.append(f"Leaf ontology types with no entities/companies yet ({len(empty)}): {', '.join(empty) or 'none'}")
    linked = {r["subject_id"] for r in dbs["relations"]} | {r["object_id"] for r in dbs["relations"]}
    orphans = [e["id"] for e in dbs["entities"] + dbs["companies"] if e["id"] not in linked]
    out.append(f"Entities/companies with no graph relations: {len(orphans)}")
    open_int = sum(1 for i in dbs["interview_queue"] if i["status"] == "open")
    out.append(f"Open contradictions: {sum(1 for c in dbs['contradictions'] if c['status'] == 'open')}; "
               f"documented unknowns: {sum(1 for c in dbs['claims'] if c['status'] == 'unknown')}; "
               f"open interview questions: {open_int}")
    return "\n".join(out)

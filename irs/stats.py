"""Coverage, evidence-quality and saturation metrics (inputs to the stop condition)."""
from collections import Counter

from . import db


def compute(data, merge_log, ontology):
    c = data["claims"]
    live = [x for x in c if "duplicate_of" not in x]
    sources = {s["id"]: s for s in data["sources"]}
    out = {
        "counts": {k: len(v) for k, v in data.items()},
        "claim_status": dict(Counter(x["status"] for x in live)),
        "claim_confidence": dict(Counter(x["confidence"] for x in live)),
        "claim_type": dict(Counter(x["claim_type"] for x in live)),
        "source_tier": dict(Counter(s["tier"] for s in data["sources"])),
        "claims_citing_tier1": sum(1 for x in live if any(sources.get(s, {}).get("tier") == 1 for s in x.get("source_ids", []))),
        "live_claims": len(live),
        "open_contradictions": sum(1 for k in data["contradictions"] if k["status"] == "open"),
        "open_interview_items": sum(1 for i in data["interview_queue"] if i["status"] == "open"),
    }
    units = data["research_units"]
    by_dim = {}
    claims_by_ru = Counter(x["research_unit"] for x in live)
    for u in units:
        d = by_dim.setdefault(u["dimension"], {"units": 0, "done": 0, "claims": 0})
        d["units"] += 1
        d["done"] += u["status"] in ("fact_checked", "done")
        d["claims"] += claims_by_ru.get(u["id"], 0)
    for dim in (ontology or {}).get("dimensions", []):
        by_dim.setdefault(dim["id"], {"units": 0, "done": 0, "claims": 0})
    out["coverage_by_dimension"] = by_dim
    out["unit_status"] = dict(Counter(u["status"] for u in units))

    # saturation: per merge batch, share of new claims that duplicated existing ones,
    # and how many genuinely new entities/companies/terms/regulations appeared.
    sat = []
    for m in merge_log:
        new_claims = m["new"].get("claims", 0)
        novel = sum(m["new"].get(k, 0) for k in ("entities", "companies", "glossary", "regulations"))
        sat.append({"batch": m["batch"], "date": m["date"], "new_claims": new_claims,
                    "duplicate_rate": round(m["duplicate_claims"] / new_claims, 2) if new_claims else None,
                    "new_nodes": novel})
    out["saturation"] = sat
    return out


def run(slug, as_json=False):
    import json
    ind = db.industry_dir(slug)
    s = compute(db.load_all(ind), db.read_jsonl(ind / "databases" / "merge_log.jsonl"), db.load_ontology(ind))
    if as_json:
        print(json.dumps(s, indent=2))
        return 0
    print(f"# {slug} status\n")
    print("Records:", ", ".join(f"{k} {v}" for k, v in s["counts"].items() if v) or "none")
    print(f"Live claims: {s['live_claims']} | status {s['claim_status']} | confidence {s['claim_confidence']}")
    print(f"Claims citing a tier-1 source: {s['claims_citing_tier1']} | sources by tier {s['source_tier']}")
    print(f"Open contradictions: {s['open_contradictions']} | open interview items: {s['open_interview_items']}")
    print(f"Research units: {s['unit_status']}\n")
    print("| dimension | units | done | claims |\n|---|---|---|---|")
    for d, v in sorted(s["coverage_by_dimension"].items()):
        print(f"| {d} | {v['units']} | {v['done']} | {v['claims']} |")
    if s["saturation"]:
        print("\n| batch | new claims | duplicate rate | new nodes |\n|---|---|---|---|")
        for r in s["saturation"][-15:]:
            print(f"| {r['batch']} | {r['new_claims']} | {r['duplicate_rate']} | {r['new_nodes']} |")
    return 0

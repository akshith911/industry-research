"""Research queue: which units are ready, and status changes."""
from . import db

DONE = {"researched", "fact_checked", "done", "dropped"}
PRIORITY = {"P0": 0, "P1": 1, "P2": 2}


def ready(units):
    status = {u["id"]: u["status"] for u in units}
    out = [u for u in units if u["status"] == "queued" and all(status.get(d) in DONE for d in u.get("depends_on", []))]
    return sorted(out, key=lambda u: (u["wave"], PRIORITY[u["priority"]], db.id_sort_key(u["id"])))


def run_next(slug, n):
    units = db.load_all(db.industry_dir(slug))["research_units"]
    r = ready(units)
    for u in r[:n]:
        print(f"{u['id']}  w{u['wave']} {u['priority']}  [{u['dimension']}]  {u['title']}")
    print(f"\n{len(r)} ready of {sum(u['status'] == 'queued' for u in units)} queued")
    return 0


def run_set(slug, ids, status, note=None):
    ind = db.industry_dir(slug)
    data = db.load_all(ind)
    by_id = {u["id"]: u for u in data["research_units"]}
    for i in ids:
        if i not in by_id:
            raise SystemExit(f"unknown unit {i}")
        by_id[i]["status"] = status
        if note:
            by_id[i]["status_note"] = note
    db.save_all(ind, data)
    print(f"{len(ids)} unit(s) -> {status}")
    return 0

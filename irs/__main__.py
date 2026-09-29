"""Industry research system CLI.

    python -m irs init <slug> --name "Global semiconductor industry"
    python -m irs merge <slug> [batch ...] [--dry-run]   # all pending batches if none given
    python -m irs validate <slug>
    python -m irs recompute <slug>
    python -m irs status <slug>
    python -m irs next <slug> [-n 10]
    python -m irs set-status <slug> <status> RU-0001 [RU-0002 ...] [--note text]
    python -m irs saturation <slug>
    python -m irs coverage <slug>
    python -m irs score <slug>
    python -m irs build <slug>
    python -m irs diff <slug> <git-ref>
"""
import argparse
import shutil
import sys

from . import build as build_mod
from . import db, diff as diff_mod, merge as merge_mod, report, score as score_mod
from .validate import validate


def main(argv=None):
    ap = argparse.ArgumentParser(prog="irs", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("slug"); p.add_argument("--name", required=True)
    p = sub.add_parser("merge"); p.add_argument("slug"); p.add_argument("batches", nargs="*"); p.add_argument("--dry-run", action="store_true")
    for name in ("validate", "recompute", "status", "saturation", "coverage", "score", "build"):
        sub.add_parser(name).add_argument("slug")
    p = sub.add_parser("next"); p.add_argument("slug"); p.add_argument("-n", type=int, default=10)
    p = sub.add_parser("set-status"); p.add_argument("slug"); p.add_argument("status"); p.add_argument("units", nargs="+"); p.add_argument("--note")
    p = sub.add_parser("diff"); p.add_argument("slug"); p.add_argument("ref")
    a = ap.parse_args(argv)

    if a.cmd == "init":
        ind = db.INDUSTRIES / a.slug
        if ind.exists():
            sys.exit(f"{ind} already exists")
        for d in ("databases", "staging", "atlas", "logs", "phase0"):
            (ind / d).mkdir(parents=True)
        for name in db.DBS:
            (ind / "databases" / f"{name}.jsonl").touch()
        (ind / "staging" / ".gitkeep").touch()
        cfg = (db.ROOT / "templates" / "config.yaml").read_text()
        (ind / "config.yaml").write_text(cfg.replace("{{NAME}}", a.name).replace("{{SLUG}}", a.slug).replace("{{DATE}}", db.today()))
        shutil.copy(db.ROOT / "templates" / "ontology.yaml", ind / "ontology.yaml")
        print(f"created {ind.relative_to(db.ROOT)}")
        return

    ind = db.industry_dir(a.slug)
    if a.cmd == "merge":
        stage = ind / "staging"
        batches = [stage / b for b in a.batches] or sorted(
            d for d in stage.iterdir() if d.is_dir() and not d.name.startswith("_"))
        if not batches:
            print("no pending batches")
        for b in batches:
            s = merge_mod.merge_batch(ind, b, dry_run=a.dry_run)
            print(f"{'checked' if a.dry_run else 'merged'} {b.name}: added {s['added']} reused {s['reused']} "
                  f"near-duplicate claims {s['near_duplicate_claims']}")
    elif a.cmd == "validate":
        errors, warnings = validate(ind)
        for w in warnings:
            print("WARN ", w)
        for e in errors:
            print("ERROR", e)
        print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1 if errors else 0)
    elif a.cmd == "recompute":
        dbs = db.load_all(ind)
        merge_mod.apply_fact_checks(dbs)
        n = merge_mod.recompute(dbs)
        db.save_all(ind, dbs)
        print(f"updated confidence on {n} claim(s)")
    elif a.cmd == "status":
        print(report.status(ind))
    elif a.cmd == "next":
        for u in report.next_units(ind, a.n):
            print(f"{u['id']}  w{u['wave']} {u['priority']}  [{u['dimension']}]  {u['title']}")
    elif a.cmd == "set-status":
        report.set_unit_status(ind, a.units, a.status, a.note)
        errors, _ = validate(ind)
        if errors:
            sys.exit("\n".join(errors[:20]))
        print(f"{len(a.units)} unit(s) -> {a.status}")
    elif a.cmd == "saturation":
        print(report.saturation(ind))
    elif a.cmd == "coverage":
        print(report.coverage(ind))
    elif a.cmd == "score":
        md = score_mod.to_markdown(score_mod.score_all(ind))
        out = ind / "atlas" / "databases" / "opportunity-scores.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md)
        print(f"wrote {out.relative_to(db.ROOT)}")
    elif a.cmd == "build":
        for p in build_mod.build(ind):
            print(f"wrote {p.relative_to(db.ROOT)}")
    elif a.cmd == "diff":
        print(diff_mod.diff(ind, a.ref))


if __name__ == "__main__":
    main()

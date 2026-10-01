import json
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from irs import build, db, merge, report, score
from irs.validate import validate

ROOT = Path(__file__).resolve().parent.parent


def make_industry(tmp: Path) -> Path:
    ind = tmp / "ind"
    for d in ("databases", "staging", "atlas", "logs"):
        (ind / d).mkdir(parents=True)
    (ind / "config.yaml").write_text((ROOT / "templates/config.yaml").read_text())
    onto = yaml.safe_load((ROOT / "templates/ontology.yaml").read_text())
    onto["entity_types"] = [{"id": "foundry", "name": "Foundry", "description": "x"},
                            {"id": "regulator", "name": "Regulator", "description": "x"}]
    (ind / "ontology.yaml").write_text(yaml.safe_dump(onto))
    return ind


def write_batch(ind: Path, name: str, agent: str, files: dict, ru="RU-0001") -> Path:
    b = ind / "staging" / name
    b.mkdir(parents=True)
    (b / "batch.yaml").write_text(yaml.safe_dump({"agent": agent, "research_unit": ru}))
    for db_name, rows in files.items():
        (b / f"{db_name}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    return b


RU = {"key": "ru1", "title": "Definition", "dimension": "definition", "why_it_matters": "x",
      "questions": ["q"], "expected_outputs": ["claims"], "depends_on": [], "wave": 0,
      "priority": "P0", "origin": "planner"}
SRC = {"key": "s1", "url": "https://www.example.gov/report/?utm_source=x", "title": "Report", "publisher": "Gov",
       "publication_date": "2025", "source_type": "government", "tier": 1}
CLAIM = {"key": "c1", "claim": "The industry had revenue of 100 in 2025.", "claim_type": "fact",
         "source_ids": ["@s1"], "evidence": "Table 1: revenue 100", "entity_ids": []}


class IRSTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.ind = make_industry(self.tmp)
        merge.merge_batch(self.ind, write_batch(self.ind, "b0", "planner-1", {"research_units": [RU]}, ru=None))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_merge_assigns_ids_resolves_refs_and_dedupes_sources(self):
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [SRC], "claims": [CLAIM]}))
        dup = dict(SRC, url="https://example.gov/report")
        c2 = dict(CLAIM, claim="A different statement entirely about fabs.", key="c2")
        merge.merge_batch(self.ind, write_batch(self.ind, "b2", "res-2", {"sources": [dup], "claims": [c2]}))
        dbs = db.load_all(self.ind)
        self.assertEqual([s["id"] for s in dbs["sources"]], ["SRC-0001"])
        self.assertEqual(dbs["claims"][1]["source_ids"], ["SRC-0001"])
        self.assertEqual(dbs["claims"][0]["status"], "unverified")
        self.assertEqual(dbs["claims"][0]["confidence"], "low")
        self.assertEqual(validate(self.ind)[0], [])

    def test_exact_duplicate_claim_is_reused_not_added(self):
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [SRC], "claims": [CLAIM]}))
        merge.merge_batch(self.ind, write_batch(self.ind, "b2", "res-2", {"sources": [SRC], "claims": [CLAIM]}))
        self.assertEqual(len(db.load_db(self.ind, "claims")), 1)
        self.assertIn("100%", report.saturation(self.ind))

    def test_self_verification_is_rejected_and_nothing_written(self):
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [SRC], "claims": [CLAIM]}))
        fc = {"claim_id": "CLM-0001", "original_interpretation": "x", "evidence_found": "y", "verdict": "verified"}
        with self.assertRaises(SystemExit) as e:
            merge.merge_batch(self.ind, write_batch(self.ind, "b2", "res-1", {"fact_checks": [fc]}))
        self.assertIn("own author", str(e.exception))
        self.assertEqual(db.load_db(self.ind, "fact_checks"), [])
        self.assertTrue((self.ind / "staging" / "b2").exists())

    def test_independent_verification_sets_confidence_from_tier(self):
        rc = dict(CLAIM, key="c2", claim="Vendor says its tool is the fastest on the market.", claim_type="reported_claim")
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [SRC], "claims": [CLAIM, rc]}))
        fcs = [{"claim_id": c, "original_interpretation": "x", "evidence_found": "y", "verdict": "verified"}
               for c in ("CLM-0001", "CLM-0002")]
        merge.merge_batch(self.ind, write_batch(self.ind, "b2", "checker-1", {"fact_checks": fcs}))
        c = db.index(db.load_db(self.ind, "claims"))
        self.assertEqual((c["CLM-0001"]["status"], c["CLM-0001"]["confidence"]), ("verified", "high"))
        self.assertEqual(c["CLM-0002"]["confidence"], "medium")  # self-reported cap
        self.assertEqual(c["CLM-0001"]["verified_by"], "checker-1")

    def test_wrong_tier_rejected(self):
        bad = dict(SRC, source_type="blog")
        with self.assertRaises(SystemExit) as e:
            merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [bad]}))
        self.assertIn("tier", str(e.exception))

    def test_tier_derived_from_source_type_when_omitted(self):
        src = {k: v for k, v in SRC.items() if k != "tier"}
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [src], "claims": [CLAIM]}))
        self.assertEqual(db.load_db(self.ind, "sources")[0]["tier"], 1)

    def test_non_latin_names_do_not_collide(self):
        a = {"name": "北方华创", "entity_type": "foundry", "description": "x"}
        b = {"name": "中微公司", "entity_type": "foundry", "description": "y"}
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"entities": [a]}))
        merge.merge_batch(self.ind, write_batch(self.ind, "b2", "res-2", {"entities": [b, dict(a)]}))
        self.assertEqual([e["name"] for e in db.load_db(self.ind, "entities")], ["北方华创", "中微公司"])

    def test_fact_without_source_rejected(self):
        with self.assertRaises(SystemExit):
            merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"claims": [dict(CLAIM, source_ids=[])]}))

    def test_unresolved_reference_rejected(self):
        with self.assertRaises(SystemExit) as e:
            merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"claims": [CLAIM]}))
        self.assertIn("@s1", str(e.exception))

    def test_dependency_cycle_detected(self):
        ups = [{"id": "RU-0001", "set": {"depends_on": ["RU-0002"]}}]
        ru2 = dict(RU, key="ru2", depends_on=["RU-0001"])
        b = write_batch(self.ind, "b1", "gap-1", {"research_units": [ru2]}, ru=None)
        (b / "updates.jsonl").write_text(json.dumps(ups[0]) + "\n")
        with self.assertRaises(SystemExit) as e:
            merge.merge_batch(self.ind, b)
        self.assertIn("cycle", str(e.exception))

    def test_ontology_enforced(self):
        ent = {"name": "Widget", "entity_type": "not_a_type", "description": "x"}
        with self.assertRaises(SystemExit):
            merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"entities": [ent]}))

    def test_scoring_is_explicit_arithmetic(self):
        cfg = yaml.safe_load((self.ind / "config.yaml").read_text())
        cfg["scoring"]["criteria"] = [{"id": "a", "name": "A", "weight": 2},
                                      {"id": "b", "name": "B", "weight": 1, "direction": "lower_is_better"}]
        (self.ind / "config.yaml").write_text(yaml.safe_dump(cfg))
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [SRC], "claims": [CLAIM]}))
        opp = {"title": "T", "description": "d", "problem_claim_ids": ["CLM-0001"],
               "inputs": {"a": {"value": 4, "rationale": "r"}, "b": {"value": 1, "rationale": "r"}}}
        merge.merge_batch(self.ind, write_batch(self.ind, "b2", "res-2", {"opportunities": [opp]}))
        r = score.score_all(self.ind)[0]
        self.assertEqual(r["score"], round(100 * (2 * 4 + 1 * 4) / 15, 1))  # 80.0

    def test_atlas_lint(self):
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "res-1", {"sources": [SRC], "claims": [CLAIM]}))
        (self.ind / "atlas" / "page.md").write_text(
            "Revenue was 100 [CLM-0001].\n\nIt grew 12% last year.\n\nSee [CLM-0999].\n")
        errors, warnings = validate(self.ind)
        self.assertTrue(any("CLM-0999" in e for e in errors))
        self.assertTrue(any("1 paragraph" in w for w in warnings))

    def test_queue_respects_dependencies_and_build_runs(self):
        ru2 = dict(RU, key="ru2", title="Market size", depends_on=["RU-0001"], wave=1)
        merge.merge_batch(self.ind, write_batch(self.ind, "b1", "gap-1", {"research_units": [ru2]}, ru=None))
        self.assertEqual([u["id"] for u in report.next_units(self.ind)], ["RU-0001"])
        report.set_unit_status(self.ind, ["RU-0001"], "researched")
        self.assertEqual([u["id"] for u in report.next_units(self.ind)], ["RU-0002"])
        self.assertTrue(build.build(self.ind))


if __name__ == "__main__":
    unittest.main()

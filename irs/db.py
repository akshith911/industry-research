"""Storage layer: one JSONL file per database, one record per line, sorted by id.

JSONL keeps every record on its own line, so `git diff` shows exactly which
records changed between atlas versions.
"""
import json
import re
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schemas"
INDUSTRIES = ROOT / "industries"

# name -> (id prefix, schema file). Order matters: it is the merge order,
# so every database only references databases that come before it (or itself).
DBS = {
    "sources": ("SRC", "source"),
    "entities": ("ENT", "entity"),
    "companies": ("CO", "company"),
    "regulations": ("REG", "regulation"),
    "glossary": ("TRM", "glossary"),
    "research_units": ("RU", "research_unit"),
    "claims": ("CLM", "claim"),
    "relations": ("REL", "relation"),
    "contradictions": ("CON", "contradiction"),
    "fact_checks": ("FC", "fact_check"),
    "interview_queue": ("INT", "interview"),
    "opportunities": ("OPP", "opportunity"),
    "red_team": ("RT", "red_team"),
}
PREFIX_TO_DB = {p: name for name, (p, _) in DBS.items()}
ID_RE = re.compile(r"^([A-Z]+)-(\d{4,})$")


def today() -> str:
    return date.today().isoformat()


def industry_dir(slug: str) -> Path:
    d = INDUSTRIES / slug
    if not d.is_dir():
        raise SystemExit(f"unknown industry '{slug}' (no folder {d})")
    return d


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def load_db(ind: Path, name: str) -> list:
    path = ind / "databases" / f"{name}.jsonl"
    if not path.exists():
        return []
    rows = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{n}: invalid JSON: {e}")
    return rows


def load_all(ind: Path) -> dict:
    return {name: load_db(ind, name) for name in DBS}


def save_db(ind: Path, name: str, rows: list) -> None:
    path = ind / "databases" / f"{name}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda r: id_num(r["id"]))
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows))


def save_all(ind: Path, dbs: dict) -> None:
    for name, rows in dbs.items():
        save_db(ind, name, rows)


def id_num(rid: str) -> int:
    m = ID_RE.match(rid)
    return int(m.group(2)) if m else 0


def next_id(rows: list, prefix: str) -> str:
    n = max((id_num(r["id"]) for r in rows), default=0) + 1
    return f"{prefix}-{n:04d}"


def index(rows: list) -> dict:
    return {r["id"]: r for r in rows}

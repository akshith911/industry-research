# industry-research: operating rules

This repo is a reusable system for building evidence-linked Industry Knowledge Atlases. Methodology: `METHODOLOGY.md`. Entry point: the `/research-industry` skill (`.claude/skills/research-industry/SKILL.md`).

## Rules for every session

- **Data lives in `industries/<slug>/databases/*.jsonl`** and changes only through `python -m irs merge` of staging batches. Never hand-edit the JSONL, and never edit generated pages in `atlas/databases/`.
- **Evidence contract**: `.claude/skills/research-industry/references/evidence-and-staging.md`. No fabricated sources, URLs, numbers, company facts or quotes. Unknown is a valid answer.
- **Separation of duties**: whoever records a claim cannot verify it (enforced in code). The orchestrator does not research or write atlas prose.
- **Arithmetic, scoring, confidence, tiers, dedupe and validation are code** (`irs/`), never an LLM's judgment.
- `python -m irs validate <slug>` must pass before every commit. Run `python -m unittest discover -s tests -t .` after changing `irs/` or `schemas/`.
- Commit messages: `research(<slug>): ...` for research, `system: ...` for tooling/methodology. Bump `METHODOLOGY.md` version for methodology changes and note it in `CHANGELOG.md`.
- Git remote: `https://github.com/akshith911/industry-research.git`. Never use any other GitHub account.

## Setup

```
pip install -r requirements.txt
python -m unittest discover -s tests -t .
```

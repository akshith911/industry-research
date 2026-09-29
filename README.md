# industry-research

A reusable system for building **evidence-linked Industry Knowledge Atlases**: start from zero knowledge of an industry and end with a navigable, auditable knowledge base in which every claim traces to its source and has passed an independent check.

## Atlases

| Industry | Folder | Status |
|---|---|---|
| Global semiconductor industry | [`industries/semiconductors`](industries/semiconductors) | Phase 0 done (ontology, maps); Phase 1 (research tree) next |

## How it works

- **`/research-industry "<industry>"`** (Claude Code skill in `.claude/skills/research-industry/`) orchestrates parallel research agents: planner, researcher, fact-checker, contradiction-checker, gap-finder, synthesizer and red-team (`.claude/agents/`).
- Agents write **staging batches**; `python -m irs merge` validates them and merges them into JSONL databases (`industries/<slug>/databases/`). Rule checks, confidence, dedupe and scoring are done in code.
- `python -m irs build <slug>` generates the browsable database pages (claims ledger, companies, metrics, regulations, sources, glossary, contradictions, gaps, interview pack, research tree, graph).

Read [`METHODOLOGY.md`](METHODOLOGY.md) for the method and [`CLAUDE.md`](CLAUDE.md) for the operating rules.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -t .
python -m irs status semiconductors
python -m irs next semiconductors
```

Then in Claude Code, in this folder: `/research-industry continue semiconductors`.

## Running research locally (recommended for research waves)

Research waves need hundreds of web searches, so run them in Claude Code on your machine with the search cap raised and Chrome connected:

```bash
cd ~/Work/Factory/Biz/industry-research && git pull
source .venv/bin/activate
CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION=3000 claude --chrome
```
then type: `/research-industry continue semiconductors`

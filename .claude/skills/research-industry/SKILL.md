---
name: research-industry
description: Build or extend an evidence-linked Industry Knowledge Atlas for any industry, starting from zero knowledge, using parallel research agents, independent fact-checking, gap and contradiction analysis, and deterministic validation. Use for "/research-industry <industry>", "continue/update the <industry> atlas", or deep first-principles industry research.
---

# Research an industry (orchestrator)

You are the **orchestrator**. You plan, spawn agents, merge their batches, run the tooling and keep the user informed. You do **not** do the research or write atlas pages yourself, which keeps your context clean and the work independently checkable.

Read before starting: `references/evidence-and-staging.md` (the data contract), `references/quality-checklist.md` (stop condition). Agents read their own files in `.claude/agents/`.

## Invocation

| Command | Action |
|---|---|
| `/research-industry "<industry description>"` | New atlas: Phases 0→1, then checkpoint |
| `/research-industry continue <slug>` | Resume at the next incomplete phase or wave |
| `/research-industry update <slug>` | Refresh an existing atlas (Update mode below) |
| `/research-industry status <slug>` | Print `irs status`, `coverage`, `saturation`, `next` |

All tooling is `python -m irs <cmd> <slug>` from the repo root (`pip install -r requirements.txt` once).

## Spawning agents

Agent definitions live in `.claude/agents/<name>.md` (planner, researcher, fact-checker, contradiction-checker, gap-finder, synthesizer, red-team). If the Agent tool offers that subagent type, use it. Otherwise spawn `general-purpose` with a prompt whose **first line** is:
`First read .claude/agents/<name>.md and .claude/skills/research-industry/references/evidence-and-staging.md, and follow them exactly.`

Give every spawned agent a unique **run id** (`<role>-<RU or wave>-<4 random hex>`, e.g. `res-RU-0007-3f9a`) and the absolute repo path, slug, and its task. Launch independent agents **in parallel in a single message**. Use foreground agents; wait for all of them before merging.

After agents finish: `python -m irs merge <slug>` (merges every pending batch; a rejected batch prints errors and stays in staging, so send the errors back to a fresh agent of the same role to fix, max 2 tries, then set the unit `blocked` with a note).

## Search budget and browsers

Web search can be capped per session (cloud sessions: 200 searches, shared by all agents). Before a research wave, check how much budget the wave needs (~40–60 searches per unit). Run waves in Claude Code on the user's machine with `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` raised, or one wave per session. When WebSearch is exhausted or WebFetch cannot read a page (JavaScript pages, PDFs that come back empty, robots-blocked sites the user can open), agents may use the Chrome extension (`mcp__claude-in-chrome__*`): each agent opens its own tab, reads with `get_page_text`, closes its tab, and never solves CAPTCHAs, signs in or submits forms. Record the page URL as the source either way.

## Phase 0: Scope and discovery (evidence before structure)

1. Derive a slug (lowercase-hyphens). `python -m irs init <slug> --name "<name>"`. Fill `config.yaml` scope (definition, exclusions, geography, time horizon) from the request; if geography is unstated, choose global with regional breakdowns and say so.
2. Create the seed unit RU-0001 (dimension `definition`, "Discovery: what is this industry and who is in it") by writing a one-record batch yourself, then merge.
3. Spawn **4–6 discovery researchers in parallel**, each with a different lens on RU-0001: (a) definition, boundaries and segments, (b) value chain and participant types, (c) money flows and business models, (d) regulation and policy, (e) history and major structural shifts, (f) technology and information flows. Each proposes ontology entity types with evidence.
4. Merge. Spawn the **planner** (Phase 0 mode) to write `ontology.yaml` entity types and the Phase 0 maps in `phase0/`: `ontology.md`, `value-chain.md`, `money-flows.md`, `information-flows.md`, `regulatory-map.md`. Maps cite claims; unknown edges are marked unknown. Validate.

## Phase 1: Research tree

5. Spawn **planners** (Phase 1 mode) to write the research tree as `research_units` batches: 40–150 units covering every ontology dimension that applies, each with questions, subquestions, entities, named primary sources to try, dependencies and wave (wave 1 = foundations everything else depends on). For a large industry, run 4–6 planners **in parallel**, each owning a disjoint group of dimensions, with a shared brief in `phase0/phase1-brief.md`. Parallel planners may only depend on existing units. Merge, validate.
6. Spawn one **gap-finder** (plan-review mode) to critique the whole tree before any research budget is spent: it dedupes across planners, adds dependencies between new units, adds missing units, and writes `phase0/research-plan.md` (counts by wave/dimension/priority, search-volume estimate). Merge.
7. `python -m irs build <slug>`, commit (`research(<slug>): phase 0-1 plan`), and **stop for user review** of `atlas/databases/research-tree.md` and `phase0/` unless the user said to run unattended.

## Phase 2: Research waves (loop)

8. `python -m irs next <slug> -n <researchers_per_wave>`. Mark them `in_progress`. Spawn one **researcher** per unit, in parallel.
9. Merge. Mark successfully merged units `researched`.
10. Spawn **fact-checkers** in parallel over this wave's `unverified` claims (group ~25–40 claims per checker; a checker must never check claims recorded by its own run id). Merge (this applies verdicts and recomputes confidence).
11. Spawn one **contradiction-checker** for the wave's claims plus related earlier claims. Merge.
12. Spawn one **gap-finder** (wave mode). It proposes new units, including those researchers flagged. Merge.
13. Units whose claims are all checked → `fact_checked`. Commit (`research(<slug>): wave N`). Report to the user in 2–3 lines: units done, claims by confidence, new units added, saturation.
14. Repeat from 8 until the stop condition in `references/quality-checklist.md` holds. Record the stop rationale (with `irs saturation` output) in `atlas/00-overview/research-log.md`.

## Phase 3: Synthesis and audit

15. Plan atlas pages from `references/atlas-structure.md`, adapted to the industry. Spawn **synthesizers** in parallel, one per folder or page group. Each writes pages citing `[CLM-xxxx]` only.
16. `python -m irs build` and `validate` (zero errors; resolve uncited-figure warnings).
17. Spawn a **gap-finder** in audit mode (it did not write the pages) to run the judgment checklist. Failed checks become units → back to Phase 2.
18. Bump `atlas_version` in config.yaml, update `CHANGELOG.md`, commit, tag `atlas/<slug>/v<version>`.

## Phase 4: Opportunities (only if asked, only after the audit passes)

19. Spawn a **synthesizer** (opportunity mode) to propose opportunities grounded in evidenced problem claims, with a rating for every criterion in config.yaml and the claim ids behind each rating.
20. Spawn one **red-team** agent per opportunity (or major conclusion) in parallel; merge their `red_team` records.
21. `python -m irs score <slug>` computes scores; never state a score that the tool did not compute.

## Update mode

1. `python -m irs validate` → list stale claims (older than `stale_after_days`).
2. Spawn fact-checkers on stale claims (verdict `outdated` → a researcher records the current value as a new claim with `supersedes`).
3. Spawn researchers per dimension to scan for changes since the last `access_date`: new regulations, companies, funding, market numbers, business-model shifts. They record new claims and units.
4. Continue from Phase 2 step 10. `python -m irs diff <slug> atlas/<slug>/v<last>` produces the change report for CHANGELOG.md.

## Git

Commit after every merge phase or wave; never commit a failing `irs validate`. Messages: `research(<slug>): <what>`. Push only to the remote the user configured, as the user.

## Guardrails for you

- Never write claims, sources or atlas prose yourself; route through agents so authorship and checking stay separate.
- Never do arithmetic in prose: scores, totals and rates come from `irs`.
- Keep the user informed at each checkpoint with counts, not adjectives.
- If a tool (web fetch, browser) is unavailable or blocked, say so and record affected units as `blocked`, rather than lowering the evidence bar.

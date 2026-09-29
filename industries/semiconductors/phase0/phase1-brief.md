# Phase 1 brief (shared by parallel planners)

Build the research tree for the GLOBAL semiconductor industry. Several planners work in parallel, each owning a **disjoint set of dimensions**. Stay inside your dimensions; if you notice a gap elsewhere, mention it in your reply instead of creating the unit.

State: discovery (RU-0001) merged 571 unverified claims, 222 sources, 156 glossary terms, 14 contradictions and 21 interview items. Phase 0 produced `ontology.yaml` (101 entity types, 23 dimensions) and the maps in `phase0/` (ontology.md, value-chain.md, money-flows.md, information-flows.md, regulatory-map.md), each with its unknowns. There are also 138 entities, 39 regulations and 138 relations. 46 queued units already exist (RU-0002..RU-0047).

For your dimensions:
1. **Review the existing units** in `databases/research_units.jsonl` with those dimensions. Improve them via `updates.jsonl` (`{"id":"RU-00xx","set":{...}}`): sharpen questions and subquestions, name primary sources, fix dependencies, wave and priority. Merge duplicates by setting the weaker unit to `"status":"dropped"` with a `status_note` naming the unit that absorbs it.
2. **Add new units** (`research_units.jsonl`) so every leaf participant type, value-chain stage, major jurisdiction (US, China, Taiwan, South Korea, Japan, EU/Netherlands/Germany, India, Southeast Asia incl. Malaysia/Singapore/Vietnam, Israel where relevant), historical period and phase0 unknown that falls in your dimensions is covered. No opportunity-analysis units.
3. **Waves**: wave 1 = foundations others depend on; wave 2 = deep dives by segment, participant, jurisdiction or workflow; wave 3 = topics that need the rest first. `depends_on` may reference only EXISTING units (RU-0001..RU-0047). A consolidator will add links between new units afterwards, so name intended prerequisites in `open_questions` as "prereq: <title>".
4. **Each unit**:
   - `title`, and a `dimension` from your set.
   - `why_it_matters` in plain words; 3–8 questions, plus subquestions.
   - `entities` (names or ENT/REG ids).
   - SPECIFIC `primary_sources`: named regulators, filings, statistical series, association reports. Add "(to verify)" if you have not confirmed a source exists.
   - `secondary_sources`, `expected_outputs`, `depends_on`, `open_questions`, `wave`, `priority` (P0/P1/P2).
   - `origin` "planner", `status` "queued".
5. **Do not pad and do not compress.** Units should be researchable by one agent in one sitting (roughly 40–60 searches). Split anything bigger.
6. **Do NOT use WebSearch** (the session budget is exhausted). Work from the databases, the phase0 maps and your knowledge of where primary sources live.
7. **Validate** with `cd /home/claude/industry-research && python3 -m irs merge semiconductors <your batch> --dry-run` and fix all errors. Do not run a real merge.

Reply briefly:
- active unit counts by wave and priority
- units updated or dropped
- gaps you saw outside your scope

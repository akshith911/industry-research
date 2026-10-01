# RU-0043 res-RU-0043-0f1f notes
- Restart of crashed run res-RU-0043-aba9; every URL re-opened in this run (curl to SEC with UA, web_extract, or browser). Lead list used only for discovery.
- Companies: 50 rows of ECIA's 2024 worldwide top-50 authorized distributors enumerated (long tail recorded with ECIA type and HQ; native-script names in business_model text only), plus Mouser, Rochester and 8 chip makers. TI/NXP/onsemi/Infineon names match RU-0011 staging records so they will dedupe.
- metric_claim_ids were dropped from company records because the merge resolves @refs in file order (companies before claims); orchestrator may add them via a later updates.jsonl once ids exist.
- ECIA 2025 global table was read from a third-party PDF reprint (ecworld.ru, Electronics Sourcing North America Sept 2025) - fact-checkers should try to re-point to TrustedParts original.
- Infineon channel pie has no numbers; recorded as unknown, no estimate taken from the image.
- Not opened/failed: WT Microelectronics site (DNS/unreachable), Mouser/DigiKey/TTI (bot walls), DLA QSLD booklet (request rejected), TrustedParts worldwide table body (truncated text, images only).

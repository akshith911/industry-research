# Phase 0 discovery: core technology and information flows

Run `disc-tech-f8d1` · RU-0001 · 2026-09-29 · batch `staging/RU-0001-disc-tech-f8d1/` (not merged yet)

Everything here is backed by claims and glossary terms in the batch. Every claim is unverified until an independent fact-check. When a source is a company describing its own product, the claim is recorded as a `reported_claim`.

## 0. The picture in plain words

A chip (an integrated circuit) is a slice of silicon holding billions of tiny switches called transistors. Chips are made hundreds at a time on round silicon **wafers**. There are three stages:

1. **Design.** Engineers use EDA software and licensed IP blocks to go from a logic description (RTL) to a physical layout file (GDSII or OASIS). They follow the foundry's **PDK**, which is the rulebook and parts kit for one manufacturing process. The hand-off of the finished layout is called the **tape-out**.
2. **Front-end fabrication.** A mask shop turns the layout into a **mask set**, with one photomask per layer. In the fab, the wafer goes through the same loop of deposition, resist coating, lithography, etch and implant hundreds of times. That comes to 400–1,400 steps, up to about 100 layers, and a cycle time of about 12 weeks.
3. **Back-end (assembly, test and packaging).** Each chip is tested while still on the wafer (**wafer sort**). The wafer is then cut into individual **dies**, which are packaged and tested again (**final test**, sometimes followed by system-level test). **Yield** is the share of dies that work.

The name of a process node ("3 nm") is a **label for a generation of technology, not a measurement**. Intel said so itself in 2021 (`c_node_names`), and Mark Bohr said the same in 2013 (`c_bohr`).

## 1. Technology and product/process categories that should become ontology types

These are proposed as *technology/product* entity types. Participant types (foundry, fabless, IDM, OSAT, EDA vendor, IP vendor, mask shop, equipment maker, materials supplier, ATE maker, MES/YMS software vendor, standards body) come out of this lens too, but they should be reconciled with the value-chain discovery pass.

| Proposed type id | What it is | Parent | Evidence (source URLs) |
|---|---|---|---|
| `process_technology` | A named node or process, e.g. TSMC N2 or Samsung 3 nm GAA | technology | https://newsroom.intel.com/tech101/explaining-common-chip-terms ; https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm |
| `transistor_architecture` | Planar, FinFET or gate-all-around (nanosheet) | technology | https://news.samsung.com/global/samsung-begins-chip-production-using-3nm-process-technology-with-gaa-architecture ; https://download.intel.com/newsroom/2021/client-computing/accelerating-process-innovation.pdf |
| `lithography_technology` | i-line, KrF/ArF DUV, ArF immersion, EUV 0.33 NA, High-NA EUV 0.55 NA | technology | https://www.asml.com/en/products/euv-lithography-systems ; https://www.asml.com/en/products/duv-lithography-systems ; https://www.asml.com/en/news/stories/2024/5-things-high-na-euv |
| `process_step` | Deposition, lithography, etch, ion implantation, CMP, metrology/inspection | workflow | https://www.asml.com/en/news/stories/2021/semiconductor-manufacturing-process-steps |
| `packaging_technology` | 2.5D interposer (CoWoS), 3D stacking/hybrid bonding (SoIC), fan-out, glass substrates | technology | https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm ; https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/SoIC.htm ; https://www.imec-int.com/en/expertise/cmos-advanced/connect/3d-integration ; https://download.intel.com/newsroom/archive/2025/en-us-2023-09-18-intel-unveils-industryleading-glass-substrates-to-meet-demand-for-more-powerful-compute.pdf |
| `power_delivery_technology` | Backside power (PowerVia, Super Power Rail) | technology | https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A16 |
| `semiconductor_product_category` | WSTS taxonomy: discretes, optoelectronics, sensors/actuators, ICs (analog, micro, logic, memory, with subtypes DRAM, NAND, MPU, MCU …) | product | https://www.semiconductors.org/wp-content/uploads/2021/02/Product_Classification_2021.pdf |
| `memory_technology` | DRAM, HBM (stacked DRAM with TSVs), 3D NAND | product | https://news.skhynix.com/become-a-semiconductor-expert-with-sk-hynix-hbm/ ; https://news.skhynix.com/sk-hynix-starts-mass-production-of-world-first-321-high-nand/ |
| `substrate_material` | Silicon wafer sizes (200/300 mm), GaN, SiC | material | https://cset.georgetown.edu/wp-content/uploads/The-Semiconductor-Supply-Chain-Issue-Brief-1.pdf ; https://www.ieee-pels.org/magazine/infineon-reveals-first-300-mm-power-gan-wafers/ |
| `design_artifact` | RTL, netlist, layout (GDSII/OASIS), PDK, IP block, mask data, mask set | information | https://news.synopsys.com/2018-03-19-Synopsys-Introduces-Breakthrough-Fusion-Technology-to-Transform-the-RTL-to-GDSII-Flow ; https://github.com/google/skywater-pdk ; https://store-us.semi.org/products/p03900-semi-p39-specification-for-oasis%C2%AE-open-artwork-system-interchange-standard ; https://www.sec.gov/Archives/edgar/data/810136/000114036125045801/ef20057458_10k.htm |
| `manufacturing_data_type` | WAT/PCM, FDC sensor data, metrology, defect, wafer sort/bin maps, final test, genealogy | information | https://www.pdf.com/semiconductor-manufacturing-data-101-an-introduction/ ; https://www.semi.org/en/standards-watch-2026-apr/major-revision-underway-for-semi-e142 |
| `information_system` | EDA tools, MES, FDC, YMS, ATE/test data, foundry customer portal | system | https://www.siemens.com/en-us/products/opcenter/execution/semiconductor/ ; https://www.tsmc.com/english/dedicatedFoundry/services/eFoundry |
| `technical_standard` | SEMI P39 (OASIS), E30/E5/E37 (SECS/GEM), E142 (substrate maps), STDF, JEDEC HBM4, UCIe | standard | https://store-us.semi.org/products/e03000-semi-e30-specification-for-the-generic-model-for-communications-and-control-of-manufacturing-equipment-gem ; https://www.jedec.org/news/pressreleases/jedec%C2%AE-and-industry-leaders-collaborate-release-jesd270-4-hbm4-standard-advancing ; https://www.uciexpress.org/ |
| `test_insertion` | Wafer sort, final test, burn-in, system-level test | workflow | https://investors.teradyne.com/sec-filings/all-sec-filings/content/0000950170-25-023784/ter-20241231.htm ; https://www.semiconductors.org/wp-content/uploads/2018/06/0_2015-ITRS-2.0-Test-.pdf |

Suggested new predicates: `hands_off_design_to` (tape-out), `certifies_flow_for` (foundry → EDA flow/IP), `tests_for`, `enables` (technology → process_technology).

## 2. Information-flow edges

| Producer → Consumer | What data | Which system / format | Status | Evidence |
|---|---|---|---|---|
| Foundry → fabless/IDM designers | PDK (design rules, device models, cell libraries, EDA tech files) | Foundry portal; PDK file bundle | **Evidenced** (contents: SKY130 open PDK; portal: TSMC eFoundry/OIP). Access terms are **unknown** | `c_pdk_contents`, `c_oip`, `c_nda_unknown` |
| Foundry → EDA vendors, IP vendors | Process tech files, certification of flows, silicon validation of IP | TSMC OIP EDA/IP alliances | **Evidenced** (reported by TSMC) | `c_oip` |
| IP vendor → designer | Licensed reusable blocks (soft or hard IP) | Licence and deliverables | **Evidenced** (BCG, CSET); formats and terms unknown | `c_eda_ip` |
| Designer → foundry / mask shop | Final layout at tape-out | GDSII / OASIS (SEMI P39); TSMC-Online secure tape-out transfer | **Evidenced** | `c_oasis`, `c_efoundry_sec`, `c_mask_data` |
| Mask shop (merchant or captive) → fab | Mask set (physical plates); first layers sometimes within 24 h of design data | Mask data conversion; e-beam/laser writers | **Evidenced** | `c_mask_set`, `c_mask_24h`, `c_mask_captive` |
| Process equipment → fab host / MES | Equipment state, events, recipes, sensor data | SECS/GEM (SEMI E5/E30/E37); FDC | **Evidenced** | `c_gem`, `c_fdc` |
| Fab MES → itself / back-end | Lot/WIP tracking, genealogy, recipes, masks | MES (e.g. Siemens Opcenter) | **Evidenced** (vendor) | `c_mes`, `c_mes_siemens` |
| Foundry → fabless customer | WAT/PCM, wafer yield, pilot lots, quality/reliability data; lot status 3×/day | TSMC-Online/eFoundry; TSMC-Direct system-to-system | **Evidenced** (reported by TSMC). Defect and metrology data are *usually not shared* (single tier-3 source) | `c_efoundry_eng`, `c_efoundry_log`, `c_pcm_share` |
| Wafer sort → assembly/OSAT → final test | Wafer/bin maps by die XY coordinate | SEMI E142 substrate maps over SECS/GEM | **Evidenced** | `c_e142`, `c_mes_siemens` |
| ATE (sort/final test) → YMS / product engineering | Test results per lot, wafer, part and test | STDF V4 | **Evidenced** (tier-3 copy of spec) | `c_stdf`, `c_test_levels` |
| Chiplet/HBM suppliers → package integrator | Known-good-die test data | Unknown | **Requirement evidenced; the actual flow is unknown** | `c_kgd`, interview queue |
| OEM/Tier-1 ↔ chip supplier ↔ foundry | Demand forecasts, orders, allocation | Unknown (portals, EDI, spreadsheets?) | **Unknown**. GAO experts say firms are reluctant to share, so demand is hard to see | `c_gao_share`, `c_gao_proprietary`, `c_inventory` |
| Trusted suppliers ↔ US DoD | Design and manufacturing of sensitive ICs under confidentiality controls | DMEA accreditation | **Evidenced** (scope only) | `c_dmea_cats`, `c_dmea_why` |
| EDA vendor → restricted destinations | GAAFET-capable ECAD software | Export licence (BIS) | **Evidenced** (Aug 2022 rule) | `c_bis_ecad` |

**Where data is sensitive or handled by hand:** PDKs and design layouts are the most closely guarded IP. Open PDKs such as SKY130 are the exception. Foundries treat defect and metrology data as internal. Defence work adds trusted-supplier controls, and EDA exports are controlled for GAAFET design. Manual steps could not be established from public sources. Forecast exchange and multi-die failure analysis are the most likely places for manual work, and both are in the interview queue.

## 3. Technology transitions and what they depend on

| Transition | Status (per source) | Depends on |
|---|---|---|
| FinFET → gate-all-around (nanosheet) | Samsung 3 nm initial production June 2022; TSMC N2 volume 4Q25; Intel RibbonFET | Leading-edge foundries/IDMs; GAAFET-capable EDA (export-controlled); EUV |
| Frontside → backside power delivery | Intel PowerVia; TSMC A16 | Wafer thinning/bonding equipment; new EDA flows |
| EUV 0.33 NA → High-NA 0.55 NA | First modules to Intel Dec 2023; 4 systems recognized 2025 (R&D); HVM support expected 2027 | ASML (sole EUV maker); Carl Zeiss SMT optics; ~5,100 ASML suppliers |
| Monolithic SoC → chiplets / 2.5D / 3D | CoWoS-L in volume since 2024; SoIC 3 nm stacking in volume 2025; UCIe v3.0 | Foundry packaging capacity, OSATs, interposers/substrates (glass emerging), hybrid bonding, KGD test |
| HBM3E → HBM4 | JEDEC HBM4 released Apr 2025 (2 TB/s, 2048-bit, up to 16-high/64 GB) | DRAM makers, TSV stacking, 2.5D packaging |
| 3D NAND layer scaling | 321 layers in mass production (SK hynix, Nov 2024) | Deposition/etch equipment for high-aspect-ratio structures |
| Wide-bandgap to larger wafers | Infineon 300 mm GaN (announced Sept 2024; 2.3× chips vs 200 mm) | Existing 300 mm silicon lines; GaN epitaxy |

## 4. Key terms (79 glossary records in the batch)

Core: integrated circuit, transistor, wafer, ingot, die, yield, fab, front-end, back-end, process node, leading-edge vs legacy node, cycle time, lot.
Lithography: photolithography, photoresist, photomask/reticle, mask set, captive mask shop, DUV, immersion, EUV, High-NA EUV, numerical aperture, Rayleigh criterion, critical dimension.
Process: deposition, etch, ion implantation, FinFET, gate-all-around, backside power delivery, 3D NAND, DRAM, GaN.
Packaging: advanced packaging, chiplet, interposer, 2.5D, 3D integration, hybrid bonding, TSV, HBM, CoWoS, SoIC, UCIe, package substrate, glass substrate, known good die.
Test: wafer sort, final test, system-level test, burn-in, ATE, STDF, wafer map.
Design: EDA, semiconductor IP, PDK, design rules, RTL, logic synthesis, place and route, signoff, RTL-to-GDSII flow, GDSII, OASIS, tape-out.
Data/systems: MES, SECS/GEM, FDC, metrology, WAT/PCM, yield management system.
Business models: foundry, fabless, IDM, OSAT, trusted supplier.

## 5. Proposed follow-up research units (queued in the batch, origin RU-0001)

1. Design enablement and design-data handoff (EDA, IP, PDK, tape-out, mask data): P0, `information_flows`
2. Advanced packaging and HBM supply chain: P0, `technology`
3. Manufacturing and test data systems, standards and cross-company sharing: P1, `data`
4. Lithography and critical equipment dependencies (EUV/High-NA, masks, resists): P1, `technology`
5. Process roadmap transitions (GAA, backside power, 3D memory, SiC/GaN): P1, `dynamics`
6. Demand forecasting, allocation and supply-chain visibility: P1, `information_flows`
7. Security, IP protection, trusted suppliers and export controls on design tools: P2, `regulation`

## 6. What could not be established

- **Mask set cost and lead time** at leading-edge nodes: no tier-1 figure was found; only trade press has one (`c_mask_cost_unknown`).
- **PDK access terms** (NDAs, licence scope, export screening) and how design data is protected in transit (`c_nda_unknown`).
- **Share of layers printed with EUV versus DUV** per node (`c_euvlayers_unknown`). ASML's DUV page only says DUV stays cost-effective for most layers.
- **Formats and systems for exchanging forecasts and capacity reservations** between OEMs, fabless firms, foundries and OSATs.
- **Known-good-die and failure-analysis data flows** in multi-die (chiplet + HBM) packages.
- **Data foundries share beyond WAT/PCM.** The claim that defect and metrology data are usually withheld rests on one tier-3 vendor blog (`c_pcm_share`).
- **Leading-edge fab and SoC design costs.** The available figures are BCG estimates from 2019–2021; current tier-1 numbers were not found.
- **Tool and budget limits:** the web-search budget ran out in this session. Several WebFetch results were summaries rather than full verbatim passages; these are flagged where the evidence says "paraphrase". The IEEE IRDS roadmap, SEMI standards texts (paywalled) and Intel's newsroom HTML (blocked by robots.txt; PDF copies were used instead) were not read.

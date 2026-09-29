# Semiconductors: Phase 1 research plan

Prepared by the gap finder (`gap-plan-6a1d`, plan-review mode) on 2026-09-30 from the tree built by planners A-E (`PLAN1-plan1-A..E`). The changes are in staging batch `industries/semiconductors/staging/PLAN1-gap-plan-6a1d/` (207 updates and 1 new unit). The dry run is clean. Nothing has been merged yet. The counts below are what the tree will look like after the orchestrator merges the batch.

## 1. Headline counts

| | Before | After |
|---|---|---|
| Queued (active) units | 244 | **167** |
| Wave 1 / 2 / 3 | 51 / 184 / 13 | **38 / 113 / 16** |
| P0 / P1 / P2 (active) | n/a | **50 / 91 / 26** |
| Dropped by this batch | n/a | 78, each folded into a survivor |
| New units | n/a | 1 (Middle East AI-chips); trade flows handled by extending RU-0177 |
| Total questions across active units | n/a | 1,150 |

The target was about 150 active units. We stopped at 167 because merging further would give single units more than about 12 questions, which is more than one researcher can cover in 40-60 searches. It would also remove the only unit covering some leaf types or jurisdictions. The 141 P0/P1 units fall inside the methodology's 40-150 range. The 26 P2 units could be deferred to a later pass if needed (see section 6).

## 2. Active units by dimension, wave and priority

| Dimension | w1 | w2 | w3 | P0 | P1 | P2 | Total |
|---|---|---|---|---|---|---|---|
| adjacent | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| business_models | 1 | 7 | 0 | 1 | 4 | 3 | 8 |
| capital | 1 | 9 | 0 | 2 | 6 | 2 | 10 |
| competition | 2 | 3 | 1 | 3 | 3 | 0 | 6 |
| data | 1 | 1 | 0 | 0 | 1 | 1 | 2 |
| definition | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| dynamics | 5 | 2 | 0 | 4 | 2 | 1 | 7 |
| geography | 1 | 1 | 10 | 2 | 8 | 2 | 12 |
| history | 1 | 4 | 0 | 0 | 3 | 2 | 5 |
| information_flows | 2 | 4 | 0 | 1 | 3 | 2 | 6 |
| labor | 1 | 4 | 0 | 2 | 3 | 0 | 5 |
| market_size | 1 | 1 | 0 | 1 | 1 | 0 | 2 |
| money_flows | 1 | 6 | 0 | 3 | 3 | 1 | 7 |
| participants | 1 | 5 | 0 | 2 | 4 | 0 | 6 |
| problems | 0 | 4 | 0 | 1 | 2 | 1 | 4 |
| regulation | 5 | 22 | 2 | 7 | 18 | 4 | 29 |
| risks | 0 | 2 | 2 | 2 | 2 | 0 | 4 |
| segmentation | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| supply_chain_concentration | 1 | 7 | 1 | 4 | 5 | 0 | 9 |
| technology | 2 | 6 | 0 | 4 | 2 | 2 | 8 |
| unit_economics | 3 | 4 | 0 | 2 | 5 | 0 | 7 |
| value_chain | 7 | 10 | 0 | 3 | 11 | 3 | 17 |
| workflows | 0 | 10 | 0 | 5 | 4 | 1 | 10 |
| **Total** | 38 | 113 | 16 | 50 | 91 | 26 | 167 |

The active dimension counts are lower than the raw `irs coverage` numbers, because `coverage` also counts dropped units. Every ontology dimension still has at least one active unit. Every value-chain stage still has an owner:

- research: RU-0058
- design: RU-0059, RU-0034, RU-0006, RU-0060
- masks: RU-0061
- materials: RU-0041, RU-0064, RU-0065, RU-0066, RU-0055, RU-0049
- equipment: RU-0042, RU-0050, RU-0037
- fabrication: RU-0062, RU-0003
- assembly and test: RU-0007, RU-0063
- distribution: RU-0043, RU-0019, RU-0088
- system integration: RU-0068
- post-sale and end-of-life: RU-0156
- logistics: RU-0070
- facilities: RU-0071

Every major jurisdiction still has a regulation unit and a profile: US, China, Taiwan, South Korea, Japan, EU/UK, India, Southeast Asia, Israel, the Middle East (new unit), and secondary locations (RU-0245).

## 3. Wave design and search volume

- **Wave 1 (38 units): the foundations.** These are the market series and methodology, segmentation, definitions, the stage maps (EDA, design, back-end, materials, equipment, distribution, fab capacity), the value-pool and business-model catalogue, and the fab cost model. Also here: capex and the cycle, the shortage, rankings, the census method, workforce baseline, and the four regulatory anchors (US export controls, CHIPS, tariffs/customs, EU Chips Act, China export controls). No wave-1 unit depends on a later wave.
- **Wave 2 (113 units): depth.** This covers sub-segments, money flows, workflows, country regimes, problems, labour and capital. Some wave-2 units depend on other wave-2 units, for example the chains fab cost → die cost → AI accelerator cost stack, and foundry order-to-delivery → yield-data exchange → RMA. `irs next` puts them in order.
- **Wave 3 (16 units): synthesis.** These are the cross-country policy comparison with subsidy effectiveness (RU-0014), the chokepoint scorecard (RU-0057), export-control effectiveness (RU-0152), AI-capex risk (RU-0206), resilience and the risk matrix (RU-0212), and durable advantage (RU-0225). The 10 country profiles are also here (RU-0235 to RU-0245). They reuse claims from the country regulation, capital and labour units, so their search budget is lower.

| Wave | Units | Searches at 40/unit | Searches at 60/unit | Note |
|---|---|---|---|---|
| 1 | 38 | 1,520 | 2,280 | about 6-7 dispatch rounds at 6 researchers per wave |
| 2 | 113 | 4,520 | 6,780 | about 19 rounds; 54 units carry merged scope and will run toward the 60 end |
| 3 | 16 | 640 | 960 | synthesis; realistically 20-40 searches/unit (320-640) |
| **Total** | **167** | **6,680** | **10,020** | plus fact-check searches (config `fact_check: all`) |

If the 26 P2 units were deferred, the total would drop by about 1,000-1,600 searches.

## 4. Dedupe decisions for the overlaps the planners flagged

- **Nexperia 2025.** RU-0137 (European export control and investment screening, which now also covers the UK) owns the legal record: the Goods Availability Act order, the court measures, China's export ban and the suspension. RU-0169 (allocation), RU-0200 (weaponisation), RU-0030 (China retaliation) and RU-0052 (legacy-chip dependence) cite it for their own angle only. RU-0169 and RU-0200 now depend on RU-0137.
- **Distribution, RU-0019 vs RU-0043.** Both are kept, with a clean split. RU-0043 covers structure, the channel share and enumeration (it absorbs RU-0232). RU-0019 covers channel economics, accounting and problems (it absorbs RU-0196). The duplicated "share through distribution" question was removed from RU-0019. RU-0088 owns counterfeit depth and absorbs RU-0197.
- **Equipment, RU-0021 vs RU-0042.** Both are kept. RU-0042 covers segments, billings and customer concentration. RU-0021 covers the commercial model plus the purchase-to-production workflow (it absorbs RU-0171). The duplicated customer-concentration question was removed from RU-0021. The used-equipment question moved from RU-0042 to RU-0050, which absorbs the fab-support services unit RU-0046.
- **RU-0014 vs RU-0020.** Both are kept, and the split is clean. RU-0020 records Japan, Korea and Taiwan money amounts at wave 2. RU-0014 is the wave-3 cross-country synthesis and now also absorbs subsidy effectiveness (RU-0117). RU-0014's prereqs are resolved to RU-0138, 0141, 0142, 0143, 0144, 0098, 0106, 0108, 0109, 0135, 0020, 0026, 0028 and 0031.
- **Taiwan.** RU-0051 covers concentration, hazards and cross-Strait scenarios, and absorbs RU-0199. RU-0141 covers regulation. RU-0237 is the wave-3 profile, which reuses RU-0051 and RU-0141 and absorbs Taiwan workforce (RU-0120).
- **Chokepoints.** RU-0048 stays in wave 1 as the register: it inventories the published chokepoint lists and fixes the metric definitions. RU-0057 is the wave-3 scorecard and absorbs single-supplier consequences and mitigation (RU-0205).
- **Enumeration.** The stage units record leaders and shares. The enumeration units (RU-0227 to 0230, plus RU-0043, RU-0060 and RU-0068) record the long tail as company records, using the RU-0226 method. RU-0226 absorbs disclosure systems (RU-0176). RU-0231 went into RU-0060, RU-0232 into RU-0043, and RU-0233 into RU-0068.
- **Memory.** RU-0018 absorbs RU-0012 and now covers the business model, price cycle and consolidation history. RU-0220 absorbs RU-0094 and covers market structure plus the HBM commercial model. RU-0072 stays as HBM manufacturing technology.
- **Smuggling and diversion.** RU-0133 absorbs RU-0209 and covers enforcement and diversion cases. RU-0145 stays because it covers Southeast Asian legal regimes. RU-0159 stays because it covers traceability and location verification, and it now depends on RU-0088.
- **Country profiles vs country units.** Country workforce units were folded into the profiles:

  | Workforce unit | Folded into |
  |---|---|
  | RU-0120 | RU-0237 |
  | RU-0121 | RU-0238 |
  | RU-0122 | RU-0239 |
  | RU-0124 | RU-0240 |
  | RU-0125 | RU-0243 |
  | RU-0126 | RU-0144 (SEA policy, which already holds the NSS talent target) |

  US (RU-0119) and China (RU-0123) workforce stay separate. They are P0/P1 and policy-heavy.

  Other profile changes: RU-0242 went into RU-0241, and RU-0146 into RU-0244. The UK regime (RU-0147) went into RU-0137. China state capital (RU-0107) went into RU-0138. China build-out (RU-0183) went into RU-0053, and mature-node dynamics (RU-0184) into RU-0052.
- **RU-0008 vs product taxonomy.** RU-0008 absorbs RU-0217. It becomes the single segmentation unit (dimension changed from dynamics to segmentation) and covers both product and end-use segmentation. AI/HBM demand mechanics stay in RU-0016. Chip content per device (RU-0218) went into RU-0189.

## 5. Full merge table (78 units dropped)

| Survivor (active) | Absorbed (now dropped) |
|---|---|
| RU-0002 Market size: sizing methodology (WSTS vs Gartner vs others) and the 1986-2026 global time serie | RU-0215 Global chip market time series 1986-2026: WSTS totals by product categ |
| RU-0008 Segmentation: product taxonomy and segment sizes (WSTS classes, ASSP/ASIC/general-purpose), end | RU-0217 Product taxonomy and segment sizes: WSTS product classes and sub-class |
| RU-0009 Definitions and classification: legal and statistical meanings of 'semiconductor', leading-edge | RU-0214 Definitions register: legal and statistical meanings of 'semiconductor |
| RU-0014 Cross-country comparison of chip industrial policy: design, money committed vs disbursed, and e | RU-0117 Subsidy effectiveness: did public money change where fabs are built an |
| RU-0018 Memory: business model, price cycle, and the history of memory cycles and consolidation (1970-2 | RU-0012 History: memory cycles and memory-maker consolidation (1970-2025) |
| RU-0019 Distribution channel economics and problems: margins, ship-and-debit, price protection, stock r | RU-0196 Problems in the distribution channel: excess inventory, price erosion, |
| RU-0021 Equipment makers' commercial model and the purchase-to-production workflow: pricing, down payme | RU-0171 Workflow: equipment purchase to production (order, down payment, deliv |
| RU-0022 Packaging and test unit economics and OSAT problems: pricing basis, utilisation, advanced-packa | RU-0194 Problems of OSATs and advanced-packaging providers: capacity bottlenec |
| RU-0024 Design-enablement business models: EDA licensing (time-based, emulation, cloud) and IP/patent r | RU-0095 EDA commercial model: time-based licences, emulation hardware, cloud a |
| RU-0027 US tariffs on semiconductors (Section 232, 301, reciprocal) plus customs classification, rules  | RU-0136 Customs classification, rules of origin and the WTO Information Techno |
| RU-0032 Environmental, chemical and resource constraints on fabs: PFAS, F-gas, RoHS/REACH, water, power | RU-0211 Resource and environmental constraint risk: water, power, emissions an |
| RU-0035 Manufacturing and test data systems and their vendors: MES, FDC/APC, SPC, yield management, AMH | RU-0078 Manufacturing software and fab automation suppliers: MES, APC/FDC, yie |
| RU-0043 Distribution channel structure and enumeration: authorised distributors, catalogue houses, inde | RU-0232 Enumerate channel intermediaries: authorised distributors, catalogue h |
| RU-0045 Custom silicon: hyperscaler/OEM in-house chip design, ASIC design-service houses, their busines | RU-0092 Custom-silicon and ASIC design-service business model: NRE, turnkey pr |
| RU-0049 Critical minerals and inputs for chips: gallium, germanium, rare earths, tungsten, antimony, he | RU-0204 Critical-input supply risk: gases, minerals, chemicals and quartz (neo |
| RU-0050 Equipment sub-tier supply base and fab-support services: optics, lasers, RF power, vacuum, cera | RU-0046 Fab-support services: parts cleaning and coating, wafer reclaim and te |
| RU-0051 Taiwan concentration and cross-Strait risk: share of leading-edge logic, physical hazards, conf | RU-0199 Taiwan concentration and cross-Strait conflict risk: scenarios, exposu |
| RU-0052 Mature-node (28nm and above) capacity concentration and dynamics: China's buildout, supply-dema | RU-0184 Mature-node (28nm and above) supply, demand and pricing dynamics, incl |
| RU-0053 China's build-out and localisation by value-chain stage (2014-2026): domestic share of equipmen | RU-0183 China's semiconductor build-out: localisation, self-sufficiency progre |
| RU-0054 Supplier qualification, second-sourcing and switching costs: copy-exactly, PCNs, automotive req | RU-0170 Workflow: qualifying a second source for materials, chemicals, gases a |
| RU-0057 Chokepoint scorecard synthesis: consistent concentration metrics per stage, and consequences an | RU-0205 Single-supplier chokepoint risk: consequences and mitigation where one |
| RU-0058 Pre-competitive research: consortia, national labs, university programmes and public/consortium | RU-0115 Public and consortium R&D funding flows: imec, NSTC/Natcast, Leti, ITR |
| RU-0060 Semiconductor IP market and design-enablement enumeration: processor, interface and foundation  | RU-0231 Enumerate design-enablement providers: EDA vendors, IP licensors and d |
| RU-0061 Mask-making stage and photomask economics: captive vs merchant shops, mask blanks, pellicles, w | RU-0100 Photomask economics: mask-set cost by node, captive versus merchant ma |
| RU-0062 Fab capacity structure and fab datasets: wafer sizes, node bands, product mix, fab counts, the  | RU-0178 Fab and capacity datasets: coverage and reliability of fab-level datab |
| RU-0066 Lithography materials and other fab consumables: photoresists, ancillaries, CMP slurries/pads,  | RU-0067 Other fab consumables: CMP slurries and pads, sputtering targets, depo |
| RU-0068 System integration and chip buyers: EMS/ODM board and AI-server assembly, OEMs, top chip purcha | RU-0233 Chip buyers: top purchasers by spend, OEM and EMS/ODM enumeration, and |
| RU-0073 Leading-edge process capability and technology execution risk: 3nm/2nm-class nodes, yields, Chi | RU-0207 Technology execution risk: node delays, yield failures and technology  |
| RU-0074 Chiplets and heterogeneous integration: die-to-die standards (UCIe, BoW), chiplet business mode | RU-0097 Chiplet and multi-die business models: who is the prime contractor, kn |
| RU-0075 Wide-bandgap and compound semiconductors (SiC, GaN, GaAs, InP): value chains and unit economics | RU-0102 Wide-bandgap (SiC and GaN) unit economics: substrate cost, yields, 200 |
| RU-0076 Specialty and mature process platforms (BCD, eNVM, RF-SOI, FD-SOI, CIS, MEMS) and competition i | RU-0224 Other segment competition: FPGAs, image sensors, optoelectronics, MEMS |
| RU-0087 Foundry-customer money flows: IDM outsourcing to foundries, capacity reservation, prepayments a | RU-0081 IDM-to-foundry outsourcing flows: how much IDMs buy from foundries, fr |
| RU-0088 Open-market brokers, grey market and counterfeit/recycled chips: shortage pricing, scale, entry | RU-0197 Counterfeit, recycled and grey-market chips: scale, where they enter,  |
| RU-0093 Analog, power, MCU and discrete IDMs: business model (fab ownership, 300mm, long product lives, | RU-0223 Analog, power, microcontroller and discrete competition: shares, Chine |
| RU-0099 Chip cost stack: die cost per transistor, die size, yield, masks, design cost, packaging, test  | RU-0104 Fabless chip cost-of-goods stack: wafer, packaging, test, royalties an |
| RU-0105 Industry capital expenditure and the capacity investment cycle: totals by segment, company and  | RU-0186 Capacity investment cycle: capex decisions, fab lead times and utilisa |
| RU-0106 Fab project pipeline and the reshoring wave: announced, under construction, delayed, cancelled  | RU-0185 Reshoring and the global fab-building wave: announced vs realised capa |
| RU-0113 Mergers, acquisitions and consolidation: deal flow, valuations, blocked deals, merger-review pa | RU-0187 Consolidation and M&A dynamics: major deals, blocked deals and merger- |
| RU-0114 Public markets, cost of capital and financial distress: listings, valuations, debt, bankruptcie | RU-0210 Company-failure and financial risk: bankruptcies and distressed exits  |
| RU-0116 History: technology generations (wafer size, lithography, packaging), rising capital intensity  | RU-0079 Technology history: wafer-size transitions, lithography generations an |
| RU-0127 Talent supply: skills pipeline (degrees, technicians, apprenticeships) and immigration/mobility | RU-0128 Skills pipeline: degrees, technician training, apprenticeships and ind |
| RU-0129 Wages, labour cost, working conditions and labour relations in fabs, OSATs and design | RU-0130 Labour relations and working conditions: unions, strikes, working hour |
| RU-0133 US Entity List, end-user controls, VEU revocations, export-control enforcement and AI-chip dive | RU-0209 Regulatory enforcement and compliance risk: export-control penalties,  |
| RU-0135 US fab siting: federal environmental permitting, water, and state and local incentives (AZ, NY, | RU-0110 US state and local incentives for fabs: grants, tax abatements and inf |
| RU-0137 European export control and investment screening (EU, member states, UK NSI Act and UK strategy | RU-0147 United Kingdom semiconductor regime: National Semiconductor Strategy,  |
| RU-0138 China industrial policy and state capital: State Council IC policies, Big Fund I-III, local gui | RU-0107 China's state and quasi-state capital in semiconductors: Big Fund I-II |
| RU-0144 Southeast Asia industrial policy and talent targets: Malaysia NSS (incl. 60,000-engineer target | RU-0126 Southeast Asia semiconductor workforce: Malaysia NSS 60,000-engineer t |
| RU-0150 IP theft, trade secrets, cyber and insider risk, and IP enforcement (ITC Section 337, criminal  | RU-0208 Cybersecurity, IP theft and insider risk in the semiconductor supply c |
| RU-0152 Effectiveness and cost of export controls, and the datasets that track controls, entity lists,  | RU-0180 Policy and enforcement datasets: tracking controls, entity lists, subs |
| RU-0153 Cross-company yield, quality and test-data exchange: foundry/OSAT to designers, and known-good- | RU-0154 Known-good-die, HBM and chiplet test-data exchange across memory maker |
| RU-0155 Information flows between chip companies and governments, incl. the incentive application-to-di | RU-0174 Workflow: government incentive application to disbursement (US CHIPS,  |
| RU-0156 Post-sale and end-of-life: PCN/PDN, material declarations, obsolescence, last-time buys, author | RU-0069 Post-sale and end-of-life: product longevity, obsolescence and last-ti |
| RU-0162 Workflow: tape-out to production release (mask making, MPW shuttles, first silicon, bring-up, r | RU-0161 Workflow: tape-out to first silicon and bring-up (mask making, MPW shu |
| RU-0163 Workflow and problems: new fab and new process ramp, incl. cost, delays, permits and workforce  | RU-0193 Fab construction and ramp problems outside East Asia: cost, delays, pe |
| RU-0164 Workflow: wafer order-to-delivery at a foundry through back-end order flow at an OSAT (forecast | RU-0165 Workflow: back-end order flow at an OSAT (consigned wafers, assembly,  |
| RU-0167 Workflow: customer returns (RMA) and failure analysis, incl. automotive 8D, multi-die attributi | RU-0198 Silent data corruption and reliability problems in large compute fleet |
| RU-0172 Workflow: OEM and EMS chip sourcing and the money path to the board (design-in, AVL, turnkey vs | RU-0085 Who buys the chips: EMS/ODM turnkey versus OEM-consigned procurement a |
| RU-0173 Workflow: design-win sales cycle and distribution-channel data (design registration, POS report | RU-0157 Distribution-channel information flows: design registration, point-of- |
| RU-0181 The semiconductor business cycle: drivers, inventory dynamics, turning points (1985-2026) and l | RU-0175 Leading indicators and high-frequency datasets for the semiconductor c |
| RU-0189 Consumer and device demand dynamics and chip content per device: smartphones, PCs, servers, AI  | RU-0218 Chip content per device: semiconductor bill-of-materials share in smar |
| RU-0195 Problems of equipment and materials suppliers: export-control revenue loss, lead times, restric | RU-0158 Equipment-to-fab information flows: tool data access, remote diagnosti |
| RU-0200 Geopolitical risk: weaponisation of chip supply chains (2019-2026) and conflict risks beyond Ta | RU-0201 Geopolitical and conflict risks beyond Taiwan: Korean peninsula, Israe |
| RU-0202 Physical disruption risk: natural hazards, operational incidents (fires, contamination, outages | RU-0056 Disruption case studies 2011-2025: how chokepoints behaved in real sho; RU-0203 Operational disruption risk: fab fires, contamination, power outages,  |
| RU-0212 Business continuity and resilience practices, and the risk exposure matrix by participant type  | RU-0213 Risk exposure matrix by participant type and region (synthesis) |
| RU-0219 Company rankings and concentration: top chip vendors' shares (2000-2025) and share by headquart | RU-0234 Market share by company headquarters country, 1985-2025, and how it di |
| RU-0220 Memory market structure and HBM commercial model: DRAM/NAND/HBM shares by firm and country, vol | RU-0094 HBM commercial model and unit economics: annual volume-price contracts |
| RU-0226 Participant census method and company disclosure systems (EDGAR, MOPS, DART, EDINET, HKEX, SSE/ | RU-0176 Company disclosure systems by jurisdiction: what chip companies must p |
| RU-0237 Taiwan country profile incl. workforce: foundry, OSAT, IC design and supply clusters, output, e | RU-0120 Taiwan semiconductor workforce: talent shortage, demographics, oversea |
| RU-0238 South Korea country profile incl. workforce: memory, foundry, Yongin/Pyeongtaek cluster, supply | RU-0121 South Korea semiconductor workforce: shortage estimates, working-hours |
| RU-0239 Japan country profile incl. workforce: equipment and materials strength, device makers, new fab | RU-0122 Japan semiconductor workforce: rebuilding talent for JASM, Rapidus and |
| RU-0240 Europe country profile incl. workforce: EU and UK strengths, Silicon Saxony, Netherlands, Irela | RU-0124 European semiconductor workforce: shortage estimates, the European Chi |
| RU-0241 Southeast Asia profile: Malaysia, Singapore, Vietnam, the Philippines and Thailand (back-end hu | RU-0242 Southeast Asia profile II: Vietnam, the Philippines and Thailand - ass |
| RU-0243 India country profile incl. workforce: design centres, first fabs and OSATs, chip imports, ISM  | RU-0125 India semiconductor workforce: design-engineer base, ISM/C2S training  |
| RU-0244 Israel profile and policy regime: design/R&D centres, Intel and Tower fabs, start-ups, Innovati | RU-0146 Israel semiconductor regime: Innovation Authority, Capital Investment  |
| RU-0246 History: origins of the industry 1947-1980 and the offshoring of assembly to East and Southeast | RU-0131 History: labour and the offshoring of assembly to East and Southeast A |
| RU-0248 History: Japan's rise and decline and the US response 1970s-2010s (SEMATECH, US-Japan agreement | RU-0015 History: Japan's rise and decline in semiconductors (1970s-2010s) |
| RU-0249 History: Europe's and China's paths before 2014, and trade/industrial policy before 2018 (COCOM | RU-0151 Semiconductor trade and industrial policy before 2018: COCOM to Wassen |

## 6. Dependency and wave fixes

- **Prereq notes.** All "prereq: <title>" notes in `open_questions` were removed. Each was either resolved into a real `depends_on` id or rewritten as a cross-reference.
- **Mutual prereqs.** Five were broken, and the reason is kept in each unit's notes:

  | Resolution | Pair |
  |---|---|
  | RU-0106 depends on RU-0105 | capex vs pipeline |
  | RU-0172 depends on RU-0084 | buyer terms vs EMS procurement |
  | RU-0162 depends on RU-0160 | design vs tape-out |
  | RU-0159 depends on RU-0088 | traceability vs counterfeit |
  | RU-0156 feeds RU-0172 | PCN info vs sourcing |

- **Wave inversions removed.** These deps were dropped:
  - RU-0098 on RU-0026 and RU-0014. RU-0129 (wages) now depends on RU-0098 instead of the reverse.
  - RU-0106, RU-0108, RU-0115 and RU-0174 on RU-0014.
- **References to units dropped earlier were rewired:** RU-0004 → RU-0042, RU-0005 → RU-0041, RU-0013 → RU-0025, RU-0044 → RU-0036.
- **Cycles.** The dry-run cycle check passes. Two cycles that the merges created were cut: RU-0043 ↔ RU-0088 (distribution vs brokers) and RU-0248 ↔ RU-0249 (history).
- **Priority changes.** When units merged, the survivor took the higher priority. RU-0045 (custom silicon, now including its business model) moved to wave 2 at P1, and its dependents follow it.

## 7. New and extended units (gap finder)

- **New: Middle East (UAE, Saudi Arabia) AI-chip imports and fab ambitions.** Regulation dimension, wave 2, P1, depends on RU-0132. A search confirmed that the US Commerce Department licensed Blackwell-class exports to G42 and Humain in November 2025 (to be verified from commerce.gov by the researcher). RU-0245 was narrowed to Mexico/Costa Rica, Central and Eastern Europe, and Russia.
- **Extended: RU-0177, trade flows of chips and tools by country pair.** It gains four questions: HS 8542/8486 flows by country pair for 2015-2025, China's imports by origin, processing and re-export trade, and post-2022 rerouting. Its dimension changes from data to geography. Where profits are booked (RU-0089) stays a separate P2 money-flows unit.

## 8. Decisions for the user

1. **Accept 167 active units, or defer the 26 P2 units** (for example logistics, fab construction, due diligence, patent datasets, photonics, Israel, secondary locations) to a later pass so wave 2 starts with about 141.
2. **Workforce folding.** Six country workforce units are now handled inside wave-3 country profiles. If labour is a priority for the eventual opportunity analysis, Taiwan and South Korea workforce could be split back out.
3. **Regulation weight.** Regulation has 29 of the 167 active units (17%). This reflects the 2025-2026 policy churn, but it could be trimmed further if the atlas's purpose leans commercial.

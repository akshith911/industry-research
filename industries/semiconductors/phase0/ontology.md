# Ontology: the kinds of things in the semiconductor industry

> Scope: the entity types, relation predicates and research dimensions in `ontology.yaml`, and why they are shaped this way. Period: evidence gathered 2026-09-29 (historical claims flagged). Geography: global.
> Built from research unit RU-0001 (six discovery lenses: definition, value chain, money, regulation, technology, history). Planner run `plan0-9c2e`, 2026-09-29.

**Evidence status, read this first.** Every claim cited on this page is still **unverified, low confidence**. No independent fact-check has run yet. The type tree below is a working map. Its shape is supported by several independent lenses, but each individual citation may still fail a check.

## What this means

An ontology is the list of *kinds of things* the atlas talks about, plus the *kinds of links* between them. For example, "foundry" is a kind of participant, "EUV lithography" is a kind of technology, and "foundry `supplies` fabless company" is a kind of link. Every company, entity, rule and relation in the databases must use one of these types, so the list has to reflect how the industry really works.

One rule shaped the whole tree. **A company can hold several roles at once.** Samsung is an IDM and also sells foundry capacity. ASE is an OSAT but earns about 40% of its revenue from electronics manufacturing services (EMS). Arm licenses IP and now also sells chips [CLM-0566] [CLM-0535] [CLM-0501]. Roles are therefore separate types, and a company record will list several `roles`. Company records are not created yet; a later research wave will discover companies systematically.

## The type tree

101 types grouped under 8 top-level parents. The indentation shows each type's parent.

```
participant (36)                      who does business in the chain
├─ chip_company                       sells chips under own name / designs for own use
│  ├─ idm ── memory_maker
│  ├─ fabless_company
│  └─ custom_silicon_system_company   hyperscalers/OEMs designing own chips
├─ design_enablement_provider
│  ├─ eda_vendor
│  ├─ ip_licensor
│  └─ design_service_provider         design house / turnkey ASIC
├─ patent_licensor                    device-level patent royalties
├─ manufacturing_service_provider
│  ├─ foundry ─┬─ pure_play_foundry
│  │           └─ idm_foundry_business
│  ├─ osat
│  └─ mask_maker
├─ upstream_supplier
│  ├─ equipment_maker ─┬─ wafer_fab_equipment_maker
│  │                   └─ test_equipment_maker
│  ├─ materials_supplier ─┬─ wafer_supplier
│  │                      ├─ process_chemical_supplier
│  │                      ├─ specialty_gas_supplier
│  │                      ├─ packaging_materials_supplier
│  │                      └─ critical_mineral_producer
│  └─ manufacturing_software_vendor   MES / FDC / yield software
├─ channel_intermediary ─┬─ authorized_distributor
│                        └─ open_market_broker
├─ chip_buyer ─┬─ oem
│              └─ ems_provider
└─ capital_provider ── financial_co_investor
institution (18)
├─ government_body
│  ├─ export_control_authority        ├─ industrial_policy_agency
│  ├─ trade_remedy_authority          ├─ investment_screening_authority
│  ├─ state_investment_fund           ├─ security_review_authority
│  ├─ competition_authority           ├─ environmental_chemical_regulator
│  ├─ securities_disclosure_regulator └─ statistical_classification_authority
├─ multilateral_regime   ├─ industry_association   ├─ statistics_body
├─ market_research_firm  ├─ standards_body         └─ research_organisation
semiconductor_product (13)   integrated_circuit {logic_ic {ai_accelerator}, memory_ic {dram, hbm, nand_flash},
                             analog_ic, micro_ic}, discrete_semiconductor, optoelectronics, sensor_actuator
technology (7)               process_technology, transistor_architecture, lithography_technology,
                             packaging_technology, power_delivery_technology, substrate_technology
production_process (4)       value_chain_stage, process_step, test_insertion
information_artefact (7)     design_artifact, manufacturing_data, information_system, technical_standard,
                             market_statistic, industry_classification
end_market (7)               computing, communications, consumer, automotive, industrial, government/military
commercial_arrangement (9)   long_term_supply_agreement, capacity_prepayment, consignment_service_agreement,
                             ip_licence_and_royalty, software_licence, franchised_distribution_agreement,
                             equipment_service_subscription, government_incentive
```

### What each group is, and the evidence

**Chip companies.** These are the firms that sell chips. WSTS, the body that counts the market, admits only companies that "at least design and sell" chips under their own trade name [CLM-0002].
- **IDMs** design chips, make them, and package and test them in-house [CLM-0483]. By one 2019 estimate they had about 70% of sales [CLM-0484].
- **Memory makers** sit under IDM because every memory maker in the evidence runs its own fabs. Memory prices are renegotiated periodically and swing by roughly ±40% a year [CLM-0266] [CLM-0267].
- **Fabless companies** design chips and outsource all manufacturing [CLM-0485] [CLM-0186].
- **System companies that design their own chips** (hyperscalers) have a separate type. They design silicon for their own use, not for sale [CLM-0502] [CLM-0503].

**Design enablement.** These firms supply what designers need.
- **EDA vendors** sell design software [CLM-0475] [CLM-0199].
- **IP licensors** charge a licence fee plus a per-chip royalty [CLM-0213].
- **Design-service / ASIC houses** take a customer's chip from specification to finished product [CLM-0504].
- **Patent licensors** have their own type because the business is different. They license *patents* to *device makers*, and the royalty is a share of the device price [CLM-0196].

**Manufacturing services.** These firms make, package or test chips designed by others.
- **Foundries** make chips to customers' designs [CLM-0161] [CLM-0486]. There are two kinds. Pure-play foundries only make chips for customers [CLM-0106] [CLM-0490]. IDM foundry businesses are foundry arms inside chip companies [CLM-0113] [CLM-0258].
- **OSATs** package and test under contract [CLM-0488].
- **Mask makers** turn each design into photomasks. They are either captive (inside a chipmaker) or merchant (independent) [CLM-0527].

**Upstream suppliers.**
- **Equipment makers.** Chipmaking uses more than 50 tool types [CLM-0472], and SEMI splits the tools into front end and back end [CLM-0059]. Test equipment is a distinct business [CLM-0513].
- **Materials suppliers**, split into wafers [CLM-0474], chemicals and photoresist [CLM-0524], specialty gases [CLM-0530], packaging substrates [CLM-0540] and critical minerals [CLM-0344] [CLM-0345].
- **Factory-software vendors** [CLM-0448] [CLM-0449].

**Channel and buyers.**
- **Authorized distributors** resell under franchise agreements with chipmakers [CLM-0541] [CLM-0270].
- **The open market** of brokers sits outside the authorized channel [CLM-0544].
- **OEMs and EMS providers** buy the chips [CLM-0541] [CLM-0534].

**Capital.**
- **Financial co-investors** fund fabs, e.g. Intel's SCIP partners [CLM-0257].
- **State investment funds** sit under government, e.g. China's Big Fund and the US equity stake in Intel [CLM-0350] [CLM-0259].

**Institutions.** Government bodies are split by *function*, not by country, because one ministry often does several jobs. The functions found are:
- export control [CLM-0301] [CLM-0336] [CLM-0339] [CLM-0344]
- incentives [CLM-0312] [CLM-0358]
- tariffs and trade remedies [CLM-0319] [CLM-0351]
- investment screening [CLM-0325] [CLM-0333]
- state equity [CLM-0350]
- security review and trusted-supplier accreditation [CLM-0353] [CLM-0458]
- competition [CLM-0120]
- chemicals and environment [CLM-0335]
- disclosure [CLM-0326]
- statistical classification [CLM-0017]

Non-government institutions:
- **The Wassenaar Arrangement** is a multilateral control regime [CLM-0342].
- **Industry associations** such as SIA and SEMI [CLM-0007] [CLM-0058].
- **The statistics body** WSTS [CLM-0001].
- **Market-research firms** such as Gartner and TrendForce [CLM-0052] [CLM-0554].
- **Standards bodies** such as SEMI Standards, JEDEC and UCIe [CLM-0361] [CLM-0363] [CLM-0442].
- **Research organisations** such as SEMATECH, ITRI and imec [CLM-0102] [CLM-0104] [CLM-0438].

**Products.** These follow the official WSTS taxonomy: discretes, optoelectronics, sensors/actuators, and ICs split into analog, micro, logic and memory [CLM-0013] [CLM-0014]. Two sub-types are added because regulation singles them out:
- **AI accelerators**, the target of export controls and the Section 232 tariff [CLM-0301] [CLM-0307] [CLM-0319].
- **HBM**, which has its own export-control classification (ECCN) [CLM-0304] [CLM-0439].

**Technology, process and information.** These types come from the technology lens:
- process nodes, which are labels, not measurements [CLM-0379]
- transistor architectures [CLM-0401] [CLM-0406]
- lithography [CLM-0386] [CLM-0400]
- packaging [CLM-0435] [CLM-0437]
- backside power [CLM-0405]
- wafer substrates [CLM-0381] [CLM-0411]
- design artefacts [CLM-0419] [CLM-0421]
- manufacturing data [CLM-0451] [CLM-0454]
- information systems [CLM-0448] [CLM-0457]
- technical standards [CLM-0453] [CLM-0440]

**End markets.** These follow the WSTS End Use Survey. Computing/AI was 34.9% of 2024 demand [CLM-0560] and automotive 9.9% [CLM-0561]. Military sits inside Government [CLM-0074]. The other four 2024 shares are **not reliably established** [CLM-0073].

**Commercial arrangements.** These are recurring contract forms that decide who carries risk. The money lens found them to be the main way risk moves between participants [CLM-0300]:
- LTAs [CLM-0175] and prepayments [CLM-0169]
- consigned wafers [CLM-0232]
- royalties [CLM-0213]
- EDA licences [CLM-0199]
- distributor price protection [CLM-0270]
- equipment service subscriptions [CLM-0230]
- government incentives [CLM-0283]

## How the six lenses were reconciled

| Proposed by lenses | Decision | Why |
|---|---|---|
| `design_house` (definition), "ASIC / turnkey design-service firm" (value chain) | Merged into `design_service_provider` | Same role: specification-to-product services [CLM-0504] [CLM-0085] |
| `ip_vendor`, `ip_licensor`, "Semiconductor IP licensor" | `ip_licensor` | Same business model [CLM-0213] [CLM-0475] |
| `equipment_supplier`, `equipment_maker`, "wafer-fab equipment maker", "test-equipment maker", "equipment service business" | `equipment_maker` with two children; service is a commercial arrangement, not a separate participant | Equipment makers themselves run the service business [CLM-0511] [CLM-0509] |
| `government_funder_regulator`, `government_funder`, "export-control authority", "state investment fund" | Split by function under `government_body` | One ministry holds several functions (METI does export controls and subsidies [CLM-0339] [CLM-0340]) |
| `mask_maker` (SEMI counts masks as a *material*; TSMC counts mask-making as part of "Foundry 2.0") | Kept as a participant under `manufacturing_service_provider` | Mask shops make custom products from confidential designs, which is a service to designers [CLM-0529] [CLM-0064] [CLM-0061] |
| `end_market_customer` / "OEM / end-market buyer" | Split: `oem` and `ems_provider` are participants; end-use segments are `end_market` types | Buyers and demand segments are different things |
| "IDM foundry units" (value chain, not researched) | `idm_foundry_business` | Evidenced in foundry rankings and Intel Foundry [CLM-0553] [CLM-0258] |
| Money lens "co_investor" | `financial_co_investor` | Evidence is one company (Intel SCIP) [CLM-0257]; low confidence that it is a general category |
| Technology lens `memory_technology` | Not a separate type; DRAM/HBM/NAND are product types, and stacking is `packaging_technology` | Avoids two types for the same thing |

## New relation predicates

These were added only where the generic list could not express a relation the evidence shows:
- `hands_off_design_to`: the tape-out handoff of layout data [CLM-0457] [CLM-0425].
- `certifies_flow_for`: foundries certify EDA flows and IP [CLM-0420].
- `tests_for`: OSATs test chips for their customers [CLM-0488].
- `enables`: one technology is required for another; EUV is needed at 7 nm and below [CLM-0399].
- `accredits`: DMEA accredits trusted suppliers [CLM-0458].
- `measures`: a statistics body counts a population [CLM-0003].

## New research dimension

One dimension was added, `supply_chain_concentration` ("Supply-chain concentration & chokepoints"). SIA/BCG found more than 50 points in the chain where one region holds over 65% of the market [CLM-0546]. Several of them are single-firm or single-country chokepoints:
- EUV scanners come from one supplier [CLM-0506].
- About 96% of EDA was US-supplied in 2019 [CLM-0497].
- The listed photoresist makers are all Japanese [CLM-0524].
- Ukraine supplied about half of the world's neon, or about 70% by another estimate (CON-0011) [CLM-0531] [CLM-0532].

This topic does not fit cleanly under `geography`, which covers where things are, or `risks`, which covers what could go wrong. It needs its own units that measure concentration point by point.

## How confident we are in the categorisation

| Part of the tree | Confidence in the *category* | Basis |
|---|---|---|
| IDM, fabless, foundry, OSAT, EDA, IP, equipment, materials | Higher | Proposed independently by 3-5 of the 6 lenses, each with tier-1 sources (government reports, filings) behind the claims |
| Authorized distributor vs open market; design services; custom-silicon system companies; mask makers | Medium | 1-2 lenses; some evidence is companies describing themselves (`reported_claim`) |
| Product and end-market types | Higher for products (official WSTS taxonomy); medium for end markets (4 of 6 shares unconfirmed [CLM-0073]) | |
| Government functions | Medium | Well evidenced for the US, EU, NL, JP and CN; Korea and Taiwan rest on tier-2/3 news [CLM-0354] [CLM-0356] |
| critical_mineral_producer, manufacturing_software_vendor, financial_co_investor, environmental_chemical_regulator, patent_licensor | Low | One or two claims each. The environmental regulator's semiconductor relevance is itself unknown [CLM-0334] [CLM-0335] |
| Commercial arrangements | Medium | Each is evidenced in one or two company filings, not as an industry norm |

## What we still don't know

- **Types that may be missing.** Specialised logistics providers [CLM-0568]. Fab construction and cleanroom contractors, gas purifiers as a separate step, reclaim wafers, and probe-card makers are also candidates (RU-0046). Cloud providers as *buyers* of chips may need a type: NVIDIA holds US$27bn of cloud service agreements [CLM-0193], a flow in the opposite direction that we do not understand yet.
- **Where to count foundry revenue.** WSTS probably does not count foundry wafer revenue as a separate population. This is an inference [CLM-0009]. TSMC's "Foundry 2.0" definition, by contrast, adds packaging, masks and IDM manufacturing (CON-0004) [CLM-0064] [CLM-0065].
- **How WSTS assigns sales to regions.** The basis is not public [CLM-0080] (INT-0001). Chips designed by system companies for their own use may also be missing from the market total (INT-0002).
- **Business-model shares.** No time series of fabless vs IDM share was found [CLM-0152].

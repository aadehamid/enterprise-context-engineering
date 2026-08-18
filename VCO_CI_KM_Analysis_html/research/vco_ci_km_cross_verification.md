# Cross-Verification — VCO Lookback/Backcasting & CI Knowledge Management Study
**Date:** 2026-07-18 | **Inputs:** vco_ci_km_dim01.md … dim12.md | **Method:** Orchestrator comparison of all dimension outputs; tier classification per deep-research-swarm Phase 4.

## A. HIGH CONFIDENCE (confirmed by ≥2 dimensions from independent sources)

| # | Finding | Corroborating dimensions |
|---|---------|--------------------------|
| H1 | The "plan vs actual" gap ("margin leakage") between LP plan, schedule, and operations is the industry's central, explicitly named lookback problem; it is quantified, persistent, and only partially closed even at best-in-class operators | dim01, dim02, dim03, dim04, dim08 |
| H2 | Lookbacks are predominantly *variance quantification/reporting* (margin bridges, benchmark gaps, variance commentary) and rarely convert into institutionalized causal learning; the loop from insight → updated planning models/policies is open at almost every link | dim02, dim03, dim08, dim10 |
| H3 | Lessons are generated but not retained or reused — proven at the severest level by CSB repeat-incident records (Texas City, Richmond, Toledo, Anacortes, Geismar) and by lessons-learned system audits (NASA LLIS GAO/OIG) | dim04, dim08, dim10, dim11, dim12 |
| H4 | Downstream data is structurally fragmented across historians/DCS/LIMS/CMMS/ERP/TMS/ETRM/POS with no consistent keys or semantics; ISA-95 L3/L4 boundary is the chronic failure point | dim02, dim04, dim05, dim07 |
| H5 | Decision rationale/assumptions/trade-offs are systematically not captured (emails, logbooks, heads); industrial "contextualization" practice covers data/asset context, not decision context | dim07, dim11, dim12 |
| H6 | LP model maintenance is person-dependent, senior-specialty-owned, episodic (vector regeneration "once in a year or few years"); monthly backcasting exists only in best-practice specs (e.g., Aramco) | dim02, dim08 |
| H7 | KPI definitions (margin, availability, utilization, OTIF, emissions intensity) are non-standard and non-portable, blocking cross-asset and longitudinal comparison; functional KPIs structurally conflict (refinery push vs depot pull) | dim03, dim04, dim09 |
| H8 | Backcasting fails at the embedding/implementation interface: end states idealized, interim milestones fragile (Shell 2035 target retired; BP abandoned), capex misaligned (TPI: 98% not aligned), pathways updated episodically by investor pressure rather than evidence triggers | dim06; corroborated by dim01 (IEA overcapacity data) |
| H9 | RCA practice quality is shallow and non-reproducible: method pluralism, single-cause bias, "cause of mutual convenience", ~45–70% action implementation, compliance-anchored investigation (PSM doesn't require RCA) | dim04, dim10 |
| H10 | Institutional memory is person-held and at demographic risk ("Great Crew Change": >45% tenured retiring in 5–7 yrs); rotation and blame culture compound loss of decision context; psychological safety is the binding constraint on candid lookbacks | dim07, dim11 |
| H11 | Lessons-learned/KM failure modes are stable and well-catalogued (capture without reuse, black-hole repositories, no ownership, no context, no conversion into standards); successful counter-examples share: resourced curator roles, validation, quality tiering, push dissemination, in-workflow capture, communities | dim11, dim12 |
| H12 | GenAI does not compensate for weak KM — it amplifies it; <1% of unstructured enterprise data is AI-consumable; KM maturity (taxonomy, context, tiering, governance) is a prerequisite for AI-enabled lookback | dim07, dim12 |

## B. MEDIUM CONFIDENCE (single authoritative source, or vendor-sourced quantification)

- M1. End-to-end VCO value ≈ $30–85M/yr mid-sized refiner; crude/yield optimization $0.50–1.00/bbl (dim01, consultancy estimates)
- M2. Margin capture rate as public lookback KPI (Marathon 105% FY2025; Suncor 96% vs 5-2-2-1) with decomposition warnings (dim03, company disclosures)
- M3. Solomon RAM/Fuels benchmarking as dominant external retrospective; ~850 staff-hours data effort per study; top-vs-bottom ≈ 7% PRV (dim03, dim04, Solomon)
- M4. IPA capital-project lookbacks: FEL-1 schedule slip ~50%; 22% megaproject success rate; slip "remarkably constant" (dim03, IPA)
- M5. Forecast bias: WEO 5-yr price MAPE ~37%; professionals don't beat random walk; FVA: 52% of forecasts worse than naive (dim03, dim10, academic)
- M6. Energy ≈ 60% of EU refinery cash opex; fired heaters 74–78% of energy use (dim01, Concawe)
- M7. CMMS/event data quality structural defects: 93% Friday closures; misc/other code evasion; timestamp misalignment "a major obstacle" (dim10, NIST/PHM)
- M8. Backcasting tech-stack consensus (efficiency→electrification→H₂→CCS→offsets) and OGCI/Wood >65% by 2040 claim (dim06)
- M9. Demurrage/port-call documentation still "PDFs and memory"; recurring logistics bottlenecks unfixed for decades absent regulatory force (dim05)
- M10. ISO 30401 / APQC maturity levels; most orgs at KM levels 1–2; KCS "reuse is review"; Admiralty-Code tiering analogue; ADR decision-record template (dim12)
- M11. Retail pricing optimization is a mature but decoupled island (Kalibrate scale/benefits) (dim02)
- M12. Industry clean-energy capex ~2.5% of total (IEA 2022) vs ~50% NZE benchmark (dim06)

## C. LOW CONFIDENCE / USE WITH CARE

- L1. Vendor benefit claims generally (AVEVA $50–300M/refinery/yr; ExxonMobil 70¢/bbl; "500K/hr downtime"; AI demurrage recovery 10–20%) — unaudited marketing; use directionally only
- L2. "50–70% of CI programs fail" — contested statistic; all datasets agree sustainment is the minority outcome but the precise figure is unreliable (dim08)
- L3. IBM $3.1T data-quality cost and Gartner $12.9M/org — methodology caveated (dim07)
- L4. "2–3 yr rotation cadence" as driver of context loss — plausible, thinly sourced (dim11)

## D. CONFLICT ZONES (analyzed; resolved analytically where possible)

- CZ1. **Crack spread levels.** dim01: 3-2-1 averaged ~$17/bbl (2007–20) and $29.50 (2021–25) [TP ICAP/PVM] vs trade-press 2025 avg $12–15 and 10-yr avg $8–10. *Resolution:* different benchmark formulas, regions, and averaging windows; not a factual contradiction. Present as ranges with basis noted.
- CZ2. **Margin-leakage magnitude.** $0.05–0.15/bbl (ARC/AspenTech, closed-loop integration) vs ~$0.50/bbl (IZZI/AVEVA, LP decay) vs ~$0.25/bbl (AIGC) vs "up to 25% of planning margin" (Digital Refining, crude-logistics case) vs "up to 10% of crude margin" (Aramco Yanbu). *Resolution:* different constructs (integration uplift vs model decay vs specific-event loss). Treat as layered components of one gap; cite per construct.
- CZ3. **VCO value pool.** dim01 $30–85M/yr (mid-sized) vs dim02 AVEVA $50–300M/yr per refinery vs ARC $0.05–0.15/bbl. *Resolution:* vendor best-case vs independent incremental estimate; report the spread and attribute.
- CZ4. **Downtime cost variance >100×.** dim04 documents $1.2–3M/day (Valero FCC overrun, EIA) vs KBC per-unit marginal values vs vendor "$500K/hr". *Resolution:* depends on basis (lost conversion margin vs total revenue vs replacement); use the margin-on-lost-conversion basis (dim04 recommendation) and flag spread.
- CZ5. **Decarbonization pathway sequencing.** OGCI/Wood: electrification primary (>$65% by 2040, <$150/t) vs WEF/IEA: CCUS primary (+7–9% cost). *Resolution:* genuine disagreement in the field; present both, note dependence on power price/availability assumptions.
- CZ6. **Availability KPI bases.** BP reports Solomon OA; Valero reports MA; utilization can exceed 100% of nameplate. *Resolution:* definitional; evidence of H7 rather than contradiction.
- CZ7. **"Closed loop" vendor claims vs own evidence.** Vendors market closed-loop plan-schedule-actual integration while their practice decks describe Excel-based, person-dependent loops. *Resolution:* frontier vs baseline maturity bimodality (dim02 KF9); both true at different sites.
- CZ8. **Unused-data share.** Seagate/IDC 68% vs AVEVA 43% vs "1% of rig sensor data examined" (McKinsey). *Resolution:* different populations/definitions; directionally consistent (large majority unused).

## E. Phase 5 determination
No unresolved factual conflicts requiring targeted validation sub-agents: all Conflict Zone items are construct-definition/basis differences or genuine field disagreements to be reported as such. Proceeding to Phase 6.

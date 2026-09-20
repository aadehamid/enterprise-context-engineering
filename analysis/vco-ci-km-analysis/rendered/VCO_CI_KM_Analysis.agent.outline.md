# From Variance Reports to Institutional Learning: Downstream Value Chain Optimization, Lookback/Backcasting Practice, and the Case for a CI-Focused Knowledge Management Foundation

## Executive Summary (~800 words; written last; self-contained per consulting style)
### Key Findings
#### Downstream companies have industrialized the measurement of plan-vs-actual gaps but not learning from them; the missing layer is governed knowledge/context infrastructure, not more analytics
#### Eight systemic gaps — data fragmentation, reporting- (not learning-) oriented lookbacks, an open lookback→planning loop, weak uncertainty treatment, KPI misalignment, weak causal discipline, organizational knowledge loss, and backcasting's embedding failure — explain why lookbacks/backcasts underperform
#### COMPANY's CI initiative already generates the raw knowledge; the risk is context decay across decision cycles (rotation, attrition, annual model updates, episodic strategic reviews)
#### A CI-first KM foundation is the correct entry point: CI is the one function whose output *is* knowledge, with short, monetizable value chains (margin leakage components of $0.05–0.50/bbl; VCO value pools of $30–85M/yr for a mid-sized refiner)
### Required elements: 1 table (the eight gaps → KM requirement mapping preview); no charts

## 1. The Downstream Value Chain and What Value Chain Optimization Means (~3,200 words, 2 tables, 1 chart)
### 1.1 The downstream value chain for an integrated refiner/marketer
#### 1.1.1 Crude and feedstock procurement: benchmark ± differential pricing, light/heavy differential swings (+$15.51/bbl 2006 to −$3.64/bbl 2011), GPW/netback valuation, and why crude ≈ 85% of refining operating cost makes feedstock selection the largest value lever
#### 1.1.2 Refining operations: CDU/VDU, conversion units (FCC, hydrocracker, coker, reformer, alkylation), hydrotreating/hydrogen, blending, utilities; Nelson Complexity (topping 1 → coking 9+; US avg ~10) as the determinant of crude optionality and slate
#### 1.1.3 Product slate optimization: gasoline/diesel/jet/LPG/petchem feedstocks/fuel oil/specialties; crack spreads re-rating (~$17/bbl avg 2007–20 vs ~$29.50/bbl 2021–25, basis-dependent); energy ≈ 60% of EU refinery cash opex linking operations to both margin and emissions
#### 1.1.4 Logistics layer: terminals, tank farms, 95,000-mile US product pipeline network, shipping/rail/truck; distribution+marketing ≈ 10–16% of pump price; crude-by-rail $8.54–13.00/bbl
#### 1.1.5 Marketing channels: wholesale/rack, B2B, aviation, bunker, petrochemicals, export, retail; razor-thin retail fuel margins (~$0.13/gal net) vs non-fuel profit (39% of revenue, 63% of gross profit)
### 1.2 What "VCO" means in practice
#### 1.2.1 VCO as integrated planning and optimization from crude selection through refining and logistics to marketing and pricing — a layered stack (LP planning → scheduling/blending → APC/DCS execution) wrapped by network optimization, demand forecasting, retail pricing, ETRM
#### 1.2.2 The LP oligopoly (Aspen PIMS, Honeywell RPMS, Haverly GRTMPS, AVEVA Spiral/USC, Chevron PETRO); multi-period/multi-site extensions; scheduling state of practice (Aspen Petroleum Scheduler >45% of refineries) with Excel as documented maturity floor
#### 1.2.3 S&OP/IBP convergence (SAP IBP, aspenONE SCM, ExxonMobil–Kinaxis 2024) vs ARC's caution that O&G has "historically relied on numerous spreadsheets and manual processes"; retail pricing as a mature but decoupled optimization island (Kalibrate scale)
#### 1.2.4 VCO as a cross-functional organization: three observed models (site LP custodians/economists; central supply & optimization groups; national hydrocarbon-system planning at Aramco incl. monthly "back-casting" LP-gap reports)
### 1.3 Why decisions across the chain matter: margin, risk, emissions, service, strategy
#### 1.3.1 Decision couplings: crude slate ↔ unit constraints ↔ logistics feasibility ↔ channel netbacks; local optima destroy enterprise value (refinery push vs market pull)
#### 1.3.2 Quantified stakes: VCO value pools ($30–85M/yr mid-sized refiner; crude/yield optimization $0.50–1.00/bbl; vendor best cases vs ARC's $0.05–0.15/bbl independent estimate); structural pressures (IEA demand peak ~2027; overcapacity 11.4 mb/d by 2030; McKinsey value pool −35% by 2030s)
### Required elements: table of chain segments with decision levers and value stakes; table of the VCO stack layers with tools and planning horizons; 1 chart (crack spread re-rating or margin-leakage component ranges, basis noted per Conflict Zone CZ1/CZ2)

## 2. How Lookback and Backcasting Are Done Today (~4,200 words, 3 tables, 1 chart)
### 2.1 Margin and performance retrospectives
#### 2.1.1 Margin capture rate as the public lookback KPI (Marathon 105% FY2025; Suncor 96% vs custom 5-2-2-1) and why practitioners demand decomposition (inventory lag 15–45 days/phantom profit, RINs, hedges, yield mix, basis)
#### 2.1.2 The monthly controller bridge (crack spread → reported gross margin) and mandatory yield reconciliation; Solomon Fuels Study as dominant external retrospective (320+ refineries, ~850 staff-hours data effort, cause-level gap analysis)
#### 2.1.3 The LP plan-vs-actual gap ("margin leakage"): quantified components ($0.05–0.15/bbl closed-loop integration; ~$0.50/bbl LP decay persisting months-to-years; up to 25% of planning margin in crude-logistics case; up to 10% of crude margin at Yanbu) — presented as layered constructs per Conflict Zone CZ2
### 2.2 Operations and reliability lookbacks
#### 2.2.1 Solomon RAM benchmarking on monetized downtime; MA ≥ OA ≥ on-stream availability stack (EDC-weighted); top-vs-bottom ≈ 7% of Plant Replacement Value; investor-grade availability KPIs (BP OA-basis vs Valero MA-basis)
#### 2.2.2 Incident investigation and RCA practice: OSHA PSM compliance anchor (no RCA mandate; 48h/team/5-yr retention), EPA 2024 RMP root-cause mandate and AFPM resistance; method pluralism (5-Why → TapRooT/Apollo/ICAM) and CCPS's multiple-root-cause discipline
#### 2.2.3 Lookback data plumbing: historian event frames, ISA-18.2 alarm KPIs (Toledo: 3,712 alarms/12h), LIMS quality records, production accounting mass balances — rarely fused, on different clocks
#### 2.2.4 The operational→commercial bridge: downtime monetization anchors ($1.2–3M/day FCC turnaround overrun; KBC per-unit values; DOE shutdown ledger; PES $750M loss) — mostly manual
### 2.3 Supply chain, logistics, and commercial lookbacks
#### 2.3.1 Inventory/working-capital reviews (days of supply, DIO/CCC; $200B trapped cash estimate); stockouts visible mainly in crises (UK 2021; OR Tambo)
#### 2.3.2 Demurrage and port/rail lookbacks: 72-hr SHINC laytime norms, claims from "PDFs and memory", berth/jetty root causes ($2M/yr refiner case), rail demurrage contention under PSR
#### 2.3.3 OTIF and network utilization: definition fragmentation (97% internal vs 82% customer = $800k penalties); pipeline allocation/interface losses ($50k/interface; automation cuts 40–75%); terminal occupancy reporting (Vopak 84–94%)
#### 2.3.4 Commercial lookbacks: pricing post-mortems tool-led (Kalibrate/PDI), channel/customer/netback profitability redesigns; campaign ROI attribution "a constant struggle"; ETRM post-trade retrospective tooling absent in public evidence
### 2.4 Backcasting practice
#### 2.4.1 Method origins (Robinson 1982; Holmberg; Quist–Vergragt) and the canonical weakness at the embedding/implementation step; forecasting vs backcasting complementarity
#### 2.4.2 Refinery decarbonization backcasts: technology-stack consensus (efficiency→electrification→low-carbon H₂→CCS→offsets); OGCI/Wood >65% by 2040 vs WEF/IEA CCUS-primary (+7–9% cost) — genuine field disagreement (CZ5)
#### 2.4.3 Corporate instruments: exploratory scenarios (Shell tradition; Horizon normative) vs laddered targets, with Shell's own firewall ("not expressions of strategy"); portfolio backcasting margin/policy-led (IEA Oil 2025 closures; conversions: Rodeo, Martinez, Vertex reversal)
#### 2.4.4 Connection to capital planning and CI: clean-energy capex ~2.5% vs ~50% NZE benchmark; TPI 98% misalignment; milestone fragility (Shell 2035 retired; BP abandoned); episodic updates via investor votes vs DAPP signposts/triggers
### 2.5 Tooling and data used today — and the intended learning loop
#### 2.5.1 The full tooling map (BI dashboards, LP/APS, S&OP, historians, ERP, CMMS, TMS/TAS, demand forecasting, pricing engines) and how companies conceptually intend lookback/backcasting to improve future decisions (PDCA intent vs practice, forward reference to §3)
### Required elements: table of lookback types × cadence × artifact × tooling × known weakness; table of backcasting instruments; table of margin-leakage components with basis notes; 1 chart (margin-leakage component ranges or availability stack schematic)

## 3. Why Lookback and Backcasting Underperform: Eight Systemic Gaps (~4,800 words, 2 tables, 1 chart, 4 named case examples)
### 3.1 Data fragmentation and weak context capture
#### 3.1.1 The siloed stack by design (OT built for uptime, IT for transactions; ISA-95 L3/L4 boundary); historians holding 10–20 yrs of data isolated from analytics; terminal/POS vendor walled gardens
#### 3.1.2 No consistent keys/taxonomy/semantics (asset hierarchies conflicting; ISO 15926 vs MIMOSA camps; incomplete RDLs); quantified impact (>50% engineer time searching; 32% of data used; 1% of rig sensor data examined; 1.5–2% material imbalances ≈ up to $5M/yr)
#### 3.1.3 Decision rationale/assumptions/trade-offs systematically lost (emails, paper logbooks ~80% unstructured; up to 80% of O&G staff time hunting unstructured data); industrial "contextualization" covers data context, not decision context
### 3.2 Reporting-oriented lookbacks rather than learning-oriented lookbacks
#### 3.2.1 Variance quantification is mature, causal learning is not: post-audits conducted ~36% of the time, "did not affect future capital budgeting decisions"; IPA slip "remarkably constant" for a decade despite lessons-learned rhetoric
#### 3.2.2 Findings become point solutions/local corrective actions; no standard capture of broader themes, reusable guidance, or decision rationales; NASA LLIS as canonical built-but-bypassed repository (58% couldn't retrieve right lessons; 6/28 PMs found it useful)
### 3.3 The open loop between lookback findings and planning/optimization
#### 3.3.1 LP vectors regenerated "once in a year or few years", Excel-based and person-dependent; monthly backcasting aspiration vs "time consuming, hard to pinpoint causes" reality; corporate LP gatekeeping
#### 3.3.2 No systematic feedback into logistics network models, inventory policies, demand forecasts, pricing, contracts; actuals capture (Sigmafine-class) mature but handoff manual; S&OP/IBP maturity plateaus after 3–4 years
#### 3.3.3 Single-loop vs double-loop learning (Argyris): defensive routines and "skilled incompetence" keep embedded model assumptions unchallenged
### 3.4 Limited treatment of uncertainty and robustness
#### 3.4.1 Point-forecast reliance despite evidence: WEO 5-yr price MAPE ~37%; professionals don't beat random walk; futures under-predict ~$1.8/bbl at 6 months; OPEC/EIA opposite institutional biases
#### 3.4.2 Narrow scenario ranges in backcasting; lookbacks measure error magnitude (MAPE pathologies) not structural bias in assumptions/models; FVA evidence that 52% of forecasts fail vs naive and management adjustments destroy value; SR 11-7 as the regulated-rigor contrast
### 3.5 KPI misalignment and inconsistent metrics
#### 3.5.1 Structural functional conflict (refinery throughput/cost vs depot fill rates vs logistics freight cost); shared-KPI remedy worth $0.2–0.6/bbl (BCG)
#### 3.5.2 Definition non-portability: margin (gross/net/cash/variable/RC vs accounting), availability (OA vs MA vs >100% utilization cases), OTIF (no standard; $800k penalty case), emissions intensity (allocation swings ~10 gCO2e/MJ)
#### 3.5.3 Consequence: reviews debate whose number is right instead of what to change; Goodhart's Law and incentive design (Wells Fargo analogue; Solomon-quartile-linked executive bonuses)
### 3.6 Weak causal inference and RCA discipline
#### 3.6.1 Dashboard-era correlation reading (87% low BI maturity; confirmation bias; Google Flu "big data hubris") vs causal analysis
#### 3.6.2 Event data quality: free-text CMMS, cause-code evasion, 93% Friday closures, timestamp misalignment "a major obstacle"; API 754 Tier-1 under-classification 10–20%
#### 3.6.3 RCA shallowness: "cause of mutual convenience", administrative fixes, 45–70% implementation, "tombstone effect", no controlled validation; CSB repeat incidents (Texas City 8 uninvestigated precursors; Richmond 2002 flag; Toledo 2019→2022; Geismar known-bad gasket 14 yrs)
### 3.7 Organizational and governance barriers
#### 3.7.1 Tribal knowledge and the Great Crew Change (>45% tenured retiring in 5–7 yrs; 41% rarely/never capture retiree know-how; $31.5B/yr Fortune 500 sharing losses)
#### 3.7.2 Rotation/mobility erasing decision context between planning cycles; improvement gains not self-sustaining ("rubber band effect"; ~12% of transformations sustain past 3 yrs)
#### 3.7.3 Blame culture and defensive narratives suppressing candor (Edmondson detection-vs-rate; variance review as "monthly autopsy"); lessons governed for documentation compliance, not transfer (~70% repeat causal factor)
### 3.8 Backcasting-specific weaknesses
#### 3.8.1 Idealized/politically driven end states; scenario-to-plan firewall; capex misalignment (TPI 98%; 2.5% vs 50%)
#### 3.8.2 Under-specified pathways: milestones collapse at the planning horizon (Shell 2035); no signposts/triggers; pathways not re-baselined as evidence accumulates; academic verdicts on time-path neglect
### 3.9 How the gaps manifest: four downstream case vignettes
#### 3.9.1 Recurring logistics bottleneck (OR Tambo decade-known storage constraint; berth/jetty demurrage root causes recurring across seasons/teams)
#### 3.9.2 Systematic crude selection/planning issues (LP decay persisting months-to-years; crude-logistics plan-vs-actual erosion up to 25%)
#### 3.9.3 Repeated margin erosion in channels (capture-rate decomposition obscured; pricing post-mortem discipline absent; campaign ROI unattributed)
#### 3.9.4 Misaligned decarbonization pathways (conversion reversals — Vertex; Rodeo reduced rates; milestone retirements; OGCI vs CCUS sequencing dispute never reconciled with operating plans)
### Required elements: table mapping eight gaps → evidence anchors → primary affected VCO decisions; table of metric-definition fragmentation; 1 chart (e.g., forecast-error/bias evidence or CI sustainment statistics); 4 case vignettes as boxed mini-cases

## 4. COMPANY's Situation: A CI Program Generating Knowledge Faster Than It Can Keep It (~2,000 words, 1 table)
### 4.1 What COMPANY has built
#### 4.1.1 The VCO CI initiative: decision lookback matrix, decision-point maturity assessments, defined governance modes, operational lookbacks, refinery backcasts, regional backcasting, post-audits, recurring CI reporting
#### 4.1.2 The knowledge already being generated: findings/lessons, decision rationales and narratives, improvement opportunities and recommendations
### 4.2 The core problem: capture, context, governance, discoverability
#### 4.2.1 Retention/reuse resting on individual experience, informal follow-up, person-dependent knowledge; no standardized, consistently discoverable capture of broader themes, decision context, reusable guidance
#### 4.2.2 The three stated risks — recurring issues, institutional knowledge loss through role change/attrition, future decisions made without prior learning — mapped to the industry evidence (Great Crew Change; ~3-year organizational memory; 70% repeat causal factor)
### 4.3 Why COMPANY mirrors and amplifies the generic gaps
#### 4.3.1 The paradox of a mature CI investor: more lookbacks/backcasts → more knowledge artifacts → faster context decay; amplification mechanism (cadence mismatches: monthly lookbacks vs annual LP updates vs 2–3-yr rotations vs episodic strategic reviews)
#### 4.3.2 What is different for COMPANY: the raw material and governance intent already exist — the deficit is the knowledge/context layer, not the CI process layer; failure-mode preview (NASA LLIS "built but bypassed") if capture is attempted without quality tiering, ownership, and in-workflow integration
### Required elements: table — COMPANY's stated risks × industry evidence anchors; no charts (interpretive chapter)

## 5. Requirements for a CI-Focused Knowledge Management and Context Management Capability (~4,000 words, 3 tables; no solution architecture)
### 5.1 Purpose and scope of the capability
#### 5.1.1 Mission: capture, contextualize, govern, and enable reuse of CI-generated institutional knowledge; convert findings, lessons, rationales, recommendations, SME knowledge into structured, searchable, reusable knowledge assets; improve future planning, scheduling, optimization, execution decisions
#### 5.1.2 Knowledge scope: formal deliverables (backcast reports, lookback decks, post-audits, CI reports, decision documentation, recommendations, governance outputs) + informal/semi-structured sources (emails, minutes, recordings, working notes, SME mental models) + all CI processes beyond Integrated Backcasting
### 5.2 Capability dimension 1: requirements reconciliation and validation
#### 5.2.1 Reconciling VCO KM functional requirements with AI-enabled KM requirements from the Integrated Backcasting lens; identifying aligned/unique/conflicting/missing requirements; validating against full CI scope — requirement: a governed requirements baseline with traceability, not a one-off workshop output
### 5.3 Capability dimension 2: CI knowledge source inventory and assessment
#### 5.3.1 Identifying sources/artifacts for capture; assessing quality, ownership, reuse readiness — requirement: a living inventory with per-source quality/ownership metadata, addressing the evidence that organizations don't know what they know (and that ~80% of relevant content is unstructured)
### 5.4 Capability dimension 3: knowledge taxonomy and contextualization framework
#### 5.4.1 Naming conventions, categories, tags, metadata, domain structures, capture templates, contextual attributes — designed around the three context layers (data context, decision context, learning context), with ADR-style decision records (context/decision/consequences/status) as the decision-rationale template class
#### 5.4.2 Templates for lessons learned, best practices, decision rationales, recommendations, expert judgment — embedding NASA's significance/validity/applicability quality gates and mandatory context fields (constraints, information available, alternatives considered), which also serve psychological safety (system-framed, not blame-framed records)
### 5.5 Capability dimension 4: knowledge quality tiers and confidence model
#### 5.5.1 Distinguishing authoritative/reviewed/approved from indicative/support sources; how source type, review status, recency, business relevance, approval status drive confidence and reuse — analogues: Schlumberger tiering, Admiralty-Code source/content ratings, KCS "reuse is review"
#### 5.5.2 Why tiering is the keystone: enables governance, trust-based reuse, and AI grounding; the LLIS failure as the counter-case of un-tiered capture
### 5.6 Capability dimension 5: governance model and lifecycle design
#### 5.6.1 Lifecycle states (draft → verified → approved → deprecated → archived), review/approval workflows, ownership roles, versioning, auditability, refresh triggers (event- and time-based), archival rules, escalation paths — addressing the documented failure patterns (no closure verification, unsearchable storage, learning stays local)
#### 5.6.2 How content moves from draft/indicative to approved and reusable; "reuse is review" as the quality loop; interface closures required: finding→planning model, lesson→standard, pathway→plan, person→system
### 5.7 Capability dimension 6: industry perspective
#### 5.7.1 How downstream and adjacent process industries approach KM, contextualization, quality tiering, governance, AI readiness (CCPS RBPS "Learn from Experience", API 754/75, ISO 30401, APQC maturity L1–5, CALL/Schlumberger/Shell CoP counter-examples) — informing COMPANY's framework while COMPANY retains ownership of business context, decision logic, operating model
### 5.8 Capability dimension 7: technology approach and architecture direction (requirements only, no vendor/architecture selection)
#### 5.8.1 Scalable, AI-ready, aligned with COMPANY standards and digital strategy; GenAI amplifies rather than fixes KM (<1% of unstructured data AI-consumable; >50% rate data foundations inadequate); context engineering as the operational discipline; hallucination control as governance (source binding, citation-required, refusal-on-weak-evidence, human approval for high-impact outputs)
#### 5.8.2 Principle: AI enablement leverages captured context rather than replacing COMPANY decision logic; KM maturity as prerequisite, not parallel track
### 5.9 Capability dimension 8: implementation roadmap (sequencing logic, dependencies, decisions, resourcing, process change)
#### 5.9.1 Sequencing: contextualize existing CI assets → stand up taxonomy/tiering → governance activation → pilots on highest-pain loops → expansion → AI-enabled capabilities; dependencies and sustainment requirements (management routines; the ~12% transformation sustainment warning; sponsor and ownership prerequisites)
### 5.10 Traceability: each dimension mapped to the §3 gaps it closes
#### 5.10.1 Consolidated mapping table (eight gaps × capability dimensions × evidence anchors) demonstrating root-cause coverage
### Required elements: 3 tables incl. the consolidated traceability map; no charts

## 6. The Conceptual Link: How Context Management Makes Lookback and Backcasting Effective (~2,400 words, 1 table, 1 diagram-style chart optional)
### 6.1 From the value chain to the learning loop
#### 6.1.1 Recap of the chain: VCO decisions → outcomes → lookback explanation → lessons → updated planning assumptions/models → better decisions; where each §3 gap breaks the chain
### 6.2 What robust contextualization delivers
#### 6.2.1 Accuracy, reproducibility, comparability of lookbacks over time (versioned assumptions against decisions; separation of market-driven vs execution-driven variance — bad luck vs bad decisions)
#### 6.2.2 Pattern visibility across lookbacks and CI processes (recurring decision biases, structural bottlenecks, cross-functional misalignments) — from episodic artifacts to longitudinal evidence
#### 6.2.3 Systematic feed of lessons into planning, optimization models, and governance (closed PDCA; double-loop capability; living backcast pathways with signposts and re-baselining triggers)
### 6.3 Why CI-first, not generic enterprise KM
#### 6.3.1 CI/VCO is where decision quality directly moves margin, resilience, emissions, customer outcomes; value chains are short and monetizable (leakage components; reliability gaps ≈ 7% PRV; VCO value pools)
#### 6.3.2 CI already generates the raw knowledge as a byproduct — marginal capture cost; and contextualized CI knowledge is the high-leverage asset for future AI enablement (KM as prerequisite for AI, not parallel investment)
### Required elements: table — lookback limitation → contextualization mechanism → decision impact; optional diagram (learning-loop chain)

## 7. Strategic Insights and Implications (~1,600 words)
### 7.1 Eight cross-cutting insights from the research
#### 7.1.1 Insights 1–8 (measurement industrialized, learning not; episodic artifacts and context decay; three context layers; interface failures map to KM requirements; variance misattribution; tiering as keystone; CI-first rationale; culture-systems coupling), each with derived-from evidence and implication for COMPANY
### 7.2 Implications for COMPANY's next decisions
#### 7.2.1 What to decide first (requirements baseline, quality tiering, ownership model) and what to defer (AI enablement) — with confidence grades per insight
### Required elements: no tables required; prose synthesis with inline citations

# References
## VCO_CI_KM_Analysis.agent.outline.md
- **Type**: Report outline
- **Description**: This outline file
- **Path**: /mnt/agents/output/VCO_CI_KM_Analysis.agent.outline.md
## vco_ci_km_dim01.md … vco_ci_km_dim12.md
- **Type**: Research dimension reports
- **Description**: 12 deep-research evidence files with verbatim sources
- **Path**: /mnt/agents/output/research/
## vco_ci_km_cross_verification.md
- **Type**: Confidence tiers and conflict-zone analysis
- **Description**: Phase 4-5 verification results
- **Path**: /mnt/agents/output/research/vco_ci_km_cross_verification.md
## vco_ci_km_insight.md
- **Type**: Cross-dimension insights
- **Description**: Phase 6 synthesis feeding chapters 4–7
- **Path**: /mnt/agents/output/research/vco_ci_km_insight.md
## user_pasted_clipboard_long_content_as_file_You are an expert an.txt
- **Type**: User brief (task specification)
- **Description**: COMPANY's six-part analysis brief; chapters 4–6 must follow it closely
- **Path**: /mnt/agents/upload/user_pasted_clipboard_long_content_as_file_You are an expert an.txt

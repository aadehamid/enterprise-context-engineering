# Dimension 03 — Margin, Financial & Commercial Lookback Practices in Downstream Refining & Marketing

**Research date:** 2026-07-18 | **Method:** 36 independent web searches (consultancies, IPA publications, trade press, academic papers, vendor blogs, benchmarking references) | **Analyst:** VCO/CI-KM deep-research (Dimension 03)

---

## KEY FINDINGS (Top Summary)

1. **"Margin capture" is the industry's de-facto lookback KPI.** Major refiners publicly report a quarterly "margin capture rate" — realized gross margin ÷ a company-specific benchmark index (e.g., Marathon: 114% capture Q4 2025, 105% FY2025; Suncor: 96% vs its custom "5-2-2-1 index"). Finance practitioners warn the single headline number "obscures the reasons for under-capture" and should always be decomposed into a bridge: inventory-method timing, yield mix vs. crack formula, RIN costs, hedge timing, basis. [^7^][^8^][^9^][^12^]
2. **The "LP plan vs. actual" gap is a recognized, monetized problem — but closing it is framed mostly as a real-time optimization issue, not a causal-learning exercise.** Vendors quantify "margin leakage" between plan, schedule and operations at $0.05–0.15/bbl (AspenTech), ~$0.50/bbl from LP model inaccuracy persisting "for months or even years" (IZZI/AVEVA), and ~$0.25/bbl from plan-schedule-actual gaps (AIGC). Literature acknowledges "many approaches" exist for "attributing the money values of these variations," implying no settled standard for retrospective driver attribution. [^1^][^2^][^3^][^4^][^5^]
3. **The monthly "controller bridge" (economics-to-reported margin) is the canonical cadence artifact.** Best practice described in refinery-controlling literature: a written, signed, one-page monthly bridge reconciling benchmark crack spread → reported gross margin, covering inventory lag (15–45 days, "phantom profit"), RINs, hedges, yield variance (>0.5%/product investigated), and fixed-cost absorption. Yield reconciliation is a required close procedure. [^12^]
4. **Benchmarking (Solomon Fuels Study) is the dominant external retrospective mechanism** — biennial, 320+ refineries (~85% of global capacity), an average **850 hours of internal data-collection effort per refinery per study**, producing gap analyses and "bridging cash margin to what is possible based on refinery configuration and location." Solomon states its results presentations have evolved "to delve into the underlying causes of these gaps" — a shift from variance reporting toward causal learning. [^13^][^14^][^15^]
5. **Commercial lookbacks are tool-led but decision-post-mortem discipline is weakly evidenced.** Fuel-pricing vendors (Kalibrate, PDI) sell "analyze past pricing decisions to understand their impact on profitability," price/margin reporting and elasticity models; consulting demand exists for "channel profitability, customer profitability, and regional netbacks" redesign. Evidence of *structured* pricing post-mortems or campaign evaluations in fuel retail is thin — convenience-retail ROI literature describes campaign attribution as "a constant struggle." [^16^][^17^][^18^][^19^]
6. **Post-audit/post-investment appraisal is institutionalized in capital projects but compliance is spotty and learning loops often fail.** Surveys: utilities conduct post-completion audits only ~36% of the time; 19.6% of firms have no review mechanism at all, and respondents said post-audits "did not affect future capital budgeting decisions." Textbook purposes (compare actual vs. forecast, explain differences, hold people responsible, improve future forecasts) are well documented. [^20^][^21^][^22^]
7. **IPA's database-driven "lookback" research quantifies systematic optimism:** average schedule slip vs. targets set at FEL 1 is 50% (80% range >120%); even FEL 3 estimates are off 17% on average; oil & gas megaprojects: only 22% "successful," 33% average real cost overrun (cost index 1.37), 30% execution schedule slip, 64% with "serious and enduring production attainment problems" in first 2 years. Middle East projects: median execution slip >30% since 2010 — "remarkably constant" despite lessons-learned rhetoric. [^23^][^24^][^25^]
8. **Forecast accuracy evidence shows structural bias downstream planners must absorb:** IEA WEO 5-year price projections MAPE ≈37% (supply only 4%); professional oil-price forecasters do not beat a random walk and under-predicted realized prices by ~6.5% on average (1989–2008 Consensus data); futures under-predict spot by ~$1.8/bbl at 6 months (~8%); OPEC and EIA show *opposite-directional institutional biases* (OPEC revises demand up +130 kb/d, EIA down −90 kb/d after 12 months). [^26^][^27^][^28^][^29^][^30^]
9. **Core tension for VCO design:** every actor (controllers, Solomon, IPA, pricing vendors) produces *variance quantification*, but repeated evidence shows variance reporting does not automatically become causal learning — post-audits don't change decisions, schedule slip persists "amazingly constant," turnaround lessons "are not systematically captured," and LP errors "persist for months or even years." The gap between *explaining variances* and *institutionalizing learning* is the open opportunity. [^2^][^22^][^24^][^31^]
10. **Tooling landscape today:** Excel/ERP-actuals bridges at close (controller practice), BI dashboards (AspenTech Performance Management), planning/scheduling suites (Aspen Unified PIMS + GDOT closed loop), data-reconciliation/yield-accounting layers (AIGC, Refinium), pricing suites (Kalibrate 50+ reports), and external benchmarks (Solomon, IPA). ETRM/CTRM post-trade retrospective tooling was **not** found in public sources — a notable silence. [^4^][^5^][^6^][^12^][^16^]

---

## 1. Margin Retrospectives: Realized Margin vs. Plan, Driver Decomposition, LP-vs-Actual Gaps

### 1.1 The LP plan-vs-actual gap is the central acknowledged problem

**Imubit (vendor blog, 2026-04-15)** frames the retrospective gap explicitly:
> "Refineries lose margin between LP plans and actual operations… The opportunity sits in the gap between what LP models plan and what refinery operations actually achieve. Every hour of suboptimal operation erodes value that no amount of downstream correction recovers." [^1^]
> "LP models assume linear relationships in a world of nonlinear chemistry, update on planning cycles rather than operating cycles, and treat each unit as an independent block… LP accuracy degrades quickly outside the conditions it was built on, and by the time the next planning run catches up, the refinery has already been operating suboptimally for hours or days." [^1^]

**Academic/industry literature (scialert.net, 2011)** confirms attribution practice is non-standard:
> "The use of Linear Programming (LP) tools for both long-term planning and day to day scheduling is fairly common in any refinery; still there is a gap between the LP run results and the actual operations. The related variations can be attributed to both external or market forces and internal operational constraints. There are many approaches followed for finding and attributing the money values of these variations in performances. Use of some of the LP tools is one of the best ways for identifying and quantifying these variations." [^2^]

**IZZI Business Services / AVEVA PI System presentation (LP accuracy – Best Practices)** on model maintenance as retrospective discipline:
> "For known reasons, LP process models become less accurate over time. In typical hectic work environment, significant LP errors can persist for months or even years. As a result, Margins are lower than they should be… Typical refiner with multi-crude processing should expect to see approximately 0.50$/BBL improvement in margin." [^3^]

**ARC Advisory on AspenTech V12 (Aspen Unified)** — "margin leakage" as named construct:
> "…a critical component of its overall strategy to address what the company refer to as 'margin leakage' between plan, schedule, and operations (process controls). AspenTech claims that, by aligning these activities, a refinery could increases margin, capturing from $0.05 to $0.15/bbl by vertically integrating planning, scheduling, and advanced process control in a closed loop." [^4^]

**AIGC (vendor)** on plan–schedule–actual reconciliation:
> "It is fully integrated with planning models, which reduces the gap between Plan vs. Schedule vs. Actual… resulting in up to 25 cents per barrel margin uplift and reduces product quality giveaway in blending." [^5^]

**Refinium AI (vendor platform, financial module)** — closest to a productized "lookback" tool:
> "Refinium Financial Analyzer — EBITDA, gross margin per barrel, product margin by slate, netback analysis and P10/P50/P90 scenarios. NPV, IRR, DSCR. **Plan-vs-actual variance with drill-down to operating cause.** CFO · CONTROLLER · PLANNING & ECONOMICS." [^6^]

### 1.2 "Margin capture rate" as the public reporting form of the lookback

**Marathon Petroleum (FY2025 Annual Report / Q4 2025 coverage):**
> "The reliability and competitiveness of our fully integrated value chains, as well as the depth of our commercial capabilities, enabled us to achieve 94% refining utilization and **105% margin capture** for the full year." [^7^]
> "Refining margins did the heavy lifting, with the company **capturing 114% of the benchmark crack spread, up from 96% in the third quarter**." (Motley Fool, 2026-02-21) [^8^]

**Suncor (2025 Annual Report)** — full reconciliation disclosure of a custom index:
> "…resulting in **refining and marketing margin capture of 96% relative to Suncor's 5-2-2-1 index**… Refining and marketing gross margin – LIFO ($/bbl) 39.50 … Suncor custom 5-2-2-1 index ($/bbl) 41.15 … Refining and marketing margin capture (%) 96." [^9^]
> "For Suncor, this results in a disconnect between the sales prices for refined products, which reflect current market conditions, and the amount recorded as the cost of sale for the related refinery feedstock… This lag between purchase and sale can be anywhere from several weeks to several months…" [^9^]

**Phillips 66 (Q1 2023, OGJ)** — driver-attributed variance narrative in earnings:
> "Realized margins increased to $20.72/bbl… as lower market crack spreads were **more than offset by higher clean product differentials, improved feedstock advantage, and secondary products**." [^10^]

**PBF Energy (Argus, 2023-08-09)** — capture rate explained by operational events:
> "A coker unit turnaround at PBF Energy's 171,000 b/d Delaware City refinery… 'certainly impacted **capture rates** on the east coast,' PBF Energy chief executive Matthew Lucey said." [^11^]

### 1.3 The controller's monthly bridge — drivers, cadence, and artifact

**Refinery Accounting Handbook (refinerycontroller.com)** — the most detailed public description of the monthly margin lookback:

On the two views being reconciled:
> "Commercial / Economics View — Market Margin: Based on current spot prices for crude and products… What traders and the CEO watch daily. Accounting / Reported View — Reported Margin: Based on actual inventory cost (WAC, FIFO, or LIFO), hedge settlement timing, RIN accruals, and period cut-off. What the P&L shows. **Often lags economics by 15–45 days.**" [^12^]

On cadence and artifact ("Controller Bridge"):
> "**Controller Bridge (Economics-to-Reported Margin):** The written monthly analysis prepared by the controller that reconciles the theoretical benchmark crack spread (the market's economic expectation) to the actual reported gross margin per barrel. Quantifies each contributing factor — inventory cost lag, RIN costs, hedge timing effects, yield mix, throughput variance — in both $/bbl and total dollar terms… This document is the controller's signature contribution **every single monthly close. Without exception.**" [^12^]

Driver list for divergence (in order of impact):
> "1. Inventory cost lag — the most significant driver. COGS reflects purchase cost from 15–45 days ago… 2. RIN price movement… 3. Hedge settlement timing… 4. Fixed cost absorption — throughput variance below budget spreads fixed costs over fewer barrels. 5. Product mix yield — actual yield vs. budget… 6. LCM write-downs." [^12^]

On "phantom profit" (a key lookback concept):
> "Phantom profit occurs when rising crude prices create the appearance of strong margins, but the reported income reflects the benefit of lower-cost inventory purchased earlier rather than current economics… Quantify it every period: Economic margin (at current Brent cost) vs. Reported margin (at WAC or FIFO cost). The difference is the phantom. Write it down. Present it explicitly. **Never permit it to drive capital allocation, dividend, or bonus decisions.**" [^12^]

On capture-rate decomposition (weakness of headline metric):
> "Capture rate is a useful one-number summary for CFO and board presentations, but it aggregates multiple independent drivers. Decompose it: inventory method timing (±X%), actual vs. benchmark yield mix (±X%), RIN cost deduction (−X%), hedge timing impacts (±X%), basis risk (±X%). **Present the bridge, not just the number.**" [^12^]

On price capture (commercial execution):
> "Track realized price vs. benchmark price as a 'price capture' or 'capture rate' analysis. Systematic shortfalls of realized vs. benchmark price represent **commercial execution efficiency issues** worth investigating and explaining separately from inventory method timing effects." [^12^]

On yield reconciliation at close:
> "Product Yield Reconciliation: The monthly accounting process that compares actual product volumes produced (per plant data) to the theoretical volumes implied by crude charged, budget yield assumptions, and inventory movements… **Yield reconciliation is a required close procedure.** Unexplained variances above threshold represent either physical inventory shrinkage, measurement inaccuracy, or a cost system error." [^12^]

### 1.4 GRM vs. net margin bridge and LP-based planning artifacts

**Academic explainer (academia.edu, 2018):**
> "Gross Refining Margin (GRM) is the differential between the product realization and the cost of crude processed… Net Margin, calculated as GRM minus operating costs, represents refinery profitability… GRM is influenced by the crude mix, available secondary processing facilities, and external factors such as international crude prices and supply-demand balance." [^32^]

**MDD Forensic Accountants (2024-02-22)** — the LP's planning artifacts that later serve as the "plan" baseline in lookbacks (and insurance claims):
> "Term Plans – Whether this is for annual budgeting purposes, term crude contracts or maintenance shutdown planning… Production Planning – Refineries will run an LP model to determine the best operating mode to maximise their margins in a given month. The inputs to the production plan are typically finalised towards the end of the month before the target month…" [^33^]

**Galp (2025 Annual Integrated Report)** — LP simulation as the margin-estimation basis in impairment testing:
> "Management's estimate of refining margins used in the impairment testing was based on a **linear refinery simulation software** considering the current refinery configuration and to generate, on an optimised basis, estimated refinery products yields and energy consumption data…" [^34^]

**bp (2025 Annual Report)** — indicator vs. realized margin tension:
> "bp has retired the refining marker margin (RMM) and replaced it with the bp refining indicator margin (RIM)… **Actual margins realized by bp may vary due to a variety of factors, including the actual mix of crude and product for a given quarter.**" [^35^]

---

## 2. Commercial Lookbacks: Pricing Post-Mortems, Campaigns, Channel & Customer Profitability

### 2.1 Retail fuel pricing lookbacks — vendor-evidenced practice

**Kalibrate (fuel pricing software, accessed 2026):**
> "Analyze past pricing decisions to understand their impact on profitability." [^16^]
> "PRICING INSIGHT AND REPORTING — Clear visibility into fuel pricing performance. Access a comprehensive library of pricing reports that visualize performance and **reveals the true impact of pricing on volume, margin, and profitability**… Analyze your way, with 50+ system reports, exports, and APIs." [^16^]
> On AI recommendations: "you'll see the factors influencing your price points, like elasticity models and volume forecasts, so you can understand, trust, and act on the insights." [^16^]

**Kalibrate Canada** — margin reporting products used for retrospective market review:
> "Kalibrate offers an extensive database of current and historical petroleum retail prices, wholesale prices, **refiner and marketer gross margin analysis**, taxation histories and crude oil postings… Pricing analytics, including **benchmarking, margins, and timelines**." [^17^]

**Kalibrate consulting** — campaign/marketing-ROI style retrospective engagements:
> "Pump to in-store spend in fuel retail: Quantifying the relationship between fuel pricing strategies and c-store spending… Fuel price changes are tracked alongside c-store revenue. Kalibrate builds a model to estimate pricing's impact on total site revenue change." [^18^]
> "Tracking ROI from billboard advertisements… Insight provides retailers with an understanding of how billboards serve local and transient audiences." [^18^]

**PDI Technologies (2022-12-09)** — pricing analytics best practices and the Excel weakness:
> "If you're still manually compiling data in a spreadsheet, it's time to automate that work… Using a spreadsheet to analyze pricing doesn't give managers or operators the full view of their operations… the majority of consumers (59 percent) choose a gas station based on fuel prices." [^19^]

### 2.2 Channel/customer profitability as consulting demand signal

**Umbrex firm profiles (2026)** — what refiners hire consultants to fix, indicating current weakness in channel/customer-level lookbacks:
> CVR Energy: "Commercial margin analytics: **redesign fuel and fertilizer commercial reporting to show true channel profitability, customer profitability, and regional netbacks**." [^36^]
> Valero: "**Branded wholesale channel profitability analysis** to improve dealer segmentation, pricing architecture, trade support, and territory economics." [^37^]
> Phillips 66: "Commercial excellence programs for wholesale fuels, industrial accounts, aviation, and export channels, including salesforce design and account prioritization… Refining-network performance diagnostics to **improve capture rates**…" [^38^]

### 2.3 Campaign evaluation weakness (convenience retail evidence)

**Cloudpick / ARSA (2025-12 / 2026-01)** — generic convenience-retail evidence that promotion post-evaluation is hard and often absent:
> "Difficulty Proving Campaign Effectiveness: Did that new end-cap display boost sales? Was the recent promotion truly effective in attracting more visitors or converting existing ones? Without granular data on customer engagement before, during, and after a campaign, **attributing ROI to specific initiatives is a constant struggle**." [^39^]
> "43% [of retailers] — Proving ROI… Solution: Establish baseline performance metrics to quantify the impact of implementation." [^40^]

---

## 3. Post-Audit / Post-Investment Appraisal in Oil & Gas

### 3.1 The textbook post-audit and its stated purposes

**Finance textbook (via bsdinsight.com PDF):**
> "The post-audit is an important part of the capital budgeting process, because (1) it **compares actual results with those forecast and explains the reasons for differences** and (2) it facilitates a decision on whether the project should be continued or terminated. Differences between actual and projected results may be due to changes in the economy… or forecasting errors… Investigating these differences may improve forecasts in the future due to new methods being developed or just the knowledge that **people are being held responsible for their projections**." [^41^]

**Fiveable study guides (2024–2025)** — process mechanics:
> "Post-audit processes assess project outcomes against initial goals, analyzing financial and non-financial metrics… By examining variances, cash flows, and implementing monitoring systems, companies can identify areas for improvement. This process captures lessons learned, establishes feedback mechanisms, and fosters a culture of continuous improvement in capital investment decision-making." [^42^]

**Accounting Exams Mastery (2025-09-16)** — challenges:
> "Data Availability… Bias and Subjectivity: Ensuring objectivity in the post-audit process can be challenging, particularly if stakeholders have vested interests. Engaging independent auditors or consultants can help mitigate this risk… Resistance to Change: Stakeholders may resist implementing recommendations from post-audits." [^43^]

### 3.2 Survey evidence: post-audits are inconsistent and often non-influential

**Cameron University survey of publicly traded utilities (Journal of Business & Economics Research, Vol. 13):**
> "The next question asked the respondents to indicate what percent of the time their companies conduct a post-completion audit for capital budgeting projects. **The mean response was 36% of the time**… 17% chose never… These findings support the research of **Cooper, Cornick and Redmon (1992) who reported that 19.6% of the respondents indicated their firms had no review mechanism. They also reported that their respondents indicated that the post-completion audit process did not affect future capital budgeting decisions**." [^22^]
> Authors' conclusion: "it is evident that a serious inefficiency in the budgeting process could occur and go undetected." [^22^]

**Classic literature lineage (Springer reference list):** Neale, C.W. and Holmes, D. (1988) "Post-completion and its costs and benefits," *Management Accounting*; Neale & Holmes (1991) *Post-completion Auditing*, Pitman; Pike (1983) CIMA survey — establishing that post-completion auditing has been a recognized-but-imperfect practice for 40+ years. [^44^]

### 3.3 IPA (Independent Project Analysis) — database-driven lookbacks

**IPA Newsletter 2021 Q1 (Luke Wallace, Senior Consultant)** — schedule target accuracy from >2,000 projects:
> "The capital projects industry has struggled to generate accurate project schedule targets… irrespective of their development phase, projects tend to experience schedule slip… the **average slip of the targets set at FEL 1 is 50 percent. The 80 percent range… is over 120 percent. The performance improves in subsequent phases, but even our most detailed estimates (FEL 3) are off by 17 percent, on average.** The fact is, schedule target accuracy is far less certain than advertised." [^23^]

**IPA Newsletter 2020 Q4 (Rolando Gachter, Director)** — persistence of poor performance despite known benchmarks:
> "…the uncomfortable truth is that the region's oil and gas, refining, and chemicals projects **have not succeeded at incorporating real project performance metrics and execution schedule estimating Best Practices into their project development and delivery systems** and continue to experience schedule slip at levels well above the global average… projects located in the Middle East have experienced a **median execution slip of more than 30 percent since 2010**… median execution schedule slip in the Middle East has remained **amazingly constant** since it first degraded in 2012… How many years of disappointing schedule predictability have to pass before estimating practices are changed?" [^24^]

**Merrow/IPA megaproject lookback statistics (via IGI Global; ResearchGate/OTC paper):**
> "Reporting from Edward Merrow, President of IPA, **roughly two-thirds of the oil industry's megaprojects come in late, over-budget or fail on other key metrics**. In addition some **64% of upstream megaprojects suffer from serious and enduring production attainment problems in the first two years**." [^25^]
> "Meanwhile, the performance of oil and gas megaprojects collapsed; **only 22% of these projects could reasonably be called successful**… the other 78% were equally unimpressive with **33% real cost overruns, cost indices that averaged 1.37, and execution schedule slip of 30%**." [^25^]
> "Success, measured by how well we meet promises made at the time of the financial investment decision (FID), declines rapidly with project size (Merrow 2003). (Note: **IPA benchmarks projects before FID and project systems** in the oil and gas and other capital-intensive industrial sectors.)" [^25^]

**Flyvbjerg reference-class evidence (via IGI Global):**
> "Costs are underestimated in almost 9 out of 10 projects. For a randomly selected project, the likelihood of actual costs being larger than estimated costs is 86 percent… (Flyvbjerg et al., 2002)… optimism connected with 'strategic misrepresentation' of the costs by the owner and contractor, presumably to get the project approved." [^25^]

### 3.4 Turnaround-level lookbacks: the feedback loop that usually isn't

**TAAL Tech (2026-02-21):**
> "According to Independent Project Analysis (IPA), **constructability issues contribute to 10–15% of schedule overruns** in capital projects… **No Feedback Loop from Previous Turnarounds:** Engineering teams often start from scratch without leveraging insights from previous turnaround cycles. Critical lessons—such as what failed, what worked, and what could have been improved—**are not systematically captured**. Impacts: Repetition of past mistakes; Lack of historical benchmarking… Mitigation: Conduct formal post-turnaround reviews… Maintain a structured lessons-learned database… Integrate lessons learned into future FEED packages." [^31^]

**AFPM FCC Seminar APC post-audit example (Petrocontrol PDF)** — unit-level benefit post-audit practice:
> "Benchmark — Compare Refinery's APC applications and performance to industry. Audit — Evaluate Refinery's approach to APC. Gap Analysis — Identify performance gaps and opportunities… Example APC Post Audit-1: Increase LCO recovery $0.44/BBL… Total evaluated $0.50/BBL." [^45^]

---

## 4. How Lookbacks Are Done Today: Tooling, Cadence, Participants, Weaknesses

### 4.1 Cadence and artifacts (synthesized from sources)

| Rhythm | Artifact / Forum | Participants (evidence) | Source |
|---|---|---|---|
| Monthly close | "Controller Bridge" (crack spread → reported margin, written 1-pager, signed, filed in close package); yield reconciliation; "CFO Bridge Pack" | Controller, CFO; yield variances investigated with technical accounting | [^12^] |
| Monthly (pre-month + in-month) | LP production plan finalized end of prior month; crude evaluation 2–3 months ahead of delivery | LP economist/planning, crude traders, scheduling | [^33^][^46^] |
| Quarterly | Public earnings: R&M margin/bbl, capture % vs. company index, utilization, driver narrative (clean product differentials, feedstock advantage, secondary products) | Investor relations, segment leadership, CFO | [^7^][^8^][^9^][^10^][^11^] |
| Biennial | Solomon Fuels Study gap analysis, custom peer groups, results presentations, target-setting workshops; ~850 hours data collection per refinery per study | Site data coordinators, VP Refining, executive leadership | [^13^][^14^][^15^] |
| Project-gated | IPA evaluations at FEL gates + post-completion benchmarking vs. proprietary database; post-turnaround reviews (often skipped) | Project teams, owner project systems, IPA analysts | [^23^][^24^][^25^][^31^] |
| Continuous/daily | Retail pricing review: price vs. competition, volume/margin dashboards, elasticity recalibration; price-decision audit trail | Pricing managers, category/field teams | [^16^][^19^] |

### 4.2 Tooling observed

- **Excel + ERP actuals:** controller bridges and CFO packs remain document/worksheet artifacts ("written, signed, documented analysis"); PDI explicitly criticizes spreadsheet-based pricing analysis. [^12^][^19^]
- **BI/performance dashboards:** AspenTech "Performance Management — real-time monitoring of business metrics via dashboards, alerts, and pattern matching"; Aspen Unified Reconciliation and Accounting for production accounting. [^46^]
- **Closed-loop plan-to-operations:** Aspen GDOT "vertically integrates planning, scheduling and advanced process control in closed loop… dynamic data reconciliation that reflects plant actual performance." [^4^][^46^]
- **Data reconciliation & yield accounting as the system of record:** AIGC ("closing the mass balance and production accounting"); Refinium Yield Accounting ("The bridge between operational data and the financial ledger"). [^5^][^6^]
- **Pricing suites:** Kalibrate (150k+ prices/day, 65,000+ sites, 50+ reports, 12-week live A/B-style trials to "measure improvement against your existing fuel pricing processes"). [^16^]
- **External benchmark databases:** Solomon (320+ refineries, 40-year database); IPA (proprietary completed-projects database; regression-based schedule/cost toolkits updated annually). [^13^][^14^][^23^]

### 4.3 Known weaknesses (variance reporting vs. causal learning)

1. **Headline metrics hide drivers** — capture rate "obscures the reasons for under-capture"; best practice demands a decomposed bridge. [^12^]
2. **Post-audits don't change decisions** — survey respondents reported the post-completion audit "did not affect future capital budgeting decisions." [^22^]
3. **Lessons not systematically captured** — turnaround teams "start from scratch"; repetition of past mistakes. [^31^]
4. **Metrics not embedded in delivery systems** — IPA: owners "have not succeeded at incorporating real project performance metrics… into their project development and delivery systems"; slip "amazingly constant" for a decade. [^24^]
5. **LP model decay** — errors persist "months or even years," so the "plan" baseline against which actuals are judged is itself stale. [^3^]
6. **Benchmark participation burden** — ~850 staff-hours per refinery per Solomon study; results can "seem a bit complicated and confusing" (Solomon sells a 2-day "How to Use the Data" seminar). [^15^]
7. **Accounting-vs-economics confusion risk** — phantom profit must never "drive capital allocation, dividend, or bonus decisions"; inventory-method effects masquerade as performance. [^12^]
8. **Attribution in commercial spend** — promotion ROI "a constant struggle" without baselines. [^39^][^40^]

---

## 5. Forecast Accuracy / Bias Evidence Relevant to Refining Planning

**IEA World Energy Outlook retrospective (Wachtmeister, Henke, Höök, *Applied Energy* 2018; ScienceDirect):**
> "Projection accuracy follows the size and directions of these revisions, with high accuracy for Non-OPEC (**mean absolute percentage error of 4.8% on a 5 year horizon**) and low for OPEC (8.9%) and unconventional (37%). Counteracting error directions contribute to accurate total World oil supply projections (4%) **while price projections have low accuracy (37%)**." [^26^]

**Baker Institute (2024-08-23)** — institutional bias in demand forecasts:
> "OPEC tended to **undershoot** on its annual demand forecast and would on average revise its oil demand figure **up after one year by 130,000 b/d**. The EIA tended to **overshoot**… and would on average revise its oil demand figure **down by 90,000 b/d**… organizations—and analysts within them—are shaped by their experience." [^27^]

**Bundesbank discussion paper (Reitz et al., "Are oil price forecasters finally right?")** — Consensus Economics 1989–2008:
> "In summary, we find that forecasters—on average—**do not outperform a random walk forecast**… forecasters expect a lower oil price than actually occurred… the forecast error is, on average, positive. **Forecasters—on average—expected the oil price to be 6.5 percent lower than it actually was**… Oil price forecasts suffer from the peso problem." [^28^]

**ECB Working Paper 1735 (Brent forecasting):**
> "No single forecasting approach consistently outperforms the no-change forecast or the futures at every point over the sample period or across horizons… the bias inherent in the forecast, tends to be **negative for all models across different horizons**… most models tend to underpredict actual oil prices." [^29^]

**Bank of Canada (Pagano & Pisani, risk-adjusted oil futures):**
> "The futures is not an unbiased predictor: the value of the constant at each forecast horizon n is significantly negative… a **six-month contract under-predicts the realized spot by $1.8, or around 8 per cent** if evaluated at the mean price of the sample." [^30^]

**Finance Research Letters (2025-05-01):** "VAR forecasts do not significantly outperform the random walk for horizons under one year… the average-price benchmark systematically biases the Diebold–Mariano test statistic." [^47^]

**Implication for downstream lookbacks:** plan-vs-actual margin variance is dominated by price/crack forecast error that is (a) large (5-yr MAPE ~37%), (b) directionally biased depending on the forecaster's institution, and (c) not beatable by naive methods — so lookback designs must separate **unforecastable market variance** from **controllable execution variance** (the exact split the controller bridge and capture-rate decomposition attempt).

---

## 6. Tensions & Contradictions Noted

1. **Capture rate >100% is celebrated (MPC 114%) yet the metric's own proponents warn it "obscures the reasons for under-capture"** — over-capture vs. an index can reflect index mismatch (slate, geography) rather than execution excellence; Suncor discloses the full index reconciliation, others don't. [^7^][^9^][^12^]
2. **LP treated as ground truth in insurance/forensic contexts** (MDD: "Linear programs are a reliable tool") **vs. practitioners documenting persistent LP errors for months/years** (IZZI) and LP-actual gaps (Imubit, scialert). [^33^][^3^][^1^][^2^]
3. **Post-audit theory says it improves forecasts and accountability; survey evidence says it often isn't done (36%) and doesn't influence future decisions.** [^41^][^22^]
4. **OPEC vs. EIA opposite institutional biases** complicate any single "forecast bias" correction factor for planning decks. [^27^]
5. **Vendor benefit claims ($0.05–0.15/bbl, $0.25/bbl, $0.50/bbl, "4–5% EBITA") are unaudited marketing figures** — directionally consistent but not independent evidence. [^1^][^4^][^5^][^3^]
6. **Solomon now markets causal gap analysis** ("delve into the underlying causes") **while its own seminar materials admit users find results "complicated and confusing"** — causal insight still requires expert intermediation. [^13^][^15^]
7. **Silence on ETRM/CTRM post-trade lookbacks** in public sources — trading retrospective practice (deal P&L attribution vs. plan) is not publicly documented; likely proprietary.

---

## Sources

[^1^] Imubit, "Oil Refinery Optimization: How AI Builds on What LP Models Leave Behind," 2026-04-15. https://imubit.com/articles/oil-refinery-roi-optimization
[^2^] Scialert (Asian J. Scientific Research), "Optimal Design of Petroleum Refinery Topology…," 2011-02-26. https://scialert.net/fulltext/?doi=ajsr.2011.95.113
[^3^] Tatariya (IZZI Business Services), "LP accuracy – Best Practices," AVEVA PI System UC 2022. https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS20-IZZI-Tatariya-LP-accuracy-Best-Practices.pdf
[^4^] ARC Advisory Group, "AspenTech's Unified Solution Helps Users Move Toward the Self-optimizing Plant." https://www.arcweb.com/industry-best-practices/aspentechs-unified-solution-helps-users-move-toward-self-optimizing-plant
[^5^] AIGC, "Optimization & Modelling," 2021-05-18. https://www.aigcom.com/Solution/optimization-modelling/
[^6^] Refinium AI, "Integrated Refinery Intelligence Platform." https://www.refinium-ai.com/
[^7^] Marathon Petroleum, 2025 Annual Report & 10-K. https://www.marathonpetroleum.com/content/documents/Investors/Annual_Report/2025_MPC_Annual_Report_and_10K.pdf
[^8^] Motley Fool, "Marathon Petroleum Returned $4.5 Billion to Shareholders in 2025," 2026-02-21. https://www.fool.com/investing/2026/02/21/marathon-petroleum-returned-45-billion-to-sharehol/
[^9^] Suncor Energy, 2025 Annual Report (MD&A, non-GAAP reconciliations). https://www.suncor.com/-/media/project/suncor/files/investor-centre/annual-report-2025/2025-annual-report-en.pdf
[^10^] Oil & Gas Journal, "First-quarter 2023 earnings benefit from higher refining margins," 2023-05-22. https://www.ogj.com/general-interest/article/14295516/first-quarter-2023-earnings-benefit-from-higher-refining-margins
[^11^] Argus Media, "Crude fundamentals may support 2H US coke supply," 2023-08-09. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2477784-crude-fundamentals-may-support-2h-us-coke-supply
[^12^] Refinery Accounting Handbook (refinerycontroller.com), accessed 2026-07. https://www.refinerycontroller.com/
[^13^] Solomon, "Fuels Study – Refining Benchmarking." https://www.solomoninsight.com/industries/refining/benchmarking/fuels-study
[^14^] Solomon, "Solomon Achieves Record Fuels Study Participation." https://www.solomoninsight.com/news/solomon-achieves-record-fuels-study-participation
[^15^] Solomon, "Refining Benchmarking Seminars" (850-hour data effort; 2-day How to Use the Data seminar). https://www.solomoninsight.com/industries/refining/refining-benchmarking-seminars
[^16^] Kalibrate, "Fuel Pricing Software" and "Fuel | Kalibrate Global," 2025–2026. https://kalibrate.com/kalibrate-fuel-pricing-software/ ; https://kalibrate.com/industries/fuel/
[^17^] Kalibrate Canada, "Fuel & Convenience Retail Analytics," 2026-07-08. https://kalibrate.com/canada/
[^18^] Kalibrate, "Consulting," 2023-10-10. https://kalibrate.com/products/consulting/
[^19^] PDI Technologies, "4 Best Practices for Fuel Pricing Strategies," 2022-12-09. https://pditechnologies.com/blog/4-fuel-pricing-strategies/
[^20^] (reserved – folded into 22)
[^21^] Fiveable, "Post-Audit of Capital Projects" study guides, 2024-07-25 / 2025-08-22. https://fiveable.me/strategic-cost-management/unit-18/post-audit-capital-projects/study-guide/RbcjWnZ83JacVYRx
[^22^] Cameron University, "A Survey of Capital Budgeting in Publicly Traded Utility Companies," JBER Vol. 13. https://www.cameron.edu/storage/departments/business/Journals/Vol-13-A-Survey-Of-Capital-Budgeting-In-Publicly-Traded.pdf
[^23^] IPA Newsletter 2021 Q1 (Vol. 13 Issue 3), Luke Wallace, schedule target accuracy. https://www.ipaglobal.com/wp-content/uploads/2021/06/IPA-Newsletter-2021-Q1-Volume-13-Issue-3.pdf
[^24^] IPA Newsletter 2020 Q4 (Vol. 12 Issue 4), Middle East schedule slip. https://www.ipaglobal.com/wp-content/uploads/2020/12/IPA-Newsletter-2020-Q4-Volume-12-Issue-4.pdf
[^25^] IGI Global chapter citing Merrow/IPA & Flyvbjerg; Merrow OTC megaprojects paper (ResearchGate). https://www.igi-global.com/viewtitle.aspx?TitleId=172634&isxn=9781522517900 ; https://www.researchgate.net/publication/313272481_Development_of_industry_performance_metrics_for_offshore_oil_and_gas_project
[^26^] Wachtmeister, Henke, Höök, "Oil projections in retrospect: Revisions, accuracy and current uncertainty," Applied Energy (2018/2020 online). https://www.sciencedirect.com/science/article/pii/S0306261918303428
[^27^] Baker Institute, "What's Happening to Oil Market Forecasts?" 2024-08-23. https://www.bakerinstitute.org/research/whats-happening-oil-market-forecasts
[^28^] Bundesbank discussion paper, "Are oil price forecasters finally right? Regressive expectations and the peso problem." https://www.bundesbank.de/resource/blob/703530/3f8a46eedc3ab008a23096ca6474f8db/mL/2009-12-08-dkp-32-data.pdf
[^29^] ECB Working Paper 1735, "Forecasting the Brent oil price: addressing time-variation in forecast performance." https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1735.pdf
[^30^] Bank of Canada WP, Pagano & Pisani, "Risk-adjusted forecasts of oil prices." https://www.bankofcanada.ca/wp-content/uploads/2010/08/pagano.pdf
[^31^] TAAL Tech, "Plant Engineering Mistakes That Lead to Costly Turnarounds," 2026-02-21. https://www.taaltech.com/plant-engineering-mistakes-that-lead-to-costly-turnarounds/
[^32^] Academia.edu, "Understanding the Operating Cost of a Refinery and Its Gross Refining Margin," 2018-03-16. https://www.academia.edu/36176487/
[^33^] MDD Forensic Accountants, "The Importance of Linear Programs (LPs) in Refinery Claims," 2024-02-22. https://www.mdd.com/forensic-accounting-articles/the-importance-of-linear-programs-in-refinery-claims/
[^34^] Galp, Annual Integrated Report 2025 (impairment/refining margin estimation). https://www.galp.com/corp/Portals/0/Recursos/Investidores/IMR2025/AnnualIntegratedReport2025.pdf
[^35^] bp, Annual Report and Form 20-F 2025 (RIM definition). https://www.bp.com/content/dam/bp/country-sites/de_de/germany/home/global-assets/bp-annual-report-and-form-20f-2025.pdf
[^36^] Umbrex, "CVR Energy Strategy and Business Model," 2026-06-01. https://umbrex.com/resources/company-profiles/cvr-energy/
[^37^] Umbrex, "Valero Strategy and Business Model," 2026-05-26. https://umbrex.com/resources/company-profiles/valero/
[^38^] Umbrex, "Phillips 66 Strategy and Business Model," 2026-05-28. https://umbrex.com/resources/company-profiles/phillips-66/
[^39^] ARSA Technology, "Measuring ROI in Convenience Stores," 2026-01-21. https://arsa.technology/machine-state/unlocking-profitability-a-strategic-guide-to-measuring-roi-in-convenience-stores-with-arsa-smart-retail-counter-utpiwm/
[^40^] Cloudpick, "How to evaluate ROI for autonomous retail in convenience store chains," 2025-12-05. https://blog.cloudpick.ai/evaluate-roi-autonomous-retail-convenience-grocery-stores/
[^41^] Capital budgeting textbook excerpt (post-audit section), bsdinsight.com PDF, 2025-04. https://bsdinsight.com/wp-content/uploads/2025/04/Phan-tich-tai-chinh-cho-cap-quan-ly.pdf
[^42^] Fiveable, "Post-Audit of Capital Projects | Cost Accounting," 2024-07-25. https://fiveable.me/cost-accounting/unit-14/post-audit-capital-projects/study-guide/VLwdMUJtJ4qBpu9r
[^43^] Accounting Exams Mastery, "11.9 Post-Audit of Capital Projects," 2025-09-16. https://accountingexamsmastery.ca/introduction-to-managerial-accounting/11-capital-budgeting/11-9-post-audit-of-capital-projects/
[^44^] Springer, "Capital investment decisions: 2" (reference list: Neale & Holmes 1988/1991; Pike 1983). https://link.springer.com/chapter/10.1007/978-1-4899-6828-9_15
[^45^] Petrocontrol (AFPM 2012 FCC Seminar APC Workshop), "FCC Advanced Process Control – What's it worth?" https://petrocontrol.com/wp-content/uploads/2020/07/2012-AFPM_FCC_Seminar_APC_Workshop-rev104.pdf
[^46^] AspenTech, "Production Optimization for Refining." https://www.aspentech.com/en/solutions/production-optimization-for-refining
[^47^] Finance Research Letters (Bank of Canada staff), "Putting VAR forecasts of the real price of crude oil to the test," 2025-05-01. https://www.sciencedirect.com/science/article/pii/S1544612325002041

*Additional context sources consulted: University of Oklahoma refinery planning report; arXiv 2605.15085 (MOL Group AspenTech PIMS anomaly detection on monthly plans); Henry Fund MPC report (Q4 2025, 114% capture corroboration); OGJ Q4 2024 earnings roundup; Fortune/Quartr HF Sinclair 8-K (adjusted refinery gross margin non-GAAP definition); Solomon Combined Site/Lube Study pages; CONCAWE-Solomon CWT methodology paper; FasterCapital post-completion audit guide; Stratrix/BlueMorrow backcasting explainers (methodology contrast); IEF comparative oil-market report analyses; Dallas Fed energy capex discipline note (2025-03-31); Sinopec News Phillips 66 Q2 2023; Consumer Watchdog California refiner margins (regulatory push for standardized monthly margin reporting — SB 1322).*

---
*End of Dimension 03 evidence file.*

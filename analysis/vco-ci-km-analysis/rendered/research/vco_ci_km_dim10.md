# Dimension 10 — Weak Causal Inference and RCA Discipline in Retrospective Analysis

**Study:** Value Chain Optimization (VCO), Lookback/Backcasting, and CI Knowledge Management — Downstream Refining & Marketing
**Research date:** 2026-07-18
**Method:** ≥15 independent web searches (35+ distinct queries executed) across safety science, reliability engineering, academic analytics, CSB-derived sources, healthcare RCA-effectiveness literature, forecasting practice literature, and model risk management regulation. All excerpts verbatim; each source listed with URL and date; tensions flagged at the end of each section.

---

## KEY FINDINGS

1. **Operational/commercial retrospective analysis is dominated by correlation-level reading of dashboards, and the industry data confirms most organizations never leave that level.** Gartner's 2018 survey (n=813) found "more than 87 percent of organizations are classified as having low business intelligence (BI) and analytics maturity," with "basic" organizations limited to "spreadsheet-based analyses and personal data extracts" [^2^]. Academic reviews of dashboard consumption find executives "frequently treat[ing] dashboard outputs as authoritative representations rather than partial abstractions," with initial visual impressions discounting later contradictory evidence (confirmation bias) [^1^]. The canonical big-data cautionary case (Google Flu Trends) shows a correlation-built model degrading silently once the data-generating process changed — "big data hubris" [^3^].

2. **Event data quality is a measured, structural problem — not anecdote.** NIST/PHM researchers document free-text work orders, cause-code evasion ("misc"/"other" + free text), and non-random entry errors that bias downstream KPIs [^5^][^6^]. In a 10-year HVAC CMMS dataset, ~93% of 21,107 work orders were "closed" on Fridays, proving timestamps reflect administrative batch closure, not physical completion [^6^]. Timestamp misalignment between systems is explicitly identified as "a major obstacle" to sequence-of-events and root-cause investigation [^9^]. Refinery-specific evidence: monthly mass reconciliations at two Shell refineries were found "erroneous or out of industry average oil loss" [^11^].

3. **RCA practice quality is consistently found to be shallow, person-focused, and weakly governed.** The most-cited methodological critique (Peerally et al., *BMJ Quality & Safety* 2017) finds the name "root cause analysis" itself "promotes a flawed reductionist view"; teams stop at "a cause of mutual convenience"; corrective actions show an "endemic tendency" toward "administrative and perhaps 'weaker' solutions (such as reminders)"; action implementation rates are only ~45–70%; and RCA often degenerates into a "tombstone effect… a procedural ritual" [^13^]. A systematic review found **no controlled trials** of the RCA framework and only "anecdotal evidence" of effectiveness [^14^]. Dekker's New View: "Human error is not a cause. It is the consequence of system design" [^15^]; Reason supplies the latent-conditions/active-failures model and the "substitution test" [^18^]. Field studies in industry (Drupsteen & Hasle 2014) confirm investigations stop at "direct causes i.e. human or technical causes" and "the quick fix often turns out to be the permanent solution" [^20^].

4. **CSB investigations repeatedly find prior lessons documented-but-not-learned.** Tesoro Anacortes: "management repeatedly failed to ensure that these hazards were controlled" despite a history of leaks/fires [^22^]. BP Texas City: "Warning signs of a possible disaster were present for several years, but company officials did not intervene effectively" [^22^]; CSB said applying lessons from prior incidents "could have corrected flawed systems prior to March 23, 2005" [^23^]. Honeywell Geismar (CSB final report May 2025): the failed gasket type was known-bad since 2007; replacement was deferred "on an attrition basis"; 14 years later it killed a worker; CSB: three incidents "entirely preventable" [^24^]. CSB-linked analysis: the systemic problems of Bhopal "remain the underlying causes of many incidents," including "Lack of root cause incident investigations and communication of lessons learned" [^25^]. Rosenthal: "implementation of lessons already learned could have prevented the large majority of process accidents" [^23^].

5. **Forecast/plan evaluation practice optimizes error magnitude (MAPE) and neglects structural bias and assumption quality.** MAPE's failure modes are formally catalogued (zero-division, asymmetry, low-volume distortion) [^26^][^27^]; "unbiasedness is a distinct desideratum from accuracy" [^26^]. Forecast Value Added (FVA) studies show the process itself often destroys value: Newell Rubbermaid's management-review step subtracted 3 points of accuracy [^30^]; Morlidge found 52% of forecasts across eight businesses failed to beat a naive baseline [^30^], and 40–50% of low-level forecasts "perform worse than the naive and so destroy value" [^31^]. Model risk management (SR 11-7) shows what institutionalized rigor looks like where regulation forces it: conceptual soundness review of assumptions, ongoing monitoring, and outcomes analysis/back-testing as mandatory, independent disciplines [^32^] — a standard refining lookbacks do not approach.

6. **"Good" is known but rarely institutionalized.** Causal-inference-grade methods applicable to industrial retrospectives exist — Bayesian belief networks fusing fault-detection outputs with process knowledge for true-root-cause diagnosis (demonstrated on an FCC unit) [^33^], fuzzy fault-tree→Bayesian-network mappings [^34^], bias/variation error decomposition [^31^], FVA stair-stepping [^30^], counterfactual discipline via Reason's substitution test and Dekker's local rationality [^18^][^15^], and RCA governance via professionalized independent investigation bodies, hierarchy-of-controls-based corrective actions, and aggregated cross-incident analysis [^13^]. Evidence these remain rare: 87% low analytics maturity [^2^], "exemplary practice in the analysis of healthcare incidents is rare" [^13^], no controlled validation of RCA after two decades [^14^], organizational memory of events fading after ~3 years [^21^].

---

## 1. CORRELATION vs CAUSATION IN OPERATIONAL/COMMERCIAL ANALYTICS

### Finding 1.1 — Dashboard consumption is recognition-biased; outputs are treated as authoritative, not as partial abstractions

> "Empirical studies indicate that once an initial visual impression is formed, contradictory information is frequently discounted. This effect is reinforced in dashboard environments…"

> "Empirical studies like Hjelle et al. (2024) show that executives' decision making rely heavily on visual summaries to assess organizational performance, allocate resources, and evaluate strategic risks, frequently treating dashboard outputs as authoritative representations rather than partial abstractions. Visualization-induced bias can therefore shape organizational strategy by prioritizing easily visualized metrics over less visible but strategically critical factors, such as long-term risk exposure, uncertainty, or distributional effects."

> "Cognitive psychology and visualization research consistently demonstrate that visual encodings interact with biases such as anchoring, availability, framing, and confirmation bias, influencing decision outcomes even when underlying data are accurate (Franconeri et al., 2021; Lisnic et al., 2023)."

- **Source:** "The Impact of Data Visualization on Decision-Making" (review), *IRE Journals* [^1^]
- **URL:** https://www.irejournals.com/formatedpaper/1715288.pdf
- **Date:** undated (references through 2025); accessed 2026-07-18

### Finding 1.2 — Most organizations are stuck at descriptive/spreadsheet analytics maturity

> "More than 87 percent of organizations are classified as having low business intelligence (BI) and analytics maturity, according to a survey by Gartner, Inc. This creates a big obstacle for organizations wanting to increase the value of their data assets and exploit emerging analytics technologies such as machine learning."

> "The survey based on 813 responses found that organisations with low maturity fall in 'basic' or 'opportunistic' levels on Gartner's IT Score for Data Analytics. Organisations deemed 'basic' have BI capabilities that are predominantly spreadsheet-based analyses and personal data extracts. Those at the opportunistic level find that individual business units pursue their own data and analytics initiatives as stand-alone projects, lacking leadership and central guidance."

- **Source:** Gartner press release "Gartner Data Shows 87 Percent of Organizations Have Low BI and Analytics Maturity" (Dec 6, 2018), as reported by *Information Age* [^2^]
- **URL:** https://www.information-age.com/low-bi-and-analytics-maturity-12257/
- **Date:** Gartner release 2018-12-06; accessed 2026-07-18
- **Relevance to VCO lookbacks:** variance commentary built on descriptive dashboards ("what moved") is the default maturity level; diagnostic/causal analysis ("why it moved, what would have happened otherwise") sits two maturity levels up, where few organizations operate.

### Finding 1.3 — The canonical big-data correlation failure: Google Flu Trends

> "'Big data hubris' is the often implicit assumption that big data are a substitute for, rather than a supplement to, traditional data collection and analysis." — Lazer, Kennedy, King & Vespignani, "The Parable of Google Flu: Traps in Big Data Analysis," *Science* 343 (2014): 1203–1205 [^3^]

> "Lazer et al. (2014) highlighted a series of issues with its predictions, including a systemic bias that produced an overestimate in 100 out of the 108 weeks analyzed during a two-year period." (Cambridge University Press, *Big Crisis Data*, ch.9) [^3^]

> "As Lazer et al. (2014:2) note, Big Data hubris fails to recognize that '… quantity of data does not mean that one can ignore foundational issues of measurement and construct validity and reliability….'" (AAPOR Report on Big Data) [^4^]

> "Effectively, if in the first 2009 version of GFT, 'big data were overfitting the small number of cases' and 'GFT was part flu detector, part winter detector', the new GFT version 'has been persistently overestimating flu prevalence for a much longer time'." (Moro & Sobolevsky, summarizing Lazer et al. 2014 and Butler, *Nature* 2013) [^3^]

- **Sources:** Lazer et al., *Science* 2014;343:1203-1205 (primary); corroborating summaries: Cambridge Core *Big Crisis Data* ch.9 (https://www.cambridge.org/core/books/big-crisis-data/validity-biases-and-pitfalls-of-social-media-data/D0DB80718C71FCD37C282688206129A6); AAPOR Big Data Task Force Report (https://doku.iab.de/grauepap/2015/BigDataTaskForceReport_FINAL_2_12_15.pdf); Lazer et al. follow-up working paper, Harvard DASH (https://dash.harvard.edu/entities/publication/73120378-c595-6bd4-e053-0100007fdf3b) [^3^][^4^]
- **Date:** 2014; accessed 2026-07-18
- **Relevance:** a model built by mining correlations ("some [search terms] were bound to highly correlate with flu during the development process despite being structurally unrelated") failed silently when the data-generating process changed ("algorithm dynamics") and produced **structural bias** (persistent overestimation), not random error — the exact failure mode of assumption-unexamined planning models (see §4).

### Finding 1.4 — Measure-target distortion (Goodhart) and the "causal" Goodhart failure mode

> "Goodhart's Law states that 'when a measure becomes a target, it ceases to be a good measure.' In other words, when we use a measure to reward performance, we provide an incentive to manipulate the measure in order to receive the reward. This can sometimes result in actions that actually reduce the effectiveness of the measured system while paradoxically improving the measurement of system performance."

- **Source:** CNA, "Goodhart's Law" (Sept 2022) [^12^]
- **URL:** https://www.cna.org/analyses/2022/09/goodharts-law
- **Date:** 2022-09-01; accessed 2026-07-18

> "Causal [type of Goodhart's Law]: Confusing Causation vs Correlation when selecting measurements. Data might indicate increasing ice cream sales when people wear sunglasses. However, providing more sunglasses won't necessarily boost ice cream sales because they are both caused by a third factor, ie. sunny, hot days."

- **Source:** ModelThinkers, "Goodhart's Law" [^12b^]
- **URL:** https://modelthinkers.com/mental-model/goodharts-law
- **Date:** 2018-03-27; accessed 2026-07-18
- **Relevance:** KPI trees in downstream marketing (volume, margin capture, OTIF) are mostly *correlates* of value-chain performance; once targeted and commented monthly, they are gamed or diverge from drivers — corrupting the variance narrative.

### Finding 1.5 — CSB critique of refinery metric fixation (BP Texas City)

> "BP's internal performance measurement and incentive systems for safety performance focused almost exclusively on injury rates, and did not include measurement of process safety performance. As a result, safety programs at the refinery focused on personal safety initiatives, and company officials received reports of improving safety performance at the refinery, based on lower injury rates, even as process safety deteriorated and the risk of major accident remained high."

- **Source:** CSB senior investigator (Don Holmstrom), "Some observations about major chemical accidents from CSB investigations," IChemE symposium paper [^22b^]
- **URL:** https://www.icheme.org/media/9698/xx-paper-03.pdf
- **Date:** undated (post-2007); accessed 2026-07-18
- **Relevance:** a dashboard showing improving KPIs coexisted with deteriorating underlying risk — direct evidence that metric-level variance commentary can certify the wrong causal story.

### Tensions — Section 1
- Visualization bias research also shows well-designed visuals *reduce* cognitive load and improve accuracy; the critique is of consumption practice (anchoring, authority bias), not dashboards per se [^1^].
- Gartner's 87% figure dates from 2018 and is consultancy survey work, widely recycled by vendors; treat the level, not the precision, as the signal [^2^].
- Google Flu Trends performed acceptably in some jurisdictions/periods (e.g., Canada 2010–2014, ρ=0.77–0.90 vs physician data), i.e., correlation models are not uniformly useless — they are fragile and unaudited without causal grounding [^3^].

---

## 2. EVENT DATA QUALITY: CLASSIFICATION, FREE TEXT, AND TIME-ALIGNMENT

### Finding 2.1 — Maintenance work-order data is structurally "un-useful" for analysis (NIST)

> "It involves manual work on the equipment and data collection by maintainers, which itself involves free-text and pre-specified categories or controlled vocabulary, rather than collection via sensors. Often this data is un-useful, in that it does not support the digitization of work."

> "As a specific example encountered quite often in our controlled-vocabulary case, this form of error is encountered when a technician selects a field that enables his ability to skip categorization (i.e., 'misc', or 'other'), and enter free-form text anyway (bypassing the intent of such a system)."

- **Source:** Sexton, Hodkiewicz & Brundage, "Categorization Errors for Data Entry in Maintenance Work-Orders," NIST (PHM Society 2019) [^5^]
- **URL:** https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=928437
- **Date:** 2019; accessed 2026-07-18

### Finding 2.2 — Data-entry errors are non-random and bias the KPIs built on them (PHM Society 2021 case study)

> "MWO datasets commonly have poor data quality. During data entry, fields may be left empty on certain MWOs, rendering a MWO ineffective for analyses, or in extreme cases, meaningless."

> "Using Day-of-Week Frequencies, we notice MWO reports are initiated on dates distributed approximately evenly throughout the work-week (around 20% for each weekday). However, the MWO closures mostly occur at the end of the week. Indeed, 19,597 MWOs out of 21,107 (around 93%) happened on Fridays, as opposed to the 4,000-5,000 we would expect from the uniformly distributed start-days."

> "Our findings indicate that human-caused data quality errors are likely to be non-random. Instead, they may be inadvertently bound-up with the resultant KPIs in unexpected ways."

> "In fact, restricted-entry systems can increase error probability under some circumstances (Sexton, Hodkiewicz, & Brundage, 2019)."

- **Source:** Conte, Bolland, Phan, Brundage & Sexton, "The Impact of Data Quality on Maintenance Work Order Analysis: A Case Study in HVAC Work Durations," *Proc. 6th European Conf. of the PHM Society 2021* (NIST) [^6^]
- **URL:** https://papers.phmsociety.org/index.php/phme/article/download/2814/1781
- **Date:** 2021; accessed 2026-07-18
- **Relevance:** if closure timestamps are administrative artifacts, any duration-based KPI (MTTR, downtime attribution) and any event-vs-process time alignment built on them is systematically wrong — a direct threat to lookback/backcasting time-series alignment.

### Finding 2.3 — Practitioner/consensus data on CMMS data quality failure modes

> "MIT Sloan Management Review research reveals that 47% of newly-created data records contain at least one critical error that would impact downstream processes."

> "Incomplete work order documentation: Between 40-60% of work orders close with missing critical information: no failure description, no root cause analysis, no parts consumed, or labor hours rounded to meaningless estimates like '4 hours' for everything."

> "Unreliable failure code categorization: When technicians have 50 failure codes to choose from (or worse, a free-text field), consistency evaporates. One technician codes a bearing failure as 'mechanical failure,' another as 'lubrication issue,' a third as 'vibration problem.' Analytics that should reveal 'bearing failures are our number one problem' instead show scattered, unactionable noise."

> "Poor timestamp accuracy: Work orders opened Monday but backdated to Friday to meet SLA targets. Completion times logged in bulk at shift end rather than actual finish time. PM tasks marked complete the day before they were actually performed. These temporal distortions make cycle time analysis, resource planning, and technician productivity metrics completely unreliable."

- **Source:** Infodeck, "CMMS Data Quality and Governance Guide" [^7^]
- **URL:** https://www.infodeck.io/resources/blog/cmms-data-quality-governance-guide/
- **Date:** 2026-03-18; accessed 2026-07-18
- **Note:** vendor/consultancy source, but consistent with the academic NIST findings above; MIT Sloan statistic widely cited in data-quality literature (Redman).

> "The CMMS is often treated like a place to log work, close tickets, and move on. Over time it becomes a database of activity, not a database of truth… Teams select 'Other,' 'Unknown,' or a default category because it's easier than making a judgment. Over time, the failure code history becomes meaningless."

> "When CMMS data is weak, KPIs become noise: MTBF looks better or worse than reality depending on how failures are logged… Pareto charts identify the wrong 'top problems' because codes are inconsistent… In short, the CMMS stops being a learning tool and becomes a compliance tool."

- **Source:** IVC Technologies, "How Wireless Vibration Monitoring Improves CMMS Data" [^8^]
- **URL:** https://ivctechnologies.com/2026/02/28/how-wireless-vibration-monitoring-improves-cmms-data/
- **Date:** 2026-02-28; accessed 2026-07-18

### Finding 2.4 — Manual downtime capture misses events and degrades timestamps (methods comparison)

> "Manual and paper-based logging… Limitations: data is incomplete, timestamps are approximate, reason codes are inconsistent, and the process depends entirely on operator compliance. Short stops are routinely missed."

> Comparison table: Manual/paper — Data completeness "Low (50-70%)", Timestamp accuracy "Low (estimated)", Reason code quality "Low (inconsistent)"; CMMS/MES — "Medium (work order events only)" completeness because "only captures events that generate a work order, which means minor stops and short-duration events are still missed."

- **Source:** Tractian, "Machine Downtime Tracking: Methods and Metrics" [^9b^]
- **URL:** https://tractian.com/en/blog/machine-downtime-tracking
- **Date:** 2026-03-18; accessed 2026-07-18

### Finding 2.5 — Time-alignment between event data and process data is a recognized technical obstacle

> "Gateways introduce latency, typically 50 to 200 milliseconds per transaction. More critically, they break timestamp alignment. A PLC event at 10:00:01.123 may arrive at the DCS with a different timestamp. For sequence-of-events analysis or root cause investigation, this mismatch becomes a major obstacle."

- **Source:** Emerson DCS-PLC Integration Engineering Guide (automation engineering practice blog) [^9^]
- **URL:** https://www.etowonauto.com/blogs/product-guide/emerson-dcs-plc-integration-engineering-guide
- **Date:** 2026-04-19; accessed 2026-07-18
- **Relevance:** trip/ESD event reconstruction requires ms-aligned process and event data; commercial lookbacks face the monthly analog — events logged in CMMS/incident systems must be re-aligned to daily production accounting and market data that use different clocks, calendars, and cut-offs.

### Finding 2.6 — Refinery-specific reconciliation data quality failures

> "Analyzed refineries' monthly reconciliation data and determined they were either erroneous or out of industry average oil loss… Evaluation of historical monthly mass reconciliation data for two refineries showed that: % loss/gain were not within industry average; Variation in monthly % loss/gain was not normal; % loss/gain in mass was positive for many months and it is not normal as there can never a positive gain in mass and negative gain in volume. This affects the financial results."

- **Source:** GlobalOMS, "Evaluation Study of a Refinery Mass Reconciliation Software" (Shell US/non-US refineries, Invensys MAB vs Aspen Advisor) [^11^]
- **URL:** https://www.globaloms.com/oms-project/bench-marking-study-for-a-refinery-hydrocarbon-management-hm/
- **Date:** 2019-11-01; accessed 2026-07-18

> "PIMS yields are the planning and budgeting benchmark. Actual plant yields (from DCS and laboratory data) are the accounting reality. Monthly reconciliation of PIMS budget yield to actual plant yield data is a required close procedure. Sustained underperformance vs. PIMS may indicate process unit degradation requiring disclosure assessment."

- **Source:** Refinery Accounting Handbook — Crude Economics, Inventory & RINs (refinerycontroller.com) [^10^]
- **URL:** https://www.refinerycontroller.com/
- **Date:** accessed 2026-07-18
- **Relevance:** plan-vs-actual reconciliation exists as a month-end *financial control*; the same document shows the variance "bridge" is a controller narrative exercise ("Present the bridge, not just the number") rather than a causal inference protocol.

### Tensions — Section 2
- Vendor sources (CMMS vendors, sensor vendors) have commercial incentive to exaggerate data-quality failure to sell automation; however, the magnitudes converge with independent academic findings (NIST), and the PHM/NIST case study quantifies the mechanism non-commercially.
- Controlled vocabularies are the standard fix for free-text chaos, yet NIST finds restricted-entry systems "can increase error probability under some circumstances" — data-quality governance is socio-technical, not just a dropdown design problem [^5^][^6^].
- Sensor/automated capture fixes timestamps and completeness but "reason codes still require operator input after the fact" — automation does not solve causal classification [^9b^].

---

## 3. RCA PRACTICE QUALITY: SHALLOW INVESTIGATIONS, "HUMAN ERROR" STOPPING RULES, AND IGNORED LESSONS

### Finding 3.1 — The field-defining methodological critique (Peerally et al., BMJ Quality & Safety 2017)

> "…RCA does have potential value in healthcare, but it has been widely applied without sufficient attention paid to what makes it work in its contexts of origin, and without adequate customisation for the specifics of healthcare. As a result, its potential has remained under-realised and the phenomenon of organisational forgetting remains widespread."

> "The first problem with RCA is its name. By implying—even inadvertently—that a single root cause (or a small number of causes) can be found, the term 'root cause analysis' promotes a flawed reductionist view. Incident investigation… too often results in a simple linear narrative that displaces more complex, and potentially fruitful, accounts of multiple and interacting contributions to how events really unfold."

> "…despite the complexities, sensitivities and challenges of this work, RCAs in healthcare are typically conducted by local teams, not the expert accident investigators who are proficient in systems thinking and human factors, cognitive interviewing, staff engagement and data analysis that are characteristic of other high-risk industries. Further, inconsistent use is made of the various investigative tools that are available. As a result, exemplary practice in the analysis of healthcare incidents is rare."

> "Investigating teams may end their analysis once they have reached a cause of mutual convenience, perhaps one that edits out causes (and thus solutions) deemed to be beyond the remit or capacities of the organisation…"

> "The available evidence points to the endemic tendency of investigators to settle for administrative and perhaps 'weaker' solutions (such as reminders) rather than those that address the latent causes, such as poorly designed technology or defective operational systems."

> "…few incentives exist to follow-up formally on action plans: estimates of implementation rates vary between 45% and 70%."

> "The eight problems we have discussed here mean that, too often, RCA results in the tombstone effect: though its purpose is to guard against a similar incident in the future, it may instead function primarily as a procedural ritual, leaving behind a memorial that does little more than allow a claim that something has been done."

> Box 1 ("Lessons not learnt"): wrong intraocular lens implanted → RCA → action plan of protocol, training, documentation, poster → "One year later, in the same hospital, a different patient with a different surgeon had the same procedure. Once again, the wrong lens was implanted."

- **Source:** Peerally MF, Carr S, Waring J, Dixon-Woods M, "The problem with root cause analysis," *BMJ Quality & Safety* 2017;26:417-422 (online 2016-06-25), DOI 10.1136/bmjqs-2016-005511 [^13^]
- **URL:** https://qualitysafety.bmj.com/content/26/5/417
- **Date:** 2016-06-25 (online); accessed 2026-07-18

### Finding 3.2 — Systematic review: no controlled trials; only anecdotal effectiveness evidence

> "Discussion of RCA did not emerge in the literature until the late 1990s, and there have been no controlled trials that test the RCA framework. Twenty-three articles describe the RCA process, 38 articles present RCA case studies, and 12 articles analyze weaknesses of the RCA framework. Eleven of the case studies measure RCA effectiveness, 3 using clinical outcome measures and 8 using process measures. All 11 articles report improvement of safety following RCA. RCA participants report the difficulty in forming causal statements and in developing/implementing corrective actions. Criticisms of RCA include the uncontrolled study design and participant biases."

> "Overall, the limited literature on RCA effectiveness provides anecdotal evidence that RCA improves safety. At the same time, it highlights the numerous theoretical problems with the analytical framework."

- **Source:** Percarpio KB, Watts BV, Weeks WB, "The effectiveness of root cause analysis: what does the literature tell us?" *Joint Commission Journal on Quality and Patient Safety* 2008;34(7):391-398 [^14^]
- **URL:** https://pubmed.ncbi.nlm.nih.gov/?term=Percarpio+root+cause+analysis+effectiveness
- **Date:** 2008; accessed 2026-07-18
- **Related:** Wu A, Lipshutz AKM, Pronovost PJ, "Effectiveness and efficiency of root cause analysis in medicine," *JAMA* 2008;299(6):685-687 — verified citation (cross-referenced in Peking Union Medical College Hospital study reference list); full text paywalled. Widely cited for the finding that RCA is required/ubiquitous yet its effectiveness is unproven and recommendations skew to weak actions [^14b^].

### Finding 3.3 — Dekker's New View: "human error" as conclusion is the core analytical failure

> "Human error is not a cause. It is the consequence of system design." — cover thesis of Dekker, *The Field Guide to Understanding Human Error* (2002; 3rd ed. 2014) [^15^]

> "Finding a 'human error' by any other name, or by any other human, is only the beginning of your journey, not a convenient conclusion." (publisher's description, Taylor & Francis) [^16^]

> "human error is systematically connected to people's tools, tasks and working environment" and "human error should be the start of an accident investigation, instead of the conclusion of an investigation" (New View summary) [^15b^]

- **Sources:** Dekker, *The Field Guide to Understanding Human Error*, 3rd ed., CRC/Taylor & Francis 2014 — https://www.taylorfrancis.com/books/mono/10.1201/9781315239675/field-guide-understanding-human-error-sidney-dekker [^16^]; summary analyses: controlhorizon.io (https://controlhorizon.io/blog/sidney-dekker-just-culture, 2026-05-09) [^15^]; altuent.com (https://altuent.com/insights/field-guide-to-understanding-human-error/, 2025-06-07) [^15b^]
- **Date:** book 2014 (3rd ed.); accessed 2026-07-18

### Finding 3.4 — Counterfactual reasoning and hindsight bias as documented failure modes of retrospectives

> "…[counterfactuals] make you spend your time talking about a reality that did not happen (but if it had happened, the mishap would not have happened.)" — Dekker, *Field Guide* (2006), p.39 [^17^]

> "James Reason's 'substitution test' can help here – asking whether another well-motivated, equally competent person might have done the same thing in that situation. 'Substitute the individual concerned, for someone else coming from the same domain of activity and possessing comparable qualifications and experience. Then ask the question "In the light of how events unfolded and were perceived by those involved in real time, is it likely that this new individual would have behaved any differently?"' If the answer is yes, the issue isn't the person, it's the system." [^17^]

- **Source:** PsychSafety, "Counterfactuals" (quoting Dekker 2006 p.39 and Reason 2003) [^17^]
- **URL:** https://psychsafety.com/counterfactuals/
- **Date:** 2025-11-04; accessed 2026-07-18

> "Selecting fragments of data can be a process of cherry-picking and story-crafting, whereby similar pieces are lumped together into a coherent narrative. The result is never truly 'objective,' since the construction of an event is influenced by the investigator's 'background, preferences, experiences, biases, beliefs, and purposes.'"

> "…many audits exhibited a 'comprehensive shallowness,' delving excessively into minor system details and paperwork rather than addressing critical factors. A plausible interpretation is that, in the clarity of hindsight, critical aspects amid a sea of issues become evident, embodying 'delusional clarity.'"

- **Source:** Hutchinson B, Dekker S, Rae A, "How audits fail according to accident investigations: A counterfactual logic analysis," *Process Safety Progress* (AIChE) 2024, DOI 10.1002/prs.12579 [^19^]
- **URL:** https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.12579
- **Date:** 2024-01-26; accessed 2026-07-18

### Finding 3.5 — Reason's model and his own warning about over-reaching causal attribution

> "Reason hypothesizes that most accidents can be traced to one or more of four levels of failure: Organisational influences, Unsafe supervision, Preconditions for unsafe acts, and The unsafe acts themselves." (Reason, *Human Error* 1990; BMJ 2000 "Human error: models and management") [^18^]

> "Reason himself worried that the model was being applied too broadly and dogmatically, '…the pendulum may have swung too far in our present attempts to track down possible errors and accident contributions that are widely separated in both time and place from the events themselves.' (from Managing Risks of Organizational Accidents, 1997)" [^18b^]

- **Sources:** SAE RM13010 Human Factors (quoting Reason) — https://pdfcoffee.com/rm13010-human-factors-pdf-free.html [^18^]; PsychSafety, "The Swiss Cheese Model" — https://psychsafety.com/the-swiss-cheese-model/ [^18b^]; further: "Understanding Safety in Healthcare: The System Evolution, Erosion and Enhancement Model," PMC4147744 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4147744/ ("Latent conditions result from poor decisions made by the higher management in an organization…")
- **Date:** accessed 2026-07-18

### Finding 3.6 — Even Toyota's own leadership criticized 5-Whys depth

> "…it has been criticized by Teruyuki Minoura, former managing director of global purchasing for Toyota, as being too basic a tool to analyze root causes to the depth that is needed to ensure that the causes are fixed. Reasons for this criticism include: Tendency for investigators to stop at symptoms rather than going on to lower level root causes. Inability to go beyond the investigator's current knowledge - can't find causes that they don't already know. Lack of support to help the investigator to ask the right 'why' questions. Results aren't repeatable - different people using 5 Whys come up with different causes for the same problem. The tendency to isolate a single root cause, whereas each question could elicit many different root causes."

- **Source:** Konstantoulakis F., "Root Cause Analysis" thesis, NTUA (citing Minoura; Serrat, ADB) [^14c^]
- **URL:** https://dspace.lib.ntua.gr/xmlui/bitstream/handle/123456789/3348/konstantoulakisi_rootcauseanalysis.pdf?sequence=3&isAllowed=y
- **Date:** undated thesis; accessed 2026-07-18

### Finding 3.7 — Field study of why organizations don't learn: investigations stop at direct causes; quick fixes become permanent

> "In the incident investigation there was a strong focus on direct causes and on the human error, and not on the context in which an error occurred and on the reasons for certain behavior. As a result, structural measures for improvement were not taken and follow-up actions mainly consisted of reminders of existing rules and procedures."

> "The quality of accident investigation was considered to be insufficient, because the investigators did not have the knowledge and experience to carry out root cause analyses. The quality was also limited because the investigators were afraid to include human factors, for a fear of blame colleagues. The lack of knowledge and fear to include all factors resulted in investigations in which underlying issues were not addressed."

> "After an incident there was often an immediate solution, the 'quick fix'. After the quick fix, people got back to normal day to day work, and as one participant stated 'the quick fix often turns out to be the permanent solution'."

> Bottleneck table: "Systematic causes not identified (A,D,F,G) — Limitation to direct causes i.e. human or technical causes, limitation to mitigating actions, time pressure on completion analysis."

> "…not learning from incidents, is an incident to be analyzed in itself."

- **Source:** Drupsteen L, Hasle P, "Why do organizations not learn from incidents? Bottlenecks, causes and conditions for a failure to effectively learn," *Safety Science* 2014 (focus groups in 7 organizations incl. chemical and oil & gas companies) [^20^]
- **URL:** https://mvzo.org/wp-content/uploads/2024/06/140811-drupsteen-Why-do-organizations-not-learn-from-incidents.pdf
- **Date:** 2014 (available online 2014-08-11); accessed 2026-07-18

### Finding 3.8 — Organizational memory loss documented in the energy industry

> "As Kletz has stated, 'Organizations do not learn from the past or, rather, individuals learn but they leave the organization, taking their knowledge with them, and the organization as a whole forgets.'"

> "Interviewees were well aware of all events within the last three years. Beyond three years, interviewees were unaware of the event unless one of three reasons existed: [personal involvement; company-changing significance; recent similar event triggering memory]."

> "Perry's Chemical Engineer's Handbook… reiterates what Kletz states, saying that we know how to prevent most accidents, but they occur because we do not utilize the information that is available to us. Over time, the recommendations made following an accident are forgotten, procedures are allowed to lapse, changes are made to equipment and the accident is just waiting to happen again."

- **Source:** Thrones B, "Keeping the Memory Alive: Preventing Memory Loss That Contributes to Process Safety Events" (review of 84 PSE investigation reports + interviews at a Canadian energy company) [^21^]
- **URL:** https://www.cheminst.ca/wp-content/uploads/2019/04/Keeping20the20Memory20Alive20-20Barry20Thrones-1.pdf
- **Date:** undated (post-2014); accessed 2026-07-18

### Finding 3.9 — CSB findings: repeated incidents with prior lessons documented but ignored

> Tesoro Anacortes (2010, 7 fatalities): "Although the refinery had a history of frequent leaks and some fires during this activity, management repeatedly failed to ensure that these hazards were controlled and that the number of workers exposed to these hazards was minimized." (UCLA LOSH teaching guide summarizing CSB Report 2010-08-I-WA) [^22^]

> BP Texas City (2005, 15 killed): "The Texas City disaster was caused by organization and safety deficiencies at all levels of the BP Corporation. Warning signs of a possible disaster were present for several years, but company officials did not intervene effectively to prevent [it]." (CSB, via UCLA LOSH guide) [^22^]

> Tesoro Martinez (2014): "CSB issued a special case study on how a weak process safety culture created conditions that were contributing factors to these two similar incidents. Examples to support this finding: Incident investigations: Failure to learn from past incidents…" [^22^]

- **Source:** UCLA LOSH, "Using Chemical Safety Board Reports and…" (teaching guide compiling CSB reports) [^22^]
- **URL:** https://losh.ucla.edu/wp-content/uploads/sites/37/2021/02/CSB-Guide.pdf
- **Date:** 2021; accessed 2026-07-18

> "The CSB's October 27, 2005 news release noted that if BP had applied lessons learned from previous incidents at the Texas City facility, BP could have corrected flawed systems prior to March 23, 2005, possibly preventing the disaster. In commenting more broadly on the concept of 'lessons learned' in chemical process safety, Rosenthal noted, 'It is clear that implementation of lessons already learned could have prevented the large majority of process accidents.'"

- **Source:** McQuiston TH et al., "Beyond Texas City: The State of Process Safety in the Unionized U.S. Oil Refining Industry," *New Solutions* 19(3):271-88 (2009) [^23^]
- **URL:** https://www.researchgate.net/publication/26835843_Beyond_Texas_City_The_State_of_Process_Safety_in_the_Unionized_US_Oil_Refining_Industry
- **Date:** 2009; accessed 2026-07-18

> Honeywell Geismar (CSB final report, May 27, 2025 — three HF incidents Oct 2021–Jun 2024): "In the fatal October 2021 incident, board investigators found that Honeywell was aware in 2007 of corrosion damage to the type of gasket that failed and had documented the need to change to a different kind of gasket technology. However, Honeywell decided to replace the gaskets on an attrition basis. At the time of the incident in 2021—more than 14 years later—Honeywell still hadn't replaced all the gaskets (including the one that failed)."

> CSB Chairperson Steve Owens: "Not only were these three serious incidents completely unacceptable, our investigation found that they also were entirely preventable."

- **Source:** EHS Daily Advisor, "CSB Issues Final Report on Chemical Incidents at Honeywell Facility" [^24^]
- **URL:** https://ehsdailyadvisor.com/2025/06/csb-issues-final-report-on-chemical-incidents-at-honeywell-facility/
- **Date:** 2025-06 (report 2025-05-27); accessed 2026-07-18

> "CSB investigations indicate that the systemic problems identified at Bhopal remain the underlying causes of many incidents. These include: Lack of awareness of reactive hazards. Lack of management of change. Inadequate plant design and maintenance. Ineffective employee training. Ineffective emergency preparedness and community notification. Lack of root cause incident investigations and communication of lessons learned."

- **Source:** Mannan MS et al., CSB-authored paper (with disclaimer: authors' views), via ResearchGate [^25^]
- **URL:** https://www.researchgate.net/publication/221947346_An_approach_for_risk_reduction_methodology_based_on_optimizing_the_facility_layout_and_siting_in_toxic_gas_release_scenarios
- **Date:** undated (mid-2000s); accessed 2026-07-18

> "…a common thread that emerges in CSB investigations is the inadequacy of management systems that might have prevented the incident from occurring. Examples of the systemic issues identified in CSB reports are: Lack of hazard review to predict and prevent incidents; Insufficient investigation and follow-up after previous incidents; Inadequate training of staff; Failure to implement effective mechanical integrity programs." — CSB investigator Angela S. Blair, *Process Safety Progress* 2004 [^25b^]

- **Source:** Blair AS (CSB), "Management Systems: Causal Factors in Incidents" (via Park & Blair, "Insights into process safety incidents from an analysis of CSB investigations") [^25b^]
- **URL:** https://www.researchgate.net/publication/305679453_Insights_into_process_safety_incidents_from_an_analysis_of_CSB_investigations
- **Date:** 2004/2016; accessed 2026-07-18

### Tensions — Section 3
- **Counterfactuals cut both ways:** Dekker/safety science attack counterfactual reasoning in *blame-oriented* investigations ("they should have…"), while formal causal inference treats counterfactuals as the rigorous standard for attribution ("what would margin have been absent event X?"). The reconciliation: counterfactuals are legitimate as model-based estimands with stated assumptions; illegitimate as hindsight judgment of people. Reason himself warned the pendulum "may have swung too far" in chasing remote latent contributions — causal depth must remain actionable [^17^][^18b^].
- **Effectiveness evidence vs. publication bias:** all 11 RCA case studies reviewed by Percarpio reported improvement, yet the same review stresses uncontrolled designs and participant bias — positive cases are plausibly selected for publication [^14^].
- **Transfer problem:** RCA was imported to healthcare from high-risk industries; Peerally argues healthcare adopted the ritual without the expert-investigator infrastructure. In refining (a "high-risk industry of origin"), the critique applies in reverse: expert CSB-style investigations exist but are external and rare; internal RCAs share the healthcare pathologies (Drupsteen evidence) [^13^][^20^].
- **Blame vs accountability:** New View does not abolish accountability ("when blatant transgressions, neglect or unacceptable behaviour is found, it is clearly wrong to write accountability out of the picture" — Peerally) [^13^].

---

## 4. FORECAST/PLAN EVALUATION PRACTICE: ERROR MAGNITUDE vs STRUCTURAL BIAS AND ASSUMPTIONS

### Finding 4.1 — MAPE's documented pathologies; accuracy metrics say nothing about direction or structure

> "Despite its ubiquity, MAPE has well-documented mathematical pathologies. Hyndman and Koehler (2006) provide a systematic treatment of these failure modes and argue that MAPE should be used cautiously or replaced in many practical forecasting contexts. Division by zero… Asymmetric penalty structure. Over-forecasting is bounded at 100% error… while under-forecasting is unbounded. This asymmetry means MAPE implicitly penalizes under-forecasting more heavily than over-forecasting of the same absolute magnitude, potentially biasing model selection toward systematically high forecasts."

> "Hyndman and Koehler (2006) note that unbiasedness is a distinct desideratum from accuracy, and that optimizing for accuracy metrics alone does not guarantee bias elimination."

- **Source:** WFM Labs wiki, "MAPE WAPE and Forecast Bias" (citing Hyndman RJ & Koehler AB, "Another look at measures of forecast accuracy," *Int. J. Forecasting* 22(4):679-688, 2006) [^26^]
- **URL:** https://wiki.wfmlabs.org/wiki/MAPE_WAPE_and_Forecast_Bias
- **Date:** 2026-05-17; accessed 2026-07-18

> "MAPE does not reflect the direction of errors (over-predictions vs. under-predictions), which can be crucial in supply chain demand planning… Blindly optimizing for MAPE can result in sub-optimal forecasts."

- **Source:** alitiq docs, "Pitfalls using MAPE as forecast accuracy metric" (citing Armstrong & Collopy 1992; Goodwin & Lawton 1999) [^27^]
- **URL:** https://docs.alitiq.com/knowledge/2024/10/16/pitfalls-using-mape-as-forecast-accuracy-metric/
- **Date:** 2024-10-16; accessed 2026-07-18

> Goodwin P, Lawton R, "On the Asymmetry of the Symmetric MAPE," *Int. J. Forecasting* 15(4):405-8 (1999): "although the modified APE is symmetric when A and F are interchanged, it in fact creates a new problem of asymmetry which is more likely to be of practical concern…" [^28^]

- **URL:** https://www.academia.edu/12644241/On_the_asymmetry_of_the_symmetric_MAPE
- **Date:** 1999; accessed 2026-07-18

### Finding 4.2 — Bias analysis is the structural diagnostic practice is missing

> "A forecast that is randomly wrong by 20% in both directions may produce adequate operational outcomes… A forecast that is systematically wrong by 10% in one direction — always over-forecasting by 10% — creates compounding operational and financial consequences: Systematic over-staffing… Systematic under-staffing… Planning credibility erosion — when operational managers learn that forecasts are reliably wrong in a predictable direction, they apply informal adjustments that undermine the formal forecasting process."

> "Fildes and Goodwin (2007) document that judgmental adjustments to statistical forecasts are on average harmful, particularly for large upward adjustments."

- **Source:** WFM Labs wiki, "MAPE WAPE and Forecast Bias" [^26^]
- **URL:** https://wiki.wfmlabs.org/wiki/MAPE_WAPE_and_Forecast_Bias
- **Date:** 2026-05-17; accessed 2026-07-18

> Morlidge interview: "Typically we find that most businesses struggle to beat the performance of the naïve forecast by more than 10-15% and that 40-50% of low-level forecasts perform worse than the naive and so destroy value… Our approach involves decomposing the RAE measure into its two constituent parts – bias (the result of systematic under or over-forecasting) and variation (unsystematic error – relative to the naïve forecast) as they impact the business in different ways and have different causes requiring different solutions."

- **Source:** Demand-Planning.com, "Forecast Value Added (FVA) – Series 3 Interview" (Gilliland interviewing Morlidge) [^31^]
- **URL:** https://demand-planning.com/2015/03/02/forecast-value-added-fva-series-3-interview-2/
- **Date:** 2015-03-02; accessed 2026-07-18

### Finding 4.3 — Forecast Value Added (FVA): process steps are rarely validated; often destroy value

> "Here, averaged across all products, naive (random walk) achieved forecast accuracy of 60%. The company's statistical forecast delivered five percentage points of improvement, but management review and adjustment delivered negative value. Such findings – not uncommon – urge further investigation into causes and possible process corrections (such as training reviewers or limiting adjustments)." (Newell Rubbermaid stairstep: Naive 60% → Statistical 65% → Adjusted 62%; management review FVA −3%)

> "Morlidge's (2014b) study of eight consumer and industrial businesses found 52% of their forecasts failed to [beat naive]. And, as shown, Newell Rubbermaid beat naive by just two percentage points after management adjustments."

> "It has long been recognised (Chatfield, 1986; Lawrence, 2000) that the practice of forecasting falls well short of the potential exhibited in academic research…"

> "Prediction intervals in software generally underestimate uncertainty, often dramatically, leading to unrealistic confidence in the forecast. And even when provided, PIs largely go unused by practitioners."

- **Source:** Petropoulos F et al. (incl. Gilliland), "Forecasting: theory and practice," *Int. J. Forecasting* 2022 (arXiv 2012.03854) [^30^]
- **URL:** https://ar5iv.org/abs/2012.03854
- **Date:** 2020-09-05 (arXiv); accessed 2026-07-18

### Finding 4.4 — Model risk management as the institutionalized analogue (Federal Reserve SR 11-7)

> "Evaluation of Conceptual Soundness. This element involves assessing the quality of the model design and construction, as well as review of documentation and empirical evidence supporting the methods used and variables selected for the model. This step in validation should ensure that judgment exercised in model design and construction is well informed, carefully considered, and consistent with published research and with sound industry practice."

> "Ongoing Monitoring. This step in validation is done to confirm that the model is appropriately implemented and is being used and performing as intended. It is essential to evaluate whether changes in products, exposures, activities, clients, or market conditions necessitate adjustment, redevelopment, or replacement of the model…"

> "Outcomes Analysis. This step involves comparing model outputs to corresponding actual outcomes. Back-testing is one form of outcomes analysis that involves the comparison of actual outcomes with model forecasts during a sample time period not used in model development at a frequency that matches the model's forecast horizon or performance window."

- **Source:** Board of Governors of the Federal Reserve System / OCC, SR 11-7: "Supervisory Guidance on Model Risk Management" (April 4, 2011) [^32^]
- **URL:** http://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.pdf
- **Date:** 2011-04-04; accessed 2026-07-18
- **Relevance:** SR 11-7 makes *assumption review* (conceptual soundness), *bias/drift monitoring* (ongoing monitoring), and *outcomes analysis vs actuals* (back-testing) mandatory, independent, and documented — precisely the triad absent from typical refinery plan-vs-actual lookbacks, where evaluation stops at variance magnitude and narrative.

### Finding 4.5 — Refinery plan-vs-actual practice exists as financial control, not causal evaluation

> "The written monthly analysis prepared by the controller that reconciles the theoretical benchmark crack spread (the market's economic expectation) to the actual reported gross margin per barrel. Quantifies each contributing factor — inventory cost lag, RIN costs, hedge timing effects, yield mix, throughput variance — in both $/bbl and total dollar terms… It should be one organized, clearly labeled page, delivered proactively before the CFO asks for it… Not a verbal explanation — a written, signed, documented analysis."

> "Controller: Fixed OpEx per barrel rises mechanically when throughput declines below budget (volume variance). Comparing OpEx per barrel across periods without normalizing for throughput volume creates misleading efficiency conclusions."

- **Source:** Refinery Accounting Handbook (refinerycontroller.com) [^10^]
- **URL:** https://www.refinerycontroller.com/
- **Date:** accessed 2026-07-18
- **Note:** this is *good* practice guidance (decomposition, normalization) — evidence the "bridge" discipline exists in refinery accounting — but it is an accounting attribution, not an assumption/model audit: it quantifies factor contributions to margin without testing whether the LP model's structural assumptions (yields, constraints, price relationships) were causally valid.

### Tensions — Section 4
- **Metric debates are unsettled:** Makridakis defended sMAPE against Goodwin & Lawton's critique; the literature is "littered with errors" and competing definitions (Hyndman) — practitioner guidance itself is conflicted [^27^][^28^].
- **FVA has its own critics:** "FVA… does not yield insights into why statistical models might under-perform, simply that they under-perform. FVA is thus not so much a diagnostic tool as a magnifying glass" (Lokad); and Goodwin: "FVA, as it is often applied, is really Forecast Accuracy Added (FAA)" — accuracy is not business value [^30b^].
- **Vendor incentive:** many anti-MAPE sources sell alternative metrics/engines; the core academic critique (Hyndman & Koehler) is metric-focused, not a wholesale rejection of magnitude metrics.
- **SR 11-7 is banking-regulatory:** its evidentiary burden is enforced by supervisors; transferring it to internal planning models has no equivalent external forcing function — which is itself the finding.

---

## 5. WHAT "GOOD" LOOKS LIKE: CAUSAL METHODS, RCA GOVERNANCE — AND THE EVIDENCE THEY ARE RARELY INSTITUTIONALIZED

### Finding 5.1 — Causal-inference-grade methods exist for industrial retrospectives

> "This paper develops a methodology to combine diagnostic information from various fault detection and isolation tools to diagnose the true root cause of an abnormal event in industrial processes. Limited diagnostic information from kernel principal component analysis, other on-line fault detection and diagnostic tools, and process knowledge were combined through Bayesian belief network (BBN)… The proposed methodology was applied to Fluid Catalytic Cracking unit and Tennessee Eastman Chemical Process. In both cases, the proposed approach showed a good capability of diagnosing the root cause of abnormal conditions."

- **Source:** "Root Cause Diagnosis of Process Fault Using KPCA and Bayesian Network," *Industrial & Engineering Chemistry Research* 2017, DOI 10.1021/acs.iecr.6b01916 [^33^]
- **URL:** https://www.x-mol.com/paper/1518635631412895744
- **Date:** 2017-02-14; accessed 2026-07-18

> "…the fuzzy fault tree is mapped to Bayesian network for reliability analysis, and the fuzzy probability of bottom event is taken as priori probability to calculate probability of leaf node occurrence, thus posterior probability, probability importance and key importance of root node are obtained, so as to quickly determine fault type and fault location."

- **Source:** Zhang, Xu, Sun, Meng, "Fault diagnosis of mine hoist based on fuzzy fault tree and Bayesian network," *Journal of Mine Automation* 2020;46(11):1-5 [^34^]
- **URL:** http://www.gkzdh.cn/en/article/doi/10.13272/j.issn.1671-251x.17562
- **Date:** 2020-11-20; accessed 2026-07-18

**Complementary "good practice" building blocks identified in this research:**
- **Counterfactual discipline for people-systems:** Reason's substitution test; Dekker's local rationality — reconstruct "why it made sense at the time" rather than judging against a fictional alternative [^17^].
- **Decomposition:** Morlidge's bias/variation split of forecast error [^31^]; refinery controller bridge decomposition of margin variance [^10^]; FVA stairstep attribution to process steps [^30^].
- **Model governance:** SR 11-7 triad (conceptual soundness / monitoring / outcomes analysis) with independent validation [^32^].
- **Data-quality forensics before analysis:** EDA-based detection (day-of-week histograms, category-value counts, zero/negative durations), survival-analysis correction of censored timestamps (NIST/PHM) [^6^].

### Finding 5.2 — What good RCA governance looks like (Peerally's proposals, echoed across sources)

> "The first step in securing improvement is likely to involve the professionalisation of incident investigation: those conducting it need specialist expertise in underlying theories, ergonomics, human factors and hands-on experience of analytical methods. For these reasons, the establishment of professional investigatory bodies… are welcome."

> "Fourth, healthcare must focus increasingly on aggregated analysis of incidents… At the national level, aggregated analyses offer a way of identifying common themes across similar and apparently more disparate incidents and may also serve as a means of generating actions that require collaborative efforts…"

> "…healthcare urgently needs to develop and evaluate much better methods for designing risk controls and other improvement actions. One possibility that could be evaluated, for example, is that of a hierarchy of risk controls… the use of active surveillance of issues that have already been detected and monitoring of effectiveness of risk controls need to become a routine part of the risk management process following RCAs."

- **Source:** Peerally et al., *BMJ Quality & Safety* 2017;26:417-422 [^13^]
- **URL:** https://qualitysafety.bmj.com/content/26/5/417
- **Date:** 2016-06-25; accessed 2026-07-18

> "…studying the learning process does, however, require a shift from learning from incidents to learning to learn… not learning from incidents, is an incident to be analyzed in itself."

- **Source:** Drupsteen & Hasle, *Safety Science* 2014 [^20^]
- **URL:** https://mvzo.org/wp-content/uploads/2024/06/140811-drupsteen-Why-do-organizations-not-learn-from-incidents.pdf
- **Date:** 2014; accessed 2026-07-18

### Finding 5.3 — The evidence that rigor is rarely institutionalized

| Institutionalization gap | Evidence |
|---|---|
| Analytics maturity | 87% of organizations at "basic" or "opportunistic" BI/analytics maturity (Gartner 2018, n=813) [^2^] |
| RCA exemplars | "exemplary practice in the analysis of healthcare incidents is rare" (Peerally et al. 2017) [^13^] |
| RCA validation | "there have been no controlled trials that test the RCA framework" (Percarpio et al. 2008) [^14^] |
| Corrective action strength | "endemic tendency… to settle for administrative and perhaps 'weaker' solutions (such as reminders)" (Peerally) [^13^]; "follow-up actions mainly consisted of reminders of existing rules and procedures" (Drupsteen & Hasle) [^20^] |
| Action completion | "estimates of implementation rates vary between 45% and 70%" (Peerally) [^13^]; "the quick fix often turns out to be the permanent solution" (Drupsteen) [^20^] |
| Forecast process validation | 52% of forecasts failed to beat naive (Morlidge, 8 businesses); management adjustments subtract value (Newell Rubbermaid) [^30^]; "most companies never create a naive forecast and do not perform the second step of comparing their current forecast against the naive" (Brightwork) [^30c^] |
| Uncertainty practice | "Prediction intervals in software generally underestimate uncertainty, often dramatically… PIs largely go unused by practitioners" (Petropoulos et al. 2022) [^30^] |
| Organizational memory | events forgotten beyond ~3 years absent personal involvement (Thrones, energy industry) [^21^]; Kletz: organizations forget as individuals leave [^21^] |
| Repeat incidents | CSB: Tesoro Anacortes, Texas City, Tesoro Martinez, Honeywell Geismar — lessons documented years earlier, not implemented [^22^][^23^][^24^] |

### Finding 5.4 — Tensions and caveats for the "good practice" agenda
- **Methods exist vs. are used:** BBN/fault-tree RCA is demonstrated in academic case studies (FCC, Tennessee Eastman) but there is little evidence of routine adoption in plant lookback processes — the publication record is methodological, not operational [^33^][^34^].
- **Formal counterfactuals vs. Dekker's critique:** causal-inference counterfactuals (rung 3, Pearl) require explicit causal models and assumptions; Dekker's target is *unmodeled* counterfactual storytelling. A VCO lookback can legitimately ask "what would have happened without the trip?" only with an explicit causal/decomposition model — otherwise it reproduces the blame narrative in commercial dress [^17^][^19^].
- **Depth vs. actionability:** Reason's own "pendulum" caution implies governance must bound causal depth to controllable system changes; unbounded latent-factor hunts dilute accountability [^18b^].
- **Independent investigation trades speed for rigor:** professionalized bodies (CSB/HSIB model) are slower and external; internal RCA is fast but conflicted ("lack of independence from the organisation where the event took place" — Peerally) [^13^].
- **FVA/SR-11-7 discipline has a cost:** naive-benchmarking and back-testing require retained forecast vintages and assumption logs that most planning organizations do not keep — a data-architecture precondition, not just an analytical choice [^30c^][^32^].

---

## SOURCE LIST

[^1^] IRE Journals — "The Impact of Data Visualization on Decision-Making" (review). https://www.irejournals.com/formatedpaper/1715288.pdf (undated; accessed 2026-07-18)
[^2^] Information Age — "Gartner finds 87% of organisations have low BI and analytics maturity" (Gartner press release, 2018-12-06, n=813). https://www.information-age.com/low-bi-and-analytics-maturity-12257/ (accessed 2026-07-18)
[^3^] Lazer D, Kennedy R, King G, Vespignani A — "The Parable of Google Flu: Traps in Big Data Analysis," *Science* 2014;343:1203-1205. Corroborating: Cambridge Core, *Big Crisis Data* ch.9 (2026-05-16 update) https://www.cambridge.org/core/books/big-crisis-data/validity-biases-and-pitfalls-of-social-media-data/D0DB80718C71FCD37C282688206129A6; Lazer et al. follow-up, Harvard DASH https://dash.harvard.edu/entities/publication/73120378-c595-6bd4-e053-0100007fdf3b (accessed 2026-07-18)
[^4^] AAPOR — "AAPOR Report on Big Data" (2015). https://doku.iab.de/grauepap/2015/BigDataTaskForceReport_FINAL_2_12_15.pdf (accessed 2026-07-18)
[^5^] Sexton T, Hodkiewicz M, Brundage MP (NIST/UWA) — "Categorization Errors for Data Entry in Maintenance Work-Orders" (PHM 2019). https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=928437 (accessed 2026-07-18)
[^6^] Conte A, Bolland C, Phan L, Brundage M, Sexton T (NIST) — "The Impact of Data Quality on Maintenance Work Order Analysis: A Case Study in HVAC Work Durations," PHM Society Europe 2021. https://papers.phmsociety.org/index.php/phme/article/download/2814/1781 (accessed 2026-07-18)
[^7^] Infodeck — "CMMS Data Quality and Governance Guide" (2026-03-18). https://www.infodeck.io/resources/blog/cmms-data-quality-governance-guide/ (accessed 2026-07-18)
[^8^] IVC Technologies — "How Wireless Vibration Monitoring Improves CMMS Data" (2026-02-28). https://ivctechnologies.com/2026/02/28/how-wireless-vibration-monitoring-improves-cmms-data/ (accessed 2026-07-18)
[^9^] Emerson DCS-PLC Integration Engineering Guide (2026-04-19). https://www.etowonauto.com/blogs/product-guide/emerson-dcs-plc-integration-engineering-guide (accessed 2026-07-18)
[^9b^] Tractian — "Machine Downtime Tracking: Methods and Metrics" (2026-03-18). https://tractian.com/en/blog/machine-downtime-tracking (accessed 2026-07-18)
[^10^] Refinery Accounting Handbook — Crude Economics, Inventory & RINs. https://www.refinerycontroller.com/ (accessed 2026-07-18)
[^11^] GlobalOMS — "Evaluation Study of a Refinery Mass Reconciliation Software" (2019-11-01). https://www.globaloms.com/oms-project/bench-marking-study-for-a-refinery-hydrocarbon-management-hm/ (accessed 2026-07-18)
[^12^] CNA — "Goodhart's Law" (2022-09-01). https://www.cna.org/analyses/2022/09/goodharts-law (accessed 2026-07-18)
[^12b^] ModelThinkers — "Goodhart's Law" (2018-03-27). https://modelthinkers.com/mental-model/goodharts-law (accessed 2026-07-18)
[^13^] Peerally MF, Carr S, Waring J, Dixon-Woods M — "The problem with root cause analysis," *BMJ Quality & Safety* 2017;26:417-422 (online 2016-06-25). https://qualitysafety.bmj.com/content/26/5/417 (accessed 2026-07-18)
[^14^] Percarpio KB, Watts BV, Weeks WB — "The effectiveness of root cause analysis: what does the literature tell us?" *Jt Comm J Qual Patient Saf* 2008;34(7):391-398 (PubMed abstract). https://pubmed.ncbi.nlm.nih.gov/?term=Percarpio+root+cause+analysis+effectiveness (accessed 2026-07-18)
[^14b^] Wu A, Lipshutz AKM, Pronovost PJ — "Effectiveness and efficiency of root cause analysis in medicine," *JAMA* 2008;299(6):685-687 (citation verified via PUMCH reference list: https://www.sciengine.com/PUMCH/doi/10.12290/xhyxzz.20200020; full text paywalled) (accessed 2026-07-18)
[^14c^] Konstantoulakis F — "Root Cause Analysis" thesis, NTUA (citing Minoura; Serrat/ADB). https://dspace.lib.ntua.gr/xmlui/bitstream/handle/123456789/3348/konstantoulakisi_rootcauseanalysis.pdf?sequence=3&isAllowed=y (accessed 2026-07-18)
[^15^] Control Horizon — "Sidney Dekker. Killing the Human Error Label" (2026-05-09), quoting Dekker, *The Field Guide to Understanding Human Error* (2002). https://controlhorizon.io/blog/sidney-dekker-just-culture (accessed 2026-07-18)
[^15b^] Altuent — "The Continued Relevance of Dekker's Field Guide" (2025-06-07). https://altuent.com/insights/field-guide-to-understanding-human-error/ (accessed 2026-07-18)
[^16^] Taylor & Francis — Dekker, *The Field Guide to Understanding Human Error*, 3rd ed. (2014/2017 e-book). https://www.taylorfrancis.com/books/mono/10.1201/9781315239675/field-guide-understanding-human-error-sidney-dekker (accessed 2026-07-18)
[^17^] PsychSafety — "Counterfactuals" (2025-11-04), quoting Dekker (2006) p.39 and Reason (2003) substitution test. https://psychsafety.com/counterfactuals/ (accessed 2026-07-18)
[^18^] SAE RM13010 Human Factors (quoting Reason 1990). https://pdfcoffee.com/rm13010-human-factors-pdf-free.html; also Reason J, "Human error: models and management," *BMJ* 2000;320:768-770 (accessed 2026-07-18)
[^18b^] PsychSafety — "The Swiss Cheese Model" (2025-12-22), quoting Reason, *Managing the Risks of Organizational Accidents* (1997). https://psychsafety.com/the-swiss-cheese-model/ (accessed 2026-07-18)
[^19^] Hutchinson B, Dekker S, Rae A — "How audits fail according to accident investigations: A counterfactual logic analysis," *Process Safety Progress* 2024, DOI 10.1002/prs.12579. https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.12579 (accessed 2026-07-18)
[^20^] Drupsteen L, Hasle P — "Why do organizations not learn from incidents? Bottlenecks, causes and conditions for a failure to effectively learn," *Safety Science* 2014. https://mvzo.org/wp-content/uploads/2024/06/140811-drupsteen-Why-do-organizations-not-learn-from-incidents.pdf (accessed 2026-07-18)
[^21^] Thrones B — "Keeping the Memory Alive: Preventing Memory Loss That Contributes to Process Safety Events," Chemistry Institute of Canada conf. paper. https://www.cheminst.ca/wp-content/uploads/2019/04/Keeping20the20Memory20Alive20-20Barry20Thrones-1.pdf (accessed 2026-07-18)
[^22^] UCLA LOSH — "Using Chemical Safety Board Reports and [Videos in the Classroom]" (2021). https://losh.ucla.edu/wp-content/uploads/sites/37/2021/02/CSB-Guide.pdf (accessed 2026-07-18)
[^22b^] Holmstrom D (CSB) — "Some observations about major chemical accidents from CSB investigations," IChemE paper. https://www.icheme.org/media/9698/xx-paper-03.pdf (accessed 2026-07-18)
[^23^] McQuiston TH et al. — "Beyond Texas City: The State of Process Safety in the Unionized U.S. Oil Refining Industry," *New Solutions* 19(3):271-88 (2009). https://www.researchgate.net/publication/26835843_Beyond_Texas_City_The_State_of_Process_Safety_in_the_Unionized_US_Oil_Refining_Industry (accessed 2026-07-18)
[^24^] EHS Daily Advisor — "CSB Issues Final Report on Chemical Incidents at Honeywell Facility" (2025-06; CSB report 2025-05-27). https://ehsdailyadvisor.com/2025/06/csb-issues-final-report-on-chemical-incidents-at-honeywell-facility/ (accessed 2026-07-18)
[^25^] Mannan MS et al. (CSB-authored) — "An approach for risk reduction methodology based on optimizing the facility layout and siting in toxic gas release scenarios" (incl. Bhopal systemic problems list). https://www.researchgate.net/publication/221947346 (accessed 2026-07-18)
[^25b^] Park S, Blair AS (CSB) — "Insights into process safety incidents from an analysis of CSB investigations," *Process Safety Progress* (Blair 2004 paper quoted). https://www.researchgate.net/publication/305679453 (accessed 2026-07-18)
[^26^] WFM Labs wiki — "MAPE WAPE and Forecast Bias" (2026-05-17; citing Hyndman & Koehler 2006; Fildes & Goodwin 2007). https://wiki.wfmlabs.org/wiki/MAPE_WAPE_and_Forecast_Bias (accessed 2026-07-18)
[^27^] alitiq docs — "Pitfalls using MAPE as forecast accuracy metric" (2024-10-16). https://docs.alitiq.com/knowledge/2024/10/16/pitfalls-using-mape-as-forecast-accuracy-metric/ (accessed 2026-07-18)
[^28^] Goodwin P, Lawton R — "On the Asymmetry of the Symmetric MAPE," *Int. J. Forecasting* 1999;15(4):405-408. https://www.academia.edu/12644241/On_the_asymmetry_of_the_symmetric_MAPE (accessed 2026-07-18)
[^30^] Petropoulos F et al. — "Forecasting: theory and practice," *Int. J. Forecasting* 2022 (arXiv:2012.03854, 2020-09-05). https://ar5iv.org/abs/2012.03854 (accessed 2026-07-18)
[^30b^] Lokad — "Forecast Value Added" (2021-01-20). https://www.lokad.com/forecast-value-added/ (accessed 2026-07-18)
[^30c^] Brightwork Research — "How to Best Understand the Naive Forecast" (2024-01-18). https://www.brightworkresearch.com/naive-forecast/ (accessed 2026-07-18)
[^31^] Demand-Planning.com — "Forecast Value Added (FVA) – Series 3 Interview" (Gilliland/Morlidge, 2015-03-02). https://demand-planning.com/2015/03/02/forecast-value-added-fva-series-3-interview-2/ (accessed 2026-07-18)
[^32^] Federal Reserve / OCC — SR 11-7, "Supervisory Guidance on Model Risk Management" (2011-04-04). http://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.pdf (accessed 2026-07-18)
[^33^] (Authors via X-MOL) — "Root Cause Diagnosis of Process Fault Using KPCA and Bayesian Network," *Ind. Eng. Chem. Res.* 2017, DOI 10.1021/acs.iecr.6b01916. https://www.x-mol.com/paper/1518635631412895744 (accessed 2026-07-18)
[^34^] Zhang M, Xu T, Sun H, Meng X — "Fault diagnosis of mine hoist based on fuzzy fault tree and Bayesian network," *J. Mine Automation* 2020;46(11):1-5. http://www.gkzdh.cn/en/article/doi/10.13272/j.issn.1671-251x.17562 (accessed 2026-07-18)

---
*Prepared 2026-07-18. Searches executed: 16 search batches (35+ distinct queries) plus 7 targeted document opens. Verbatim excerpts preserved incl. original spelling/grammar. Vendor/consultancy sources flagged where used; core claims anchored to academic (NIST, PHM Society, BMJ, Safety Science, I&EC Research, IJF, AIChE) and regulatory (CSB-derived, Federal Reserve) sources.*

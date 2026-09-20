# Dimension 12 — Knowledge Management / Lessons-Learned Practice & AI Readiness in Process Industries

**Research brief for:** Downstream refining & marketing VCO / lookback-backcasting / CI knowledge-management study
**Research date:** 2026-07-18
**Method:** 38 independent web searches (KM academic & trade literature, ISO/CCPS/API standards commentary, government audits (GAO, NASA OIG, CSB), consultancies, KM vendor/industry blogs, 2024–2026 GenAI + industrial-knowledge sources). Verbatim excerpts retained with source/URL/date; inline citations [^N^]; tensions flagged in §6.
**Scope note:** This brief maps the problem space (state of practice, standards, failure modes, AI-readiness). It does not recommend specific tools, vendors, or architectures.

---

## KEY FINDINGS (summary)

1. **Lessons-learned systems fail mostly at reuse, not capture.** The canonical evidence is NASA's LLIS: two federal audits (GAO 2002; NASA OIG 2012) found the database built but bypassed — 58% of program/project managers said the systems "do not allow them to retrieve the right lessons at the right time," 53% found useful lessons less than 25% of the time, and only 6 of 28 project managers surveyed in 2012 described LLIS as useful [^1^][^2^]. Project-management survey data (Reich 2007) shows the same pattern industry-wide: 62% of 961 experienced PMs had formal lessons-learned procedures, only 12% adhered closely to them [^7^].
2. **Failure modes are stable and well-catalogued:** capture without transfer; "black-hole" repositories; post-mortem-only capture; symptom-not-root-cause capture; lessons recorded without context; weak keyword/metadata discipline; no dedicated ownership or resources; no conversion of lessons into standards/process changes [^6^][^7^][^9^].
3. **The counter-examples (US Army CALL, Schlumberger InTouch/Eureka, Shell CoPs) share the same design features:** dedicated resourced roles, human validation/gatekeeping, tiered knowledge quality, active "push" dissemination, integration into the work process itself, and communities — not just repositories [^3^][^4^][^36^][^37^][^38^][^40^].
4. **Standards exist but govern management systems, not lesson quality.** ISO 30401:2018 is the first international KM-system standard (principles-based MSS, non-prescriptive) [^11^][^13^]. In process safety, CCPS RBPS ("Learn from Experience" pillar) and API RP 754 (process-safety indicators) frame learning from incidents; API RP 75/SEMS shows a 17-year voluntary-to-mandatory trajectory that only Deepwater Horizon resolved [^21^][^15^][^18^]. CSB criticized API RP 754 for over-weighting lagging indicators [^15^].
5. **KM maturity is measurable.** APQC's five-level model (Initiate → Develop → Standardize → Optimize → Innovate) and its Capability Assessment Tool are the de-facto benchmark (and inspired the US Army's KM3); most organizations self-assess at Levels 1–2 where knowledge is ad hoc and siloed [^24^][^25^][^26^].
6. **Context is the missing ingredient in most lesson records.** Practitioners repeatedly identify "capture lessons without capturing the context within which it happened" as the core defect [^7^]; software-engineering Architecture Decision Records (ADRs — context/decision/consequences, status lifecycle, append-only) offer a transferable template for decision-rationale capture, though they too suffer abandonment ("written once and never updated") without operational support [^27^][^28^].
7. **Quality tiering and provenance are established practice in adjacent fields.** Schlumberger tiers best practices as "Good Idea / Local Best Practice / Schlumberger Best Practice" after screening [^38^]; intelligence tradecraft's Admiralty Code (NATO AJP-2.1) independently rates source reliability (A–F) vs information credibility (1–6) — a ready analogue for authoritative-vs-indicative tiering of CI knowledge [^31^][^32^].
8. **Knowledge has a lifecycle that must be governed:** named owners, review dates, event-triggered refresh, states (draft → verified → deprecated → archived), version control, and deprecation analytics; "reuse is review" (KCS) turns everyday use into the quality loop [^41^][^42^][^43^].
9. **GenAI does not fix weak KM — it amplifies it.** Enterprise research (HBR Analytic Services/AWS, n=646) finds >50% of organizations rate their data foundations inadequate for GenAI and that deployed against poorly organized content, LLMs "cannot distinguish authoritative sources from outdated documents, reconcile conflicting terminology across departments, or recognize when information contradicts itself" [^46^]. <1% of unstructured enterprise data is AI-consumable; only 16% of AI initiatives reach enterprise scale (IBM IBV 2025) [^48^].
10. **"Context engineering" has emerged in 2025–2026 as the discipline that operationalizes this:** curating metadata, taxonomies, provenance and grounding so RAG systems retrieve the right, current, authoritative content; measured via retrieval precision, faithfulness, and hallucination rate [^49^][^50^][^51^].
11. **Hallucination risk in industrial settings is a governance problem first.** Effective mitigations are layered guardrails: strict source binding with citations (60–75% hallucination drop reported), refusal-on-weak-evidence ("Show Sources or Say Sorry"), schema-validated outputs, domain eval suites, and human approval for high-impact outputs [^52^][^53^][^54^]. Ungoverned lesson content fed to RAG propagates errors "at machine speed" [^47^].
12. **For a refining/marketing CI-learning context, the implication is bidirectional:** the VCO lookback generates lessons whose reuse depends on KM maturity (taxonomy, context, tiering, lifecycle); and any GenAI layer over CI knowledge will only be as good as that same KM foundation. KM is therefore a prerequisite investment for AI-enabled lookback, not a parallel one [^46^][^49^].

---

## 1. WHY LESSONS-LEARNED SYSTEMS UNDERPERFORM

### 1.1 The classic failure modes (synthesis of practitioner literature)

The practitioner literature converges on a consistent catalogue. Henrico Dolfing (project-lessons specialist, 2025) lists why organizations "learn the little lessons… but the big lessons seem to be relearned time and time again":

> "Organizations have an ineffective lessons capture process. Lesson learning crucially needs a standard lessons reporting format and structure, an effective approach to root cause analysis, a focus on lesson quality, openness and honesty, and a validation process." — Dolfing [^6^]

> "Project teams do not see the benefit of a Lessons Learned session. Lessons Learned captured on a project seldom benefit that project. They benefit future projects." — Dolfing [^6^]

> "Under-resourcing lesson-learning is a major reason why the process so often fails." — Dolfing [^6^]

Dolfing also supplies the widely used NASA definition, which embeds quality gates in the definition itself:

> "A lesson learned is knowledge or understanding gained by experience… A lesson must be **significant** in that it has a real or assumed impact on operations; **valid** in that is factually and technically correct; and **applicable** in that it identifies a specific design, process, or decision that reduces or eliminates the potential for failures and mishaps, or reinforces a positive result." — NASA definition, quoted in [^6^]

OwnerTeamConsult (capital-projects consultancy, 2020), citing Reich (2007), quantifies the execution gap and enumerates the failure modes:

> "Reich (2007) found from a survey of 961 experienced project managers that although 62% had formal procedures for learning lessons from projects, only 12% adhered closely to them." [^7^]

> "- **No transfer of knowledge:** Lessons learned are captured very well, but not transferred to new projects.
> - **No learning from successes:** Lessons learned from failures are captured diligently, but successes (best practices) are ignored.
> - **Black hole knowledge repositories:** Lessons are captured into systems from which they prove difficult, or impossible, to extract.
> - **Poor documentation of lessons learned:** Lessons are poorly documented, mostly because of improper training and/or a poorly designed lessons learned registers.
> - **Post-mortem lessons only:** Lessons are not captured throughout the project life-cycle but only after project completion.
> - **Improper analysis of lessons learned:** The symptoms are captured instead of the root causes. No recommendations are made to remedy the real problem.
> - **Poor selection of keywords:** Lessons learned are typically searched for based om keywords. Rather have too many than too few.
> - **Lack of management support… Lack of resources… Lack of motivation to fix the issues.**" — OwnerTeamConsult [^7^]

On context loss specifically:

> "A typical mistake project managers make, is to capture lessons without capturing the context within which it happened." — OwnerTeamConsult [^7^]

On timing, PMPeople (2026) states the closure-capture paradox bluntly:

> "Capturing lessons learned at project closure is not effective: We don't remember well, we don't want to document mistakes, and we prefer to think about the next project." [^8^]

Plane.so (2026) adds the repository-placement and conversion failures:

> "**Storing lessons where no one looks.** Lessons stored in scattered documents or private folders rarely influence future work… **Failing to convert lessons into process changes.** Documentation alone does not improve delivery. When lessons remain static notes, recurring issues persist across projects." [^9^]

### 1.2 Case evidence: NASA LLIS — the two federal audits

NASA's Lessons Learned Information System (LLIS) is the most thoroughly audited lessons-learned system in existence, and the audits are damning in a specific, instructive way: the failure was not the database but the socio-technical system around it.

**GAO-02-195, "Better Mechanisms Needed for Sharing Lessons Learned" (Jan 30, 2002)** [^1^]:

> "We found that NASA's processes, procedures, and systems do not effectively capture and share lessons learned and therefore, NASA has no assurance that lessons are being applied towards future missions." [^1^]

> "One reason LLIS is not widely used, according to one center official, is because its lessons cover so many topics that it is difficult to search for an applicable lesson. Another respondent indicated that it is difficult to weed through all the irrelevant lessons to get to the few 'jewels' that you need to find." [^1^]

Key quantitative findings: 43% of program/project managers had not submitted a lesson to LLIS in the prior 2 years; 27% were unaware LLIS existed before the survey; 58% said current processes "do not allow them to retrieve the right lessons at the right time"; 53% "found lessons useful less than 25 percent of the time"; 39% believed implementing lessons learned contributes "only some or little to improving mission effectiveness" [^1^].

On cultural barriers:

> "Managers noted that there is a reluctance to share negative lessons for fear that they might not be viewed as good project managers… One manager noted that 'People are never rewarded for telling about how they screwed-up and caused a problem/mistake…. This will continue to be a problem until a way is found to allow and encourage people to talk about their mistakes without feeling that they are risking their careers.'" [^1^]

> "'Until we can adopt a culture that admits frankly to what really worked and didn't work, I find many of these tools to be suspect.'" [^1^]

GAO also contrasted NASA's pull-model with push-models elsewhere: "NASA's LLIS requires users to search for possible useful lessons. In contrast, at the Department of Energy users receive automatic e-mail alerts regarding important lessons learned. Similarly, individuals at Ford receive new best practices every time they open the database system. Also, we found that organizations frequently dedicate 'gatekeepers' to manage and monitor knowledge-sharing databases in order to keep the information up to date and relevant." [^1^]

**NASA OIG IG-12-012, "Review of NASA's Lessons Learned Information System" (2012)** [^2^] — ten years later, marginal improvement:

> "We found that NASA program and project managers rarely consult or contribute to LLIS even though they are directed to by NASA requirements and guidance… Specifically, only 16 of the 28 (57 percent) project managers indicated that they used LLIS during the project acquisition life cycle… only 12 of the 28 project managers (43 percent) contributing lessons learned from their projects to LLIS." [^2^]

> "Of the 16 project managers who stated they had used LLIS… only 6 describing LLIS as useful… The other 10 managers said LLIS did not contribute to their projects' success or provide any information that assisted in managing their projects." [^2^]

> "One project manager stated, '[We] didn't find anything useful, but we were able to say that we had checked this box.'" [^2^]

On the economics and policy erosion:

> "The primary reason that lessons learned are not formally well captured is that during the execution of a flight project, capturing and documenting lessons learned is essentially unfunded scope for an effort that is almost always cost- and schedule-challenged already. Once a mission is launched, it is quickly disbanded both for budgetary reasons, as well as to reassign critical human resources to ongoing Projects." [^2^]

> "Over time NASA has relaxed its internal requirements regarding the level and timing of project managers' use of and contributions to LLIS… NASA's current policy, in effect since 2007, does not explicitly require the use of LLIS and does not require project managers to identify or archive lessons learned until project conclusion or closeout." [^2^]

> "Consequently, LLIS has been marginalized in favor of other NASA knowledge sharing system components and is of diminishing and questionable value… we question whether the three quarters of a million dollars NASA spends annually on LLIS activities constitutes a prudent investment." [^2^]

Governance fragmentation was also documented: 8 of 10 Centers had not fully complied with NPR 7120.6; 4 Centers had no Center-level Lessons Learned Committee; 6 of 10 did not cross-reference lessons to engineering standards [^2^].

*Note: LLIS itself has a structured template — lesson learned, recommendation(s), "Evidence of Recurrence Control Effectiveness," driving event, mission directorate, topic tags (see e.g. llis.nasa.gov lesson records) [^35^] — illustrating that template structure alone does not create reuse.*

### 1.3 Case evidence: US Army CALL — the positive control

The US Army's Center for Army Lessons Learned (CALL, est. 1985, Fort Leavenworth) is the standard counter-example, notable precisely because it invested in the elements NASA under-resourced: collection embedded in operations, human validation, active dissemination, and analysis.

CSIS (2018) describes the operating model:

> "The Army has a particularly elaborate program operated by the Center for Army Lessons Learned (CALL). The center gathers data, primarily from unit reports but also from forward-deployed liaison officers. Teams at CALL analyze the collected data and develop best practices at the tactical, operational, and strategic levels. Finally, the dissemination division publishes CALL's reports, which includes shipping, as they describe it, 'thousands of books a month in direct response to soldier requests…'" [^3^]

CSIS also warns about speed — the failure mode of slow learning:

> "The U.S. experience with torpedoes in World War II comes to mind where it took an unconscionably long time to identify the problem. In a future conflict, the United States will not be able to wait two years to get one of its main weapons working properly." [^3^]

A KM-practitioner analysis (Social Media Today) identifies CALL's five strategic elements — Collection, Repository, Transfer Process, Implementation, Analysis & Data Mining — and the resourcing behind the repository:

> "CALL serves as the central repository for the US Army. Two hundred employees work in the CALL center checking documents for classification, adding metadata and archiving data… RFI - CALL has 11,000 requests a year that are answered drawing on knowledge stored within the repository. RFIs from deployed units are answered within 24 hours." [^4^]

The same source gives the "First Hundred Days" example of analysis-as-synthesis (mining thousands of AARs to produce a handbook for new combatants) and the "Rat Claw" example of 24-hour lesson propagation via deployed L2I analysts [^4^]. A Naval Postgraduate School thesis underscores the in-workflow capture principle: "The important part of this is, 'while doing their job.' … If documentation of Best Practices and Lessons Learned (BPLL) is considered an additional thing to do, it most likely will not get done." [^59^]

Critically, CALL distinguishes **validated lessons** from raw observations — a governance function most corporate systems lack. DVIDS (Army journal):

> "The CALL provides a system in which discovered lessons and best practices are validated, and corrective actions are implemented into doctrine, training, education, leader development, and operations… It employs a defined and verifiable process translating usable observations into lessons learned applicable to our Army. Some so-called lessons learned from other sources do not undergo the rigors of the CALL process. As such, one may take an observation and elevate it to a lesson learned regardless of the dissimilarities in conditions…" [^5^]

Escalation governance is explicit: issues rise from an action-officers working group to a Council of Colonels to a General Officer Steering Committee that can direct remediation [^4^]. The NATO variant formalizes the same loop: analysis phase → remedial action phase → endorsement, implementation, validation, dissemination; Vego (2007) cautions that deriving lessons learned is "complicated and time consuming" [^60^]. PMI's account of CALL's Acquisition Branch draws the corporate transfer lesson: "No organization, regardless of size or industry, can afford to ignore the dividends earned by establishing a lessons learned program." [^61^]

### 1.4 Oil & gas lessons-learned practice

At industry level, the UK Oil & Gas Authority's five-year review of 58 major projects (2011–2016) is a rare example of a regulator systematically harvesting and re-feeding lessons:

> "The lessons learned outlined in the report have been derived from extensive engagement with industry, with focus on how major projects are planned and executed… One of the key findings was that there was no correlation found between the size and complexity of projects and delay, with the key factors being non-technical in nature." — OGA/NSTA [^10^]

The downstream relevance: the root causes of lookback-relevant value leakage were organizational (decision-making, behaviors, culture) rather than technical — matching the KM-literature emphasis that learning failures are socio-technical, and that cross-project lesson transfer requires industry-level stewardship ("The OGA will continue to work with operators using our asset stewardship processes to ensure learnings are transferred") [^10^]. Company-level O&G KM exemplars (Schlumberger, Shell) are treated in §4.3.

---

## 2. STANDARDS & FRAMEWORKS RELEVANT TO CI LEARNING

### 2.1 ISO 30401:2018 — Knowledge Management Systems (Requirements)

ISO 30401 (published November 2018, under ISO/TC 260) is the first international standard for KM systems, written as a certifiable Management System Standard (MSS) in the ISO Harmonized Structure (context, leadership, planning, support, operation, performance evaluation, improvement) [^11^][^12^].

Scope and intent:

> "ISO 30401:2018 Knowledge management systems — Requirements sets requirements and provides guidelines for establishing, implementing, maintaining, reviewing, and improving an effective management system for knowledge management in organizations." [^11^]

> "The purpose of this standard for knowledge management is to support organizations to develop a management system that effectively promotes and enables value-creation through knowledge." — quoted in Springer, *Towards Architecting a Knowledge Management System* [^13^]

Core definitions from the standard:

> "Knowledge — human or organizational asset enabling effective decisions and action in context." [^13^]

> "Knowledge management system — part of a Management system with regard to knowledge. Note 1 to entry: The system elements include the organization's knowledge management culture, structure, governance and leadership; roles and responsibilities; planning, technology, processes and operation, etc." [^13^]

Its eight guiding principles (Nature of knowledge; Value; Focus; Adaptive; Shared understanding; Environment; Culture; Iterative) include two that directly address lessons-learned failure modes:

> "6. **Environment**: Knowledge is not directly managed, knowledge management focuses on managing the working environment, thus fostering the knowledge life cycle.
> 7. **Culture**: Culture is critical to effective knowledge management." — ISO 30401 guidelines summary [^12^]

Implementation requirements include: KM policy aligned to mission; identification of key knowledge domains, holders, gaps; defined processes for capture/sharing/access/protection; integration into workflows and culture; measurement of "the **value and outcomes** of knowledge management efforts, not just activities"; and systems for "lesson-learned documentation, communities of practice, and mentoring" [^12^]. Clause 4.4 requires the organization to "establish, implement, maintain and continually improve a knowledge management system" with explicit knowledge-development dimensions (acquiring, applying, retaining current knowledge) [^14^].

**Caveats/tensions:** (a) The standard is deliberately non-prescriptive — "It does not prescribe specific tools or methods" [^12^] — so it governs the *management system*, not the quality of individual lessons. (b) Its relationship to ISO 9001:2015 clause 7.1.6 (organizational knowledge) is explicitly positioned as the means to satisfy that clause (ISO 30401 Annex B) [^14^]. (c) KM commentators caution against over-reading modest requirements: Nick Milton (Knoco) noted of the ISO 9001 clause that "the new clause does not constitute a Knowledge Management standard, nor does it require organizations to implement Knowledge Management as a formal requirement… it only requires that sufficient attention is paid to knowledge to ensure the good and consistent quality of goods and services" [^14^]. (d) Annexes cover the knowledge spectrum, adjacent disciplines, and KM culture — signaling that culture, not IT, is the hard part [^11^].

### 2.2 API RP 754 — Process Safety Performance Indicators (learning from incidents via metrics)

API RP 754 (*Process Safety Performance Indicators for the Refining and Petrochemical Industries*, 1st ed. April 2010; 3rd ed. August 2021) was a direct institutional-learning artifact of the BP Texas City explosion (2005): the Baker Panel (2007) and CSB recommendations "drove publication of API RP 754… and revisions to the EPA Risk Management Plan rule" [^17^][^15^]. It establishes tiered lagging indicators (Tier 1/2 loss-of-primary-containment events) and leading indicators (Tier 3/4: near-miss reporting, mechanical-integrity overdue work, challenges to safety systems) [^17^][^16^]. IOGP Report 456 (3rd ed., May 2023) aligns upstream KPIs with it: "This third edition of Report 456, published in May 2023, incorporates revisions from the third edition of API RP 754. API published the third edition of API RP 754 in August 2021." [^16^]

**Documented tension — CSB's critique (2012):**

> "The CSB found that its indicator definitions place undo emphasis on lagging measures that are too infrequent to be useful to drive performance improvements, yet do not comprehensively count and report a likely sizeable number of leading measures that can be considered to be predictors of potentially serious process failures, and could, therefore, play a more critical prevention role." — National Law Review, reporting CSB classification of API's response as "Open–Acceptable Action" [^15^]

Also: "The CSB investigation found the root cause of the incident was multiple technical, system and organizational deficiencies. The CSB, B.P. and the oil and refining chemical sectors did not have an effective system of indicators to evaluate their safety performance. B.P. and industry sectors were, instead, typically using personal safety indicators, such as slips or trips-and-falls to measure safety performance." [^15^] — a direct analogue for VCO lookback metric design (measuring what's easy vs. what predicts).

### 2.3 API RP 75 / SEMS — the voluntary-to-mandatory learning arc

API RP 75 (*Safety and Environmental Management System for Offshore Operations and Assets*) illustrates how an industry learning framework can stall for decades without forcing events. Cambridge University Press's regulatory-history account:

> "The first attempt was in 1991… MMS acceded to this proposal and participated in the API's standard-setting process, which was concluded in 1993 when the API published its 'Recommended Practice 75' (API RP-75) as a guidance document… The second rule-making attempt… in 2006 and 2009… Once more, the API opposed this regulation, arguing that the implementation of SEMS should remain voluntary. The API presented several arguments… (a) the offshore industry had an admirable safety record, (b) voluntary programs that have enough flexibility to suit the culture of each company are the best way to promote safety in the industry, and (c) having a detailed plan on paper will not ensure an improvement in performance… In the middle of this rule-making procedure, the DWH accident occurred, and the federal government adopted SEMS regulations, taking the API RP-75 as its backbone." [^18^]

Post-DWH, SEMS became mandatory (30 CFR 250 Subpart S, effective November 2011; "SEMS II" effective June 2014 added stop-work authority, ultimate work authority, employee participation, mandatory reporting of unsafe conditions), with independent third-party audits [^19^]. The 4th edition (2019) made RP 75 performance-based and global in scope: "The 4th edition of API RP 75, published in 2019, is performance-based, necessitating a new auditing approach compared to previous editions" [^20^]. Elements include safety & environmental information, hazards analysis, MOC, operating procedures, safe work practices, training, mechanical integrity, pre-startup review, emergency response, **incident investigation, auditing, records and documentation** [^19^].

### 2.4 CCPS Risk Based Process Safety (RBPS) — "Learn from Experience" pillar

CCPS's *Guidelines for Risk Based Process Safety* (2007) organizes 20 elements under 4 accident-prevention pillars: **Commit to Process Safety; Understand Hazards & Risk; Manage Risk; Learn from Experience** [^21^][^23^].

Pillar 4 — Learn from Experience — comprises four elements: **(17) Incident Investigation; (18) Measurement & Metrics; (19) Auditing; (20) Management Review & Continuous Improvement** [^21^][^22^]. Practitioner summary of element 17's learning requirements:

> "Incident investigation identifies the root causes of incidents and near misses to prevent recurrence. Effective investigations focus on learning, avoid blame, and generate corrective actions that strengthen systems. Lessons must be shared with relevant personnel and tracked until fully implemented." [^22^]

Two RBPS features are directly relevant to CI-KM design: (a) **Process Knowledge Management** is itself an element (Pillar 2, element 6) — "Focuses on info that can be recorded in documents (specifications, calculations, chemicals and equipment uses, etc.)" [^21^] — i.e., the knowledge base is a safety-critical asset with its own management requirements; (b) **Process Safety Competency** (element 3) requires "Continuously improving knowledge and competency of the company as a whole; Ensuring the appropriate info is available to people who need it; Consistently applying what has been learned" (secondary summary of CCPS element definitions) [^66^]. RBPS explicitly "Builds on lessons learned since early 1990s" and applies Plan-Do-Check-Act management-system principles [^21^].

### 2.5 APQC Knowledge Management Maturity Model

APQC's five-level KM maturity model (2007) is the dominant enterprise benchmark and "helped inspire the U.S. Army's own model, KM3":

> "The APQC's Levels of Knowledge Management Maturity consist of five distinct levels:
> - **Initiate**: No formal knowledge management strategy or dedicated resources
> - **Develop**: Processes established in certain areas with some leadership recognition
> - **Standardize**: Formalized knowledge management processes across the organization
> - **Optimize**: Knowledge activities integrated into processes with strong leadership support
> - **Innovate**: Knowledge management drives innovation and competitive advantage
> As organizations move through each maturity level, their knowledge undergoes its own evolution as follows: Ad hoc knowledge → Applied knowledge → Leveraged knowledge → Dynamic knowledge" — Coveo summary [^24^]

Stage 3 is the pivot where reuse becomes systematic: "Stage-three organizations have consistent processes, approaches, and technologies for capturing, transferring, accessing, and reusing insights. There's standardized taxonomies and workflows. Leadership dedicates resources to knowledge management in this stage, and there's usually a core insights team…" [^25^]. APQC's diagnostic is the Knowledge Management Capability Assessment Tool (KM CAT), evaluating strategy, people, process, content/IT across 12 core capabilities including objectives and governance [^24^]. Applied studies show most organizations cluster at Levels 1–2 (e.g., a 2025 study of Iranian audiovisual archives: majority at Level 1 — "unstructured and scattered approaches"; none at Levels 4–5; barriers: no KM strategy, insufficient funding, fragmented communication, absent standardized processes, limited technology integration) [^26^].

**Note:** Secondary sources render APQC's level names inconsistently (Initiate/Develop/Standardize/Optimize/Innovate [^24^] vs Initial/Repeatable/Defined/Managed/Optimizing [^1968-variant; treated as same model via ^24^]) — a minor but real taxonomy-governance lesson in itself.

### 2.6 Knowledge-Centered Service (KCS) — in-workflow knowledge lifecycle

KCS (Consortium for Service Innovation, since 1992) is the leading methodology for embedding knowledge capture/reuse in the flow of work — the support-industry answer to "capture without reuse":

> "KCS works through a **Double Loop Process**: the Solve Loop and the Evolve Loop. The **Solve Loop** is the day-to-day request-response workflow… The **Evolve Loop** looks at patterns across many Solve Loop activities… to improve article quality, identify recurring issues, improve processes…" [^43^]

Solve Loop practices: **Capture** ("Capture knowledge in the moment, capture the requester's context, searching is creating"), **Structure** ("Use a simple template"), **Reuse** ("Search early search often"), **Improve** ("Reuse is review, Flag it or fix it, license to modify"). Evolve Loop practices: **Content Health, Process Integration, Performance Assessment, Leadership & Communication** [^45^]. KCS's defining deviation from classic lessons-learned programs: "We only spend time on improving knowledge articles that are being used, and knowledge articles will reflect our collective experience on a daily basis" [^44^] — demand-driven maintenance rather than blanket curation. Documented results include ServiceNow's "52% Faster Time to Relief" [^69^].

---

## 3. KNOWLEDGE TAXONOMY, METADATA & CONTEXTUALIZATION

### 3.1 Lesson-record structure and findability discipline

Practitioner guidance emphasizes that findability is designed, not emergent. A 2026 quality-management blueprint (IntellaQuest) gives concrete, transferable conventions:

> "**4) Design for findability: Taxonomy + metadata + naming.** People search, not browse. Standardize:
> - **Titles:** \[Process\] – \[Step/Asset\] – \[Doc Type\] – \[Version\] (e.g., 'Fill Line 12 – Torque Check – WI – v7').
> - **Metadata:** product family, process cell, equipment ID, risk ID, supplier, training role, regulatory tag (e.g., OSHA LOTO).
> - **Keywords and synonyms:** include common aliases ('die head / extruder head').
> - **Smart collections:** 'Line 6 Setup Pack' auto-assembles WI, settings, last change note, and troubleshooting checklist." [^30^]

With an implementation checklist: "Define 6–8 mandatory metadata fields. Rename top 100 docs to the standard title format. Build 10 smart collections for your highest-risk lines. Review search logs monthly and fix top 10 failed searches." [^30^] — the last item being a rare, practical feedback loop between search failure and taxonomy improvement (directly applicable to a CI-lessons repository).

The KCS article structure offers a minimal, battle-tested lesson template: **Issue, Environment, Cause, Resolution** — with the requester's own words preserved as search metadata: "A KCS article captures the requestors issue (in their own words) and the environment as well as the resolution from the responder." [^44^] NASA LLIS records similarly separate **Lesson(s) Learned / Recommendation(s) / Evidence of Recurrence Control Effectiveness / Program phase / Topic tags** [^35^]. OwnerTeamConsult adds the keyword lesson from hard experience: "Poor selection of keywords: Lessons learned are typically searched for based on keywords. Rather have too many than too few." [^7^]

### 3.2 Decision records: the ADR pattern and its abandonment risk

For capturing *decision rationale* (as distinct from event lessons), the software industry's Architecture Decision Record (ADR) — Michael Nygard, 2011 — is the dominant lightweight template: **Title, Status, Context, Decision, Consequences**, stored with the work product, append-only, with status lifecycle (proposed → accepted → deprecated/superseded-by) [^27^][^29^].

The motivating problem statement maps one-to-one onto CI lookback/backcasting rationale:

> "ADRs help newcomers to a project understand the rationale behind past decisions. Without this understanding they may either: blindly accept the decision or blindly change it. If a development team blindly accepts too many decisions, it 'becomes too afraid to change anything and the project collapses under its own weight' (Nygard, 2011). On the other hand, blinding changing decisions may result in damage or inadvertent introduction of technical debt." [^27^]

AWS Prescriptive Guidance (as cited in a 2025 TechRxiv paper) "defined three anti-patterns that ADRs should address — **deferred decisions, decisions without rationale, and loss of records**" [^28^]. Typical record workflow: draft ADR with status "proposed" → discuss → accept/reject → implement; if revisited, create a new ADR referencing the old; "The old ADR should not be removed or otherwise modified except for the annotation pointing to the new one." [^29^] — i.e., versioning by supersession, preserving provenance.

**Documented failure mode — abandonment:**

> "Despite such recommendations, ADRs did not achieve widespread adoption. The primary barrier was the cost of continuous documentation updates. While recording an initial design decision is relatively easy, keeping ADRs up to date as the project progresses becomes an excessive burden. As a result, ADRs follow the path to abandonment: 'written once and never updated.' This was not because the concept of ADR was flawed, but because human operational overhead killed the value of the concept." — TechRxiv, 2025 [^28^]

The same paper proposes AI as both "producer" and "consumer" of ADRs with humans limited to "approval" — an early indicator of how GenAI is being used to lower capture overhead [^28^]. Practice variants include tiered decision documentation (sub-ADR "decision notes" for local-blast-radius choices: "If every decision became an ADR, no decision would be architectural" [^68^]) and Y-statements/MADR extended formats [^27^]. For VCO: the pattern transfers directly as "optimization decision records" capturing context (market/ops state), decision (LP/schedule choice), alternatives rejected, and consequences — the missing link between a lookback finding and a durable planning assumption.

### 3.3 Quality tiering, confidence models, and provenance

**Tiering inside an industrial KM system — Schlumberger's three-level best-practice grading:**

> "These are divided into three categories: 'Good Idea,' 'Local Best Practice' and 'Schlumberger Best Practice.' After a thorough screening process, each practice is assigned a category, and information is provided for each entry: who performed the screening; the specifics of best practice; the breadth of its applicability; and systematic comments on its contents." [^38^]

Note the embedded provenance fields (who screened, applicability breadth) — the record carries its own confidence metadata.

**Independent rating of source vs. content — the Admiralty Code / NATO system.** Intelligence tradecraft's standard (NATO AJP-2.1) rates *source reliability* (A–F) and *information credibility* (1–6) independently:

> "The Admiralty Code uses a 6 × 6 alphanumeric rating system, which requires the evaluation of source reliability and information credibility independently from one another." — Cambridge, *Judgment and Decision Making* [^31^]

| Reliability | | Credibility | |
|---|---|---|---|
| A | Completely reliable | 1 | Completely credible / Confirmed |
| B | Usually reliable | 2 | Probably true |
| C | Fairly reliable | 3 | Possibly true |
| D | Not usually reliable | 4 | Doubtful |
| E | Unreliable | 5 | Improbable |
| F | Reliability cannot be judged | 6 | Truth cannot be judged |

(NATO AJP-2.1 2016 scales [^32^]; cyber-threat-intel practice applies identical tables with documented defaults, e.g., Unit 42 sets telemetry to default "A" and downgrades on evidence of interference [^33^].)

The separation principle is the key design idea for CI knowledge tiering (authoritative vs. indicative):

> "This separation is the critical principle: a reliable source can provide inaccurate information, and an unreliable source can occasionally provide valid intelligence." [^67^]

Documented critiques (relevant if adopted for KM): two-axis ratings reduce readability ("what information should be regarded as the most probable: one rated B3 or rated C2?"), source reliability is often misapplied as source-level rather than topic-level competence, and credibility criteria reduce to confirmation/denial — analysts propose adding proficiency and likelihood dimensions [^34^]. NATO STO-TR-SAS-114 additionally documents the semantic-variance problem: one analyst's "usually reliable" may mean 60% valid, another's 80% [^32^]. Takeaway: confidence models need quantified anchor definitions and calibration, not just labels.

**Provenance in lesson systems.** CALL's observation→lesson pipeline (§1.3) is fundamentally a provenance/validation model: observations are attributed, analyzed, and only promoted to "lessons learned" after validation against conditions of applicability [^5^]. GAO's KM benchmarking similarly found leading organizations "dedicate 'gatekeepers' to manage and monitor knowledge-sharing databases in order to keep the information up to date and relevant" (Ford plant focal points; DoE site coordinators) [^1^].

---

## 4. KNOWLEDGE GOVERNANCE & LIFECYCLE

### 4.1 Ownership roles and validation workflows

The consistent differentiator between failed and functioning lesson systems is **named, resourced ownership with validation authority**:

- **NASA (negative case):** fragmented governance — Chief Engineer owns LLIS, Centers run inconsistent committees; 4 of 10 Centers lacked the required Lessons Learned Committee; funding ranged from $21,785 (Ames) to $305,095 (Kennedy) with "little evidence of correlation between funding levels and the number of lessons learned that Centers contributed" [^2^]. GAO's recommendation: "Designate a lesson learned manager to lead and coordinate all agency lessons learning efforts" [^1^].
- **CALL (positive case):** ~200 staff performing classification checks, metadata tagging, archiving, plus RFI response within 24 hours; multi-echelon validation governance (working group → Council of Colonels → General Officer Steering Committee) [^4^].
- **Schlumberger (positive case):** paid, prestigious expert roles with explicit curation duty — "These InTouch Engineers also manage the validation of new shared knowledge and are responsible for keeping the knowledge base for each domain clean and up-to-date." [^36^] "Note: Schlumberger pays specific employees (InTouch Engineers) to help other employees, this role is very highly considered, and so it is one that people aspire to. How many other companies do you know which pay its own staff to help each other?" [^36^]
- **ISO 30401** institutionalizes the same expectation at management-system level: clause 5.3 roles/responsibilities/authorities; competence (7.2); awareness (7.3) [^11^].
- **GAO cross-industry benchmark:** "organizations frequently dedicate 'gatekeepers' to manage and monitor knowledge-sharing databases in order to keep the information up to date and relevant. At Ford, a 'focal point' is assigned to manage the best practices system at each plant… at the Department of Energy a lessons learned coordinator maintains the lessons learned system at each site." [^1^]

### 4.2 Lifecycle states, refresh triggers, versioning, archival

Current (2026) documentation-governance practice specifies a full content lifecycle. On ownership and versioning:

> "**Establishing owner accountability.** Assign clear ownership for each document in your knowledge base. This accountability should include responsibility for regular reviews, authority to archive or update as needed, and transition planning when roles change. Without clear ownership, orphaned documents accumulate rapidly.
> **Implementing version control systems.** Use version control to maintain a history of document changes… to see how documentation has evolved, revert to previous versions… and track who made specific edits." — Allymatter, 2026 [^41^]

On states, triggers, and metrics (knowledge-base.software deprecation-strategy guide, 2026):

> "Build these controls into the content lifecycle:
> - Require every article to have an internal owner responsible for accuracy, review, and lifecycle decisions.
> - Add review dates to time-sensitive content.
> - **Tie reviews to product releases, policy changes, vendor changes, and service retirements.**
> - Use article states such as draft, review, verified, deprecated, archived, retired, or restricted.
> - Add metadata for product version, audience, region, service, owner, and source of truth.
> - Create an easy 'flag outdated content' workflow for agents and customers.
> - Review high-risk articles after major releases or incidents." [^42^]

Health metrics recommended: "Articles past review date, articles without internal owner, duplicate clusters, deprecated articles without replacement" plus user-impact signals ("Searches leading to retired content… failed searches") [^42^]. Archival should be analytics-informed (view counts, search terms, bounce rates) with automated review reminders, and AI can assist by "detecting contradictions between documents, spotting outdated terminology, flagging documents that haven't been updated despite significant changes elsewhere" [^41^].

The KCS lifecycle principle distributes this burden: "'reuse is review' and 'flag it or fix it'… the people who use the knowledge base should be part of the quality loop" [^42^][^45^] — i.e., every use is a validation event, and articles are improved just-in-time rather than on a blanket review calendar [^44^].

### 4.3 Communities of practice in oil & gas: Shell and Schlumberger

**Shell.** CoPs were a deliberate, supported design: "Shell has created 13 communities of practice that encompass more than 10,000 users. Anyone who wants to build a new CoP within Shell receives a consultant's support to interview potential members. They look at common challenges and problems across units and teams that could serve as the base for the community." [^40^] Wenger & Snyder (2000) caution against over-engineering: CoPs "should not be created in a vacuum. In most cases, informal networks of people with the ability and the passion to further develop an organization's core competencies already exist. The task is to identify such groups and help them come together as communities of practice." [^40^] Shell's KM history also includes early AI: a case-based-reasoning application to "identify similar situations systematically" so operating units could access relevant prior experience (Chapter 16, *Knowledge Management at Shell: Innovation and Integration*) [^56^].

**Schlumberger** — the most fully documented O&G KM ecosystem (KM strategy since 1997; chairman Euan Baird: "We must become experts in capturing knowledge, integrating and preserving it and then making what has been learned quickly and easily available to anyone who will be involved in the next business decision") [^36^]:

- **InTouch** (est. 1996): 24/7 expert-support service; "150 dedicated experts covering 80 technology and service domains," backed by ~4,000 experts (ACEs — Applied Community Experts in the field; SMEs in technology centers); InTouch Engineers answer field questions, capture solutions, and "conduct root cause analysis of why assistance was needed. The latter is used to drive improvement in hardware, software, documentation and training updates. InTouch has over a million attached files, 56,000 users and 2.8 million logins per year" [^36^][^37^]. Before InTouch, "average delays ran from 2 to 16 weeks to get an answer to a technical question; 16 weeks to make engineering modifications; and 2 to 5 years to update archived material" [^38^]. Claimed economics: "Schlumberger states that its InTouch system, which provides technical and operational support to field staff, saves more than USD 200 million per year. The company has also measured a 95% improvement in response time for technical queries." [^39^]
- **Eureka** communities of practice: 24 communities/127 SIGs (early-2000s account) growing to "around 160 'Eureka' communities of practice with over 300 leaders and 25,000 plus members" (2011), with democratically elected leaders, bulletin-board problem discussions feeding technology roadmaps, white papers, and 250+ technical webinars annually [^36^][^37^].
- **Lifecycle realism:** "Communities have a life cycle—they emerge, they live, and they can eventually die." And on KM permanence: "KM needs a constant push and encouragement. 'You can never declare victory and feel that the KM problem is solved.'" [^37^]
- **Organic emergence vs. design tension:** Henry Edmundson (then Director of Technical Communities): "It's fairly chaotic, and that's good. You can't force these things. People will use groups the way they want to – or they won't use them at all." [^39^]

**Governance pattern common to both:** communities and expert networks handle *tacit* knowledge and validation; repositories handle *explicit* validated content; the two are deliberately coupled (InTouch solutions are harvested into the validated knowledge base; CoP discussions feed roadmaps and best practices) [^37^][^38^]. This is the "personalization + codification" hybrid that NASA's repository-only approach lacked (GAO: managers' first-choice improvement was mentoring and storytelling, not better search) [^1^].

---

## 5. AI READINESS: GenAI/RAG OVER INDUSTRIAL KNOWLEDGE & LESSONS LEARNED

### 5.1 How GenAI/RAG is being applied to industrial knowledge

Documented application patterns (2024–2026):

- **Maintenance/technical-documentation assistants.** Enterprise RAG over manuals, work orders and engineering documents: "our GenAI Document Assistant implements enterprise-grade RAG systems that transform how workers access technical documentation… building comprehensive knowledge graphs that enable natural language queries and cross-document comparison" (manufacturing vendor description, 2025) [^64^]. In O&G specifically, Shell's predictive-maintenance program (C3.ai-based) moved in its Phase 3 (2023–2025) to "Incorporation of AI-based failure root cause analysis and Generative AI troubleshooting assistants for technicians," with an "AI-driven insights created a centralized knowledge base for maintenance best practices" (vendor case summary citing Shell Sustainability Report 2024; treat figures as vendor-reported) [^55^].
- **Agentic maintenance workflows** (2025–2026 marketing-claims territory): failure-pattern detection → procedure retrieval → parts check → work-order creation "without any human in the loop," with "high-criticality decisions or novel failure modes escalate to human review automatically" [^65^] — vendor claims indicative of direction, not verified performance.
- **AI-assisted knowledge work around ADRs/decision records:** AI as "producer" and "consumer" of decision records with humans limited to "approval," explicitly proposed to fix ADR abandonment by reducing "the cost of ADR recording, retrieval, and updating to near zero" [^28^].
- **Knowledge-base hygiene:** AI identification of archival candidates "by detecting contradictions between documents, spotting outdated terminology, flagging documents that haven't been updated despite significant changes elsewhere" [^41^]; duplicate-cluster detection in deprecation workflows [^42^].
- **Historical precedent:** industrial KM has used AI-shaped retrieval for decades — Shell's case-based reasoning for analogous-situation retrieval [^56^]; the current wave differs in fluency, not in the underlying dependency on curated context.

### 5.2 Why context/metadata quality determines AI usefulness

The enterprise-evidence base is now consistent that **KM/data foundations gate GenAI value**:

> "More than half of organizations moving forward with generative AI rate their data foundations as inadequate for AI implementation… Organizations must curate enterprise knowledge, establishing trusted information sources from which AI systems can reliably retrieve and utilize content. This demands processing, organizing, tagging, and structuring information to create the knowledge scaffolding enabling accurate retrieval and synthesis. Without this foundation, even sophisticated language models produce unreliable outputs that erode user trust." — HBR Analytic Services/AWS research summary (n=646), Earley & Associates [^46^]

> "When deployed against poorly organized enterprise content, these systems cannot distinguish authoritative sources from outdated documents, reconcile conflicting terminology across departments, or recognize when information contradicts itself." [^46^]

> "Data issues emerge as the top challenge organizations cite when attempting to scale AI initiatives, selected by 39% of those deploying generative AI capabilities… Organizations that addressed data quality, integration, and governance before implementing AI reported dramatically better outcomes than those attempting to skip this essential preparation." [^46^]

> "Unstructured data currently represents the vast majority of enterprise data, yet **less than 1%** of it exists in a format suitable for direct AI consumption. This structural imbalance is one of the core reasons why only **16% of AI initiatives** have reached enterprise scale, according to the IBM IBV 2025 CEO Study." — Alexander Thamm [^48^]

> "Generative AI and agentic AI systems do not create knowledge out of thin air: they amplify patterns in the data they are trained on and operate within. Feed them clean, well-governed, integrated data and they become powerful engines of productivity and insight. Feed them fragmented, inconsistent, or siloed data and they multiply mistakes at machine speed." — CloudX, 2026 [^47^]

> "Before agents, a data quality issue just risked producing a wrong chart that a business analyst would catch. But that same issue in an agentic system triggers a cascade of wrong decisions before anyone notices." [^47^]

KM-vendor perspectives make the same point from the knowledge side: "AI tools like ChatGPT, Claude, and Atlassian's Knowledge Graph promise intelligent assistance—but they need fuel. That fuel is your **structured, well-maintained knowledge base**… Without quality knowledge, AI fails: 'Garbage in, garbage out.'" [^58^]

Survey corroboration: "According to the World Economic Forum, 50% of the interviewed business leaders cite data quality and availability as major challenges to accelerating AI adoption, while 72% said they will invest in data foundations and pipelines over the next 12 months." [^47^] Gartner positions semantic context as the prerequisite: "Knowledge graphs are the appropriate target for exploiting LLMs for business value, since they are machine-readable data structures, representing semantic knowledge" and "Semantic alignment is the prerequisite for AI" [^57^].

### 5.3 Risks: hallucination and ungoverned content

For safety- and money-critical industrial use (refinery optimization, CI decisions), the risk profile is dominated by *confident fabrication* and *stale/unvetted grounding content*:

> "LLM hallucinations are answers that sound confident but aren't grounded in reality… The business risk isn't that errors occur—it's the **confidence** behind fabrications. In customer-facing or regulated contexts, that's unacceptable." — CustomGPT guardrails guide, 2026 [^53^]

Documented mitigation stack (2025–2026 practitioner consensus):

1. **Strict source binding / grounded RAG:** "the model must include a citation token tied to a source chunk for every assertion, and the system rejects responses without sufficient grounding. Companies report a 60–75% drop in hallucinations once strict source binding is enforced." [^52^] "Require citations for factual claims; Refuse when evidence is missing or conflicting." [^54^]
2. **Refusal-by-design:** "adopt the baseline rule: **S4 — Show Sources or Say Sorry**. Every factual claim gets a verifiable source; when evidence is weak or missing, the system narrows scope or declines." [^53^]
3. **Tool-constrained generation:** "When the answer can be computed or fetched, configure the model to call tools rather than rely on parametric memory… This shifts truth from probabilistic generation to deterministic systems." [^54^]
4. **Schema-validated outputs:** "When the model is forced to respond with a JSON schema… the surface area for invented information collapses dramatically." [^52^]
5. **Multi-model cross-verification for high-stakes outputs:** "roughly 12 percentage points of accuracy at the cost of a 1.7x latency hit." [^52^]
6. **Domain eval suites & continuous monitoring:** "Build a private eval set of 200–500 real customer interactions, each with a verified gold answer… Companies that invest in evals catch 4 out of 5 regressions before they reach customers." [^52^] Recommended quality metrics: Retrieval Precision@k >85%; Answer Faithfulness >90%; Context Utilization; Hallucination Rate <5% [^49^].
7. **Human approval for high-impact outputs:** "Require human approval for high-impact communications that could impact financial markets, legal standing, or public perception." [^62^]
8. **Warning on self-reported confidence:** "Over-trusting model self-reports of confidence. Calibrate confidence externally with held-out evals, not by asking the model how sure it is." [^52^]

The ungoverned-content risk is the KM-side mirror image: a RAG system faithfully grounded in a *bad* corpus is still wrong — hence the direct line from §3–§4 (tiering, validation, lifecycle) to AI safety: the corpus must be curated, tiered, and current *before* grounding, or the AI industrializes the lessons-learned failure modes of §1.

### 5.4 "Context engineering" / contextualization as an emerging discipline

By 2025–2026 the practice had a name and an emerging body of practice:

> "Context engineering is the process of designing and supplying metadata to AI systems, especially LLMs, to give them the necessary background and structure to understand and respond accurately. For data teams, this means curating the metadata that describes your datasets: table names, column descriptions, usage patterns, lineage, and relationships." — Select Star, 2025 [^50^]

> "Without context engineering, data-driven AI tools risk becoming unreliable or even misleading. With it, they become trusted extensions of your data team." [^50^]

Empirical support (observational, single-operator, n=200 interactions; treat as indicative): "context completeness may be the dominant factor… incomplete context was associated with 72% of iteration cycles. Structured context assembly was associated with a reduction from 3.8 to 2.0 average iteration cycles per task and an improvement in first-pass acceptance from 32% to 55%." The proposed five-role context package: **Authority, Exemplar, Constraint, Rubric, Metadata** [^51^].

The RAG architecture ladder quantifies why metadata/chunking/retrieval engineering matter:

| Generation | Era | Typical accuracy | Hallmarks |
|---|---|---|---|
| Naive RAG | 2020–2023 | 60–70% | Fixed chunking, top-k vector retrieval, no quality control |
| Advanced RAG | 2023–2025 | 75–85% | Hybrid search, re-ranking, query rewriting, semantic chunking |
| Agentic RAG | 2025– | 85–95% | Dynamic multi-source retrieval, self-verification, reflective correction |

(vendor/industry guide figures — directional, not audited benchmarks [^49^])

Context-engineering practice for enterprise knowledge bases additionally specifies end-to-end quality monitoring (Precision@k, faithfulness, context utilization, latency, hallucination rate) with automated LLM-as-Judge evaluation pipelines (RAGAS, DeepEval, LangSmith) run "after every knowledge base update to ensure quality does not degrade" [^49^]. Related emerging techniques: contextual embeddings (~15% retrieval-accuracy improvement reported), context caching (75–85% cost reduction), and protocol-driven context plumbing (MCP) [^63^].

**Synthesis for industrial CI knowledge:** context engineering is effectively *KM discipline re-priced by AI*. The same artifacts this brief catalogs — naming conventions, mandatory metadata, lesson templates, decision records, quality tiers, provenance, lifecycle states — are precisely the inputs that determine whether a GenAI layer over CI lessons retrieves authoritative, current, applicable knowledge or hallucinates over a black-hole repository.

---

## 6. TENSIONS & OPEN DEBATES (evidence-backed)

1. **Codification vs. personalization.** Repositories alone demonstrably underperform (NASA LLIS [^1^][^2^]); managers' preferred mechanisms were mentoring and "storytelling" [^1^]. Yet people-only approaches don't scale across a multi-site downstream organization. The documented successes (Schlumberger, CALL) deliberately *couple* both: communities/experts for tacit flow + validated repositories for explicit reuse [^37^][^38^][^4^].
2. **Pull vs. push dissemination.** NASA's search-only model failed; DoE's e-mail alerts and Ford's on-open best-practice push were cited by GAO as better practice [^1^]. CALL pushes publications and answers 11,000 RFIs/yr within 24h [^3^][^4^]. Modern KM-maturity stage-3 descriptions likewise emphasize "the platform pushes relevant insights to the right people at the right time" [^25^]. Tension: push risks noise ("Too much data inhibits information" — NASA manager [^1^]).
3. **Validation rigor vs. speed.** CALL's validated-lesson pipeline guards applicability ("one may take an observation and elevate it to a lesson learned regardless of the dissimilarities in conditions" [^5^]) but adds latency; CSIS warns lesson processes in great-power conflict "will need to operate rapidly," citing the WWII torpedo fiasco [^3^]. Corporate vetting queues (NASA LLIS multi-step Center/HQ process [^2^]) suppress contribution. KCS resolves this by publishing fast and validating through use ("reuse is review") [^45^] — a real design fork: *gate-before-publish* vs. *validate-in-use*.
4. **Capture breadth vs. curation quality.** "Difficult to weed through all the irrelevant lessons to get to the few 'jewels'" [^1^] vs. advice to over-tag ("Rather have too many [keywords] than too few" [^7^]). Volume without tiering destroys findability; over-curation without demand signals wastes effort — KCS's answer is to "only spend time on improving knowledge articles that are being used" [^44^].
5. **Failure lessons vs. success capture.** Safety regimes (CCPS, API) are incident-driven; project literature warns "No learning from successes… successes (best practices) are ignored" [^7^], and NASA managers asked for more positive lessons [^1^]. Blame fear suppresses negative-lesson sharing ("People are never rewarded for telling about how they screwed-up" [^1^]) — CCPS counters with "focus on learning, avoid blame" [^22^].
6. **Voluntary flexibility vs. mandated consistency.** API argued pre-DWH that "voluntary programs that have enough flexibility to suit the culture of each company are the best way to promote safety" and that "a detailed plan on paper will not ensure an improvement in performance"; DWH ended the debate and SEMS became mandatory with third-party audits [^18^][^19^]. ISO 30401 is certifiable yet explicitly non-prescriptive [^12^] — organizations can be compliant on paper while lessons still don't get reused (cf. NASA's compliant-but-marginalized LLIS [^2^]).
7. **Lagging vs. leading measurement.** CSB's critique of API RP 754 — over-reliance on infrequent lagging indicators, under-counting leading predictors [^15^] — mirrors a known VCO-lookback risk: measuring what is easy (margin variance after the fact) vs. what predicts (plan-vs-actual leading signals, model-assumption decay).
8. **Documentation value vs. maintenance overhead.** ADRs capture rationale but "follow the path to abandonment: 'written once and never updated'… human operational overhead killed the value of the concept" [^28^]. Any CI decision-record practice must budget the update cost or automate it (AI-as-producer proposals [^28^]).
9. **Organic vs. engineered communities.** Wenger & Snyder: CoPs can't be commissioned in a vacuum [^40^]; Edmundson: "You can't force these things" [^39^]. Yet Shell's consultant-supported CoP formation [^40^] and Schlumberger's paid InTouch engineers [^36^] show deliberate design working. Resolution in practice: identify and resource existing networks rather than create from scratch.
10. **GenAI enthusiasm vs. grounding reality.** Vendor case studies report large gains (e.g., Shell downtime −45%, ~$400M/yr savings — vendor-cited, not independently audited [^55^]), while enterprise surveys show most data foundations are not AI-ready [^46^][^48^]. The tension resolves into sequencing: KM foundations first, GenAI second — "information architecture precedes artificial intelligence" [^46^].
11. **Standard vocabulary drift.** Even KM standards suffer taxonomy drift: APQC maturity levels are rendered inconsistently across secondary sources [^24^ vs. ^26^]; Admiralty-Code reliability terms mean different percentages to different analysts (60% vs 80% "usually reliable") [^32^]. Any internal CI-knowledge taxonomy needs calibration anchors and a single owned dictionary.

---

## 7. IMPLICATIONS FOR THE VCO LOOKBACK / CI-KM STUDY (problem-space mapping)

1. **Diagnose before designing.** Assess current CI-learning maturity against APQC levels [^24^] and the §1.1 failure-mode checklist [^6^][^7^][^9^]; the NASA audits provide the archetype of a compliant-looking but marginalized system to test against ("checked this box" behavior [^2^]).
2. **Lesson records must carry context and rationale, not just findings.** Minimum fields drawn from cross-industry templates: issue/event, environment/constraints (market state, asset configuration, crude/feed slate, planning-model version), root cause, decision taken + alternatives rejected (ADR pattern [^27^][^29^]), recommendation, applicability boundary, owner, review date, quality tier, provenance [^30^][^35^][^38^][^42^][^44^].
3. **Tier CI knowledge by confidence with independent source/content ratings** (Admiralty-style: authoritative validated vs. indicative/uncorroborated), with quantified anchor definitions to avoid semantic drift [^31^][^32^][^33^][^38^].
4. **Resource the governance roles.** Named knowledge owners per domain, gatekeeper/curator capacity, a validation workflow (observation → analysis → validated lesson → standard/planning-model update), and escalation authority (CALL/GM-officer model [^4^][^5^]; Schlumberger paid-expert model [^36^]; ISO 30401 clause 5.3 [^11^]). Under-resourcing is a documented root cause of failure [^6^][^2^].
5. **Engineer reuse into the work process, not beside it.** Embed lesson retrieval/review into VCO lookback and planning-cycle workflows (capture "while doing their job" [^59^]; KCS in-workflow model [^43^][^45^]); add push mechanisms for high-value lessons (GAO push-vs-pull finding [^1^]); convert lessons into standards, checklists, and model-assumption updates (OwnerTeamConsult "convert lessons into process changes" [^9^]).
6. **Govern the lifecycle.** States (draft → verified → deprecated → archived), event-triggered refresh (turnarounds, MOCs, market regime changes, model version changes), review dates, versioning, archival analytics, and "flag it or fix it" user loops [^41^][^42^].
7. **Measure outcomes, not activity.** ISO 30401's "value and outcomes… not just activities" [^12^]; APQC KM CAT [^24^]; KCS content-health and reuse metrics [^42^][^43^]; beware lagging-only KPIs (CSB/API 754 lesson [^15^]).
8. **Treat GenAI readiness as a KM deliverable.** Before any AI layer over CI/lookback knowledge: curated corpus, mandatory metadata, quality tiers, current-content discipline [^46^][^48^][^49^]; then context-engineering practice (structured context packages, retrieval quality metrics) [^50^][^51^][^49^]; and layered hallucination guardrails (strict source binding, citation-required, refusal on weak evidence, human approval for high-impact outputs, external confidence calibration) [^52^][^53^][^54^][^62^]. Without these, AI "multiplies mistakes at machine speed" [^47^].

---

## REFERENCES

[^1^] U.S. GAO, *Better Mechanisms Needed for Sharing Lessons Learned*, GAO-02-195, Jan 30, 2002. https://www.govinfo.gov/content/pkg/GAOREPORTS-GAO-02-195/html/GAOREPORTS-GAO-02-195.htm
[^2^] NASA Office of Inspector General, *Review of NASA's Lessons Learned Information System*, IG-12-012, 2012. https://oig.nasa.gov/docs/IG-12-012.pdf
[^3^] Cancian, CSIS, *Coping with Surprise in Great Power Conflicts*, Feb 2018. https://csis-website-prod.s3.amazonaws.com/s3fs-public/publication/180227_Cancian_CopingWithSurprise_wAppen_Web.pdf
[^4^] "A Model Lessons Learned System – The US Army," Social Media Today (accessed 2026-07). https://www.socialmediatoday.com/content/model-lessons-learned-system-us-army
[^5^] DVIDS, "Army Aviation lessons learned / CALL validation," issue 76732 (accessed 2026-07). https://www.dvidshub.net/publication/issues/76732
[^6^] H. Dolfing, "Why Your Organization Doesn't Learn From Its Lessons Learned," 2025. https://www.henricodolfing.ch/en/why-your-organization-doesnt-learn-from-its-lessons-learned/
[^7^] OwnerTeamConsult, "Learning from All Projects," 2020. https://www.ownerteamconsult.com/learning-from-all-projects/
[^8^] PMPeople community, "Lessons Learned in Project Management," 2026. https://community.pmpeople.ai/lessons-learned-in-project-management
[^9^] Plane.so, "How to document lessons learned from projects," 2026. https://plane.so/blog/how-to-document-lessons-learned-from-projects
[^10^] NSTA/OGA, "Lessons Learned from Oil and Gas Projects 2011–2016" (5-year review, 58 projects). https://www.nstauthority.co.uk/news-publications/the-oga-publishes-five-year-review-of-major-oil-and-gas-projects-in-lessons-learned-from-oil-and-gas-projects-2011-2016-report/
[^11^] StandardsExplained, "ISO 30401 Knowledge Management Systems" (incl. full table of contents), 2025. https://standardsexplained.com/iso-30401-knowledge-management-systems/
[^12^] Pacific Cert, "ISO 30401:2018 – Knowledge Management Systems," 2025. https://pacificcert.com/iso-30401-2018-knowledge-management-systems/
[^13^] Springer, "Towards Architecting a Knowledge Management System: Requirements for an ISO Compliant Framework" (ISO 30401 definitions). https://link.springer.com/content/pdf/10.1007/978-3-030-35151-9_3.pdf
[^14^] ITB Digilib thesis on ISO 30401 implementation (clause 4.4 analysis; Nick Milton/Knoco comment on ISO 9001 7.1.6), 2023. https://digilib.itb.ac.id/assets/files/2023/MjAyM19UU19QUF9VdGhldSBCdWRoaSBTdXNldHlvXzI5MTE5NDQ0XyBGdWxsIFRoZXNpcy5wZGY.pdf
[^15^] National Law Review, "Chemical Safety Board Says More Public Reporting and Leading Indicators Still Needed…" Aug 30, 2012. https://natlawreview.com/article/chemical-safety-board-says-more-public-reporting-and-leading-indicators-still-needed
[^16^] IOGP, *Process Safety – Recommended Practice on Key Performance Indicators*, Report 456, 3rd ed. May 2023. https://www.iogp.org/bookstore/product/process-safety-recommended-practice-on-key-performance-indicators/
[^17^] SmartQHSE, "BP Texas City Refinery ISOM unit explosion (2005) — Investigation Deep Dive," 2026. https://www.smartqhse.com/safety-blog/bp-texas-city-2005-incident-investigation-deep-dive-2026
[^18^] Cambridge Univ. Press, *The Evolution of Transnational Rule-Makers through Crises*, Ch. 10 (API & Deepwater Horizon; RP 75 history). https://www.cambridge.org/core/books/evolution-of-transnational-rulemakers-through-crises/organizational-responses-of-transnational-private-regulators-after-major-accidents/7A6EB624360747541C8A21B1D6220749
[^19^] American Institute of Safety Professionals, "Safety and Environmental Management System (SEMS)" course overview, 2025. https://amiosp.com/courses/safety-and-environmental-management-system-sems
[^20^] ISHN, "Oil industry group updates EHS standard for offshore ops" (API RP 75, 4th ed.). https://www.ishn.com/articles/111960-oil-industry-group-updates-ehs-standard
[^21^] BakerRisk, "The Elements of Asset Integrity Management…" webinar deck (CCPS RBPS pillars/elements), 2024. https://www.bakerrisk.com/wp-content/uploads/2024/08/BakerRisk_Asset-Integrity-Webinar_Final.pdf
[^22^] PetroSolutions, "Understanding the CCPS Risk-Based Process Safety Management System," 2025. https://thepetrosolutions.com/understanding-the-ccps-risk-based-process-safety-management-system/
[^23^] AIChE/CCPS, *Process Safety Metrics: Guide for Selecting Leading and Lagging Metrics*, Apr 2018. https://www.aiche.org/sites/default/files/docs/pages/ccps_process_safety_metrics_-_april_2018.pdf
[^24^] Coveo, "What's Your Knowledge Management Maturity Level?" (APQC five levels; KM CAT; KM3), 2025. https://www.coveo.com/blog/the-4-phases-of-knowledge-management-maturity/
[^25^] Market Logic, "Knowledge management maturity: how well do you 'know what you know'?", 2022. https://marketlogicsoftware.com/blog/knowledge-management-maturity/
[^26^] DOAJ, "Evaluation of Knowledge Management Maturity Level in Iranian Audiovisual Archives Based on the APQC Model," 2025. https://doaj.org/article/cdd22b94e6dc4360b635136971b02857
[^27^] HMRC platui-adr-spike (ADR purpose; Nygard 2011 quote). https://github.com/hmrc/platui-adr-spike
[^28^] TechRxiv, "ADR history & abandonment; AI as producer/consumer of ADRs," 2025. https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177205025.54351571
[^29^] Arachne Framework, "ADR-001: Use ADRs" (workflow; supersession rules). https://github.com/arachne-framework/architecture/blob/master/adr-001-use-adrs.md
[^30^] IntellaQuest, "How Can Organizational Knowledge Be Captured in QMS?", 2026. https://intellaquest.com/how-can-organizational-knowledge-be-captured-in-qms-2/
[^31^] Irwin et al., "The effect of source reliability and information credibility on judgments of information quality in intelligence analysis," *Judgment and Decision Making*, Cambridge (accessed 2026-07). https://www.cambridge.org/core/journals/judgment-and-decision-making/article/effect-of-source-reliability-and-information-credibility-on-judgments-of-information-quality-in-intelligence-analysis/E67548E8010A47345C3439D45D9EC6B3
[^32^] NATO STO-TR-SAS-114, *Assessment and Communication of Uncertainty in Intelligence to Support Decision-Making* (AJP-2.1 & STANAG 2511 scales). https://www.sto.nato.int/publications/STO%20Technical%20Reports/STO-TR-SAS-114/$$TR-SAS-114-ALL.pdf
[^33^] Palo Alto Unit 42, *Attribution Framework* (Admiralty System implementation, default source scores), 2025. https://unit42.paloaltonetworks.com/unit-42-attribution-framework/
[^34^] BlockInt, "Critical review of the Admiralty Code" (Besombes & Revault d'Alonnes critiques). https://www.blockint.nl/intel-analysis/critical-review-of-the-admiralty-code/
[^35^] NASA LLIS lesson record example (template fields: Lesson, Recommendation, Evidence of Recurrence Control Effectiveness). https://llis.nasa.gov/lesson/758
[^36^] Finding Petroleum, "Knowledge management in Schlumberger" (InTouch/Eureka structure, validation roles). https://www.findingpetroleum.com/n/Knowledge_management_in_Schlumberger/ffe7506a.aspx
[^37^] Oil IT Journal, Apr 2011 (InTouch statistics; Eureka communities; "never declare victory"). https://oilit.com/2journal/4php/4_makemonthly.php?year=2011&month=4
[^38^] *Knowledge Management 2.0: Organizational Models and Enterprise Strategies* (Schlumberger chapter; best-practice tiering; pre-InTouch delays). https://epdf.pub/knowledge-management-20-organizational-models-and-enterprise-strategies.html
[^39^] Claxus, "Building a Professional Community" (InTouch $200M/yr, 95% response-time improvement; Edmundson quote), 2023. https://claxus.com/articles/building-a-professional-community/
[^40^] Offbeat Works, "Communities of practice. A case study" (Shell 13 CoPs/10,000 users; Wenger & Snyder 2000). https://offbeat.works/post/communities-of-practice-a-case-study
[^41^] AllyMatter, "Knowledge Base Archiving: When and How to Archive Pages Strategically," 2026. https://allymatter.com/blog/when-to-archive-a-knowledge-base-page/
[^42^] Knowledge-Base.Software, "Knowledge Base Deprecation Strategy," 2026. https://knowledge-base.software/guides/knowledge-base-deprecation-strategy/
[^43^] Knowledge-Base.Software, "What Is Knowledge-Centered Service (KCS)? A Practical Guide," 2026. https://knowledge-base.software/guides/knowledge-centered-service-kcs-framework/
[^44^] Consortium for Service Innovation, *KCS v6 Practices Guide* (Solve/Evolve loops; "reuse is review"; demand-driven improvement). https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030
[^45^] NICE CXone Expert, "KCS v6 practices" (8 practices incl. techniques list), 2024. https://expert-help.nice.com/Success_Driven_Content_Strategies/Self-Service_Strategy/KCS_Methodology/KCS_capabilities_powered_by_CXone_Expert
[^46^] Earley & Associates / HBR Analytic Services (AWS-sponsored), "Scaling Generative AI for Value / Building Enterprise AI Value Through Data Excellence," 2024. https://www.earley.com/insights/scaling-generative-ai-for-value
[^47^] CloudX, "The Data & Analytics Maturity Curve for AI readiness," 2026. https://cloudx.com/insights/the-data-and-analytics-maturity-curve
[^48^] Alexander Thamm, "An Introduction to AI-Ready Data" (IBM IBV 2025 CEO Study figures), 2026. https://www.alexanderthamm.com/en/blog/ai-ready-data/
[^49^] Meta-Intelligence, "The Complete Guide to Context Engineering: From RAG to Memory Systems," 2025 (3 RAG generations; quality metrics). https://www.meta-intelligence.tech/en/insight-context-engineering
[^50^] Select Star, "Context Engineering for Data Teams: Turning Metadata into AI Assets," 2025. https://www.selectstar.com/resources/context-engineering-for-data
[^51^] Calboreanu, "A Methodology for Structured Human-AI Collaboration" (Context Engineering; five-role context package; observational n=200), arXiv, 2025/2026. https://arxiv.org/html/2604.04258v1
[^52^] Darwin AI, "AI Guardrails in 2026: 9 Hallucination Prevention Strategies," 2026. https://blog.getdarwin.ai/en/ai-guardrails-hallucination-prevention-2026
[^53^] CustomGPT, "AI Guardrails: How to Prevent LLM Hallucinations" (S4 rule), 2026. https://customgpt.ai/ai-guardrails-how-to-prevent-llm-hallucinations/
[^54^] Blockchain Council, "Evaluating Gemini Outputs: Automated Testing, Guardrails, and Hallucination Reduction," 2026. https://www.blockchain-council.org/ai/evaluating-gemini-3-5-flash-outputs-automated-testing-guardrails-hallucination-reduction/
[^55^] Millennial.ae, "AI-Powered Predictive Maintenance in Oil & Gas: How Shell Reduced Downtime…" (vendor-cited figures incl. GenAI troubleshooting assistants Phase 3, 2023–2025). https://millennial.ae/ai-powered-predictive-maintenance-in-oil-gas-how-shell-reduced-downtime-and-improved-asset-reliability-using-machine-learning/
[^56^] Pageplace preview, *Knowledge Management at Shell: Innovation and Integration* (case-based reasoning for analogous-situation retrieval). https://api.pageplace.de/preview/DT0400.9781136374142_A24429444/preview-9781136374142_A24429444.pdf
[^57^] Stardog (Gartner), "Adopt a Data Semantic Approach to Drive Business Value with GenAI," Jun 2025. https://info.stardog.com/adopt-a-data-semantic-approach-to-drive-business-value-with-genai
[^58^] Capable, "The Strategic Power of KCS" (AI needs curated knowledge: "Garbage in, garbage out"), 2025. https://www.gocapable.com/blog/the-strategic-power-of-kcs
[^59^] CORE (NPS thesis), "Best Practices and Lessons Learned capture 'while doing their job'; AAR description." https://core.ac.uk/download/pdf/36739294.pdf
[^60^] CORE, "Facing Integrated Compression Business…" (US CALL vs NATO lessons-learned process models; Vego 2007), 2011-era. https://core.ac.uk/download/pdf/48035736.pdf
[^61^] PMI, "Lessons learned—the army way" (CALL Acquisition Branch). https://www.pmi.org/learning/library/project-lessons-learned-army-way-7
[^62^] NLIP Project, *Security Guidelines and Best Practices* (hallucination-driven fraud controls; human approval for high-impact outputs), 2025. https://github.com/nlip-project/security_guidelines
[^63^] dev.to, "The Future of AI: Context Engineering in 2025 and Beyond" (contextual embeddings; caching; MCP), 2025. https://dev.to/lofcz/the-future-of-ai-context-engineering-in-2025-and-beyond-5n9
[^64^] Data Nucleus, "How GenAI Transforms Manufacturing: RAG & Agentic AI" (GenAI Document Assistant pattern), 2025. https://datanucleus.dev/manufacturing-industrial-automation/transforming-factory-floors-how-genai-drives-productivity-and-empowers-workers-in-uk-high-value-manufacturing
[^65^] iFactory/BusCMMS, "Retrieval-Augmented Generation (RAG) for Maintenance Knowledge Management" (agentic maintenance claims), 2026. https://ifactoryapp.com/industries/aviation-management/retrieval-augmented-generation-rag-maintenance-knowledge
[^66^] Quizlet secondary summary, "CCPS: 4 Pillars and 20 Elements of Process Safety" (element definitions; secondary). https://quizlet.com/373391372/ccps-4-pillars-and-20-elements-of-process-safety-flash-cards/
[^67^] ALTSS, "The OSINT Intelligence Framework for Private Markets" (Admiralty separation principle). https://altss.com/knowledge-center/frameworks/osint-framework-for-private-markets-intelligence
[^68^] Jellyrock docs/decisions.md (sub-ADR decision notes; append-only discipline). https://github.com/jellyrock/jellyrock/blob/main/docs/decisions.md
[^69^] Consortium for Service Innovation, "ServiceNow: Implementing KCS Delivered 52% Faster Time to Relief," 2026. https://library.serviceinnovation.org/Case_Studies/KCS_Case_Studies/400_ServiceNow_KCS_Faster_Time_to_Relief

*Search-method note: 38 web searches executed 2026-07-18 across five themes (LL-system failure modes; standards; taxonomy/metadata/decision records; governance/lifecycle/CoPs; GenAI/RAG/context engineering). Vendor and consultancy sources are used for practice descriptions and are flagged where performance figures are vendor-reported rather than independently audited. Government audits (GAO, NASA OIG), regulator commentary (CSB via NatLawReview), standards bodies (ISO via secondary summaries), and academic sources (Cambridge, Springer, NATO STO, DOAJ) are prioritized for claims of fact.*

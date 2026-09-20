# Synthetic Data Generation Strategy

## Enterprise Context Engineering

**Status:** Draft for implementation  
**Version:** 0.1.0  
**Date:** 2026-09-20  
**Applies to:** `aadehamid/enterprise-context-engineering`

---

## 1. Purpose

This strategy defines how the Enterprise Context Engineering project will create a **synthetic enterprise decision-provenance corpus**: a realistic, internally consistent body of structured data and unstructured artifacts that enables users and AI agents to investigate historical-looking enterprise decisions.

The objective is to answer questions such as:

- Why was a decision made?
- What evidence was available when it was made?
- Which options were considered and rejected?
- Which operational, financial, commercial, safety, reliability, regulatory, or organizational constraints influenced the choice?
- Who had authority, who recommended the action, and who challenged it?
- What later outcome followed, and did it validate or challenge the original rationale?
- Which source artifacts directly support the explanation, which conclusions are inferred, and what remains unknown?

The project does **not** claim to recreate a real organization’s history. It creates a fictional enterprise environment that behaves like an enterprise over time: data changes, people disagree, documents are incomplete, assets evolve, procedures are revised, decisions have consequences, and evidence is scattered across systems and document types.

---

## 2. The problem this solves

Most synthetic-data approaches focus on one of the following:

- relational business data such as ERP, CRM, finance, procurement, inventory, or master data;
- time-series data such as sensor values, historian readings, alarms, and events;
- individual documents or generic instruction/response training examples; or
- privacy-preserving replicas learned from existing production data.

Those approaches are useful, but they commonly omit the **decision context** needed for enterprise knowledge management:

- a decision itself;
- contemporaneous observations and constraints;
- alternatives and trade-offs;
- roles, approvals, escalations, and disagreements;
- records distributed across multiple systems and formats; and
- outcome evidence that becomes available later.

This strategy supplies that missing layer. It produces a synthetic, evidence-linked history in which a system must retrieve and combine multiple artifacts to explain a past decision responsibly.

---

## 3. Scope

### 3.1 In scope

The corpus may include synthetic content for:

- business architecture: capabilities, value streams, processes, organizations, roles, products, customers, suppliers, and locations;
- commercial and planning decisions: supply, scheduling, pricing, margins, demand, inventory, product allocation, and capital prioritization;
- operations and OT-adjacent decisions: operating modes, throughput, maintenance deferrals, reliability actions, alarm response, quality constraints, and production planning;
- enterprise systems: ERP, EAM/CMMS, LIMS, historian/SCADA summaries, planning systems, finance, reporting, data platforms, and collaboration tools;
- unstructured evidence: emails, meeting minutes, decision memoranda, slide decks, policies, procedures, reports, work orders, laboratory summaries, and operational handover notes;
- semantic products: ontology instances, taxonomies, mappings, data contracts, provenance triples, knowledge-graph exports, and competency questions; and
- agent-training and evaluation data: evidence-aware Q&A, preference pairs, tool-use tasks, evidence selection, contradiction handling, and uncertainty-aware explanations.

### 3.2 Out of scope

- Reconstructing real company decisions from absent records.
- Representing synthetic documents as records of actual events.
- Producing control instructions for live OT systems.
- Using synthetic narrative as safety, legal, financial, accounting, environmental, regulatory, or engineering proof.
- Creating vendor-identical copies of proprietary ERP, historian, CMMS, or collaboration-system schemas.

---

## 4. Design principles

1. **Synthetic content is explicit.** Every dataset, document, artifact, graph assertion, and release is marked as synthetic.
2. **Truth precedes prose.** First create a canonical scenario and decision ledger. Generate documents and records from the ledger, not the reverse.
3. **No single artifact tells the whole story.** Evidence is intentionally distributed across source types and roles.
4. **Claims are traceable.** Each material fact in a gold answer links to one or more source artifacts and locations.
5. **Time matters.** Store decision time, source-authoring time, effective period, ingestion/generation time, and validity interval separately.
6. **Inference is not evidence.** Gold answers and agent responses must distinguish direct support, inference, contradiction, and unknowns.
7. **Controlled inconsistency is realistic.** Artifacts can contain legitimate disagreement, stale assumptions, incomplete context, and delayed approvals, while the hidden ledger retains the intended truth.
8. **Domain constraints govern generation.** Numeric values, operational states, work orders, roles, approvals, and documents must comply with the scenario’s business and engineering rules.
9. **Reproducibility is mandatory.** Record scenario version, generator version, seed, prompt/template version, model/provider, run ID, validation results, checksums, and release version.
10. **Evaluation truth is isolated.** The canonical ledger and hidden answer key must not be available to a system being evaluated.

---

## 5. Target corpus model

The corpus is constructed as a connected enterprise world, not as isolated records.

```text
Enterprise / organization
  ├── business capabilities and value streams
  ├── processes, products, customers, suppliers, and locations
  ├── assets, units, equipment, tags, and operating constraints
  ├── people and roles with time-valid authority
  ├── events and observations
  ├── decisions, alternatives, approvals, and actions
  ├── evidence artifacts in multiple systems and formats
  └── outcomes, exceptions, and retrospective findings
```

### 5.1 Core entities

| Entity | Purpose |
|---|---|
| `Scenario` | Defines the synthetic enterprise, period, scope, assumptions, and seed |
| `Organization`, `Role`, `PersonPersona` | Defines time-valid organizational context and authority |
| `Capability`, `ValueStream`, `Process` | Connects decisions and data to business architecture |
| `Asset`, `Unit`, `Equipment`, `Tag` | Represents operational/OT-adjacent context |
| `Product`, `Material`, `Customer`, `Supplier`, `Location` | Represents commercial and operational business context |
| `Observation`, `Event`, `Alarm`, `WorkOrder`, `LabResult` | Represents structured evidence and operational facts |
| `Decision` | Represents a chosen action at a point in time |
| `DecisionOption` | Represents selected, rejected, deferred, or unconsidered options |
| `Constraint`, `Risk`, `Policy`, `Procedure` | Represents boundaries and decision conditions |
| `EvidenceItem`, `Artifact`, `SourceAssertion` | Represents source records and specific assertions within them |
| `Outcome`, `Review`, `Exception` | Represents what happened after the decision |
| `Claim`, `Answer`, `EvaluationCase` | Represents user-facing explanations and scoring truth |

### 5.2 Canonical decision dossier

Each synthetic decision must be represented by an internal decision dossier. The dossier is the hidden truth layer and is not a source artifact to retrieve during a blind evaluation.

```json
{
  "decision_id": "DEC-2017-00841",
  "scenario_id": "enterprise-context-demo-v1",
  "decision_time": "2017-09-14T10:30:00-05:00",
  "decision_domain": "reliability_and_operations",
  "decision_statement": "Defer compressor C-301 bearing replacement for six weeks",
  "decision_owner_roles": ["Operations Manager", "Reliability Manager"],
  "authority_basis": "maintenance-deferral-policy-v3",
  "affected_entities": ["asset:C-301", "unit:utilities-compression"],
  "drivers": [
    "Vibration remained below trip threshold",
    "Immediate shutdown would disrupt peak seasonal production"
  ],
  "constraints": [
    "Enhanced monitoring is required",
    "Inspection must occur before the next planned shutdown",
    "Spare bearing availability is limited"
  ],
  "options": [
    "Immediate shutdown and repair",
    "Operate with heightened monitoring until planned shutdown",
    "Reduce compressor load pending repair"
  ],
  "selected_option": "Operate with heightened monitoring until planned shutdown",
  "approval_status": "approved_with_conditions",
  "expected_outcome": "Maintain production while controlling short-term reliability risk",
  "actual_outcome": "Inspection occurred during planned shutdown; wear was within revised acceptance criteria",
  "ground_truth_rationale": "The production impact of an immediate shutdown outweighed assessed near-term risk, conditional on enhanced monitoring and formal approval.",
  "known_uncertainties": ["Root cause of the vibration increase was not confirmed at decision time"],
  "synthetic": true
}
```

---

## 6. Generation architecture

The generation process uses a layered model.

```text
Semantic model + scenario configuration + deterministic seed
                         │
                         ▼
          Canonical enterprise reference data
                         │
                         ▼
          Events, observations, constraints, decisions
                         │
                         ▼
              Hidden decision ledger / truth
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
Structured records   Narrative artifacts   Knowledge graph / manifests
ERP, CMMS, LIMS,     Emails, decks,        RDF/CSV/Parquet provenance,
historian summaries  PDFs, minutes,        lineage, retrieval indexes
                     reports, handovers
          │              │              │
          └──────────────┼──────────────┘
                         ▼
              Validation and release controls
                         │
                         ▼
        Retrieval, agent evaluation, and demonstrations
```

### 6.1 Layer A — semantic and scenario foundation

Define and version:

- domain ontology, taxonomy, and controlled vocabularies;
- competency questions and answer expectations;
- organizational hierarchy and delegated authority;
- business capabilities, value streams, and process models;
- asset hierarchy and OT/operational context where relevant;
- document taxonomy and source-system profiles;
- role-specific writing styles, templates, and communication norms;
- lifecycle states, policy rules, approval thresholds, and temporal constraints; and
- scenario scale, geography, product mix, and operating calendar.

### 6.2 Layer B — canonical enterprise truth

Generate deterministic master and reference data:

- organizations, business units, departments, roles, and personas;
- sites, units, equipment, tags, products, suppliers, customers, and locations;
- reference codes, engineering units, cost centers, fiscal calendars, and document templates;
- policies, procedures, operating envelopes, and policy-version timelines.

This layer contains stable IDs and time-valid configuration. It is the source of referential integrity for all later layers.

### 6.3 Layer C — events and decisions

Generate events and observations that create realistic decision pressure:

- operational deviations, alarms, throughput changes, quality results, demand changes, supply disruptions, inventory imbalances, and reliability findings;
- maintenance condition observations, inspections, work-order states, resource constraints, and scheduled outages;
- commercial/financial signals, budget limitations, customer commitments, and planning conflicts;
- decision alternatives, approvals, dissent, escalation, deferral, reversal, and outcome monitoring.

Generate decisions through explicit state machines and rules where possible; use LLM generation for narrative variability, not as the primary truth engine.

### 6.4 Layer D — distributed artifacts

Render evidence into formats that mirror enterprise information topology.

| Artifact type | Typical contribution | Example limitations |
|---|---|---|
| Email thread | Debate, stakeholders, emerging constraints, informal approval | May be incomplete, stale, or lack final authority |
| Decision memo | Formal recommendation, authority, date, selected action | May summarize rather than preserve all debate |
| Presentation deck | Options, economics, risk framing, recommendation | Can contain assumptions later revised |
| Meeting minutes | Attendees, actions, decision wording, unresolved issues | May omit informal discussions |
| ERP/planning record | Orders, costs, inventory, schedules, commitments | Does not explain full rationale |
| CMMS/work order | Condition evidence, maintenance plan, approval status | Does not capture commercial trade-offs |
| Historian/alarm summary | Process behavior around an event | Must be derived from valid operational rules |
| Laboratory/quality report | Product or process constraints | May arrive after a key decision |
| Shift handover / report | Operational interpretation and actions | Role-specific and sometimes terse |
| Outcome review | Result, impact, lessons learned | Contains hindsight unavailable at decision time |

No artifact should expose the complete ground-truth rationale by default.

### 6.5 Layer E — retrieval and evaluation products

Build:

- source-document repository and metadata index;
- semantic graph connecting artifacts, claims, entities, time, and provenance;
- vector and keyword search indexes;
- question sets and gold answers;
- preferred/rejected answer pairs for groundedness training;
- hidden evaluation sets, evidence sets, and scoring rubrics.

---

## 7. Data types and generation methods

| Data type | Generation approach | Primary validation |
|---|---|---|
| Master/reference data | Deterministic generators, Faker-like utilities, controlled vocabularies | IDs, referential integrity, code validity, temporal validity |
| Relational enterprise records | Rule-based generators; SDV/Tonic/MOSTLY AI where appropriate | Foreign keys, lifecycle rules, reconciliations, distributions |
| OT/operational time series | State machines, constrained simulation, statistical noise models | Ranges, units, correlations, rate limits, modes, causality |
| Alarms/events | Derived from rules and state transitions | Thresholds, deadbands, persistence, event ordering |
| Decision ledger | Scenario rules plus structured LLM output under schema validation | Completeness, authority, alternatives, evidence plan, time validity |
| Narrative artifacts | LLM generation from decision dossier and artifact-specific templates | Entity/date consistency, source role, evidence fragmentation, style |
| Presentations/PDF/DOCX | Structured content plus native rendering templates | Layout, page/slide references, embedded metadata, traceability |
| Knowledge graph | Deterministic transformation from canonical data and artifact assertions | SHACL/schema validation, provenance paths, identifier resolution |
| Q&A/evaluation data | Generated from available evidence, then adjudicated against hidden truth | Citation precision, groundedness, inference/unknown handling |

---

## 8. Role of external products and frameworks

No single product should be treated as the complete synthetic decision-provenance solution.

### 8.1 Adaption Invent / Adaptive Data

Use for model-ready synthetic training and evaluation datasets:

- evidence-aware question/answer pairs;
- preference pairs contrasting supported and unsupported explanations;
- scenario variations, paraphrases, adversarial questions, and ambiguity cases;
- context-plus-answer records for fine-tuning or agent evaluation.

It is not the canonical enterprise simulator. The repository’s schema, scenario model, and decision ledger remain authoritative for synthetic truth.

### 8.2 Tonic, MOSTLY AI, Gretel, and SDV

Use selectively:

- **Tonic-type platforms:** relational databases, mock APIs, and certain unstructured-data workflows.
- **MOSTLY AI / Gretel:** privacy-safe or pattern-based synthesis when legitimate seed data becomes available.
- **SDV:** open-source multi-table, sequential, and constrained structured-data generation.

These products can accelerate record generation but must be constrained by scenario IDs, schemas, temporal rules, and release manifests.

### 8.3 LLM orchestration

Use structured output with schema validation for document plans, source assertions, and artifact metadata. LLMs should receive only the relevant slice of canonical scenario context necessary to generate each artifact. This reduces leakage of the full truth into a single document and improves role-appropriate realism.

---

## 9. Document-generation rules

### 9.1 Evidence fragmentation

For each decision, create 4–10 linked artifacts. Distribute facts deliberately.

Example: `DEC-2017-00841` may generate:

1. Maintenance-engineer email reporting vibration trend and recommending inspection.
2. Reliability-review deck comparing repair-now, defer-with-monitoring, and reduced-load options.
3. Operations meeting minutes recording production consequences.
4. Formal approval memo authorizing deferral with monitoring conditions.
5. CMMS work order marked deferred/approved.
6. Historian summary showing vibration and load context.
7. Later close-out email describing inspection results.

### 9.2 Artifact metadata

Every artifact must have a machine-readable manifest with at least:

```json
{
  "artifact_id": "ART-EMAIL-2017-00921",
  "scenario_id": "enterprise-context-demo-v1",
  "decision_ids": ["DEC-2017-00841"],
  "source_system": "synthetic-collaboration-suite",
  "artifact_type": "email_thread",
  "authored_at": "2017-09-13T15:42:00-05:00",
  "effective_from": "2017-09-13",
  "author_role": "Maintenance Engineer",
  "participants": ["Reliability Manager", "Operations Manager"],
  "entities": ["asset:C-301", "unit:utilities-compression"],
  "classification": "synthetic",
  "generator": {
    "scenario_version": "1.0.0",
    "template_version": "email-thread-v1",
    "generator_version": "0.1.0",
    "seed": 20260920
  },
  "content_hash": "<sha256>"
}
```

### 9.3 Source assertions

Extract or generate explicit assertions from each artifact, linked to their locations:

- email message ID and paragraph;
- PDF page and section;
- PowerPoint slide and shape/text block if available;
- meeting-minute agenda item;
- structured-record field and version;
- historian summary time window and tag list.

This enables a graph and answering agent to cite specific evidence rather than only a document title.

---

## 10. OT and operational realism

Where the scenario includes industrial data, language-model-generated values alone are insufficient. Use explicit operational constraints.

### 10.1 Required controls

- Engineering units and valid ranges.
- Asset/tag relationships and equipment capabilities.
- Mode/state definitions: startup, shutdown, steady state, upset, maintenance, degraded operation, turnaround.
- Rate-of-change limits and timestamps.
- Cross-variable dependencies such as flow, pressure, temperature, level, load, and quality relationships.
- Alarm thresholds, deadbands, delays, prioritization, acknowledgement/shelving conventions, and state transitions.
- Sensor-quality conditions: noise, drift, dropout, stale values, spikes, calibration flags, and bad-quality indicators.
- Maintenance lifecycle logic: detection, notification, planning, approval, deferral, execution, verification, and close-out.
- Separation of operational facts known at the decision time from later outcomes or hindsight.

### 10.2 Recommended modeling posture

Use a hybrid approach:

- deterministic/reference generation for IDs, assets, and constraints;
- state-machine or rules-based simulation for event sequences and lifecycle states;
- numerical/time-series simulation for telemetry;
- LLM-generated language for narratives, explanations, emails, reports, and varied phrasing;
- human/SME review for high-impact process, safety, and reliability scenarios.

---

## 11. Quality validation

Validation is applied at four levels.

### 11.1 Structural validation

- JSON Schema/Pydantic validation for canonical records and manifests.
- Referential-integrity checks across IDs.
- Required-field, cardinality, and controlled-vocabulary checks.
- Document-format and rendering checks for PDF/DOCX/PPTX/HTML/email artifacts.

### 11.2 Temporal validation

- Artifact authorship must occur after information becomes available and before it can be referenced.
- Decision authority, policy, asset state, organizational role, and procedure version must be valid at the decision time.
- Outcome information must not appear in pre-decision artifacts unless intentionally modeled as forecast.
- Superseded policies and decommissioned assets cannot be treated as current.

### 11.3 Domain validation

- Operating values and events comply with scenario engineering constraints.
- Work-order and approval lifecycles are valid.
- Financial, inventory, production, and planning quantities reconcile within defined tolerances.
- Decision options, risks, and constraints are plausible for the modeled business process.

### 11.4 Reasoning/evaluation validation

For each evaluation question, score:

- evidence retrieval precision and recall;
- citation/attribution precision;
- factual correctness against hidden truth;
- distinction among supported fact, inference, contradiction, and unknown;
- temporal correctness;
- absence of unsupported detail;
- answer completeness and appropriate uncertainty;
- usefulness and clarity for the intended role.

---

## 12. Evaluation design

### 12.1 Question types

Create questions at several difficulty levels:

- Direct lookup: “Who approved the deferral?”
- Evidence synthesis: “Why was the repair deferred?”
- Temporal reasoning: “What information was known before approval?”
- Contradiction detection: “Why do the maintenance email and final memo differ?”
- Alternative analysis: “Which option was rejected and why?”
- Outcome analysis: “Did later evidence support the decision?”
- Boundary assessment: “What cannot be established from the available record?”
- Lineage tracing: “Which source fields and artifacts support this KPI/decision claim?”

### 12.2 Gold-answer structure

Gold answers should use a predictable evidence discipline:

```text
Conclusion
  - concise answer to the question

Directly supported evidence
  - source-linked facts

Inference
  - bounded reasoning that combines evidence

Conflicts or uncertainty
  - disagreement, ambiguity, missing evidence, or timing limitations

Evidence references
  - artifact IDs and precise locations
```

### 12.3 Hidden-truth separation

The hidden canonical ledger supports evaluation but must not be indexed for the agent being tested. Evaluation runs should record:

- model and prompt version;
- retrieval configuration and index version;
- scenario/release ID;
- question ID;
- retrieved artifacts;
- response and citations;
- automated and human scores;
- identified failure types.

---

## 13. Storage, release, and Cloudflare R2 workflow

Large generated datasets, native document artifacts, graph exports, rendered decks/PDFs, and hidden evaluation truth must not be committed to GitHub. GitHub contains source code, Markdown docs, schemas, semantic assets, scenario configuration, tests, manifests, and small fixtures.

Use Cloudflare R2—or an equivalent controlled object store—as the durable data store:

```text
Cloudflare R2 = large shared synthetic data, document bundles, manifests, releases, hidden truth
Local disk     = temporary scratch for generation, validation, and upload
GitHub         = code, documentation, semantic assets, schemas, configurations, tests, small fixtures
```

The project should adapt the accompanying Cloudflare guidance to this repository, using a dedicated bucket and release-scoped prefixes. Recommended layout:

```text
<project-bucket>/
├── raw/                           # Optional approved public/reference inputs
├── cache/
│   ├── canonical/                 # Canonical enterprise truth; controlled access
│   ├── structured/                # ERP/CMMS/LIMS/operational variants
│   ├── documents/                 # Native synthetic emails, PDFs, DOCX, PPTX, HTML
│   ├── graph/                     # RDF, CSV, property-graph exports
│   ├── indexes/                   # Search/vector/index build inputs where appropriate
│   ├── quality/                   # Validation findings and reports
│   └── manifests/                 # Dataset and artifact manifests
├── exports/                       # Approved consumable releases
├── evaluation/
│   ├── development/               # Shareable evaluation data
│   └── hidden/                    # Held-out truth; restricted access
├── notes/                         # Run and release notes
└── _probe/                        # Disposable connectivity probes only
```

Required practices:

- One dedicated bucket per project.
- Secrets sourced from an approved secret store or protected environment; never committed or pasted into documentation/chat.
- Release/version/run prefixes; do not silently overwrite released data.
- SHA-256 checksums, manifests, schema versions, seeds, and generator versions for every release.
- Local scratch cleanup after successful validation/upload.
- Restricted access to `evaluation/hidden/` and canonical truth where appropriate.
- Small test fixtures in Git; large data and generated artifacts in R2.

See the companion file `docs/strategy/cloudflare-r2-data-storage-and-agent-workflow.md` once adapted for this repository.

---

## 14. Proposed repository structure

```text
enterprise-context-engineering/
├── docs/
│   ├── architecture/
│   ├── strategy/
│   │   ├── synthetic-data-generation-strategy.md
│   │   └── cloudflare-r2-data-storage-and-agent-workflow.md
│   ├── discovery/
│   ├── governance/
│   └── examples/
├── semantic/
│   ├── ontology/
│   ├── taxonomy/
│   ├── shapes/
│   └── mappings/
├── scenarios/
│   ├── reference-data/
│   ├── decision-ledger/
│   ├── event-models/
│   ├── constraint-library/
│   └── scenario-configs/
├── schemas/
├── generators/
│   ├── structured-data/
│   ├── documents/
│   ├── ot-events/
│   └── graph/
├── pipelines/
├── evaluations/
│   ├── development/
│   ├── hidden/
│   └── rubrics/
├── fixtures/
├── scripts/
├── tests/
└── infra/
```

Migration approach:

1. Preserve current discovery, architecture, and analysis material.
2. Add the new `docs/strategy/`, `semantic/`, `scenarios/`, `schemas/`, and `evaluations/` areas.
3. Move or link existing materials into `docs/discovery/` and `docs/architecture/` once ownership and naming are agreed.
4. Start with a small, fully validated pilot before generating a multi-year enterprise corpus.

---

## 15. Implementation roadmap

### Phase 0 — foundation

- Define repository conventions, release naming, synthetic-data labeling, and storage policy.
- Establish the ontology/taxonomy baseline and competency questions.
- Define the scenario boundary, enterprise type, time horizon, and key domains.
- Implement schemas for decisions, evidence items, artifacts, manifests, and evaluation cases.

### Phase 1 — minimum viable scenario

- Generate one organization, one site/business unit, a small asset/process footprint, and time-valid roles.
- Create 10–20 canonical decisions spanning planning, operations, reliability, and commercial context.
- Generate 4–6 evidence artifacts per decision.
- Build a basic graph and retrieval index.
- Create 50–100 evaluation questions with hidden truth.

### Phase 2 — operational and document realism

- Add CMMS, planning, ERP, LIMS, historian/event-summary, and financial context.
- Add native PDF/DOCX/PPTX/email rendering.
- Add policy/procedure versioning and organizational change.
- Add controlled ambiguity, disagreement, stale documents, and missing records.

### Phase 3 — agent and knowledge-graph evaluation

- Add graph-assisted retrieval and claim-level provenance.
- Add preference pairs and groundedness evaluation.
- Measure answer quality, citation accuracy, temporal correctness, and hallucination rates.
- Run expert review on representative decision scenarios.

### Phase 4 — scale and reuse

- Expand time horizon, business domains, and source profiles.
- Package reusable scenario templates and generator modules.
- Publish release manifests, documentation, small fixtures, and reproducibility instructions.

---

## 16. Acceptance criteria for a pilot release

A pilot release is acceptable when it demonstrates all of the following:

- A coherent fictional enterprise with stable IDs and time-valid reference data.
- At least 10 decisions with alternatives, constraints, authority, and outcomes.
- At least four heterogeneous evidence artifacts per decision.
- No single artifact contains the complete decision rationale by default.
- Structured records, documents, and graph assertions agree unless contradiction is deliberately modeled.
- Every gold-answer claim has source references.
- The agent can answer decision questions with citations and state when evidence is insufficient.
- Hidden truth is not retrievable by the evaluation agent.
- The release has a manifest, checksums, validation report, scenario version, seed, and generator version.
- All content is visibly classified as synthetic.

---

## 17. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Fluent but unsupported synthetic explanations | Build truth first; validate claims against artifact assertions; use preference data that penalizes unsupported certainty |
| Cross-document inconsistency | Generate from a canonical ledger; use stable IDs; run referential, temporal, and contradiction checks |
| Unrealistic OT content | Use explicit physical/operational constraints, state machines, and SME review; do not rely only on LLM prose |
| A single document leaks all ground truth | Use artifact-specific prompts and partial context; test evidence fragmentation |
| Evaluation leakage | Separate hidden truth prefixes, access policies, indexes, and tuning datasets |
| Uncontrolled dataset growth | Use release manifests, scenario scale profiles, retention rules, and R2 lifecycle management |
| Confusion with real history | Place synthetic classification in metadata, document headers/footers, manifests, UI, and release notes |
| Vendor/tool lock-in | Keep the canonical schemas, ontology, scenarios, manifests, and evaluation formats tool-neutral |

---

## 18. Summary

This project’s synthetic-data strategy is not merely to generate plausible rows or documents. It is to generate a **governed synthetic enterprise memory** in which decisions can be investigated through fragmented, time-aware, source-linked evidence.

The core sequence is:

```text
Semantic model + scenario rules
→ canonical enterprise truth
→ decision ledger
→ distributed structured and unstructured evidence
→ provenance graph and retrieval indexes
→ evidence-grounded question answering
→ hidden-truth evaluation
```

That approach directly supports the repository’s enterprise-context-engineering goal: enabling people and AI agents to explain what happened, why a decision was made, which evidence supports the answer, and where the record remains uncertain.

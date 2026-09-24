# Enterprise Context Engineering

> A reference architecture and build workspace for creating an evidence-grounded enterprise context layer that lets people and AI agents answer: **what happened, what changed, why a decision was made, what evidence supports that explanation, and what remains uncertain.**

## Why this repository exists

Enterprise knowledge is rarely held in one governed system. It is distributed across structured operational data, reports, dashboards, data models, spreadsheets, business-process artifacts, presentations, PDFs, emails, meeting notes, policies, work orders, and analytics outputs. The material may be correct in isolation but difficult to assemble into a trustworthy answer about the enterprise.

The problem is not merely document search. It is **context engineering**:

- connecting business concepts, processes, assets, data products, metrics, decisions, evidence, and outcomes;
- preserving the time and version in which an assertion was valid;
- distinguishing direct evidence from analytical inference and unknowns;
- retaining claim-level provenance to the source artifact, record, slide, page, query, or calculation that supports an answer; and
- giving human users and AI agents a governed way to retrieve, reason over, and explain enterprise context.

This repository develops that architecture using a realistic commercial/industrial example, including business intelligence, operations, planning, reliability, finance, and OT-adjacent information. It also provides a synthetic enterprise corpus so the approach can be built and evaluated without relying on confidential production data.

## Core questions

The intended system should support questions such as:

- What does this KPI mean, how is it calculated, what sources feed it, and who owns it?
- Which business process, capability, value-stream stage, asset, customer, or product does this metric describe?
- What changed between two reporting periods, source-system versions, or organizational configurations?
- Why was a historical operational, commercial, reliability, or planning decision made?
- Which facts are directly supported by records, which are inferred, and what cannot be determined from the available evidence?
- Which documents, emails, slides, work orders, historian windows, reports, and policies support the answer?
- How does a source-system field travel through ingestion, transformation, semantic modeling, KPI calculation, and a consuming report or agent answer?

## Architectural thesis

The platform is a **context layer**, not a replacement for operational systems, a conventional document repository, or a generic vector database. It combines five complementary layers:

| Layer | Responsibility |
|---|---|
| Source and evidence layer | Preserves structured records, documents, presentations, messages, reports, and OT/operational observations with source metadata |
| Semantic layer | Defines shared business vocabulary, ontology, taxonomy, domain models, data contracts, and mappings |
| Provenance and decision layer | Connects claims, evidence, decisions, alternatives, constraints, actors/roles, outcomes, and time validity |
| Retrieval and reasoning layer | Retrieves relevant evidence and graph context; composes bounded, cited answers; exposes uncertainty and contradiction |
| Governance and evaluation layer | Applies access control, source classification, quality validation, lineage, release control, and repeatable evaluation |

The guiding principle is:

> An answer is trustworthy only when its claims can be traced to evidence, its assumptions and inferences are visible, its temporal context is respected, and unknowns remain unknown.

## Synthetic decision provenance

A central capability of this repository is a **synthetic decision-provenance corpus**. Traditional synthetic data often covers transactions, master data, telemetry, alarms, work orders, or reports. It usually lacks the reasoning context that explains why people selected one option over another.

This project fills that gap by creating a fictional but internally consistent enterprise history in which decisions are distributed across realistic artifacts:

- email threads and approval exchanges;
- meeting minutes and action logs;
- PowerPoint review decks and option analyses;
- decision memoranda, policies, and procedures;
- planning, finance, reliability, maintenance, and operational reports;
- CMMS/work-order, ERP, laboratory, historian, and alarm summaries; and
- later outcome reports, exceptions, and retrospective reviews.

The corpus is explicitly **synthetic**. It is not a reconstruction of real historical decisions and must never be represented as factual organizational history. Its purpose is to train, demonstrate, and evaluate the system’s ability to recover a decision rationale from fragmented evidence without inventing unsupported facts.

The canonical synthetic decision ledger is the hidden truth layer. Generated artifacts intentionally reveal only portions of that truth. The agent is evaluated on whether it can assemble a grounded explanation from the evidence available to it.

See [the synthetic data generation strategy](docs/strategy/synthetic-data-generation-strategy.md).

## Design principles

- **Evidence before fluency.** Retrieval and source attribution take precedence over a polished narrative.
- **Claim-level provenance.** Material claims point to a source artifact and precise location where practical.
- **Time-aware context.** Distinguish authoring time, decision time, effective period, ingestion time, and superseded versus current versions.
- **Evidence, inference, unknown.** Responses must label what is observed, inferred, contradictory, and unavailable.
- **Semantic interoperability.** Use explicit domain vocabulary and mappings rather than embedding critical meaning only in prompts or prose.
- **Synthetic by design.** All generated records and documents carry synthetic provenance, scenario, seed, generator, and release metadata.
- **Separate truth from retrieval.** Hidden generation truth is used for validation and evaluation, never supplied to the answering agent in a test.
- **Reproducibility.** Scenarios, schemas, generator versions, seeds, manifests, checksums, and validation results are versioned.
- **Governance by construction.** Access, retention, source classification, and evaluation isolation are architecture requirements—not cleanup tasks.

## Proposed repository structure

The repository is evolving toward the following structure. Existing discovery and architecture materials can be retained during migration, then linked or reorganized into these durable areas.

```text
enterprise-context-engineering/
├── README.md
├── docs/
│   ├── architecture/
│   │   ├── solution-architecture.md
│   │   ├── context-layer-architecture.md
│   │   └── decision-provenance-model.md
│   ├── strategy/
│   │   ├── synthetic-data-generation-strategy.md
│   │   └── cloudflare-r2-data-storage-and-agent-workflow.md
│   ├── discovery/
│   │   ├── requirements.md
│   │   ├── use-cases.md
│   │   └── source-inventory.md
│   ├── governance/
│   │   ├── provenance-policy.md
│   │   ├── synthetic-data-policy.md
│   │   └── access-and-evaluation-separation.md
│   └── examples/
│       └── source-name-example.md
├── semantic/
│   ├── ontology/
│   ├── taxonomy/
│   ├── shapes/
│   ├── mappings/
│   └── competency-questions/
├── scenarios/
│   ├── reference-data/
│   ├── decision-ledger/
│   ├── event-models/
│   ├── constraint-library/
│   └── scenario-configs/
├── schemas/
│   ├── decision-dossier.schema.json
│   ├── evidence-item.schema.json
│   ├── artifact-manifest.schema.json
│   └── dataset-manifest.schema.json
├── generators/
│   ├── master-data/
│   ├── structured-data/
│   ├── documents/
│   ├── ot-events/
│   ├── graph/
│   └── shared/
├── pipelines/
│   ├── generate_canonical_truth.py
│   ├── generate_artifacts.py
│   ├── validate_release.py
│   ├── build_graph.py
│   └── publish_release.py
├── evaluations/
│   ├── development/
│   ├── hidden/                 # Never commit hidden truth or expose it to tuning
│   ├── question-sets/
│   ├── rubrics/
│   └── results/
├── fixtures/
│   ├── small/
│   └── golden/
├── scripts/
│   ├── r2_client.py
│   ├── manifest.py
│   └── checksums.py
├── tests/
│   ├── semantic/
│   ├── contracts/
│   ├── generation/
│   └── evaluation/
├── infra/
│   ├── docker/
│   ├── compose/
│   └── ci/
└── .env.example
```

Large generated data, document bundles, rendered artifacts, Parquet data, graph exports, and hidden evaluation truth should not be committed to Git. Store them in controlled object storage with versioned manifests. See the Cloudflare R2 workflow in [docs/strategy/cloudflare-r2-data-storage-and-agent-workflow.md](docs/strategy/cloudflare-r2-data-storage-and-agent-workflow.md).

## Build flow

1. **Define the semantic and scenario model** — enterprise domains, business capabilities, processes, assets, products, organizations, roles, decisions, evidence, constraints, outcomes, and temporal rules.
2. **Create canonical synthetic truth** — deterministic reference data, events, decision ledger, and expected outcomes.
3. **Generate evidence artifacts** — structured records, emails, reports, slides, memos, work orders, telemetry/event summaries, and outcome documents.
4. **Validate coherence** — schema conformance, referential integrity, temporal validity, engineering/business constraints, provenance, and controlled ambiguity.
5. **Build retrieval products** — document index, semantic graph, metadata/catalog entries, vector representations, and source-to-answer evidence links.
6. **Generate and run evaluations** — questions, expected evidence sets, gold answers, preference pairs, and hidden truth scoring.
7. **Publish a release** — manifest, checksums, release notes, validation results, and controlled exports.

## Current materials

The repository currently contains:

- end-to-end solution-architecture assets;
- discovery workbooks and build-roadmap material;
- analytical agent outputs and charts;
- a source-document example; and
- early architecture/rendering assets.

The proposed structure above provides the target organization for these materials as implementation moves from discovery toward repeatable semantic modeling, synthetic-data generation, retrieval, and evaluation.

## Getting started

1. Read the architecture and discovery materials already in the repository.
2. Read the [synthetic data generation strategy](docs/strategy/synthetic-data-generation-strategy.md).
3. Review the proposed ontology/domain model and competency questions.
4. Start with a small scenario: one business unit, a limited asset/process scope, 10–20 decisions, and 4–6 artifact types per decision.
5. Build the hidden canonical ledger first, then generate distributed evidence artifacts from it.
6. Validate a question-answering agent against the hidden truth before scaling volume or scenario breadth.

## Status and scope

This is an architecture, discovery, and implementation workspace. It is not a production system, a source of real corporate history, legal advice, safety guidance, or an operational decision authority. All synthetic content must remain clearly labeled and governed as synthetic.

## Related documents

- [Synthetic Data Generation Strategy](docs/strategy/synthetic-data-generation-strategy.md)
- [Cloudflare R2 Data Storage and Agent Workflow](docs/strategy/cloudflare-r2-data-storage-and-agent-workflow.md)
- [Source Name Example](docs/discovery/source-material/Source_Name_example.txt)
- [Project Charter](docs/charter.md)

# Shared Technical Foundation — Enterprise Context Engineering

**Status:** Proposed architecture update after PPC comparison  
**Purpose:** Define which technical components Enterprise Context Engineering (ECE) can reuse from the PPC architecture without changing ECE into a downstream application platform.  
**Related:** [EPM–ECE–PPC Operating Model](epm-ece-ppc-operating-model.md) defines ownership, dependency direction and versioned contracts.

## 1. Boundary

ECE remains a **context-layer and evaluation framework**.

It is not a CRM/ERP simulation, real-time OT platform, trading system, performance-management application, autonomous-agent platform, or downstream optimization engine.

Reuse technology only when it supports ECE's own responsibilities: synthetic truth, evidence generation, provenance, temporal context, retrieval, graph context, validation, evaluation and reproducible releases.

## 2. Recommended shared foundation

| Technology | ECE role | Why reuse |
|---|---|---|
| Cloudflare R2 | durable synthetic corpus, documents, graph exports, hidden truth | already selected; shared operating pattern |
| PostgreSQL + pgvector | artifact/source-assertion metadata and vector retrieval | simple relational + vector foundation |
| DuckDB | Parquet/JSON/CSV processing, validation, corpus analysis | lightweight local analytical compute |
| DuckLake | structured release/evaluation history when needed | durable analytical tables without separate warehouse |
| Apache Jena/Fuseki | imported Downstream Oil and Gas Ontology (from EPM), ECE context ontology, RDF provenance, SHACL/SPARQL | formal semantic/constraint layer |
| Neo4j Community | decision/evidence/context graph | efficient operational traversal |
| OpenMetadata | dataset/artifact catalog, ownership, lineage context | catalog control plane |
| Great Expectations | structured synthetic-data and release validation | explicit quality execution |
| OpenLineage | generation/retrieval pipeline run lineage | portable execution lineage |
| Dagster OSS | canonical truth → artifacts → graph → evaluation → release orchestration | asset-oriented build flow |
| Grafana OSS | generation/evaluation pipeline operational health | optional technical monitoring |
| Langfuse | retrieval/agent trace evaluation | useful for evaluation consumers, not core agency |
| MLflow | model/evaluation experiment tracking where models are used | optional; only when ECE evaluates models |

## 3. Do not inherit PPC-specific infrastructure by default

ECE does not need Twenty, ERPNext, Debezium, Kafka, Superset, OR-Tools, downstream forecasting libraries, or PPC's operational workflow application simply because PPC uses them.

A technology enters ECE only after an ECE requirement justifies it.

## 4. Formal meaning versus operational context

Use the same architectural split proven in PPC:

**Jena/Fuseki** answers: What does Evidence, Claim, Decision, Constraint, Outcome, Provenance, and temporal validity mean?

**Neo4j** answers: Which artifacts support this decision? Which claims depend on which assertions? Which evidence was available at the time? Which outcomes followed?

OpenMetadata catalogs the technical artifacts and datasets. It does not replace claim-level provenance.

## 5. Dagster asset model

ECE's natural asset graph is:

```text
scenario_config
      ↓
semantic_contracts
      ↓
canonical_truth
      ↓
 ┌────┼────────────┐
 ↓    ↓            ↓
structured      documents
records         /artifacts
 └────┬────────────┘
      ↓
provenance_graph
      ↓
retrieval_products
      ↓
development_evaluation
      ↓
release_manifest
```

Hidden evaluation truth is a restricted sibling asset path, not an input available to the evaluated agent.

## 6. DuckDB/DuckLake

DuckDB processes generated Parquet/JSON/CSV, validates releases and analyzes evaluation results.

DuckLake can store structured histories for Scenario, Decision, Artifact, Claim, EvidenceItem, SourceAssertion, EvaluationCase, EvaluationRun and Score when volume/history justify it.

R2 remains the durable object store for native documents, large datasets and hidden truth.

## 7. PostgreSQL/pgvector

Use PostgreSQL for inspectable metadata and retrieval-support tables when a service database is useful. pgvector can hold embeddings for development retrieval. Do not treat vector similarity as evidence authority; retrieved text must resolve to Artifact and SourceAssertion provenance.

## 8. OpenMetadata

Use OpenMetadata for catalog/discovery context around datasets, schemas, pipelines and release products. Keep detailed claim-level provenance in ECE's provenance graph/model.

## 9. Quality and lineage

Great Expectations validates structured outputs and release rules. SHACL validates semantic graph constraints. OpenLineage captures execution lineage. These are complementary.

## 10. Shared implementation principle

PPC and ECE may use the same technologies, containers, helper libraries and deployment patterns, but they should not share one project's data bucket, hidden truth, release namespace or domain-specific configuration.

> **Share platform patterns and reusable code. Keep project truth, semantics, releases and access boundaries separate.**

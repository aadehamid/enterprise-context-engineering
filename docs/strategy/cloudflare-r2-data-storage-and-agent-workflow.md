# Cloudflare R2 Data Storage and Agent Workflow

## Enterprise Context Engineering — Lagos Specialty Chemicals Synthetic Case Study

**Repository:** `aadehamid/enterprise-context-engineering`  
**Fictitious enterprise:** Lagos Specialty Chemicals (LSC)  
**Document status:** Draft for implementation  
**Version:** 0.1.0  
**Date:** 2026-09-20  

**Related documents:**

- `README.md`
- `docs/strategy/synthetic-data-generation-strategy.md`
- `docs/discovery/knowledge-source-inventory.md`
- `schemas/dataset-manifest.schema.json`
- `schemas/artifact-manifest.schema.json`
- `schemas/decision-dossier.schema.json`

---

## 1. Purpose

This document defines how the Enterprise Context Engineering project uses **Cloudflare R2** as the durable object store for large synthetic datasets, generated enterprise artifacts, knowledge-graph exports, retrieval indexes, evaluation assets, and data-generation manifests.

The project builds a fictional but internally consistent Lagos Specialty Chemicals (LSC) knowledge environment. Its purpose is to test whether people and AI agents can investigate past-looking commercial, planning, operations, reliability, and CI decisions from fragmented evidence while identifying direct evidence, inference, conflict, and uncertainty.

The project must follow this storage rule:

```text
Cloudflare R2 = durable store for large, shared, generated, and release-scoped project data
Local disk     = temporary scratch space for generation, processing, validation, and upload
GitHub         = code, documentation, semantic assets, schemas, mappings, tests, and small golden fixtures
```

R2 is the system of record for durable generated data and release artifacts. GitHub is **not** the warehouse. Large Parquet data, native PDF/DOCX/PPTX artifacts, email bundles, graph exports, retrieval indexes, generated source records, and hidden evaluation truth must not be committed to the repository.

---

## 2. Scope

R2 stores durable data produced or used by the Enterprise Context Engineering benchmark and demonstration environment:

- Optional approved public/reference inputs, where license and terms permit retention.
- Canonical synthetic LSC enterprise reference data and decision truth.
- Structured source-system-style records: planning, value opportunity, production impact, maintenance, laboratory, finance, and operational/OT summaries.
- Synthetic documents: email threads, meeting notes, Teams transcripts, reports, backcast decks, PowerPoint presentations, decision memoranda, policies, procedures, and outcome reviews.
- Rendered document bundles and their machine-readable artifact manifests.
- RDF, property-graph, CSV, and Parquet graph exports.
- Search, retrieval, and vector-index build artifacts when they are too large or generated for Git.
- Quality exceptions, validation output, reconciliation reports, and performance results.
- Shareable development evaluation artifacts and access-restricted hidden evaluation truth.
- Dataset manifests, checksums, release metadata, and run/release notes.

R2 does **not** replace GitHub for:

- Source code, pipeline definitions, and infrastructure templates.
- Markdown documentation.
- Ontologies, taxonomies, SHACL shapes, schemas, mapping definitions, scenario configuration, and tests.
- Small, intentionally versioned fixtures and golden examples.
- `.env.example` variable names without secrets.

---

## 3. Core storage principles

### 3.1 One bucket per project

Use **one Cloudflare R2 bucket for this project only**. Do not use an R2 bucket assigned to another initiative, and do not store an unrelated project inside this bucket.

The bucket name must be confirmed before the first write. A recommended name is:

```text
enterprise-context-engineering
```

If an organization-wide naming convention requires a prefix or suffix, use a clear project-specific equivalent, for example:

```text
lsc-enterprise-context-engineering
```

The actual bucket name is an environment/configuration value. Do not hard-code it into committed application code. Do not create multiple buckets for the same project unless an explicit security, region, retention, or organizational requirement justifies it.

### 3.2 Durable data belongs in R2

| Asset | Primary location | Reason |
|---|---|---|
| Generator code, documentation, ontology, taxonomy, mappings, schemas, scenario configuration, tests | GitHub | Small, version-controlled, code-reviewable assets |
| Small approved sample fixtures and golden test cases | GitHub | Fast test execution and code review |
| Large synthetic structured data | R2 `cache/structured/` | Durable, shareable, unsuitable for Git history |
| Canonical synthetic enterprise truth | R2 `cache/canonical/` | Controlled truth layer for generation and evaluation |
| Synthetic native documents and render bundles | R2 `cache/documents/` | Large, generated artifacts with source manifests |
| Knowledge-graph exports | R2 `cache/graph/` | Durable graph interchange and provenance products |
| Search/retrieval build artifacts | R2 `cache/indexes/` | Generated data, often large and rebuildable |
| Quality, validation, reconciliation, and performance results | R2 `cache/quality/` | Durable evidence of release quality |
| Development evaluation data | R2 `evaluation/development/` | Shareable benchmark and development assets |
| Hidden evaluation truth | R2 `evaluation/hidden/` | Must not leak into model training or standard retrieval |
| Human-readable run notes and release summaries | R2 `notes/` and GitHub docs | Data-adjacent release notes remain durable; durable policy docs remain in Git |

### 3.3 Local disk is scratch only

A generation, indexing, graph-build, or evaluation job should:

1. Confirm the project bucket and target prefix.
2. Download or stream only the objects required for the job.
3. Process data in a temporary local work area or approved compute workspace.
4. Validate contracts, schemas, semantics, temporal rules, evidence links, quality rules, and manifests.
5. Upload durable outputs to a new versioned R2 prefix.
6. Verify the uploaded objects by size, checksum, schema, and expected counts.
7. Remove local downloads and intermediates when the job completes.

Do not depend on a laptop, a one-time notebook runtime, or chat attachment storage as the durable location for generated project data.

### 3.4 Never place credentials in code or chat

R2 Access Key ID and Secret Access Key must be obtained from an approved secret manager, connector secret, CI secret store, or protected local environment file that is excluded from Git.

Never:

- Paste access keys or secret keys into chat, Markdown, notebooks, source code, commits, logs, issues, or datasets.
- Commit `.env` files containing credentials.
- Print environment variables or boto3 client configuration that contains credentials.
- Store credentials inside R2 objects.
- Put secrets in document templates, synthetic email content, or test fixtures.

---

## 4. R2 connection standard

Use an S3-compatible Cloudflare R2 connection through `boto3`.

| Field | Standard |
|---|---|
| Account ID | Supplied through protected environment/configuration; do not commit if organizational policy treats it as sensitive |
| Endpoint | `https://<CLOUDFLARE_ACCOUNT_ID>.r2.cloudflarestorage.com` |
| Region | `auto` |
| Signature version | `s3v4` |
| Client library | `boto3` using the S3 API |
| Bucket | `ECE_R2_BUCKET` environment variable |
| Access Key ID | `R2_ACCESS_KEY_ID` from protected secret storage |
| Secret Access Key | `R2_SECRET_ACCESS_KEY` from protected secret storage |

### 4.1 Python connection example

```python
import os

import boto3
from botocore.config import Config

ACCOUNT_ID = os.environ["CLOUDFLARE_ACCOUNT_ID"]
BUCKET = os.environ["ECE_R2_BUCKET"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY_ID"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_ACCESS_KEY"]

client = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(signature_version="s3v4"),
)
```

Use a project-local `.env.example` for variable names only:

```bash
CLOUDFLARE_ACCOUNT_ID=
ECE_R2_BUCKET=enterprise-context-engineering
R2_ACCESS_KEY_ID=
R2_SECRET_ACCESS_KEY=

# Optional local services and model settings
NEO4J_URI=
NEO4J_USERNAME=
NEO4J_PASSWORD=
LLM_PROVIDER=
LLM_MODEL=
LLM_API_KEY=
```

Add `.env` and `.env.*` to `.gitignore` while allowing `.env.example` to be committed.

### 4.2 Connectivity check

Before writing data, verify the expected bucket and a safe prefix with a read-only listing where possible:

```python
response = client.list_objects_v2(Bucket=BUCKET, Prefix="notes/")
for obj in response.get("Contents", []):
    print(obj["Key"], obj["Size"])
```

If a write probe is necessary, write only a tiny object under `_probe/` or `notes/`, verify it, and remove it. Never use a connectivity write probe against `cache/canonical/`, `cache/documents/`, or `evaluation/hidden/`.

---

## 5. Bucket layout

The project uses a stable prefix tree inside its dedicated R2 bucket.

```text
enterprise-context-engineering/
├── raw/                                      # Immutable approved inputs and source snapshots
│   ├── public/                               # Public/open inputs retained under approved terms
│   ├── approved-reference/                   # Curated reference inputs permitted for use
│   └── manifests/                            # Source manifests, licenses, checksums
│
├── cache/                                    # Durable generated and processed project data
│   ├── canonical/                            # Canonical synthetic enterprise truth; controlled access
│   │   └── scenario=lsc-ci-v1/
│   │       └── release=<release>/
│   ├── structured/                           # Synthetic structured system records
│   │   ├── planning/                         # LP plans, model readouts, regional economics
│   │   ├── value-opportunity/                # Opportunity and value-add tracker records
│   │   ├── production-impact/                # Production-impact log records
│   │   ├── maintenance/                      # Work orders, condition observations, approvals
│   │   ├── laboratory/                       # Quality and laboratory result summaries
│   │   ├── finance/                          # Financial/economic support data where modeled
│   │   └── ot-summary/                       # Historian, alarm, event, and operating-context summaries
│   ├── documents/                            # Synthetic native/unstructured evidence artifacts
│   │   ├── emails/
│   │   ├── meeting-notes/
│   │   ├── transcripts/
│   │   ├── reports/
│   │   ├── presentations/
│   │   ├── memoranda/
│   │   ├── policies-and-procedures/
│   │   └── outcome-reviews/
│   ├── graph/                                # Knowledge graph and provenance exports
│   │   ├── rdf/
│   │   ├── property-graph/
│   │   ├── csv-import/
│   │   └── provenance/
│   ├── indexes/                              # Generated retrieval/search index artifacts
│   │   ├── document/
│   │   ├── vector/
│   │   └── graph/
│   ├── quality/                              # Validation findings, exceptions, profiling, test reports
│   ├── reconciliation/                       # Control totals and relationship/data reconciliations
│   ├── performance/                          # Generation, indexing, and retrieval benchmark outputs
│   └── manifests/                            # Dataset, artifact, scenario, and release manifests
│
├── exports/                                  # Curated deliverables for tools and demonstrations
│   ├── benchmark-releases/                   # Approved versioned benchmark packages
│   ├── graph-exports/                        # Consumable graph interchange packages
│   ├── demo-packages/                        # Demonstration-ready data/artifact bundles
│   └── analytics/                            # Curated extracts for BI/semantic consumers
│
├── evaluation/                               # Evaluation artifacts; strict separation by access/purpose
│   ├── development/                          # Shareable development questions and labels
│   ├── validation/                           # Controlled validation assets
│   └── hidden/                               # Held-out truth; never expose to tuning or standard retrieval
│
├── notes/                                    # Small human-readable data-adjacent notes
│   ├── source-notes/
│   ├── generation-runs/
│   └── release-notes/
│
└── _probe/                                   # Tiny disposable connectivity probes only
```

### 5.1 Prefix responsibilities

| Prefix | Purpose | Write policy |
|---|---|---|
| `raw/` | Original approved inputs and immutable snapshots | Append new versioned objects; do not silently overwrite |
| `cache/canonical/` | Hidden or controlled canonical enterprise scenario truth and decision ledger | Restricted write/read; versioned generation only |
| `cache/structured/` | Generated system-style structured records | Write only via versioned generation runs |
| `cache/documents/` | Generated native evidence artifacts and their manifests | Write only via versioned artifact-generation runs |
| `cache/graph/` | Semantic, graph, and provenance exports | Write after schema and provenance validation |
| `cache/indexes/` | Generated retrieval index material | Rebuildable; version with the scenario/release/index configuration |
| `cache/quality/` | Validation output and exceptions | Append per release/run; never overwrite silently |
| `exports/` | Deliberately consumable approved outputs | Write after release checks and approval |
| `evaluation/development/` | Development evaluation questions and non-sensitive labels | Versioned write allowed |
| `evaluation/hidden/` | Held-out gold truth, citation sets, outcomes, and score keys | Restricted read/write; never use for training or retrieval tuning |
| `notes/` | Human-readable run and release notes | Versioned write allowed |
| `_probe/` | Connectivity probes | Disposable only; clean up after use |

---

## 6. Object naming and versioning

### 6.1 Required dimensions in object keys or metadata

Where applicable, include the following:

- Scenario ID and scenario version.
- Release or run ID.
- Synthetic enterprise domain and source profile.
- Region, site, business unit, or process scope.
- Source-system-style profile or artifact type.
- Schema version.
- Generator version and seed.
- Decision ID or artifact ID where the object is decision-specific.
- Effective date/time or period for time-partitioned data.
- Classification: `synthetic`, `development`, `validation`, or `hidden`.

### 6.2 Recommended object-key examples

```text
raw/public/reference-data/source_version=2026-09-20/unit-conversion.csv
raw/manifests/source=public-reference/source-manifest.json

cache/canonical/scenario=lsc-ci-v1/release=0.1.0/domain=decision-ledger/data.parquet
cache/canonical/scenario=lsc-ci-v1/release=0.1.0/domain=enterprise-reference/organizations.parquet

cache/structured/planning/scenario=lsc-ci-v1/release=0.1.0/region=south/period=2017-09/lp-model-readout.parquet
cache/structured/value-opportunity/scenario=lsc-ci-v1/release=0.1.0/region=west/value-opportunity-tracker.parquet
cache/structured/production-impact/scenario=lsc-ci-v1/release=0.1.0/decision_id=DEC-2017-00841/pir.json
cache/structured/ot-summary/scenario=lsc-ci-v1/release=0.1.0/asset=C-301/window=2017-09-13T00-2017-09-14T12/summary.parquet

cache/documents/emails/scenario=lsc-ci-v1/release=0.1.0/decision_id=DEC-2017-00841/ART-EMAIL-2017-00921.eml
cache/documents/presentations/scenario=lsc-ci-v1/release=0.1.0/decision_id=DEC-2017-00841/ART-DECK-2017-00314.pptx
cache/documents/reports/scenario=lsc-ci-v1/release=0.1.0/region=south/period=2017-09/lp-backcast-report.pdf
cache/documents/meeting-notes/scenario=lsc-ci-v1/release=0.1.0/decision_id=DEC-2017-00841/ART-MIN-2017-00917.docx

cache/graph/rdf/scenario=lsc-ci-v1/release=0.1.0/provenance.ttl
cache/graph/property-graph/scenario=lsc-ci-v1/release=0.1.0/nodes.parquet
cache/graph/property-graph/scenario=lsc-ci-v1/release=0.1.0/relationships.parquet

cache/indexes/vector/scenario=lsc-ci-v1/release=0.1.0/embedding_model=<model>/index-manifest.json
cache/quality/scenario=lsc-ci-v1/release=0.1.0/validation-report.json
cache/reconciliation/scenario=lsc-ci-v1/release=0.1.0/control-totals.json
cache/manifests/scenario=lsc-ci-v1/release=0.1.0/dataset-manifest.json

exports/benchmark-releases/lsc-ci-v1-release-0.1.0.zip
notes/release-notes/scenario=lsc-ci-v1/release=0.1.0.md
```

### 6.3 Immutability rule

Do not silently overwrite a successful released dataset or artifact bundle. Use a new `release=<version>` or `run_id=<identifier>` prefix.

If a release must be regenerated because of a defect:

1. Create a new run or release prefix.
2. Record the reason, changed generator/scenario/template version, seed, and migration implications in `notes/`.
3. Update the GitHub release reference or manifest pointer only after validation.
4. Keep the prior release for reproducibility unless retention policy requires deletion.

---

## 7. Data lifecycle workflow

### 7.1 Standard workflow

```text
1. Confirm the dedicated Enterprise Context Engineering bucket and target prefix.
2. Load R2 secrets from approved secret storage or a protected local environment.
3. Read only the required objects from R2.
4. Download or stream inputs to temporary local scratch storage.
5. Generate canonical truth, structured source-style records, documents, graph exports, and evaluation assets.
6. Validate schemas, semantic constraints, temporal rules, provenance, quality, and reconciliation.
7. Write outputs to a new versioned R2 prefix.
8. Write manifests, checksums, run notes, and validation evidence.
9. Verify uploaded objects using size, checksum, schema, and expected-count checks.
10. Clean local scratch files and intermediates.
```

### 7.2 Canonical truth generation

For every scenario generation run:

1. Retrieve scenario configuration, ontology/taxonomy version, reference data, templates, and constraints from GitHub/R2.
2. Generate canonical LSC reference entities, events, decisions, options, constraints, outcomes, and expected evidence relationships from a declared seed.
3. Validate identity, relationship, temporal, and scenario constraints.
4. Write controlled canonical outputs to `cache/canonical/`.
5. Generate a manifest with scenario version, seed, generator version, schema versions, object keys, and checksums.

The canonical decision ledger is not a normal retrieval source for an evaluation agent. It is the hidden truth layer used to generate artifacts and measure answer quality.

### 7.3 Structured source-record generation

Generate source-system-style artifacts from canonical truth:

- LP production-plan model readouts and regional economics packs.
- Distribution and specialty-blending planning/actuals summaries.
- Value Opportunity Tracker and Commercial Value Add Tracker records.
- Production Impact Log records.
- Maintenance/work-order, laboratory, finance, and OT-summary records where the scenario requires them.

Each output must retain stable entity IDs, source-profile metadata, period/effective-time metadata, scenario/release metadata, and a source manifest.

### 7.4 Document and artifact generation

Generate distributed evidence artifacts from controlled slices of canonical context:

- emails;
- meeting notes and transcripts;
- PDF/DOCX reports and decision memoranda;
- PowerPoint backcast and review decks;
- policies/procedures;
- outcome reports.

The generator must not place complete hidden truth into every document. Each document should contain the partial, role-specific information that would plausibly be available in that source.

Every rendered artifact must have a machine-readable artifact manifest that records IDs, source system/profile, author role, timestamps, related decision IDs, entities, scenario/release, template/generator version, seed, file hash, and source assertions.

### 7.5 Graph and retrieval-product generation

Build graph and retrieval products from canonical and artifact metadata:

- provenance RDF/TTL, JSON-LD, or property-graph exports;
- document metadata and source assertions;
- graph nodes/relationships for decisions, evidence, artifacts, entities, constraints, options, outcomes, and time;
- document and vector index source bundles.

Do not treat a retrieval index as the sole durable representation of evidence. Keep the original generated artifact, manifest, and graph/provenance export separately.

### 7.6 Evaluation publication

Before publishing development evaluation assets:

- Confirm that no hidden canonical truth, answer key, or restricted outcome data is included.
- Confirm every development artifact has synthetic classification.
- Store shareable question sets, evidence references, rubrics, and examples under `evaluation/development/`.
- Store held-out gold truth, expected evidence sets, hidden outcomes, and scoring keys under `evaluation/hidden/` with restricted access.

### 7.7 Local cleanup

After successful validation and upload:

- Delete downloaded raw files, generated intermediates, temporary render files, local Parquet fragments, and local document bundles from scratch storage.
- Retain local data only when explicitly part of an approved developer cache or controlled service volume.
- Do not delete durable R2 objects merely because local processing completed.

---

## 8. Manifests, provenance, and integrity controls

### 8.1 Required dataset release manifest

Every dataset release should include a machine-readable manifest similar to the following:

```json
{
  "project": "enterprise-context-engineering",
  "fictitious_enterprise": "Lagos Specialty Chemicals",
  "release": "0.1.0",
  "run_id": "ece-gen-20260920-001",
  "generated_at": "2026-09-20T00:00:00Z",
  "synthetic": true,
  "classification": "synthetic",
  "scenario": {
    "name": "lsc-ci-v1",
    "version": "1.0.0",
    "seed": 20260920,
    "scale_profile": "pilot"
  },
  "generator": {
    "repository": "aadehamid/enterprise-context-engineering",
    "git_commit": "<commit-sha>",
    "generator_version": "0.1.0"
  },
  "storage": {
    "bucket": "<ECE_R2_BUCKET>",
    "canonical_prefix": "cache/canonical/scenario=lsc-ci-v1/release=0.1.0/",
    "structured_prefix": "cache/structured/",
    "documents_prefix": "cache/documents/",
    "graph_prefix": "cache/graph/"
  },
  "artifacts": [
    {
      "key": "cache/structured/planning/scenario=lsc-ci-v1/release=0.1.0/region=south/period=2017-09/lp-model-readout.parquet",
      "classification": "synthetic",
      "artifact_type": "structured_planning_record",
      "schema_version": "1.0.0",
      "row_count": 1000,
      "sha256": "<hash>"
    }
  ],
  "validation": {
    "schema_status": "passed",
    "semantic_status": "passed",
    "temporal_validation_status": "passed",
    "provenance_validation_status": "passed",
    "reconciliation_status": "passed",
    "quality_rule_set": "quality-v1"
  },
  "restrictions": [
    "All content is synthetic and not a record of actual events.",
    "No real personal or confidential company data.",
    "Do not use for live operational, safety, legal, financial, accounting, regulatory, or engineering decisions.",
    "Hidden evaluation truth is excluded from development/tuning artifacts."
  ]
}
```

### 8.2 Required artifact manifest fields

Each rendered document, email, report, deck, transcript, or structured source artifact should retain at least:

- Artifact ID and file/object key.
- Scenario ID/version, release ID, generation run ID, seed, and generator/template version.
- Synthetic classification.
- Artifact type and source-system-style profile.
- Author/owner role and participant roles where applicable.
- Authored timestamp, effective interval, and ingestion/generation timestamp.
- Related decision IDs, asset/entity IDs, process/capability IDs, and region/site IDs.
- Content hash and native file format.
- Source assertions with locators such as page, slide, message ID, paragraph, field name, tag/time window, or meeting agenda item.

### 8.3 Checksums

Record SHA-256 checksums for release artifacts. The manifest itself should also be checksummed and retained in R2 and, when sufficiently small, in GitHub.

### 8.4 Source-to-answer provenance

A user-facing answer should be traceable through this path:

```text
Answer claim
  -> cited source assertion
  -> artifact/document/record and precise locator
  -> related decision, observation, constraint, option, or outcome
  -> scenario and source-system-style profile
  -> generator scenario, seed, template/model version, and release manifest
```

For evaluation, the hidden truth adds a separate path:

```text
Agent answer
  -> cited evidence available to agent
  -> hidden gold truth / decision ledger
  -> evaluation rubric and score record
```

The canonical ledger must remain outside the agent’s normal retrieval corpus during blind tests.

---

## 9. Development, evaluation, and access separation

### 9.1 Development artifacts

`evaluation/development/` may contain:

- Public/shareable synthetic source profiles.
- Small sample datasets and documents.
- Ontology, taxonomy, mappings, schemas, and provenance examples.
- Development questions and non-sensitive labels.
- Controlled examples of ambiguity, conflicting evidence, and incomplete records.
- Quality-rule definitions and controlled defect examples.

### 9.2 Hidden evaluation truth

`evaluation/hidden/` and, where appropriate, restricted sections of `cache/canonical/` contain information that must not be exposed to model training, prompt tuning, generic development retrieval, or unrestricted collaborators:

- Canonical decision rationale.
- Held-out decision IDs and expected outcomes.
- Gold evidence sets and citation locators.
- Expected alternatives, constraints, and causal interpretations.
- Ground-truth contradiction/uncertainty labels.
- Scoring keys and hidden rubric annotations.

Use separate R2 tokens or scoped access policies if multiple contributors, CI jobs, or agents access the bucket.

### 9.3 Public-release policy

Before publishing a benchmark release outside the project:

1. Confirm source/license terms for any retained reference inputs.
2. Remove hidden truth, secrets, internal metadata, and restricted configurations.
3. Verify that all content is visibly marked synthetic.
4. Publish only approved small fixtures in GitHub; distribute larger approved data through R2 or a controlled release mechanism.
5. Include license, attribution where needed, manifest, synthetic-data disclaimer, and reproducibility instructions.

---

## 10. R2 workflow examples

### 10.1 Download a document artifact for validation

```python
from pathlib import Path

local_path = Path("/tmp/lsc-lp-backcast-report.pdf")
key = (
    "cache/documents/reports/scenario=lsc-ci-v1/"
    "release=0.1.0/region=south/period=2017-09/lp-backcast-report.pdf"
)

client.download_file(BUCKET, key, str(local_path))

# Validate/render/extract locally here.
# Delete the local copy after successful completion.
local_path.unlink(missing_ok=True)
```

### 10.2 Upload a generated artifact and manifest

```python
from pathlib import Path

artifact_path = Path("/tmp/ART-DECK-2017-00314.pptx")
manifest_path = Path("/tmp/ART-DECK-2017-00314.manifest.json")
base_key = (
    "cache/documents/presentations/scenario=lsc-ci-v1/"
    "release=0.1.0/decision_id=DEC-2017-00841/"
)

client.upload_file(str(artifact_path), BUCKET, f"{base_key}{artifact_path.name}")
client.upload_file(str(manifest_path), BUCKET, f"{base_key}{manifest_path.name}")
```

### 10.3 Upload a release manifest and note

```python
client.upload_file(
    "/tmp/dataset-manifest.json",
    BUCKET,
    "cache/manifests/scenario=lsc-ci-v1/release=0.1.0/dataset-manifest.json",
)

client.upload_file(
    "/tmp/release-0.1.0.md",
    BUCKET,
    "notes/release-notes/scenario=lsc-ci-v1/release=0.1.0.md",
)
```

### 10.4 Avoid bulk download

Do not download every object under `cache/` or `evaluation/` by default. List the relevant prefix and retrieve only required artifacts or partitions.

```python
response = client.list_objects_v2(
    Bucket=BUCKET,
    Prefix=(
        "cache/structured/value-opportunity/"
        "scenario=lsc-ci-v1/release=0.1.0/region=south/"
    ),
)

for obj in response.get("Contents", []):
    print(obj["Key"], obj["Size"])
```

---

## 11. Integration with repository workflows

### 11.1 GitHub responsibilities

GitHub should contain:

- Generator code that reads/writes R2 through environment variables and `boto3`.
- Scenario YAML/JSON, profile configuration, data contracts, templates, ontology, taxonomy, SHACL shapes, mappings, schemas, and tests.
- `.env.example` with variable names only.
- Small sample fixtures, golden test cases, and non-sensitive development examples.
- R2 key conventions, manifest specifications, and reproducibility documentation.
- Documentation describing the distinction between synthetic artifacts, canonical truth, and hidden evaluation truth.

### 11.2 R2 responsibilities

R2 should contain:

- Large synthetic structured datasets and document artifacts.
- Canonical truth releases and controlled decision-ledger outputs.
- Source-style planning, tracker, operational, and impact records.
- Native presentation, report, memo, email, transcript, and note bundles.
- Graph/provenance exports and rebuildable retrieval indexes.
- Quality, validation, reconciliation, performance, and release outputs.
- Restricted hidden evaluation truth.

### 11.3 CI/CD and agent access

When a CI pipeline or agent requires R2 access:

- Inject `CLOUDFLARE_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, and `ECE_R2_BUCKET` via secure repository/environment secrets.
- Apply least-privilege R2 tokens where available.
- Do not echo secrets in logs.
- Use read-only credentials for validation-only jobs where possible.
- Use a dedicated write-capable token only for generation/release jobs.
- Make writes release-scoped and append-only by default.
- Do not grant ordinary retrieval agents read access to `evaluation/hidden/` or hidden canonical-truth prefixes.

---

## 12. Retention and cleanup

### 12.1 Retain

Retain the following for each approved benchmark release:

- Scenario configuration, seed, generator/template versions, and referenced ontology/taxonomy/schema versions.
- Canonical truth release under controlled access.
- Structured source-style records and generated document bundle.
- Graph/provenance export and artifact manifests.
- Quality, temporal, semantic, and reconciliation results.
- Dataset manifest, checksums, and release notes.
- Required evaluation assets and score outputs under their appropriate access controls.

### 12.2 Remove or expire

Consider lifecycle/retention rules for:

- Superseded exploratory runs and failed generation outputs.
- Temporary render artifacts that have not been released.
- Rebuildable indexes after a newer validated release exists.
- `_probe/` connectivity objects.
- Obsolete local exports and scratch artifacts.

Do not remove an artifact required to reproduce a published, reviewed, or benchmarked release unless it has been archived under an approved retention approach.

---

## 13. Security and operating rules

### Always do

- Confirm the correct project bucket before reading or writing.
- Use `boto3` with an S3-compatible Cloudflare R2 endpoint and secret-managed credentials.
- Retrieve only the minimum required objects into local scratch storage.
- Write durable outputs to release/version prefixes.
- Validate checksums, schemas, expected counts, semantic constraints, temporal validity, and manifests after upload.
- Label all generated artifacts and manifests as synthetic.
- Keep GitHub limited to code, documentation, semantic assets, schemas, configurations, tests, and small fixtures.
- Separate development from hidden evaluation truth.
- Clean local scratch after successful completion.

### Never do

- Do not store two unrelated projects in one bucket.
- Do not put large generated datasets, document bundles, graph exports, indexes, or hidden truth in Git history.
- Do not store durable generated data only on a laptop, notebook runtime, or chat attachment.
- Do not paste R2 credentials into chat, source code, Markdown, or logs.
- Do not silently overwrite released data.
- Do not run write probes against `cache/canonical/`, `cache/documents/`, or `evaluation/hidden/`.
- Do not expose canonical hidden decision rationale, gold citations, expected outcomes, or hidden score keys to model tuning or standard retrieval.
- Do not present synthetic records or artifacts as real LSC history.

---

## 14. Immediate implementation checklist

- [ ] Confirm the dedicated R2 bucket name for Enterprise Context Engineering.
- [ ] Create the bucket if it does not exist, following the one-project-per-bucket rule.
- [ ] Create the stable prefix tree: `raw/`, `cache/`, `exports/`, `evaluation/`, `notes/`, and `_probe/`.
- [ ] Add `boto3` and `botocore` to project dependencies.
- [ ] Add `.env.example` with `CLOUDFLARE_ACCOUNT_ID`, `ECE_R2_BUCKET`, `R2_ACCESS_KEY_ID`, and `R2_SECRET_ACCESS_KEY` variable names only.
- [ ] Update `.gitignore` to exclude `.env`, large generated data, local indexes, rendered artifacts, local databases, and hidden evaluation outputs.
- [ ] Implement `scripts/r2_client.py` as a shared R2 client factory.
- [ ] Implement dataset and artifact manifest creation with SHA-256 checksum validation.
- [ ] Implement distinct access/configuration paths for development and hidden evaluation data.
- [ ] Generate a small pilot LSC CI scenario with a canonical decision ledger, structured records, distributed artifacts, and manifests.
- [ ] Upload the pilot to a versioned release prefix.
- [ ] Verify that graph/provenance exports trace claims to artifacts and artifacts to generation/run metadata.
- [ ] Verify that an evaluation agent cannot retrieve hidden truth during a blind test.

---

## 15. Summary

Cloudflare R2 is the durable object-store layer for the Enterprise Context Engineering project’s synthetic LSC decision-provenance corpus. It stores the large, generated, versioned evidence environment that GitHub should not: structured records, native documents, graph exports, indexes, validation outputs, manifests, and restricted hidden evaluation truth.

The operating model is:

```text
GitHub: semantic model, schemas, scenarios, generator code, documentation, tests, small fixtures
R2:     versioned synthetic data, artifact bundles, graph exports, indexes, manifests, hidden evaluation truth
Local:  temporary scratch used for generation, validation, and controlled upload/download
```

Following this separation supports reproducibility, provenance, controlled access, scalable generation, and credible evaluation of the project’s central capability: explaining historical-looking enterprise decisions from distributed evidence without exposing the synthetic truth layer to the system being evaluated.

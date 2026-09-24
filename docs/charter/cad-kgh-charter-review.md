# CAD-KGH Charter v3 — Import Review

**Reviewed:** 2026-09-24  
**Source:** `docs/charter/cad-kgh-project-charter.md` (v3.0)  
**Verdict:** Ship as the workstream charter. Source-first vs Path B is the real bet. Fix the integration nits below before M0 compose lands.

This is a review of the imported charter against this repository, not a rewrite of v3.

---

## What holds

- **H1–H4 are testable.** Ground-truth generator + Path B baseline + per-source scorecards is the right experimental design. Without Path B you cannot claim source-first is better; without a true-model generator you cannot score it.
- **Two different simulators is the actual problem.** Abstract plant-item + representation (Sim 1) vs single-ID inheritance + DWG handle join (Sim 2) is what real multi-authoring integration looks like. A single “clean” schema would have been a toy.
- **Data policy matches the repo.** Synthetic LSC, approximations not vendor schemas, no client/employer data. Same contract as the anonymization sweep and the synthetic-data strategy.
- **Evergreen via revision diff, not full reload.** Matches ECE’s time-aware / provenance principles (`ChangeEvent`, `valid_from` / `valid_to`, source lineage on every node).
- **Copyleft is named.** pyDEXPI (AGPL-3.0), Neo4j CE (GPL-3.0), LibreDWG (GPL-3.0) are on the critical path and already in the risk table.

---

## Must resolve before M0

### 1. This is not a `cad-kgh/` product repo

§11 describes a standalone tree. This repository is `enterprise-context-engineering` and already has a docs-centric layout plus a proposed `generators/` / `schemas/` / `evaluations/` tree. CAD-KGH implementation packages should land **inside this repo** (or as a clearly linked package), not as a second product identity.

`LSC-A` / `LSC-B` are authoring-system sites. They must not collide with North / South / West commercial regions in the knowledge-source inventory.

### 2. No interface to the ECE context layer

CAD-KGH produces topology + lineage. ECE needs claim-level evidence, decisions, and uncertainty. The charter never says how a `:PipingNetworkSegment` / `:ChangeEvent` / `:SourceRecord` becomes an ECE evidence item that a decision dossier can cite.

Need a one-page contract before M5 load: node/edge → evidence item, drawing_ref → artifact locator, `ChangeEvent` → decision-adjacent event, and what is **not** asserted (no safety, isolation, or MOC authority).

### 3. License isolation is under-rated

Risk table says copyleft is Low/Low. pyDEXPI is AGPL and sits on the DEXPI exchange path (M5). Neo4j CE is GPL. LibreDWG is GPL and optional but easy to pull into the image.

M1 ADRs must pick: (a) process-isolate AGPL/GPL, (b) default graph store = Neo4j CE **or** Apache AGE, not both in M0 compose, (c) DXF-only until LibreDWG is justified, (d) project license for *this* repo.

### 4. M0–M9 is three projects

Generator + two simulators + mapping + DEXPI + Path B + evergreen + API/UI + optional Graph-RAG is a 12-milestone stack for a personal learning project. Graph-RAG in M8 is optional and should stay out of the critical path. Dual graph stores in M0 should not.

Sequence that actually tests the hypotheses: M2 Sim 1 → M4 extractor/mapping → M5 load → score H1/H3. Then M3/M4 Sim 2 for H2. Path B and evergreen after that. Consumption demos last.

---

## Should fix in the next charter pass

| Item | Why |
|---|---|
| Mapping YAML embeds SQL (`where: "component_subclass_id IN (SELECT ...)"`) | Coverage checker cannot validate this as a declarative mapping. Keep SQL in extractors; keep YAML as class/property/codelist maps. |
| Sim 2 `HandValves` mapping omits `key: PnPID` | Inconsistent with `CentrifugalPump`. Easy to copy-paste into a broken mapper. |
| Success metrics are generator-relative | ≥99.5% / 100% / 0-loss is achievable because you score against the thing you generated. Say that in the table header, not only the footnote. Otherwise it reads as an industry claim. |
| H5 (license audit) has no metric row | Add a CI license scan deliverable to M0 / M9. |
| Gephi listed as “CDDL-GPL” | Gephi is GPL-3.0. Drop Gephi from the default stack; Cytoscape.js is enough. |
| Isolation Cypher mixes `CONNECTS_TO` and `LOCATED_ON` | Fine as a demo, not as an acceptance query. Write a path grammar in M8 or the eval harness will game it. |
| No project license | THIRD_PARTY_LICENSES.md is listed; the repo license is not. |

---

## Fit to ECE principles

| ECE principle | CAD-KGH |
|---|---|
| Evidence before fluency | Source-first + Path B baseline. Good. |
| Claim-level provenance | `:DERIVED_FROM` → `:SourceRecord` is row-level, not claim-level. Enough for topology; not enough for ECE Q&A. |
| Time-aware context | Revision snapshots + `valid_from` / `valid_to`. Good. |
| Evidence / inference / unknown | `:MappingException` + confidence on nodes. Need an explicit “unreconciled ≠ absent” rule for Sim 2 drift. |
| Synthetic by design | Yes. Keep generator seed / manifest on every release. |
| Separate truth from retrieval | Ground-truth graph is eval-only. Do not load it into the explorer. |
| Governance by construction | Missing. Isolation finder must be labeled a demo, not an operational boundary. |

---

## Open questions

1. Does CAD-KGH feed the synthetic decision-provenance corpus (isolation, MOC, spec-break decisions), or is it a parallel graph?
2. One Neo4j database with `site` / `source_system` properties, or two named graphs / databases?
3. Is Path B a published baseline or an internal ablation? Changes how honest the DXF has to look.
4. Who owns unmapped pick-list values — fail the load, or land as `:MappingException` and continue?
5. Week targets in §8 are sequence markers, not a calendar. Keep them that way.

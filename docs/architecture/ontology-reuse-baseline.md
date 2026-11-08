# Ontology reuse baseline — Enterprise Context Engineering

**Status:** Proposed (survey result, 2026-11-08; not a recorded decision)
**Purpose:** Propose the publicly available ontologies ECE would import or borrow patterns from when the semantic layer is constructed, so the import set is proposed once and confirmed by review before construction starts. Until the owner records approval, every set below is a candidate, not a dependency.
**Related:** [Shared Technical Foundation](shared-technical-foundation.md) section 11 fixes the *formats* (SKOS, RDF-star, SHACL, SSSOM); this document proposes the *public vocabularies* underneath those formats. Charter section 7, item 3 leaves the EPM Downstream Oil and Gas Ontology import as an open decision; the oil-and-gas section below feeds that decision.

Method: a web survey on 2026-11-08 of candidate ontologies across ten coverage areas (upper structure, provenance, time, data products and units, industrial/OT, events, organization, decisions, downstream oil and gas, documents). Licenses and activity dates were read from the GitHub API, W3C TR pages and the ETSI portal on that date, not from search snippets, except where marked. Re-verify each entry before an actual import; activity dates below say "pushed" as of 2026-11-08.

## 1. Proposed to adopt (core import set)

| Ontology | ECE layer | License | Maturity | Use in ECE |
|---|---|---|---|---|
| [PROV-O](https://www.w3.org/TR/prov-o/) (W3C TR, verified) | provenance, governance | W3C license | W3C Recommendation, 2013 | Claim-level provenance backbone: entities, activities, agents, derivation. |
| [OWL-Time](https://www.w3.org/TR/owl-time/) (W3C TR, verified) | provenance, semantic | W3C license | W3C Recommendation, 2017 | Authoring time, decision time, effective-period semantics in the graph. |
| [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) (W3C TR, verified) | semantic, governance | W3C license | W3C Recommendation, 2024 | Release catalogs: datasets, distributions, manifests. |
| [SKOS](https://www.w3.org/TR/skos-reference/) | semantic | W3C license | W3C Recommendation, 2009 | Taxonomy and shared vocabulary; already fixed by the format baseline. |
| [QUDT](https://github.com/qudt/qudt-public-repo) | semantic | CC-BY-4.0, plus a third-party UCUM license on the bundled UCUM codes ([LICENSING.md](https://github.com/qudt/qudt-public-repo/blob/main/LICENSING.md)) (GitHub API) | actively maintained (pushed 2026-11-06) | Units, quantities and dimensions for KPIs and engineer data. Published as an all-in-one SHACL distribution, but its user-level rules only check for deprecated instances and properties: ECE must run a SHACL validator explicitly and author its own KPI shapes on top. |
| [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/) (W3C TR, verified) | semantic, provenance | W3C license | W3C Recommendation, 2017 | Sensors and observations: historian windows, alarms, lab data. |
| [ORG](https://www.w3.org/TR/vocab-org/) (W3C TR, verified) | semantic | W3C license | W3C Recommendation, 2014 | Organizations, roles, reporting structures. |
| [ODRL 2.2](https://www.w3.org/TR/odrl-vocab/) (W3C TR, verified) | governance | W3C license | W3C Recommendation, 2018 | Source-classification and access policies on artifacts. |

These eight are light, standard, and license-clean apart from QUDT's third-party UCUM terms, noted above. They carry infrastructure meaning only; none of them speaks about KPIs, decisions, evidence or epistemic status, which is where ECE's own vocabulary sits.

## 2. Proposed to adopt with caveats

| Ontology | Use in ECE | Caveat |
|---|---|---|
| [DPROD](https://github.com/ekgf/dprod) (EKGF/OMG workgroup, since 2024) | RDF/OWL data-product vocabulary for release namespace and contract metadata | Actively maintained (pushed 2026-11-08), but the GitHub license reads `NOASSERTION`. Pin the license from the workgroup's primary source before importing. |
| [IOF Core](https://spec.industrialontologies.org/) (OAGi) | Manufacturing-grade core: measurement, process, resource concepts | MIT license per the OAGi/IOF portal. The GitHub mirror `iofoundry/Core` is archived (read-only since 2022-10); the spec portal is canonical. |
| [BFO](https://github.com/BFO-ontology/BFO) | Top level if ECE follows the IOF route | CC-BY-4.0 (GitHub API), last pushed 2024-01. Choose one upper ontology: BFO (when IOF concepts are wanted) or GIST below — do not import both. |
| [GIST](https://github.com/semanticarts/gist) (Semantic Arts) | Simpler enterprise upper ontology alternative to BFO | CC-BY-4.0 (GitHub API), very active (pushed 2026-11-03). Lighter than BFO; weaker when IOF's manufacturing detail is wanted. |
| CCO ([Common Core Ontologies](https://github.com/CommonCoreOntology/CommonCoreOntologies)) | BFO-dependent core with released artifacts (BSD-3-Clause per the repository API; pushed 2026-10-02; merged CCO-2.2 Turtle published 2026-08-14) | The repository's README plans structural 3.0 and 4.0 changes, so anything built on CCO 2.2 rides a moving target. Weigh against GIST's lighter, stable alternative; re-examine at CCO 3.0 if BFO/GIST both disappoint. |
| [SAREF suite](https://saref.etsi.org/) (ETSI) | Systems, industry and manufacturing extensions behind SAREF4INMA and SAREF4SYST | ETSI publishes the suite free and versioned. `saref.etsi.org/saref4industry/` returned 404 during the survey; confirm the intended extension page before use. |
| [EPCIS 2.0 + CBV](https://www.gs1.org/standards/epcis) (GS1) | Event vocabulary with what/when/where/why/how | Standard is freely available; check whether importing the RDF vocabulary or restating its event shapes is the better fit, since EPCIS is supply-chain oriented. |
| [PREMIS OWL](https://www.loc.gov/standards/premis/ontology/) (Library of Congress) | Documents and records as evidence objects: objects, events, agents | Verified on the LoC page; heavier than PROV-O alone. Borrow its document/record shapes rather than importing wholesale. |

## 3. Borrow patterns only

| Candidate | Why not a dependency |
|---|---|
| [Decision Ontology (DO)](https://github.com/nicholascar/do-ont) | Directly on target for decisions, but last pushed 2018-04 and small (CC-BY-4.0 per GitHub API). Reuse its class shapes (decision, decision-making, options, rationale) as the starting pattern; keep the implementation in ECE's own namespace, where PROV-O can anchor agents and activities. |
| [W3C Decision Incubator model](https://www.w3.org/2005/Incubator/decision/XGR-decision-20120417/Sample_Decision_Ontology.html) (2012) | Superseded; DO above is its continuation. Reference only. |

## 4. Rejected or marginal

| Candidate | Reason |
|---|---|
| [OM (Ontology of units of Measure)](http://www.ontology-of-units-of-measure.org/resource/om-2) | Host unreachable during the survey; QUDT covers the need with better tooling. |
| [ODPS](https://opendataproducts.org/) / [Data Product Specification](https://github.com/agile-lab-dev/Data-Product-Specification) | YAML/JSON specifications, not vocabularies. DPROD is the RDF option for data products. |
| [Accenture OSDU-Ontology](https://github.com/Accenture/OSDU-Ontology) | Apache-2.0, pushed 2024-12, but upstream/subsurface-biased and a single-vendor artifact (38 stars). Reference for source-system alignment, not an import. |
| [OpenEnergy Ontology](https://github.com/OpenEnergyPlatform/ontology) | CC0 and very active, but energy-policy focused; tangential to downstream refining. |
| FaBiO / BIBO | Scholarly-bibliographic focus; PREMIS plus PROV-O cover ECE's document case. |
| DOLCE/UFO/DOL | Evidence too thin during the survey: no well-maintained release artifact surfaced that could be verified directly. Re-examine only if BFO/GIST both disappoint. |

## 5. Keep bespoke

No maintained public ontology surfaced for these ECE needs; each is planned as ECE's own vocabulary:

- **Epistemic status** — direct evidence, inference, contradiction, unknown. A 2025 survey of provenance/assertion/evidence ontologies exists, and nothing adopted-and-maintained surfaced from it.
- **The two axes** — source/data classification and epistemic status tracked separately. This separation is ECE's own design, not a known vocabulary.
- **KPI governance** — owner, calculation meaning, KPI lineage. QUDT and DCAT give units and catalog entries; they do not speak to KPI stewardship.
- **Claim locators** — pinpointing a claim inside a source artifact (slide, page, historian window, query). PROV-O needs ECE-specific refinements here; the W3C Web Annotation model is an unverified follow-up candidate for exactly this shape.
- **Downstream refining vocabulary** — processes, value streams, products, units of the worked example. See section 6.

## 6. Oil and gas: public standards versus the EPM ontology

The public downstream picture is thin, and this is the strongest input for charter section 7, item 3. The process-asset vocabulary is genuinely public: ISO 15926 is an ISO standard, but its ontology artifacts are available free from the [PCA reference data services](https://rds.posccaesar.org/services/downloads/) in Turtle, RDF-XML and JSON-LD, and ISO 15926-14 reconciles 15926 with W3C recommendations. OSDU follows subsurface definitions, and its RDF coverage is a small single-vendor bridge. Neither gives downstream refining, product, or market vocabulary. The working recommendation stands: **import the EPM Downstream Oil and Gas Ontology for domain truth; borrow ISO 15926/PCA vocabulary for asset and equipment structure; treat OSDU as a source-system alignment reference rather than an import.** That decision stays open until recorded under the charter's process.

## 7. Runtime note: RDF inside Neo4j

If the graph is served from Neo4j, [neosemantics (n10s)](https://github.com/neo4j-labs/neosemantics) imports RDF (Apache-2.0, pushed 2026-11-06) and runs SHACL validation in-graph. This is the bridge between the imported vocabularies above and the operational context graph; it is infrastructure, not an ontology.

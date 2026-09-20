# Enterprise Context Engineering

**A synthetic case study**: designing an AI-ready knowledge-management (KM) capability for a
Continuous Improvement (CI) program in a downstream process-industry company —
**Lagos Specialty Chemicals (LSC)**, a fictional specialty chemicals and refining company.

> ⚠️ **Disclaimer**: LSC is fictitious. All company-specific data, inventories, site codes, and
> discovery materials in this repository are synthetic, created to simulate and solve the problem
> end to end. Public industry citations in the research analysis (e.g., CSB incident reports,
> company 10-K filings) are real and retained verbatim, with sources linked.

---

## The problem

LSC runs a Value Chain Optimization (VCO) Continuous Improvement program: monthly backcasts,
lookbacks, post-audits, and recurring CI reporting across three regions. These processes generate
valuable findings — lessons learned, decision rationales, recommendations — but:

- **Knowledge lives in people's heads** — retention depends on individual experience and informal
  follow-up
- **Nothing is captured consistently** — no shared taxonomy, templates, or metadata for lessons,
  decision rationales, or recommendations
- **Nothing is discoverable** — future planners and schedulers make decisions without the benefit
  of prior learning

The result: similar issues recur, institutional knowledge walks out the door with attrition, and
decision quality quietly degrades.

LSC's CI program already has the raw ingredients of a decision-knowledge discipline — a decision
lookback matrix, a maturity-based view of its key decision points, and defined governance modes.
But the knowledge those processes generate spans everything from formal deliverables (backcast
reports, lookback decks, post-audits, recurring CI reports) to informal sources (email summaries,
meeting recordings, working notes, SME know-how) — with no shared taxonomy, no quality tiers, and
no governance tying them together. What's needed is a capability that establishes that taxonomy,
quality model, and governance — plus the technology direction that makes future AI safe to deploy —
while the business keeps ownership of its context and decision logic.

## The solution concept

An end-to-end, AI-ready knowledge architecture — **"AI proposes, humans approve"**:

```
CI sources (LSC Backcast Report Library, regional SharePoint sites, Teams, email,
            OneNote, Power BI, Planning DB / Impact Log)
      │  automated capture — connectors, batch crawl, event triggers
      ▼
INGEST & LAND ──► immutable raw store, lineage on every asset, sensitivity flagged at capture
      │
      ▼
AI CURATION ────► traditional AI (OCR, speech-to-text, classification, dedup)
                  + LLM drafting (template extraction, taxonomy tagging, confidence scoring,
                    embeddings) — everything lands as a DRAFT
      │
      ▼
HUMAN GATE ─────► SME review queue: accept / edit / reject
                  nothing enters the governed store unreviewed
      │
      ▼
GOVERNED PLATFORM ──► knowledge repository · metadata & taxonomy spine (MDM) ·
                      knowledge graph (decisions ↔ lessons ↔ outcomes) ·
                      vector + keyword indexes · quality tiers on every asset
      │
      ▼
CONSUMPTION ────► faceted search · Q&A assistant with citations + confidence badges ·
                  APIs/MCP · subscriptions & alerts
      │
      ▼
DECISIONS ──────► planning & scheduling · backcast & lookback processes · CI leadership reviews
                  (future phase, agentic: proactive lesson surfacing, gap detection)
      │
      └────── feedback loop: usage signals & SME corrections flow back to curation ──────┘
```

Cross-cutting: governance & lifecycle, quality-tier & confidence model, access control for
market-sensitive content, audit & versioning, continuous improvement, monitoring.

## Repository map

| Path | Contents |
|---|---|
| [`CI KM — End-to-End Solution Architecture.pptx`](CI%20KM%20—%20End-to-End%20Solution%20Architecture.pptx) | The full solution architecture, one detailed slide (PowerPoint) |
| [`CI_KM_Architecture/`](CI_KM_Architecture/) | Conceptual architecture (editable `.pptd` source) — ingest → curate → govern → consume |
| [`CI_KM_Solution_Architecture/`](CI_KM_Solution_Architecture/) | The detailed end-to-end architecture (editable `.pptd` source) |
| [`Source_Name_example.txt`](Source_Name_example.txt) | Synthetic CI knowledge-source inventory: 48 sources assessed by type, domain, structure, relevance, validity, ownership, readiness for reuse, and quality tier |
| [`EKM Discovery and Build_V2/`](EKM%20Discovery%20and%20Build_V2/) | Discovery workbooks, requirements-capture user guide, build roadmap, and an HTML prototype |
| [`VCO_CI_KM_Analysis_html/`](VCO_CI_KM_Analysis_html/) | The research foundation: a 12-dimension evidence base on lookbacks, backcasting, RCA, and KM practice in process industries, with full citations — plus the final analysis report (md/docx/html) |
| [`VCO_CI_KM_Analysis.agent.final/`](VCO_CI_KM_Analysis.agent.final/) | Final analysis markdown + charts |
| [`Discovery and Build_V0_not_needed/`](Discovery%20and%20Build_V0_not_needed/) | Superseded V0 discovery materials (kept for reference) |

## Design principles

1. **Zero new manual burden** — capture is a byproduct of work people already do (connectors, not forms)
2. **Originals are immutable** — every claim is one click from its evidence (page, slide, timestamp)
3. **AI drafts, humans decide** — every LLM output enters as a draft; SMEs hold the gate
4. **Trust is visible** — quality tiers and citations travel with the knowledge to the point of use
5. **Governance before agents** — the taxonomy, quality model, and lifecycle are prerequisites that
   make future AI/agentic capabilities safe to deploy

## Status

Working case study. The architecture slides are the current center of gravity; the research
analysis provides the evidence base; the discovery workbooks show the requirements-capture method.

# Comparison axes / rubric (Phase 4)

A scan produces **two grids, and they do different jobs** — build both:

1. **Strategic comparison matrix** — positioning, go-to-market, and credibility.
   "Where does everyone sit?" This is the analyst's map.
2. **Feature / capability grid** — the actual product capabilities a buyer
   shortlists on. "What can each one do?" This is the buyer's map.

They're easy to conflate, and most scans only build the first. The feature grid is
what your prospect (and the competitors' own "vs" pages) actually compare on, so
it's both buyer-intel and raw material for your own comparison pages later.

Include the **subject company as a column** in both, so each reads as "where
everyone sits, including us."

---

## Grid 1 — Strategic comparison matrix

Not every axis applies to every category — drop or add as the market warrants, but
keep the core consistent across a refresh series.

### Core axes (use most of the time)

| Axis | What to capture |
|---|---|
| **Positioning / category** | The competitor's one-line self-description / category claim. |
| **Primary job / buyer** | The main job-to-be-done and target buyer they serve. |
| **Entry price** | Cheapest meaningful tier/offer (and the pricing model). |
| **Pricing transparency** | Public vs quote-on-request / opaque. |
| **How a buyer evaluates & buys** | The path to purchase — self-serve, demo/sales-led, pilot/proof-of-concept, sample, or the category's equivalent. Capture whatever the buying motion actually is. |
| **Headline scale/credibility claim** | Their stated size/scale/leadership number (flag if self-reported / inconsistent). |
| **AI positioning** | Any AI-native or AI-assisted positioning or features they claim. |
| **Proof / reviews** | Review/rating-surface scores AND counts; named customers; case studies. |
| **Independent standing** | Placement in credible third-party roundups/rankings. |
| **Backing / ownership** | Bootstrapped / funded / acquired; parent company. |
| **Distribution model** | How they reach buyers — e.g. search, content, paid, partnerships, channel/retail, community, personal audience. |
| **Positions against subject?** | Do they publish a "vs [subject]" comparison? How do they frame it? |

## Optional axes (add when the category warrants)

- **Trial / access mechanics** — free trial, freemium, pilot/PoC, sample, return
  policy: whatever lowering-the-risk-of-trying looks like in this category.
- **Developer / agent surface** (tech & developer-facing products only) — public
  API, MCP server, llms.txt, SDKs, integrations/extensibility.
- **Geographic / language coverage**
- **Integrations / ecosystem**
- **Team size / company maturity**
- **Web traffic trend** (third-party estimate — mark low confidence)
- **Notable recent moves** (last 1–2 quarters)

Add whatever axes the category genuinely competes on (e.g. clinical evidence for
health products, sustainability credentials for consumer goods, SLAs for
infrastructure). The core list is a starting point, not a ceiling.

### Rules for the strategic matrix

- **Bold the standout cells** (the cheapest price, the only one with a real review
  moat, the first-mover on a surface) so the reader's eye lands on the differentiators.
- **Footnote self-claims.** Headline scale numbers are marketing until corroborated;
  say so under the table.
- Keep each cell to a few words; the detail lives in the per-competitor files. The
  matrix is a map, not the territory.

---

## Grid 2 — Feature / capability grid

The product capabilities a buyer actually shortlists on. Rows are **features**,
columns are **competitors + the subject**. This is category-specific — derive the
feature rows from what the buyer cares about and from what the competitors' own
comparison pages list (those pages are, in effect, the market telling you which
features it competes on).

**How to build the feature list (works for any category):**

1. Start from the subject company's own capabilities and its ICP's buying criteria —
   the features *this* buyer actually weighs.
2. Add every feature competitors lead with or list on their comparison/"vs" pages.
   Those pages are the market telling you which features it competes on.
3. Group into clusters that make sense for the category. **Derive the clusters from
   the domain — don't import a fixed taxonomy.** A useful way in is to ask which
   generic *lens* each feature falls under:

   - **The core job** — the central thing the product is bought to do.
   - **Inputs / coverage / data** — what the product knows, ingests, or covers, and
     how fresh/complete/trustworthy it is.
   - **Workflow & collaboration** — how work gets done in the tool: automation,
     multi-user/team, handoffs, lifecycle.
   - **Extensibility / technical** — API, integrations, exports, programmability,
     agent/AI surfaces.
   - **Trust / admin / compliance** — security, permissions, auditability, data
     handling (weight this heavily in regulated or enterprise categories).
   - **Commercial / access** — pricing transparency, entry price, seats, trial.

   These are lenses, not labels to copy — rename and re-cut them per category. A
   field-service tool, a video editor, and a payroll platform would each fill these
   lenses with completely different rows. If a lens is empty for your category, drop
   it; if the category needs one these don't cover, add it.

**Cell states** (keep these consistent with the interactive artefact):

| Symbol | Meaning |
|---|---|
| ✓ | Has it (verified or clearly stated) |
| ~ | Partial / limited / recently added |
| ✗ | Doesn't have it |
| ? | Unknown / couldn't verify |

### Rules for the feature grid

- **Cite the basis** for non-obvious ✓/✗ calls in the per-competitor file; a feature
  claim is a self-claim until you've seen it or a third party confirms it.
- **"~" is doing real work** — "recently added", "in beta", "export only", "via API
  only" are common and materially different from a full ✓. Don't round them up.
- **Don't editorialise in the grid.** It records *what exists*; the *so-what* lives
  in the strengths/weaknesses and opportunities sections of the synthesis.
- This grid is the natural centrepiece of the optional interactive artefact
  (`interactive-artefact.md`) — build the markdown grid such that it can be rendered
  directly (one row per feature, one column per competitor).

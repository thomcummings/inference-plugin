---
name: competitive-scan
description: >-
  Run a deep, multi-competitor competitive scan and turn it into a decision-ready
  synthesis. Use whenever the user wants a set of competitors analysed across
  positioning, digital presence, earned visibility, and content, structured into
  strengths, weaknesses, inconsistencies, and opportunities/threats for a subject
  company. Trigger eagerly on "competitive scan", "competitor analysis",
  "competitive landscape", "size up our competitors", "deep-dive on [rivals]",
  "how is X positioned against us", "refresh the competitive analysis", or when
  someone drops competitor URLs and wants more than a single profile. Gathers and
  structures evidence so the human makes the strategic calls; produces a
  two-register deliverable (internal evidence layer + client-ready version). Works
  for any company; becomes Inference-native when run inside an engagement folder.
  Distinct from single-competitor profiling and from building vs/alternative pages
  — this is the full fan-out, synthesis, and deliverable workflow.
---

# Competitive Scan

## What this skill is for

Produce a competitive scan that a decision-maker can act on: each competitor read
deeply across four dimensions, then synthesised into a cross-competitor picture
with clear strengths, weaknesses, inconsistencies, and opportunities/threats for
the **subject company** (the company the scan is *for*).

The governing principle, borrowed from the Inference operating model: **the agent
is the back office, the human is the analyst.** Your job is to gather, structure,
and surface evidence so the human can pattern-match against it. Surface findings,
options, and open questions. Do **not** quietly flatten messy evidence into tidy
conclusions, and do not invent strategic recommendations in the research layer —
that judgment belongs to the human. (The client-ready layer *does* carry
recommendations, but only ones the human has confirmed. See Phase 6.)

Why this matters: a competitive scan that hands down conclusions the human hasn't
examined is worse than useless — it launders assumptions into authority. The value
is in the evidence and the framing, not in pretending to have the answer.

## The two registers

Almost every run produces two layers, and conflating them is the most common failure:

- **Internal / evidence register** — per-competitor research files + a synthesis
  that *surfaces* findings (strengths, weaknesses, inconsistencies, opportunity
  and threat *candidates*, open questions). No settled strategic calls.
- **Client-ready register** — a cleaned, voice-checked version where the analyst's
  *confirmed* judgments and recommendations are folded in, internal threads and
  low-confidence scaffolding stripped, ready to share with the client.

Build the internal register first, get the human's reactions, *then* produce the
client-ready version. Never skip straight to client-ready.

## Operating modes

Detect which mode you're in before starting:

- **Inference-native** — you're inside an engagement folder (signals: an
  `AGENTS.md` / `CONTEXT.md` describing a client, a `ready-to-share/` tree, a
  pinned competitor list, a context hub). Read those first; follow the folder
  conventions; place outputs where the engagement expects them; respect any
  "don't write to shared/client-visible folders without approval" rule.
- **Standalone** — no engagement scaffolding. Ask the user for the subject
  company, the competitor set, the ICP/primary buyer, and where to save outputs.
  Produce a self-contained scan folder + synthesis.

Everything else about the workflow is identical across modes.

## The six phases

Work through these in order. Track them as a task list so the human can see progress.

### Phase 1 — Orient

Understand the subject company and the field *before* researching competitors, so
the scan deepens existing knowledge rather than repeating it.

- Inference-native: read the engagement context (`AGENTS.md`, `CONTEXT.md`), the
  pinned competitor list, the ICP, and **any prior competitive work** (earlier
  walks, audit synthesis, context-hub competitive files). Note what's already
  known so subagents go beyond it.
- Standalone: gather the same from the user — subject company, what it does, its
  ICP/primary buyer, the competitor set, and any prior research.

Capture: the subject company's positioning and ICP, the competitor list, and a
one-line "what's already known / what this scan must add."

### Phase 2 — Scope + tooling check

Confirm the shape before spending effort. Use the checklist in
`references/scope-and-tooling.md`. The decisions that change the work:

- **Competitor set** — which competitors, and any emerging/adjacent players.
- **Output structure** — per-competitor files + synthesis (default), or single
  combined doc.
- **Depth** — fresh deep re-scan, or incremental deepening over prior work.
- **Refresh vs first run** — if a prior scan exists, this may be a *diff* (see
  Phase 6 / refresh mode).

Then confirm tooling. The hard-won lesson: **plain web-fetch is often blocked or
returns empty shells on competitor marketing sites.** Prefer a renderer (e.g. Exa
search/fetch) for page content; use web search for the earned-visibility
dimension (reviews, press, rankings, community). A JS-rendering browser is useful
for live social counts and review counts but is optional. Details in
`references/scope-and-tooling.md`. If you lack a capable research tool, say so
before starting rather than producing thin results.

### Phase 3 — Per-competitor research fan-out

Spawn **one research subagent per competitor**, in parallel, each producing one
evidence file. This keeps each competitor's file-dump out of the main context and
runs concurrently.

Each subagent covers the four dimensions (full detail in
`references/research-dimensions.md`):

1. **Positioning & messaging** — verbatim from homepage/key pages: headline, value
   prop, category language, named personas/use-cases, pricing/packaging, trial
   mechanics, on-site proof, tone, messaging hierarchy.
2. **Owned & social presence** — channels they control: social accounts
   (followers, cadence, engagement, themes) and, where it's a real channel, any
   individual voice (founder, executive, practitioner) whose audience drives reach;
   their own website/SEO surface (comparison/alternative pages, programmatic pages).
3. **Earned visibility & reputation** — where they show up *without* controlling
   the narrative: presence in AI answers (and, for developer/tech products, any
   agent/MCP surface), organic search footprint, press/earned media, **category-
   appropriate** review and rating surfaces, directories/roundups, and community
   sentiment in the forums that matter for the category. Which surfaces these *are*
   depends entirely on the industry (see `references/research-dimensions.md`). This
   is the dimension teams most often skip and the one that most reveals real
   traction vs claimed traction.
4. **Content** — owned content in whatever formats the competitor actually uses
   (blog, data/research reports, programmatic pages, newsletter, video, podcast,
   webinars): themes, cadence, recency, formats, target reader, signature assets.

Brief every subagent with `references/subagent-brief-template.md`, which enforces
the evidence discipline (`references/evidence-discipline.md`): inline source URLs,
self-claims kept separate from independent corroboration, confidence ratings,
explicit gap lists, and **no subject-company-facing conclusions** in the research
layer. Each subagent writes its file and returns a short summary, not the full text.

Include a defined **"how they position against the subject company"** pass: search
"[subject] vs", "[subject] alternative", and read any competitor comparison pages.
This is consistently the richest single seam — it's the competitor telling you, in
their own words, where they think the subject is weak.

### Phase 4 — Synthesis (internal register)

Read the competitor files and build the synthesis using
`references/synthesis-structure.md`:

- Two grids (`references/comparison-axes.md`), both with the subject company as a
  column: a **strategic comparison matrix** (positioning, GTM, credibility) *and* a
  **feature / capability grid** (the capabilities a buyer actually shortlists on —
  derived from the subject's ICP criteria and from what competitors list on their
  own comparison pages). Most scans build only the first; the feature grid is what
  the buyer compares on and the raw material for the subject's own vs-pages, so
  build both.
- Per competitor: **strengths / weaknesses / inconsistencies**, as bullets, each
  evidence-grounded. Inconsistencies matter because they double as credibility
  signals and attack surfaces.
- **Opportunities and threats for the subject company** — as *candidates*, each
  paired with the open question that would decide it. Not recommendations yet.
- **Cross-cutting patterns** — the market-level signals worth the human's read.
- **Open questions** the scan can't answer (for the human / the client).

Label the synthesis as agent-authored, draft for the human's review. Hedge
appropriately on soft data ("appear to", "on this level of analysis") — desk
research can't see everything, and overclaiming erodes trust in the parts that are
solid.

### Phase 5 — Verify

Spot-check the most load-bearing and most *amplifiable* claims (the ones likely to
end up in the client deliverable or a marketing asset) against their sources.
Confirm the matrix matches the files. Flag anything low-confidence. A single
verified external ranking or quote is worth more than ten unverified self-claims —
make sure the ones you lean on are real.

### Phase 6 — Client-ready register (and refresh mode)

Only after the human has reacted to the internal synthesis:

- Produce the client-ready version — strip internal threads and scaffolding,
  re-attribute research notes neutrally, fold in the **human's confirmed**
  recommendations, and run a voice/tone pass appropriate to the audience (in
  Inference work, route external copy through the user's voice skill if available).
- Place it where the engagement expects (Inference-native) or where the user asked
  (standalone). Respect approval gates on client-visible folders.

**Output format:** markdown is the default and the source of truth. Return the
client-ready markdown to the user rather than formatting it into a deck here.

**Optional interactive artefact:** if the user wants a self-contained interactive
version — typically a sortable, filterable feature grid a client can poke at —
build it per `references/interactive-artefact.md` (a single offline `.html` file).
This complements the markdown; it never replaces it. Don't build it by default;
only when asked.

**Refresh mode:** when a prior scan exists, run Phases 1–5 fresh but add a "what
changed since [date]" delta — new entrants, positioning shifts, new proof, pricing
moves, narrative changes. The delta is often the most valuable part for a returning
client.

## Anti-patterns

- **Conclusions in the research layer.** Researchers gather; the human concludes.
- **Self-claims as facts.** "3,000+ customers", "#1 platform", "the largest [X] in
  the market" are marketing until independently corroborated. Always mark which is
  which.
- **Database/size-number arms races.** Competing on a self-reported headline number
  is a low-trust game; surface the inconsistency instead.
- **Skipping the earned-visibility dimension.** Owned channels show intent; earned
  signals show traction. The gap between them is often the finding.
- **One register doing two jobs.** Keep evidence and recommendation layers separate.
- **Overclaiming on thin data.** Hedge soft signals; reserve confidence for what's
  verified.

## Reference files

- `references/scope-and-tooling.md` — Phase 2 checklist + research-tool guidance.
- `references/research-dimensions.md` — the four dimensions in full, with
  verbatim-capture templates.
- `references/subagent-brief-template.md` — the per-competitor research prompt
  (fill the placeholders; this is the highest-value reusable asset).
- `references/comparison-axes.md` — the two grids: strategic matrix + feature grid.
- `references/synthesis-structure.md` — the synthesis template.
- `references/interactive-artefact.md` — optional self-contained interactive HTML
  output (build only when asked).
- `references/evidence-discipline.md` — claims-vs-corroboration, confidence levels,
  gap-flagging, source hygiene.

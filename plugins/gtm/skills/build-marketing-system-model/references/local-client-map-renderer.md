# Local client-map renderer

The reusable implementation of this spec is `scripts/render_client_map.py`. Run that to produce the map; only hand-build or edit the renderer when the spec itself changes. This document is the contract it implements — keep the two in sync.

Use this reference when generating a local `client-map.html` from an IMSM `client-model.json`.

The local client map is a call canvas for advisory work. It is not the public diagnostic results page, not a full audit report, and not a public website.

## Visual structure

Base the structure on the public `/marketing-system` page, not on the diagnostic results page.

Required shell:

```html
<main class="msm-shell msm-v3 msm-v4 ims-client-map">
  <div class="msm-topbar">...</div>
  <section class="msm-stage">
    <div class="msm-map-card-full">
      <div class="msm-bandmap">...</div>
    </div>
  </section>
</main>
```

Do not include a headline/subheader/stage toolbar inside the white canvas. The map should use the canvas full-screen, full-width, with the explanatory read living in the info sheet instead.

Top bar contract:

- Header text: `{client name} marketing system map`.
- Client name is white; `marketing system map` is accent yellow.
- Subline shows stage, buying motion, team shape and respondent coverage.
- Include a mode toggle in the top-right action cluster.
- Include the circular info button beside the mode toggle.

Required map architecture:

- `Objective` as the full-width direction box at the top.
- Learning loop row in this order: `Memory → Orchestration → Signals → Evaluation → Memory`.
- `Infrastructure` and `Expert Judgment` as enabling boxes beneath the loop.
- Use the same interaction grammar as the public page:
  - component boxes;
  - subtle info buttons;
  - expand buttons;
  - slide-up sheet inside the canvas;
  - optional portal view for deeper component detail.

Do not include public routes, route launchers, route filters, or generic methodology explanations in the client map unless the advisor explicitly asks for them.

## Canvas geometry

Match the public `/marketing-system` map proportions as closely as possible.

Use these layout rules:

- `.msm-bandmap` is the gridded canvas surface with the blue radial glow and 36px grid texture.
- `.msm-flowrow` is a compact flex row, not a wide CSS grid:
  - `display: flex`
  - equal component slots with `flex: 1 1 0`
  - arrow columns with `flex: 0 1 34px` and `min-width: 16px`
  - `gap: 4px`
- The learning-loop dashed SVG should be measured from the actual Memory and Evaluation box centres, not hard-coded to fixed percentages.
- Use the public-site arrow path:
  - `M5 12h13m-5-5 5 5-5 5`
  - `stroke-width: 1.8`
  - rounded caps and joins.

Component card contract:

- Use one consistent component-name font size across all seven boxes: `clamp(18px, 1.35vw, 26px)`.
- Do not use larger font sizes for Objective, Infrastructure or Expert Judgment.
- Component names use the display font, `font-weight: 400`, `line-height: 0.98`, and `letter-spacing: -0.035em`.
- Action rail sits at bottom-right of every box:
  - status pill first;
  - info button second;
  - expand button third.
- Status pill is not positioned on the left. It belongs inside `.msm-box-actions`.
- Status pill height must match the circular action buttons: `26px`.
- Action buttons are `26px × 26px`, `padding: 0`, `display: grid`, `place-items: center`.
- Icon SVGs inside action buttons are `14px × 14px` and `display: block` so the glyphs centre correctly.
- On mobile/narrow layouts, hide the icon buttons if needed but keep the status pill visible.

## Brand system

Use the advisor's brand system if the workspace has one (look for a `brand-system.md` or
equivalent), or the client's if the map is for them. Without one, use system fonts and
this neutral default palette:

- `hero` `#1D4ED8`
- `ink` `#0D0D0D`
- `accent` `#FACC15`
- `cream` `#F2EDE4`
- `ice` `#EEF3FF`
- `paper` `#FAFCFF`
- `slate` `#6B7280`

In a shareable output, load webfonts from a host you are licensed to serve them from,
never from local `file:///` paths (they resolve only on the author's machine) and never
by hotlinking another site's fonts. Keep system-font fallbacks in every `font-family`
declaration.

## Content rules

The local map should show live company information from the model, not public-facing framework education.

Condition language:

- Canonical model condition codes are `ad_hoc`, `early`, `working`, `strong`, `unknown` (stored in the model, unchanged).
- Display them using the L1–L4 ladder: `ad_hoc` → **L1 · Ad hoc**, `early` → **L2 · Activated**, `working` → **L3 · Adept**, `strong` → **L4 · Adaptive**. Keep the `L1–L4` prefix on the badge so the order reads without inference.
- Do not emit `limited` or `missing` as a capability condition in the model, rendered HTML, status labels or markdown.
- If an older source contains `limited`, normalize it to `early`; if it contains `missing`, normalize it to `ad_hoc`, before rendering.
- Never display the raw codes (`early`/`working`/`strong`) or the retired words (`Missing`/`Limited`); always show the L1–L4 label. (L1 means reactive/by-default, not absent.)

Use the top info sheet for:

- company/stage/motion/team shape;
- respondent coverage;
- desired outcomes;
- biggest constraints;
- sources processed;
- model caveat and confidence.

Use component info sheets for:

- current component condition;
- confidence;
- the working interpretation for that component;
- the capabilities that need inspection;
- source/evidence state.

Use portal/deeper component views for:

- subcomponent grouping;
- capability coverage;
- evidence gaps.

Avoid terms that make the page feel like a quiz result. Prefer:

- “working model”
- “current read”
- “source type”
- “respondent coverage”
- “evidence to check”
- “what to inspect next”

Over:

- “score”
- “diagnostic result”
- “maturity”
- “quiz”

## Evidence exposure

Do not average respondent answers into a score. Show the spread: every person as a named mark on the L1–L4 ladder, plus a range label (`Aligned · L2` or `L1–L3`). A fourth reply is another named dot and another heatmap column.

Do not make raw respondent quotes client-visible by accident. Raw answers can create unnecessary tension when one person is harsher than another.

Use exactly two display modes by default:

1. **Call mode** — default. Safe for screen-sharing. Show synthesis, confidence, respondent coverage and source counts, but hide raw respondent answers and respondent-level provenance.
2. **Review mode** — for the advisor. Show raw respondent answers, respondent roles and source-level provenance for inspection.

Mode implementation:

- Default to Call mode.
- Provide a visible top-bar toggle.
- Support `?mode=review` as a direct URL state.
- Re-render open sheets when the mode changes.
- Preserve raw answers in `client-model.json` regardless of display mode.
- Do not create separate “advisor” and “workshop” modes unless the advisor asks; Review mode covers both for now.

## Info sheet content

The info button should open the model information sheet. It should not repeat public methodology copy.

Use:

- Kicker: `Updated YYYY-MM-DD · Local working model`.
- Heading: `Current read: ...`.
- No duplicative sub-header beneath the heading.
- Model caveat: self-reported working model; not an evidence-verified audit.
- Company context cards.
- Captured priorities.
- Component read cards.

The canvas itself should not show the current-read headline or update line.

## Privacy

Generate local files by default. Do not upload `client-map.html`, `client-model.json`, sources, evidence notes or embedded snapshots to a public website without a deliberate sanitized export.

The generated HTML may embed a snapshot of `client-model.json`; treat it as client-confidential.

## Renderer completion checklist

Before handing back a local map:

- `client-model.json` validates.
- `client-model.md` is regenerated from the current JSON.
- `client-map.html` is regenerated from the current JSON.
- No visible or embedded active-model capability condition uses `limited` or `missing`; only skill legacy-normalization notes may mention them. (System-level "missing components/foundations" language is unaffected — that is a separate concept from the rung-1 capability condition.)
- Component title font size is consistent across all boxes.
- Status pills sit inside the bottom-right action rail before the info/expand buttons.
- Pill height and action button size match at `26px`.
- Action button SVGs are centred with zero button padding.
- Call mode hides raw respondent answers.
- Review mode exposes respondent/source detail.
- With two or more respondents, the info sheet shows an N-person ladder (named marks below the rungs) and an alignment heatmap with a range column. Range is the span of answers, not an average.
- Heatmap cell colours for L1–L4 use red → orange → yellow → green so the rungs read as a progression.
- The map remains local-first and client-confidential.

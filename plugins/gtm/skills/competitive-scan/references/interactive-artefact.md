# Optional interactive artefact (Phase 6)

The default deliverable is markdown — it feeds engagement folders, diffs cleanly
for refresh mode, and stays legible. **Only build this when the user asks for a
self-contained interactive version**, e.g. a competitor matrix a client can sort
and filter — otherwise just return the markdown.

## What it is

A **single self-contained `.html` file** — no build step, no external network
dependencies, openable by double-click and emailable as one attachment. It renders
the scan's structured data interactively:

- The **feature/capability grid** (`comparison-axes.md`) as the centrepiece —
  sortable by column, filterable by feature, with the subject company highlighted.
- The **strategic comparison matrix** as a second view/tab.
- Per-competitor **strengths / weaknesses / inconsistencies** as expandable cards.
- **Opportunities / threats** for the subject company.
- A confidence/legend key, and a "scanned [date]" stamp.

## Build rules

- **One file.** Inline all CSS and JS. No external `<script src>` to CDNs, no web
  fonts that require a network call — it must work fully offline. (A single small
  vendored library inlined into the file is acceptable if genuinely needed; prefer
  vanilla JS for sort/filter, which is a few dozen lines.)
- **Data-driven.** Put the scan content in a JS data object/array at the top of the
  file and render from it, so refreshing the artefact next quarter is a data swap,
  not a re-layout.
- **Honest rendering of evidence.** Carry the confidence and self-claim-vs-verified
  distinction into the UI — e.g. a marker on self-reported figures, a confidence
  dot, tooltips with the source. The artefact must not launder a self-claim into a
  hard fact just because it looks tidy in a cell.
- **Brand it lightly if a brand is known** (Inference-native: pick up the client's
  colours/wordmark if available); otherwise a clean neutral theme. Don't block on
  branding.
- **Accessibility basics** — real table semantics for the grids, keyboard-operable
  sort/filter controls, sufficient contrast.

## Feature-grid interaction

- **Sort** by any capability column (present / absent / partial), and by competitor.
- **Filter** to "only show competitors with feature X", and to "features where the
  subject company is ahead / behind".
- Use clear cell states: ✓ (has it), ✗ (doesn't), ~ (partial/limited), ? (unknown).
  Drive these from the same values used in the markdown grid so the two never drift.

## Where it goes

Save alongside the markdown deliverable (Inference-native: the engagement's
`ready-to-share` location; standalone: wherever the user asked). Respect any
approval gate on client-visible folders. Then surface it to the user as a file they
can open.

## Don't

- Don't make the interactive artefact the *only* output — it complements the
  markdown, it doesn't replace it. The markdown remains the source of truth.
- Don't pull live data at render time. It's a snapshot of the scan, dated and
  frozen, not a live dashboard.

---
name: brand-overview
description: >-
  Generate a beautiful, single-page HTML brand overview site from a brand guidelines PDF,
  a brand-system markdown file, or a live website URL. Produces an editorial-style scrollable
  reference page — white background, editorial layout — with live-rendered colour
  swatches, type specimens, spacing tokens, component previews, and a brand completeness
  checklist. Output is an HTML file + assets/ folder. Use this skill whenever the user
  mentions "brand overview", "brand guidelines page", "brand reference site", "brand
  system page", "design system overview", "brand book as a website", "internal brand
  page", "brand hub", or wants to turn a PDF/markdown/URL brand guide into a shareable
  HTML page. Also trigger when the user wants to check whether a brand system is complete,
  wants a visual audit of brand elements, or says things like "make this brand guide into
  a site", "render these guidelines", "build a public brand page", or "create an
  internal brand reference". Trigger eagerly.
---

# Brand Overview

Generate a polished, single-page HTML brand overview site from any brand source. The output is a self-contained reference page — think of a company's public `/brand` page — that renders the brand's own elements (colours, type, spacing, components) as live specimens alongside documentation.

The page is clean, white-background, editorial in layout, and includes a **brand completeness checklist** showing which components are present and which are missing.

## Workflow

1. **Identify input type** — PDF, markdown, or URL
2. **Extract brand tokens** — colours, fonts, spacing, logo info, voice, components
3. **Assess completeness** — score against the canonical checklist
4. **Generate the HTML** — one page + an assets/ folder for logos/images
5. **Iterate** — accept feedback, regenerate

---

## Step 1 — Identify input type

The user will provide one of:

- **PDF** — a brand guidelines document (most common client deliverable). Use `scripts/extract_pdf_tokens.py` to pull structured text, then parse for brand elements.
- **Markdown** — a `brand-system.md` or similar structured file. Parse headings, code blocks, hex values, font names.
- **URL** — a live website. Fetch the page, extract CSS variables, computed styles, Google Fonts imports, meta colours. Also take a screenshot via Chrome tools if available for visual reference.

If the input is ambiguous, ask one question: "Is this a PDF, a markdown file, or a URL?" — then proceed.

For PDFs: run the extraction script in the sandbox:

```bash
python /sessions/sweet-kind-edison/mnt/.claude/skills/brand-overview/scripts/extract_pdf_tokens.py <pdf-path> --output tokens.json
```

For URLs: fetch the page source and extract CSS custom properties, `<link>` tags for Google Fonts, `meta[name="theme-color"]`, and any inline Tailwind config. If the page is client-rendered, use Chrome tools (`navigate` + `get_page_text` + `javascript_tool`) to access computed styles.

For markdown: parse directly — look for hex codes (`#RRGGBB`), font family names, spacing values, and structured sections.

---

## Step 2 — Extract brand tokens

Build a structured token set. Not everything will be present in every source — that's fine, the completeness checklist will flag gaps. Extract what you can:

### Token categories

Read `references/token-categories.md` for the full canonical list. In summary:

**Foundations**: purpose, mission, vision, values, personality traits, brand story, tone of voice guidelines

**Logo**: primary logo description/usage, variations (light/dark/mono), clearspace rules, minimum sizes, favicon description, logo misuse rules

**Colour**: primary palette (name, hex, role), secondary/accent colours, semantic colours (success/error/warning/info), gradients, dark mode palette, colour usage rules

**Typography**: display/heading typeface (family, weights, source), body typeface, monospace typeface, type scale (name, size, weight, line-height, letter-spacing per step), font pairing rationale

**Spacing & Layout**: base unit, spacing scale, grid system (columns, gutters, breakpoints), content widths, section gaps

**Iconography**: icon style, library/set name, sizes, usage rules

**Photography & Imagery**: photography style, image treatments, illustration style, aspect ratios

**Components**: buttons (variants, sizes, radii), cards, form inputs, links, navigation patterns, badges/tags

**Motion**: animation principles, transition specs, easing curves

**Brand Applications**: business cards, social templates, email templates, presentation templates

---

## Step 3 — Assess completeness

Score the extracted tokens against the canonical checklist in `references/completeness-checklist.md`. Each item is either:

- **Present** — token extracted with concrete values
- **Partial** — mentioned but incomplete (e.g. "uses Inter" but no weight ramp)
- **Missing** — not found in the source

Calculate an overall completeness percentage. Group by category. This becomes the checklist section in the HTML output.

---

## Step 4 — Generate the HTML

Read `references/html-template.md` for the full template specification. Key principles:

### Design language

- **White background** (#FAFAFA base, #FFFFFF cards)
- **Dark text** (#111111 headings, #444444 body, #888888 muted)
- **Subtle borders** (#E5E5E5)
- **The brand's own typefaces** loaded via Google Fonts for specimens — but the page's UI chrome uses Inter for consistency
- **Generous whitespace** — 120px section gaps, 48px inner padding on cards
- **No emoji** — use filled/empty dots for the completeness score, colour-coded status chips
- **Sticky nav** — smooth-scroll section navigation using `scrollIntoView` (never `href="#anchor"`)

### Page sections (in order)

1. **Header** — brand name, tagline (if known), generation date, source type badge
2. **Completeness Checklist** — the scorecard. Shows each category with present/partial/missing counts. Overall percentage. Visual progress bar using the brand's primary colour.
3. **Logo** — description of logo variants, usage rules, clearspace. If logo image files are available, display them. Show do/don't rules if extracted.
4. **Colour** — rendered swatches for every colour. Each swatch shows: colour name, hex value, role/usage note. Group by primary / secondary / semantic. Show gradients if present.
5. **Typography** — load the brand's actual fonts via Google Fonts (or note if not available on Google Fonts). Show: typeface specimen (full alphabet + numbers), weight ramp (each available weight with a sample sentence), type scale (each step rendered at its actual size/weight/line-height).
6. **Spacing & Layout** — grid visualisation, spacing scale as a visual ruler, breakpoint table, content width examples.
7. **Iconography** — style description, size chart, usage rules.
8. **Photography & Imagery** — style description, aspect ratio examples, treatment rules.
9. **Components** — render actual buttons, cards, inputs using the brand's tokens. Interactive where possible (hover states on buttons).
10. **Motion** — principles and specs (text-only is fine here).
11. **Tone of Voice** — voice principles, do/don't examples, personality traits.
12. **Brand Applications** — descriptions of how the brand appears across touchpoints.
13. **Token Reference** — a comprehensive table of all extracted tokens. Columns: token name, value, notes.

**Only render sections that have content.** Skip empty sections entirely — the completeness checklist already flags what's missing.

### Asset handling

Output structure:
```
<brand-name>-brand-overview/
├── index.html
└── assets/
    ├── logos/          # Any logo files (if provided/extracted)
    └── screenshots/    # Any reference screenshots
```

For logos: if the user provides image files, copy them to `assets/logos/` and reference via relative paths. If logos are described but no files exist, render a placeholder with the description.

For screenshots: if a URL was the source, save a homepage screenshot to `assets/screenshots/`.

### HTML structure

The HTML file must be fully self-contained except for:
- Google Fonts `<link>` tags (for the brand's typefaces + Inter for UI)
- Images in the `assets/` folder referenced via relative paths

Use CSS custom properties throughout. The brand's tokens become CSS variables in `:root`, and the page components reference them — so the overview page subtly reflects the brand it's documenting while maintaining a consistent white editorial frame.

### Critical implementation notes

- **Navigation**: use `<button onclick="document.getElementById('section-id').scrollIntoView({behavior:'smooth'})">` — never `href="#anchor"` (breaks on shared platforms)
- **Responsive**: the page should work at 768px+ (don't worry about mobile — these are internal reference docs)
- **Print-friendly**: use `@media print` to hide the nav and expand all sections
- **No JS frameworks** — vanilla HTML/CSS/JS only
- **Colour swatches**: render as `<div>` elements with the actual colour as background. Show hex, RGB, and the role. Include a contrast-check indicator (dark text on light swatches, light text on dark swatches).
- **Type specimens**: use the actual font loaded via Google Fonts. If the font isn't on Google Fonts, note it and use a close alternative with a disclaimer.

---

## Step 5 — Iterate

After the first render, the user will want changes. Common requests:

- "Add the logo files" — copy provided files to `assets/logos/`, update the HTML
- "The colours are wrong" — update the token values and regenerate
- "Can you also show the dark mode palette" — add a dark mode sub-section to the colour section
- "Make it publishable" — any static host works, for example Netlify Drop
- "Export as PDF too" — suggest the pdf skill for a static version

Keep the same filename so any shared links stay current.

---

## Completeness checklist categories

The full canonical checklist (used for scoring) covers 10 categories and ~45 individual items. The detailed checklist is in `references/completeness-checklist.md`. Here's the summary:

| Category | Key items |
|---|---|
| Foundations | Purpose, mission, vision, values, personality, story, voice |
| Logo | Primary, variations, clearspace, min size, favicon, misuse |
| Colour | Primary palette, secondary, semantic, gradients, dark mode, usage rules |
| Typography | Display face, body face, type scale, weight ramp, pairing rationale |
| Spacing & Layout | Base unit, scale, grid, breakpoints, content widths |
| Iconography | Style, library, sizes, usage |
| Photography | Style, treatments, illustration, aspect ratios |
| Components | Buttons, cards, inputs, links, nav, badges |
| Motion | Principles, transitions, easing |
| Applications | Business cards, social, email, presentations |

---

## Reference files

- `references/html-template.md` — detailed HTML/CSS template specification with code examples for every section
- `references/completeness-checklist.md` — the full 45-item brand completeness checklist with scoring rules
- `references/token-categories.md` — comprehensive list of extractable brand tokens by category
- `scripts/extract_pdf_tokens.py` — PDF text extraction helper (uses pymupdf)

## Integration with other skills

- **brand-asset-renderer** — if the user wants to generate actual logo/banner/OG image files from the tokens, hand off to that skill

---
name: ui-analysis
description: Analyze UI designs and generate structured JSONC specifications for implementation. Use when the user provides a design image (screenshot, mockup, Dribbble/Figma export) or URL and wants to replicate it in code. Produces stack-aware design tokens, component inventories, and implementation context. Complements frontend-design skill (which creates from scratch) - this skill is for replicating existing designs.
---

# UI Analysis Skill

Transform visual designs into structured specifications for accurate implementation.

## Workflow

### 1. Receive Design Input

Accept design via:
- **Uploaded image**: Screenshot, mockup, export from Figma/Sketch/XD
- **Direct URL**: Link to image file (fetch and analyze)

### 2. Detect Target Stack

Examine the user's project to tailor output tokens:

```bash
# Check for framework/styling indicators
cat package.json 2>/dev/null | grep -E '"(react|vue|svelte|next|nuxt|tailwind|styled-components|emotion)"'
ls tailwind.config.* 2>/dev/null
ls postcss.config.* 2>/dev/null
```

**Stack detection priority:**
1. Tailwind → output Tailwind-compatible tokens (color scales, spacing units)
2. CSS-in-JS (styled-components/emotion) → output CSS custom properties
3. Plain CSS/SCSS → output CSS custom properties
4. Unknown → output generic tokens with CSS custom property format

### 3. Analyze the Design

Extract systematically:

**Layout Structure**
- Overall layout pattern (sidebar+content, top-nav, split-screen, bento grid, etc.)
- Grid system and column structure
- Responsive breakpoint implications
- Spacing rhythm (tight/generous, consistent increments)

**Color System**
- Background colors (primary surfaces, card surfaces, elevated surfaces)
- Text hierarchy (primary, secondary, muted, disabled)
- Accent/brand colors (primary action, secondary action)
- Semantic colors (success, warning, error, info)
- Any gradients, overlays, or transparency patterns

**Typography**
- Font families (identify or suggest closest match)
- Size scale (headings, body, caption, labels)
- Weight usage patterns
- Line height and letter spacing characteristics

**Components**
- Inventory each distinct UI element
- Note variants (hover, active, disabled states if visible)
- Border radius patterns
- Shadow/elevation system
- Icon style (outline, filled, size)

**Visual Effects**
- Shadow patterns (subtle, dramatic, layered)
- Border usage (none, subtle, prominent)
- Background treatments (solid, gradient, texture, glassmorphism)
- Any motion/animation hints

### 4. Generate Output

Produce three artifacts:

#### A. Design Specification (JSONC)

See `references/output-schema.jsonc` for complete template. Key sections:

```jsonc
{
  "meta": { "name": "...", "style": ["..."], "mode": "dark|light" },
  "layout": { /* structure, breakpoints, spacing */ },
  "colors": { /* full palette, stack-appropriate format */ },
  "typography": { /* fonts, scale, weights */ },
  "components": { /* per-component tokens */ },
  "effects": { /* shadows, borders, radii, animations */ }
}
```

#### B. Component Inventory (Markdown table)

| Component | Purpose | Variants | Notes |
|-----------|---------|----------|-------|
| NavBar | Primary navigation | - | Sticky, contains logo + links + CTA |
| StatCard | Display KPI | default, highlighted | Icon + value + label |
| ... | ... | ... | ... |

#### C. Implementation Context (brief prose)

- Detected stack and token format used
- Key implementation patterns (CSS Grid vs Flexbox, etc.)
- Responsive strategy recommendations
- Any ambiguities or assumptions made

## Output Location

Save the specification to user's project:
```
{project_root}/docs/ui-spec.jsonc      # Design tokens
{project_root}/docs/ui-components.md   # Component inventory
```

Or output directly if no clear project root.

## Quality Checklist

Before finalizing:
- [ ] Colors extracted as actual values, not descriptions
- [ ] Typography includes concrete sizes (px/rem)
- [ ] All visible components inventoried
- [ ] Tokens formatted for detected stack
- [ ] No "purple gradient" defaults - use what's actually in the design

## Reference Files

- `references/output-schema.jsonc` - Complete JSONC template with all sections
- `references/style-vocabulary.md` - Design style terms for classification

# Token Categories

Complete reference for extractable brand tokens, organised by category. When extracting from a source, work through each category and pull what's available. Not every source will have every token — that's expected.

## Extraction patterns by source type

### From PDFs
- Hex values: look for `#` followed by 6 hex characters, or RGB values like `R54 G52 B240`
- CMYK: `C97 M97 Y0 K0` — convert to hex
- Pantone: note the Pantone code but convert to hex for digital use
- Font names: usually appear near specimen text or in a "Typography" section
- Spacing: rarely specified in PDFs — mark as missing unless explicitly documented

### From Markdown
- Hex values in code blocks or inline code
- Font families in code blocks or after "Font:" / "Typeface:" labels
- CSS variable definitions
- Structured headings map to token categories

### From URLs
- CSS custom properties (`:root { --primary: #xxx }`)
- Computed styles on key elements (`body`, `h1-h6`, `.btn`, `a`)
- Google Fonts `<link>` tags — extract family and weights
- `<meta name="theme-color">` — often the primary brand colour
- Tailwind config if present in inline `<script>`
- Open Graph meta tags for brand presentation

## Token structure

```json
{
  "brand": {
    "name": "Brand Name",
    "tagline": "Optional tagline",
    "source_type": "pdf|markdown|url",
    "source_path": "path or URL",
    "generated_date": "ISO date"
  },
  "foundations": {
    "purpose": "string or null",
    "mission": "string or null",
    "vision": "string or null",
    "values": [{"name": "Value", "description": "Description"}],
    "personality": [{"trait": "Trait", "description": "Description"}],
    "story": "string or null",
    "tone_of_voice": {
      "principles": ["principle1", "principle2"],
      "do": ["example1"],
      "dont": ["example1"]
    }
  },
  "logo": {
    "description": "string",
    "variations": ["primary", "dark", "light", "mono"],
    "clearspace": "string or null",
    "min_size": "string or null",
    "favicon": "string or null",
    "misuse": ["rule1", "rule2"],
    "files": []
  },
  "colours": {
    "primary": [{"name": "Name", "hex": "#RRGGBB", "role": "Background|Text|Accent"}],
    "secondary": [{"name": "Name", "hex": "#RRGGBB", "role": "string"}],
    "semantic": {
      "success": "#hex or null",
      "error": "#hex or null",
      "warning": "#hex or null",
      "info": "#hex or null"
    },
    "gradients": [{"name": "Name", "stops": ["#hex1", "#hex2"], "angle": "deg"}],
    "dark_mode": [{"name": "Name", "hex": "#RRGGBB", "role": "string"}],
    "usage_rules": ["rule1", "rule2"]
  },
  "typography": {
    "display": {
      "family": "Font Family",
      "source": "Google Fonts|Adobe Fonts|Custom",
      "weights": [300, 400, 500, 600, 700],
      "google_fonts_import": "family=Font+Family:wght@300;400;700"
    },
    "body": {
      "family": "Font Family",
      "source": "Google Fonts|Adobe Fonts|Custom",
      "weights": [400, 500, 600],
      "google_fonts_import": "family=Font+Family:wght@400;500;600"
    },
    "mono": {
      "family": "Font Family or null",
      "source": "string or null"
    },
    "scale": [
      {
        "name": "heroTitle",
        "sizes": {"mobile": "36px", "tablet": "48px", "desktop": "72px"},
        "weight": 700,
        "line_height": 1.1,
        "letter_spacing": "-0.04em"
      }
    ],
    "pairing_rationale": "string or null"
  },
  "spacing": {
    "base_unit": "8px or null",
    "scale": [{"name": "xs", "value": "4px"}],
    "grid": {
      "columns": {"mobile": 4, "tablet": 8, "desktop": 12},
      "gutter": "24px",
      "margin": "16px"
    },
    "breakpoints": [{"name": "mobile", "value": "768px"}],
    "content_widths": [{"name": "normal", "value": "1200px"}],
    "section_gap": "string or null"
  },
  "iconography": {
    "style": "string or null",
    "library": "string or null",
    "sizes": [{"name": "sm", "value": "16px"}],
    "usage_rules": ["rule1"]
  },
  "photography": {
    "style": "string or null",
    "treatments": ["treatment1"],
    "illustration_style": "string or null",
    "aspect_ratios": [{"name": "hero", "ratio": "16:9"}]
  },
  "components": {
    "buttons": {
      "variants": ["primary", "secondary"],
      "sizes": ["sm", "md", "lg"],
      "border_radius": "string or null",
      "states": ["default", "hover", "active", "disabled"]
    },
    "cards": {
      "padding": "string or null",
      "border": "string or null",
      "shadow": "string or null",
      "border_radius": "string or null"
    },
    "inputs": {
      "border": "string or null",
      "border_radius": "string or null",
      "padding": "string or null",
      "states": ["default", "focus", "error", "disabled"]
    },
    "links": {
      "color": "string or null",
      "hover": "string or null",
      "decoration": "string or null"
    },
    "navigation": "string or null",
    "badges": {
      "styles": [],
      "sizes": []
    }
  },
  "motion": {
    "principles": ["principle1"],
    "transitions": [{"property": "all", "duration": "200ms", "easing": "ease-out"}],
    "easing_curves": [{"name": "default", "value": "cubic-bezier(0.4, 0, 0.2, 1)"}]
  },
  "applications": {
    "business_cards": "string or null",
    "social_templates": "string or null",
    "email_templates": "string or null",
    "presentation_templates": "string or null"
  }
}
```

## Extraction tips

- **Don't fabricate.** If a value isn't in the source, mark it null. The completeness checklist handles the gap.
- **Be generous with "partial".** If the source says "we use Inter" but doesn't list weights, that's partial — not missing.
- **RGB to hex**: `R54 G52 B240` → `#3634F0`
- **Pantone to hex**: use the closest standard conversion. Note the Pantone code in the `role` field.
- **Font weights from specimens**: if the PDF shows a weight ramp visually, list the weights you can identify. Common: 300 (Light), 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold), 800 (ExtraBold).
- **Type scale from headings**: if the source shows different heading sizes, measure relative sizes even if absolute values aren't given.

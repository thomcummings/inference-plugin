# HTML Template Specification

This document defines the exact HTML/CSS structure for the brand overview page. The page uses a white editorial layout — clean, spacious, and letting the brand's own elements be the visual stars.

## Page skeleton

Two-column layout: fixed left sidebar with navigation, scrollable right content area.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Brand Name] — Brand Overview</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&{BRAND_DISPLAY_IMPORT}&{BRAND_BODY_IMPORT}&display=swap" rel="stylesheet">
  <style>
    /* See CSS specification below */
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <!-- Brand name, nav links, completeness score -->
    </aside>
    <div class="content">
      <section id="header" class="section">...</section>
      <section id="completeness" class="section">...</section>
      <!-- More sections as needed -->
    </div>
  </div>
  <script>
    /* See JS specification below */
  </script>
</body>
</html>
```

## CSS foundation

```css
/* Reset */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* Brand tokens as CSS variables */
:root {
  /* Page chrome (fixed — these don't change per brand) */
  --page-bg: #FAFAFA;
  --card-bg: #FFFFFF;
  --text-primary: #111111;
  --text-secondary: #444444;
  --text-muted: #888888;
  --text-faint: #BBBBBB;
  --border: #E5E5E5;
  --border-light: #F0F0F0;
  --surface-hover: #F5F5F5;
  --nav-bg: rgba(255, 255, 255, 0.92);
  --nav-border: rgba(0, 0, 0, 0.06);

  /* Brand colours (populated from extracted tokens) */
  --brand-primary: {colours.primary[0].hex};
  --brand-primary-light: {colours.primary[0].hex} at ~8% opacity (use rgba or hex+15);
  --brand-secondary: {colours.secondary[0].hex or fallback};
  --brand-accent: {colours.secondary[1].hex or var(--brand-primary)};

  /* Brand fonts (for specimens — page UI always uses Inter) */
  --brand-display: '{typography.display.family}', sans-serif;
  --brand-body: '{typography.body.family}', sans-serif;

  /* Layout — two-column sidebar */
  --sidebar-width: 260px;
  --content-max: 960px;
  --section-gap: 100px;
  --card-padding: 40px;
  --card-radius: 16px;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 15px;
  font-weight: 300;
  line-height: 1.6;
  color: var(--text-secondary);
  background: var(--page-bg);
  -webkit-font-smoothing: antialiased;
}

/* Print styles */
@media print {
  .sidebar { display: none !important; }
  .content { margin-left: 0 !important; }
  .section { break-inside: avoid; }
  body { background: white; }
}
```

## Layout — Two-column sidebar

Fixed left sidebar with brand name, grouped nav links, and a completeness score at the bottom. Content scrolls independently on the right. Always use `scrollIntoView` — never `href="#anchor"`.

```css
.layout { display: flex; min-height: 100vh; }

.sidebar {
  width: var(--sidebar-width);
  position: fixed;
  top: 0; left: 0; bottom: 0;
  background: var(--card-bg);
  border-right: 1px solid var(--border);
  padding: 32px 0;
  display: flex;
  flex-direction: column;
  z-index: 100;
  overflow-y: auto;
  scrollbar-width: none;
}

.sidebar::-webkit-scrollbar { display: none; }

.content {
  margin-left: var(--sidebar-width);
  flex: 1;
  min-width: 0;
}
```

### Sidebar structure

```html
<aside class="sidebar">
  <!-- Brand identity -->
  <div class="sidebar-brand">
    <div class="sidebar-brand-name">[Brand Name]</div>
    <div class="sidebar-brand-sub">Brand Guidelines v[X]</div>
  </div>

  <div class="sidebar-divider"></div>

  <!-- Nav group: Overview -->
  <div class="sidebar-label">Overview</div>
  <nav class="sidebar-nav">
    <button class="sidebar-link active" onclick="document.getElementById('header').scrollIntoView({behavior:'smooth'})">
      <span class="sidebar-link-dot"></span> Overview
    </button>
    <button class="sidebar-link" onclick="document.getElementById('completeness').scrollIntoView({behavior:'smooth'})">
      <span class="sidebar-link-dot"></span> Checklist
    </button>
  </nav>

  <div class="sidebar-divider"></div>

  <!-- Nav group: Brand System -->
  <div class="sidebar-label">Brand System</div>
  <nav class="sidebar-nav">
    <button class="sidebar-link" onclick="document.getElementById('logo').scrollIntoView({behavior:'smooth'})">
      <span class="sidebar-link-dot"></span> Logo
    </button>
    <!-- More links per rendered section -->
  </nav>

  <div class="sidebar-divider"></div>

  <!-- Nav group: Reference -->
  <div class="sidebar-label">Reference</div>
  <nav class="sidebar-nav">
    <button class="sidebar-link" onclick="document.getElementById('tokens').scrollIntoView({behavior:'smooth'})">
      <span class="sidebar-link-dot"></span> Tokens
    </button>
  </nav>

  <!-- Completeness score at bottom (pushed down with margin-top: auto) -->
  <div class="sidebar-score">
    <div class="sidebar-score-label">Completeness</div>
    <div class="sidebar-score-bar">
      <div class="sidebar-score-fill" style="width: [XX]%;"></div>
    </div>
    <div class="sidebar-score-value"><strong>[XX]%</strong> — [Rating]</div>
  </div>
</aside>
```

```css
.sidebar-brand { padding: 0 28px; margin-bottom: 8px; }
.sidebar-brand-name { font-size: 22px; font-weight: 700; color: var(--text-primary); letter-spacing: -0.02em; }
.sidebar-brand-sub { font-size: 12px; color: var(--text-faint); margin-top: 2px; }

.sidebar-divider { height: 1px; background: var(--border-light); margin: 20px 28px; }

.sidebar-label {
  font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--text-faint); padding: 0 28px; margin-bottom: 8px;
}

.sidebar-nav { display: flex; flex-direction: column; gap: 2px; padding: 0 12px; }

.sidebar-link {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 16px; border-radius: 8px; border: none;
  background: transparent; color: var(--text-muted);
  font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 500;
  cursor: pointer; text-align: left; width: 100%;
  transition: all 0.12s ease;
}

.sidebar-link:hover { background: var(--surface-hover); color: var(--text-secondary); }
.sidebar-link.active { background: var(--brand-primary-light); color: var(--brand-primary); font-weight: 600; }

.sidebar-link-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: currentColor; opacity: 0.4; flex-shrink: 0;
}
.sidebar-link.active .sidebar-link-dot { opacity: 1; background: var(--brand-primary); }

.sidebar-score { margin-top: auto; padding: 0 28px; }
.sidebar-score-label {
  font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--text-faint); margin-bottom: 8px;
}
.sidebar-score-bar { height: 6px; background: var(--border-light); border-radius: 100px; overflow: hidden; margin-bottom: 6px; }
.sidebar-score-fill { height: 100%; border-radius: 100px; background: var(--brand-primary); transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1); }
.sidebar-score-value { font-size: 13px; color: var(--text-muted); }
.sidebar-score-value strong { color: var(--text-primary); font-weight: 700; }
```

## Section layout

Each section follows the same pattern: a section label (small caps), a title, optional subtitle, then content.

```css
.section {
  max-width: var(--content-max);
  padding: var(--section-gap) 48px;
  border-bottom: 1px solid var(--border-light);
}

.section:last-child { border-bottom: none; }

.section-label {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 12px;
}

.section-title {
  font-size: 36px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.15;
  margin-bottom: 16px;
  letter-spacing: -0.03em;
}

.section-subtitle {
  font-size: 17px;
  color: var(--text-muted);
  max-width: 640px;
  line-height: 1.5;
  margin-bottom: 48px;
}
```

## Header section

```html
<section id="header" class="section header-section">
  <div class="header-content">
    <div class="section-label">Brand Guidelines</div>
    <h1 class="header-title">[Brand Name]</h1>
    <p class="header-tagline">[Tagline if available]</p>
    <div class="header-meta">
      <span class="meta-badge">[Source type: PDF / URL / Markdown]</span>
      <span class="meta-date">Generated [date]</span>
    </div>
  </div>
</section>
```

```css
.header-section { padding-top: 160px; padding-bottom: 80px; }

.header-title {
  font-size: 72px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.05;
  letter-spacing: -0.04em;
  margin-bottom: 16px;
}

.header-tagline {
  font-size: 22px;
  color: var(--text-muted);
  margin-bottom: 32px;
  max-width: 600px;
}

.header-meta { display: flex; gap: 16px; align-items: center; }

.meta-badge {
  padding: 4px 12px;
  border-radius: 100px;
  background: var(--brand-primary-light);
  color: var(--brand-primary);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.meta-date { font-size: 13px; color: var(--text-faint); }
```

## Completeness checklist section

The hero section of the page. Shows overall score + category-by-category breakdown.

```html
<section id="completeness" class="section">
  <div class="section-label">Brand Completeness</div>
  <h2 class="section-title">System checklist</h2>
  <p class="section-subtitle">How complete this brand system is across 10 categories and 50 individual items.</p>

  <!-- Overall score -->
  <div class="score-hero">
    <div class="score-number">[XX]%</div>
    <div class="score-bar">
      <div class="score-bar-fill" style="width: [XX]%; background: var(--brand-primary);"></div>
    </div>
    <div class="score-label">[Rating label] — [Description]</div>
  </div>

  <!-- Category grid -->
  <div class="checklist-grid">
    <!-- One card per category -->
    <div class="checklist-card">
      <div class="checklist-card-header">
        <span class="checklist-category">Foundations</span>
        <span class="checklist-score">[5/7]</span>
      </div>
      <div class="checklist-items">
        <div class="checklist-item present">
          <span class="checklist-dot"></span>
          <span>Purpose statement</span>
        </div>
        <div class="checklist-item partial">
          <span class="checklist-dot"></span>
          <span>Mission statement</span>
        </div>
        <div class="checklist-item missing">
          <span class="checklist-dot"></span>
          <span>Brand story</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.score-hero {
  margin-bottom: 64px;
  max-width: 480px;
}

.score-number {
  font-size: 80px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1;
  letter-spacing: -0.04em;
  margin-bottom: 16px;
}

.score-bar {
  height: 8px;
  background: var(--border-light);
  border-radius: 100px;
  overflow: hidden;
  margin-bottom: 12px;
}

.score-bar-fill {
  height: 100%;
  border-radius: 100px;
  transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.score-label {
  font-size: 15px;
  color: var(--text-muted);
}

.checklist-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.checklist-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--card-radius);
  padding: 32px;
}

.checklist-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.checklist-category {
  font-weight: 600;
  font-size: 15px;
  color: var(--text-primary);
}

.checklist-score {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
}

.checklist-items { display: flex; flex-direction: column; gap: 10px; }

.checklist-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
}

.checklist-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.checklist-item.present .checklist-dot { background: var(--brand-primary); }
.checklist-item.present { color: var(--text-secondary); }

.checklist-item.partial .checklist-dot { background: #F5A623; }
.checklist-item.partial { color: var(--text-muted); }

.checklist-item.missing .checklist-dot { background: var(--border); }
.checklist-item.missing { color: var(--text-faint); text-decoration: line-through; }
```

## Colour section

Render actual swatches. Each swatch is a coloured rectangle with the hex, name, and role.

```html
<section id="colour" class="section">
  <div class="section-label">Colour</div>
  <h2 class="section-title">Brand palette</h2>
  <p class="section-subtitle">Primary, secondary, and semantic colours with their roles.</p>

  <h3 class="subsection-title">Primary</h3>
  <div class="swatch-grid">
    <div class="swatch-card">
      <div class="swatch-preview" style="background: #3634F0;">
        <span class="swatch-hex" style="color: white;">#3634F0</span>
      </div>
      <div class="swatch-info">
        <div class="swatch-name">Pure Blue</div>
        <div class="swatch-role">Primary brand colour</div>
      </div>
    </div>
  </div>
</section>
```

```css
.subsection-title {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 24px;
  margin-top: 48px;
}

.subsection-title:first-of-type { margin-top: 0; }

.swatch-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 48px;
}

.swatch-card {
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  background: var(--card-bg);
}

.swatch-preview {
  height: 120px;
  display: flex;
  align-items: flex-end;
  padding: 12px 16px;
}

.swatch-hex {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 13px;
  font-weight: 500;
  opacity: 0.9;
}

.swatch-info { padding: 16px; }

.swatch-name {
  font-weight: 600;
  font-size: 14px;
  color: var(--text-primary);
  margin-bottom: 2px;
}

.swatch-role {
  font-size: 13px;
  color: var(--text-muted);
}
```

**Contrast logic**: if the swatch colour's relative luminance is > 0.5, use dark text on the preview; otherwise use white. Calculate luminance:

```javascript
function getLuminance(hex) {
  const r = parseInt(hex.slice(1,3), 16) / 255;
  const g = parseInt(hex.slice(3,5), 16) / 255;
  const b = parseInt(hex.slice(5,7), 16) / 255;
  const srgb = [r, g, b].map(c => c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));
  return 0.2126 * srgb[0] + 0.7152 * srgb[1] + 0.0722 * srgb[2];
}
```

## Typography section

Load the brand's actual fonts and render specimens.

```html
<section id="typography" class="section">
  <div class="section-label">Typography</div>
  <h2 class="section-title">Typefaces & scale</h2>

  <!-- Typeface specimen -->
  <div class="type-specimen-card">
    <div class="type-specimen-name">[Font Family Name]</div>
    <div class="type-specimen-alphabet" style="font-family: var(--brand-display);">
      ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
    </div>

    <!-- Weight ramp -->
    <div class="type-weight-ramp">
      <div class="type-weight-row" style="font-family: var(--brand-display); font-weight: 300;">
        <span class="type-weight-label">300</span>
        <span class="type-weight-sample">The quick brown fox jumps over the lazy dog</span>
      </div>
      <!-- More weights... -->
    </div>
  </div>

  <!-- Type scale -->
  <h3 class="subsection-title">Type scale</h3>
  <div class="type-scale">
    <div class="type-scale-row">
      <div class="type-scale-meta">
        <span class="type-scale-name">heroTitle</span>
        <span class="type-scale-specs">72px / 1.1 / -0.04em / wght 700</span>
      </div>
      <div class="type-scale-sample" style="font-family: var(--brand-display); font-size: 72px; font-weight: 700; line-height: 1.1; letter-spacing: -0.04em;">
        Brand name
      </div>
    </div>
  </div>
</section>
```

```css
.type-specimen-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--card-radius);
  padding: var(--card-padding);
  margin-bottom: 48px;
}

.type-specimen-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--brand-primary);
  margin-bottom: 16px;
}

.type-specimen-alphabet {
  font-size: 20px;
  line-height: 1.6;
  color: var(--text-primary);
  margin-bottom: 32px;
  word-break: break-all;
}

.type-weight-ramp {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.type-weight-row {
  display: flex;
  align-items: baseline;
  gap: 24px;
}

.type-weight-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-faint);
  width: 40px;
  flex-shrink: 0;
}

.type-weight-sample {
  font-size: 18px;
  color: var(--text-primary);
}

.type-scale {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.type-scale-row {
  padding-bottom: 32px;
  border-bottom: 1px solid var(--border-light);
}

.type-scale-row:last-child { border-bottom: none; }

.type-scale-meta {
  display: flex;
  gap: 16px;
  align-items: baseline;
  margin-bottom: 12px;
}

.type-scale-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--brand-primary);
  font-family: 'SF Mono', 'Fira Code', monospace;
}

.type-scale-specs {
  font-size: 12px;
  color: var(--text-faint);
  font-family: 'SF Mono', 'Fira Code', monospace;
}

.type-scale-sample {
  color: var(--text-primary);
  overflow: hidden;
  text-overflow: ellipsis;
}
```

## Spacing & Layout section

Visual representations of the spacing scale and grid.

```css
.spacing-scale {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  padding: 32px 0;
}

.spacing-bar {
  background: var(--brand-primary-light);
  border: 1px solid var(--brand-primary);
  border-radius: 4px;
  width: 48px;
  position: relative;
}

.spacing-bar-label {
  position: absolute;
  bottom: -24px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  white-space: nowrap;
}

.spacing-bar-value {
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 11px;
  color: var(--text-faint);
  font-family: 'SF Mono', 'Fira Code', monospace;
  white-space: nowrap;
}
```

## Components section

Render actual interactive components using the brand's tokens.

```html
<div class="component-showcase">
  <h3 class="subsection-title">Buttons</h3>
  <div class="component-row">
    <button class="brand-btn brand-btn-primary">Primary</button>
    <button class="brand-btn brand-btn-secondary">Secondary</button>
    <button class="brand-btn brand-btn-primary" disabled>Disabled</button>
  </div>
</div>
```

```css
.component-showcase {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--card-radius);
  padding: var(--card-padding);
  margin-bottom: 24px;
}

.component-row {
  display: flex;
  gap: 16px;
  align-items: center;
  flex-wrap: wrap;
}

/* Brand buttons use extracted token values */
.brand-btn {
  font-family: var(--brand-body);
  font-size: 14px;
  font-weight: 500;
  padding: 10px 24px;
  border-radius: {components.buttons.border_radius or '8px'};
  border: none;
  cursor: pointer;
  transition: all 0.15s ease;
}

.brand-btn-primary {
  background: var(--brand-primary);
  color: white;
}

.brand-btn-primary:hover { filter: brightness(1.1); }
.brand-btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }

.brand-btn-secondary {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-primary);
}

.brand-btn-secondary:hover { background: var(--surface-hover); }
```

## Token reference section

A comprehensive table of all extracted tokens — the "developer handoff" section.

```html
<section id="tokens" class="section">
  <div class="section-label">Tokens</div>
  <h2 class="section-title">Design tokens</h2>
  <p class="section-subtitle">Complete reference table for implementation.</p>

  <h3 class="subsection-title">Colours</h3>
  <div class="token-table">
    <div class="token-row token-header">
      <span class="token-cell token-name-col">Token</span>
      <span class="token-cell token-value-col">Value</span>
      <span class="token-cell token-notes-col">Notes</span>
    </div>
    <div class="token-row">
      <span class="token-cell token-name-col"><code>--brand-primary</code></span>
      <span class="token-cell token-value-col"><code>#3634F0</code></span>
      <span class="token-cell token-notes-col">Pure Blue — primary brand</span>
    </div>
  </div>
</section>
```

```css
.token-table {
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 48px;
}

.token-row {
  display: grid;
  grid-template-columns: 200px 180px 1fr;
  padding: 12px 20px;
  border-bottom: 1px solid var(--border-light);
  align-items: center;
}

.token-row:last-child { border-bottom: none; }

.token-header {
  background: var(--page-bg);
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
}

.token-cell { font-size: 14px; }

.token-cell code {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 13px;
  background: var(--page-bg);
  padding: 2px 6px;
  border-radius: 4px;
}
```

## Tone of Voice section

```html
<section id="voice" class="section">
  <div class="section-label">Voice</div>
  <h2 class="section-title">Tone of voice</h2>

  <div class="voice-principles">
    <div class="voice-card">
      <div class="voice-trait">[Trait name]</div>
      <div class="voice-description">[Description]</div>
    </div>
  </div>

  <div class="voice-examples">
    <div class="voice-do-dont">
      <div class="voice-column voice-do">
        <h4>Do</h4>
        <ul>
          <li>[Example]</li>
        </ul>
      </div>
      <div class="voice-column voice-dont">
        <h4>Don't</h4>
        <ul>
          <li>[Example]</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

## JavaScript

```javascript
// Scroll fade-in
const sections = document.querySelectorAll('.section');
const fadeObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.05 });
sections.forEach(s => { s.style.opacity = '0'; s.style.transform = 'translateY(20px)'; fadeObserver.observe(s); });

// Active sidebar link tracking
const allSections = document.querySelectorAll('.section[id]');
const links = document.querySelectorAll('.sidebar-link');
const navObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      links.forEach(l => l.classList.remove('active'));
      const id = e.target.id;
      links.forEach(l => {
        if (l.getAttribute('onclick') && l.getAttribute('onclick').includes(id)) {
          l.classList.add('active');
        }
      });
    }
  });
}, { threshold: 0.2, rootMargin: '-40px 0px -60% 0px' });
allSections.forEach(s => navObserver.observe(s));

// Animate score bar on scroll
const scoreBar = document.querySelector('.score-bar-fill');
if (scoreBar) {
  const scoreObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        scoreBar.style.width = scoreBar.dataset.width;
      }
    });
  }, { threshold: 0.5 });
  scoreObserver.observe(scoreBar.parentElement);
}

// CSS for fade-in animation
const style = document.createElement('style');
style.textContent = '.section.visible { opacity: 1 !important; transform: translateY(0) !important; transition: opacity 0.6s ease, transform 0.6s ease; }';
document.head.appendChild(style);
```

## Gradient section (if applicable)

```html
<h3 class="subsection-title">Gradients</h3>
<div class="gradient-grid">
  <div class="gradient-card">
    <div class="gradient-preview" style="background: linear-gradient(135deg, #3634F0, #CA00F9);"></div>
    <div class="gradient-info">
      <div class="gradient-name">Brand Gradient</div>
      <div class="gradient-spec">135deg: #3634F0 → #CA00F9</div>
    </div>
  </div>
</div>
```

```css
.gradient-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
  margin-bottom: 48px;
}

.gradient-card {
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  background: var(--card-bg);
}

.gradient-preview { height: 100px; }

.gradient-info { padding: 16px; }
.gradient-name { font-weight: 600; font-size: 14px; color: var(--text-primary); margin-bottom: 2px; }
.gradient-spec { font-size: 13px; color: var(--text-muted); font-family: 'SF Mono', 'Fira Code', monospace; }
```

## Do/Don't pattern (for logo, colour, voice sections)

```html
<div class="do-dont-grid">
  <div class="do-card">
    <div class="do-label">Do</div>
    <ul class="do-list">
      <li>Use on white or light backgrounds</li>
      <li>Maintain clearspace equal to logo height</li>
    </ul>
  </div>
  <div class="dont-card">
    <div class="dont-label">Don't</div>
    <ul class="dont-list">
      <li>Stretch, rotate, or apply effects</li>
      <li>Place on busy or low-contrast backgrounds</li>
    </ul>
  </div>
</div>
```

```css
.do-dont-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 32px;
}

.do-card, .dont-card {
  padding: 24px;
  border-radius: 12px;
}

.do-card { background: #F0FAF0; border: 1px solid #C8E6C9; }
.dont-card { background: #FFF5F5; border: 1px solid #FFCDD2; }

.do-label, .dont-label {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 12px;
}

.do-label { color: #2E7D32; }
.dont-label { color: #C62828; }

.do-list, .dont-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 14px;
  color: var(--text-secondary);
}

.do-list li::before { content: ""; display: inline-block; width: 6px; height: 6px; border-radius: 50%; margin-right: 10px; vertical-align: middle; }
.do-list li::before { background: #2E7D32; }
.dont-list li::before { content: ""; display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #C62828; margin-right: 10px; vertical-align: middle; }
```

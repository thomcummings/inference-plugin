---
name: brand-architecture
description: "Brand architecture and strategic foundations skill. Three phases: (1) brand architecture design — choosing branded house, hybrid, endorsed, or house of brands and structuring product/service hierarchy; (2) brand foundations — purpose, vision, mission, brand pillars, personality using Ogilvy Big ideaL and Arielle Jackson frameworks; (3) strategic narrative — the high-altitude company story about a shift in the world, following Andy Raskin's framework. Use whenever the user mentions brand architecture, branded house, brand hierarchy, product naming, purpose/vision/mission, brand pillars, brand personality, strategic narrative, company story, or symptoms like teams can't explain how products relate, no unifying story beyond the product pitch, or leadership can't articulate why the company exists. Produces foundational documents that sit upstream of messaging and language-market fit."
---

# Brand Architecture & Foundations

The strategic foundation layer for a company's brand. This skill builds the documents that rarely change but guide everything downstream: how the brand is structured, what the company stands for, and the high-altitude narrative that frames why the company matters in the world.

## Relationship to Other Skills

This skill sits in a specific position in the marketing strategy stack:

```
[Positioning]  →  [Brand Architecture & Foundations]  →  [Messaging Framework]  →  [Language-Market Fit]
     ↑                        ↑                                  ↓                         ↓
 "What are we,          "How is the brand              "What do we say              "What exact words
  for whom,              structured, what do            at company and               make prospects
  against what?"         we stand for, and              product level?"              feel like we've
                         what's the big story?"                                      read their minds?"
```

**Positioning is an input** — if the user has completed positioning work (for example a positioning canvas), that feeds into this skill as foundational context. If they haven't, this skill can work with whatever strategic clarity exists, but should flag where positioning gaps are causing problems.

**Messaging Framework is the output consumer** — the brand architecture, foundations, and strategic narrative produced here become the inputs that the Messaging Framework skill uses to build company and product messaging houses.

## Architecture

This skill has three distinct phases, each with its own reference file. **Determine which phase the user needs before loading a reference file.** Do not load all references at once.

### Phase 1: Architecture Design
**When to use:** The user needs to define or restructure the relationship between their company brand, products, services, and sub-brands.
**Reference:** `references/architecture.md`

### Phase 2: Brand Foundations
**When to use:** The user needs to develop or refine purpose, vision, mission, brand pillars, and/or brand personality.
**Reference:** `references/foundations.md`

### Phase 3: Strategic Narrative
**When to use:** The user needs to build the high-altitude company story — the narrative about a shift in the world that creates demand for the company's existence.
**Reference:** `references/narrative.md`

## Routing Logic

1. **If the user asks about how products/services relate to the brand** → Phase 1 (Architecture Design)
2. **If the user asks about purpose, vision, mission, values, pillars, or brand personality** → Phase 2 (Brand Foundations)
3. **If the user asks about the "big story," strategic narrative, company narrative, or why the company matters** → Phase 3 (Strategic Narrative)
4. **If the user asks to "build a brand from scratch" or do "brand strategy"** → Run Phase 1 → Phase 2 → Phase 3 in sequence
5. **If the user has a specific company/product and asks broadly about brand** → Start with Phase 1 to assess the structural picture, then determine which other phases are needed
6. **If the user already has architecture and foundations, and just needs the narrative** → Go directly to Phase 3

## Core Concepts (always in context)

### Brand Architecture Is Structure, Not Identity

Brand architecture defines the hierarchy and relationships between a company's brand(s), products, services, and other components. It answers: "How do our offerings relate to each other and to our parent brand?" This is structural strategy, not visual identity.

### The Architecture Spectrum

There are four primary models, with most companies landing somewhere between them:

- **Branded House:** Single unified brand across all products (e.g., Google, Apple, Atlassian). Strongest brand equity transfer, lowest overhead, dominant in B2B SaaS.
- **Endorsed Brands:** Sub-brands with visible connection to parent (e.g., Marriott Courtyard, Sony PlayStation). Balance of independence and equity transfer.
- **House of Brands:** Independent brands with no visible parent (e.g., P&G's Tide/Pampers/Gillette). Maximum flexibility, no equity transfer, highest cost.
- **Hybrid:** Combination of approaches across the portfolio (e.g., Adobe — Creative Cloud as umbrella, Photoshop as standalone recognition). Most common in complex, multi-product companies.

### Brand Foundations Are Beliefs, Not Slogans

Purpose, vision, and mission are internal strategic commitments that guide decision-making. They're not taglines. A well-articulated purpose should make some potential business decisions obviously wrong. If your purpose doesn't constrain you, it's not specific enough.

### Strategic Narrative Is Not a Sales Pitch

A strategic narrative (Andy Raskin's framework) is a story about a change in the world that creates demand for the company. It's not about the product — it's about why the world needs what the company represents. The product appears as the vehicle for reaching the "Promised Land," not as the hero of the story. Great strategic narratives power everything: sales, marketing, fundraising, product development, recruiting.

## Working With Incomplete Information

Brand architecture work often happens when a company is growing fast and things are messy. When information is missing:

1. **Flag what's missing** — clearly identify which components need stakeholder input or market data.
2. **Provide hypothesis-quality answers** — frame incomplete components as "working hypotheses to validate with leadership" rather than leaving them blank.
3. **Recommend the right conversations** — specify which stakeholders (CEO, product leads, customer-facing teams) need to be in the room for which decisions.
4. **Surface tensions explicitly** — if different parts of the business imply different architectural or narrative choices, name the tension rather than papering over it.

## Output Formats

### Brand Architecture Map (Phase 1 output)
A visual/structural document showing:
- Architecture model selected (with rationale)
- Hierarchy diagram: parent brand → product tiers → features/services
- Naming strategy and rules
- Brand expression rules (what's consistent vs. what varies across levels)
- Growth guidelines (how new products/services enter the architecture)

### Brand Foundations Document (Phase 2 output)
A strategic document containing:
- Purpose statement (why the company exists beyond profit)
- Vision statement (the future state the company is working toward)
- Mission statement (how the company pursues the vision, what it does and for whom)
- Brand Pillars (3-5 core thematic commitments)
- Brand Personality (character traits, voice principles, archetype if useful)
- The Big ideaL (Ogilvy framework output if applicable)

### Strategic Narrative (Phase 3 output)
A narrative document structured as:
- The Shift: What's changing in the world
- The Stakes: Why there will be winners and losers
- The Promised Land: The future state for those who adapt
- The Magic Gifts: Capabilities that help get there (introducing the company)
- The Evidence: Proof it's already working
- Plus: verbal identity recommendations (1-5 terms the brand should own)

## Usage Instructions

1. Determine which phase the user needs (see Routing Logic above)
2. Read the appropriate reference file using the `view` tool
3. Gather baseline context about the company (see below)
4. Follow the phase-specific methodology in that reference
5. Produce the appropriate output format
6. If running the full process, proceed to the next phase

### Baseline Context to Gather

When the user provides a company to work on, always gather this context first:

- What does the company do? (in the user's current words)
- What products/services exist today? How do they relate?
- Who are the primary audiences/customer segments?
- What positioning work exists? (a positioning canvas, or informal positioning)
- What brand assets exist already? (purpose, vision, mission statements, brand guidelines, messaging docs)
- What triggered the need for this work now? (growth, new product, rebrand, market shift, internal confusion)
- Who are the key stakeholders for brand decisions? (is the CEO involved?)

## Method lineage

Use as lineage, not as copy:

- Andy Raskin's strategic narrative (name the shift, winners and losers, the promised
  land): the structure of `references/narrative.md` is adapted from his published
  writing.
- Woden's messaging hierarchy: the verbal identity section.
- Donald Miller's StoryBrand (the customer as hero, the company as guide). StoryBrand
  is Miller's trademark.
- Inference doctrine: architecture follows audience and trust transfer, foundations
  follow positioning.

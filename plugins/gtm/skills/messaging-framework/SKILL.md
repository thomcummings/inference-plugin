---
name: messaging-framework
description: "Build and manage messaging frameworks — the operational documents defining what a company says at every level. Three modes: (1) company messaging house — boilerplates, value propositions, proof points at multiple lengths; (2) product messaging houses — per-product umbrella statements cascading to benefits, features, use cases, and sales assets; (3) persona and competitive messaging — adapting messages for buyer personas and building differentiation talk tracks. Use whenever the user mentions messaging house, messaging framework, messaging hierarchy, boilerplate, value propositions, product messaging, persona messaging, competitive talk tracks, sales enablement copy, or symptoms like teams describing the company differently, sales not knowing what to say, or needing copy for product pages. Produces living operational documents used daily by marketing, sales, and content teams, sitting downstream of brand architecture and positioning."
---

# Messaging Framework

The operational messaging layer that translates strategy into the words people actually use. This skill builds the documents that marketing, sales, content, and support teams reference constantly — the messaging houses, persona messaging, and competitive talk tracks.

## Relationship to Other Skills

```
[Positioning]  →  [Brand Architecture]  →  [Messaging Framework]  →  [Language-Market Fit]
                                                    ↑
                                              YOU ARE HERE
```

**Inputs this skill expects:**
- **From Positioning:** Competitive alternatives, differentiated capabilities, differentiated value themes, best-fit customers, market category
- **From Brand Architecture & Foundations:** Brand architecture model, purpose/vision/mission, brand pillars, brand personality, strategic narrative (shift, promised land, magic gifts)

**If these inputs don't exist:** The skill can still work — it will produce hypothesis-quality messaging and flag which upstream work would strengthen it. Many companies need messaging before they've completed formal positioning or brand architecture work. That's fine. Build what you can, note what's missing.

**What consumes this skill's output:**
- **Language-Market Fit:** Takes messaging framework outputs and tests/refines the customer-facing words for conversion
- **Content teams:** Use messaging houses as the source of truth for all content
- **Sales teams:** Use competitive messaging and talk tracks in conversations
- **Marketing teams:** Use value propositions and product messaging across campaigns
- **PR/Comms:** Use boilerplates and descriptions for media and external communications

## Architecture

This skill has three modes, each with its own reference file. **Determine which mode the user needs before loading a reference file.** Do not load all references at once.

### Mode 1: Company Messaging House
**When to use:** The user needs to build or update the company-level messaging — boilerplates, value propositions, descriptions at multiple lengths, proof points, and brand-level copy.
**Reference:** `references/company-messaging.md`

### Mode 2: Product Messaging Houses
**When to use:** The user needs to build messaging for specific products, services, or features — umbrella statements, benefit messages, feature descriptions, use cases.
**Reference:** `references/product-messaging.md`

### Mode 3: Persona & Competitive Messaging
**When to use:** The user needs to adapt core messages for different buyer personas, or build competitive differentiation talk tracks for sales.
**Reference:** `references/persona-competitive.md`

## Routing Logic

1. **If the user says "we need a messaging house" or "build our messaging framework"** → Start with Mode 1 (company messaging), then proceed to Mode 2 if products exist.
2. **If the user asks about a specific product's messaging** → Go directly to Mode 2.
3. **If the user asks about persona-specific messaging or competitive talk tracks** → Go directly to Mode 3.
4. **If the user wants the full framework end-to-end** → Run Mode 1 → Mode 2 → Mode 3 in sequence.
5. **If the user asks to review or improve existing messaging** → Determine which level the existing messaging covers, load the relevant mode, and run the quality checks from that reference.

## Core Concepts (always in context)

### Messaging Is Not Positioning

Positioning is an internal strategic exercise — it defines what you are, for whom, against what alternatives. Messaging is the external expression — how you communicate that positioning to the world. Positioning should remain consistent; messaging can and should adapt by audience, channel, and context. Positioning is the input. Messaging is the output.

### Messaging Is Not Copywriting

A messaging framework provides the strategic raw material — the approved claims, value propositions, proof points, and talking points. Copywriting is the creative execution — turning that raw material into compelling headlines, body copy, and campaigns. The messaging framework is the "what to say." Copywriting is the "how to say it." Content creators should use the messaging framework as a brief, not as final copy.

### The Message House Metaphor

The most common structural metaphor for messaging frameworks:

- **Roof:** The strategic narrative / overarching brand story (from Brand Architecture skill)
- **Pillars (3-5):** Value themes that support the roof. Each pillar represents a major claim about value the company creates.
- **Foundation:** Positioning statement, proof points, evidence, and facts
- **Rooms:** Persona-specific or product-specific adaptations of the above

This metaphor works because it captures both the hierarchy (roof sits on pillars, pillars stand on foundation) and the modularity (different rooms for different audiences).

### The Benefit Hierarchy

Messages should be structured at multiple altitudes, from aspirational to concrete:

```
ASPIRATIONAL BENEFITS ── Why should users care? (business transformation, competitive advantage)
        ↓
EMOTIONAL BENEFITS ───── How should users feel? (confident, empowered, in control, relieved)
        ↓
FUNCTIONAL BENEFITS ──── What does the product enable? (ease of use, speed, collaboration)
        ↓
FUNCTIONAL ATTRIBUTES ── What does the product offer? (features, specifications, capabilities)
```

Most B2B companies over-index on functional attributes (features) and under-invest in the higher levels. The best messaging frameworks include all four levels and give guidance on when each level is appropriate (top-of-funnel → aspirational; bottom-of-funnel → functional).

### Length Variants Are Essential

Every key message needs to exist at multiple lengths:
- **One-liner:** 10-15 words. For social bios, elevator pitches, quick introductions.
- **Short:** 1-2 sentences. For email footers, brief descriptions, ad copy.
- **Medium:** 3-4 sentences. For about pages, partner descriptions, press mentions.
- **Long:** 1-2 paragraphs. For website pages, detailed materials, press release boilerplates.

This is not optional. Without length variants, teams will ad-lib their own shortened versions, and consistency breaks down.

### Proof Points Are Non-Negotiable

Every claim in the messaging framework must be supported by evidence. Types of proof:
- **Metrics:** Numbers that demonstrate value (200k+ participants, 50%+ response rates, <2 hours to dataset)
- **Customer evidence:** Testimonials, case studies, logos
- **Third-party validation:** Awards, analyst recognition, media coverage, academic citations
- **Product evidence:** Features, certifications, compliance standards

A claim without proof is an opinion. A claim with proof is a message.

## Quality Framework

Every message produced by this skill should pass Peep Laja's four-point validation:

1. **Clarity:** Does the audience immediately understand what's being said? No jargon, no ambiguity, no "burning calories to understand."
2. **Relevance:** Does the audience see themselves in it? "This is for me" vs. "this is generic."
3. **Value:** Does the audience see the value proposition? The "aha moment" should be immediate.
4. **Differentiation:** Does the audience understand what's different vs. alternatives? If you removed the company name, could a competitor use this message?

Flag any message that fails on one or more of these criteria and suggest revisions.

## Working With Incomplete Information

Messaging work often starts before all upstream work is complete. When inputs are missing:

1. **No positioning?** Build messaging from whatever strategic clarity exists (founder interviews, website copy, sales materials). Flag that positioning work upstream would sharpen everything.
2. **No brand architecture?** Assume a branded house (most B2B SaaS) and build accordingly. Note where architectural decisions would help.
3. **No strategic narrative?** Build the messaging house without a "roof" narrative. The pillars can still stand. Flag that narrative work would unify the message.
4. **No customer research?** Build hypothesis-quality messaging and strongly recommend customer interviews (connect to LMF skill's interview prep mode).

## Usage Instructions

1. Determine which mode the user needs (see Routing Logic above)
2. Read the appropriate reference file using the `view` tool
3. Gather baseline context about the company and existing messaging
4. Follow the mode-specific methodology in that reference
5. Produce the appropriate output format
6. Validate against the quality framework
7. If running the full process, proceed to the next mode

### Baseline Context to Gather

When the user provides a company to work on, gather:

- What messaging assets exist today? (website copy, sales decks, one-pagers, about pages)
- What upstream strategy exists? (positioning, brand architecture, narrative)
- Who will use this messaging framework? (marketing only? sales too? partners?)
- What products/services need messaging?
- What personas/buyer roles need to be addressed?
- Who are the primary competitors the sales team encounters?
- What's the most common way people discover the company?
- What's broken about the current messaging? (inconsistency? vagueness? outdated?)

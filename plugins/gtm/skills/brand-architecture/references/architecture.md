# Phase 1: Architecture Design

How to define or restructure the relationship between a company's brand, products, services, and sub-brands.

## Table of Contents

1. When Architecture Work Is Needed
2. The Architecture Spectrum (Deep Dive)
3. Decision Framework: Choosing a Model
4. Building the Architecture Map
5. Naming Strategy
6. Growth Rules
7. Common Pitfalls

---

## 1. When Architecture Work Is Needed

Architecture work is triggered by structural complexity. The most common triggers:

**The Second Product Problem:** The company launches a second product or enters a new market. Should it be "CompanyName for X" or get its own name? Without architecture, this becomes an ad-hoc political decision.

**The Acquisition Problem:** A company acquires another brand. How does it fold into the existing structure? Keep the name? Sunset it? Endorse it?

**The Audience Split Problem:** Different audiences (e.g., a marketplace's buyers vs. sellers) experience the brand differently. How much should the brand flex vs. stay consistent?

**The Feature-to-Product Problem:** Something that was a feature grows important enough to be marketed independently. When does a feature become a product? What naming conventions apply?

**The Confusion Problem:** Customers can't articulate the relationship between what the company offers. Sales is explaining the portfolio structure instead of selling value.

### Diagnostic Questions

Ask the user these to assess the current state:

- Can a new customer understand your full offering in under 60 seconds?
- When you launch something new, does it automatically benefit from your existing reputation?
- Can your sales team explain how everything connects without a diagram?
- Do different teams describe the company's structure differently?
- Are there naming inconsistencies across products/services?

---

## 2. The Architecture Spectrum (Deep Dive)

### Branded House

**How it works:** One brand name across everything. Products may have descriptive names but not brand-level identities.

**Examples:** Google (Search, Maps, Drive, Docs), Apple (iPhone, iPad, Mac), Atlassian (Jira, Confluence), Salesforce (Sales Cloud, Service Cloud)

**Best for:**
- B2B SaaS companies (dominant model in tech)
- Companies where trust transfers across the portfolio
- Companies with limited marketing resources (one brand to build, not many)
- Products that share an audience or buying centre

**Naming pattern:** `[Brand] [Descriptive Name]` or just `[Descriptive Name]` understood as part of the brand. Examples: "Google Docs," "Slack Huddles."

**Key rule:** Everything amplifies the single brand. New launches inherit brand equity. Brand expression (logo, colour, voice) stays consistent. Individual products may have visual treatments but not independent identities.

**When it breaks:** When a product serves a fundamentally different audience with different trust signals, or when a product needs to distance itself from the parent brand's associations.

### Endorsed Brands

**How it works:** Sub-brands have their own identities but carry a visible endorsement from the parent. The parent provides credibility; the sub-brand provides specificity.

**Examples:** Marriott Courtyard by Marriott, Sony PlayStation, Ralph Lauren's Polo

**Best for:**
- Companies whose products serve meaningfully different audiences
- Acquisitions where the acquired brand has significant equity worth preserving
- Products that need to establish distinct positioning while still leveraging parent trust

**Naming pattern:** `[Sub-brand] by [Parent]` or `[Parent] [Sub-brand]` where the sub-brand has its own visual identity.

**Key consideration:** Endorsement is not free — it creates a promise. If the endorsed brand disappoints, it reflects on the parent. Build quality gates.

### House of Brands

**How it works:** Multiple independent brands with no visible connection to the parent company.

**Examples:** P&G (Tide, Pampers, Gillette), Unilever (Dove, Ben & Jerry's), LVMH (Louis Vuitton, Moët, Hennessy)

**Best for:**
- Consumer packaged goods companies targeting diverse demographics
- Companies where products compete in the same category (rare in B2B)
- Situations where the parent brand association would hurt the product

**Rarely appropriate for:** B2B SaaS, startups, or any company that can't afford to build multiple brands from scratch.

### Hybrid

**How it works:** Different parts of the portfolio get different architectural treatment based on what each requires.

**Examples:** Adobe (Creative Cloud as branded house umbrella, but Photoshop maintains standalone recognition), Microsoft (Windows, Office, Xbox operate semi-independently under the Microsoft umbrella), Amazon (branded house for core commerce, but AWS has distinct positioning, and Alexa/Ring/Whole Foods are endorsed or quasi-independent).

**Best for:**
- Complex companies with multiple business lines serving different markets
- Companies that have grown through acquisition alongside organic product development
- Situations where one-size-fits-all architecture would force unnatural constraints

**Key consideration:** Hybrid requires clear rules about which products get which treatment. Without rules, it becomes "accidental inconsistency" rather than "intentional hybrid."

---

## 3. Decision Framework: Choosing a Model

Work through these questions with the user:

### Question 1: Audience Overlap
**How much do your products/services share a buyer?**
- Same buyer across everything → Branded House
- Mostly same buyer, with some exceptions → Branded House with expression flex (like Airbnb's guest and host experiences)
- Fundamentally different buyers → Endorsed Brands or Hybrid

### Question 2: Trust Transfer
**Would a customer who trusts Product A automatically give Product B a chance?**
- Yes, strong trust transfer → Branded House
- Partially — depends on the product → Endorsed Brands
- No — different trust signals needed → House of Brands (rare in B2B)

### Question 3: Marketing Resources
**How many brands can you realistically build and maintain?**
- One is hard enough → Branded House
- Two to three with clear differentiation → Endorsed Brands or Hybrid
- Unlimited budget → Still probably Branded House in B2B

### Question 4: Product Interdependence
**Do your products require each other to function?**
- Yes, ecosystem model → Branded House (products are features of the platform)
- Some independent, some connected → Hybrid
- Fully independent → Endorsed or House of Brands

### Question 5: Growth Trajectory
**What will the portfolio look like in 3-5 years?**
- More products for the same audience → Branded House scales well
- Expansion into adjacent markets → Hybrid gives flexibility
- Diversification into unrelated markets → Plan for endorsed brands

### Making the Call

For most B2B SaaS companies, especially those with <$100M ARR and fewer than 5 products: **Branded House is the right answer.** The question is not whether to use it, but how to implement it well. The research supports this — building one strong, recognisable brand is more efficient than spreading resources across multiple brands.

Present the recommendation with clear rationale tied to the diagnostic questions above. If the user disagrees or has constraints you didn't see, explore the alternatives.

---

## 4. Building the Architecture Map

The architecture map is the primary output. It's a visual/structural document that shows relationships.

### Structure Template

```
[PARENT BRAND]
├── Brand Views (audience-specific brand expressions)
│   ├── [Brand] for [Audience A]
│   └── [Brand] as [Employer]
├── Core Product
│   ├── [Platform/Core Product Name]
│   └── Core Features
│       ├── [Feature 1 — named]
│       ├── [Feature 2 — named]
│       └── [Feature N]
├── Additional Products
│   ├── [Product A]
│   ├── [Product B]
│   └── [Product C]
├── Services
│   ├── [Service A]
│   └── [Service B]
└── Future Slots
    ├── [Planned Product/Service]
    └── [Growth Direction]
```

### For Each Level, Define:

**Naming rules:** How things at this level get named. Descriptive? Evocative? Branded?

**Brand expression rules:** What stays consistent with the parent brand, what can flex. Typically: logo, primary colour, and voice stay consistent; secondary colours, imagery, and tone can flex.

**Marketing treatment:** How things at this level get marketed. Do they get their own landing pages? Sales materials? Or are they features within a larger product page?

**Audience ownership:** Who is the primary audience for this level?

### Writing the Map Narrative

Don't just produce a diagram — explain the decisions. For each structural choice, include:
- What it is
- Why this model/placement was chosen
- What it means in practice for marketing and sales
- How new additions at this level should be handled

---

## 5. Naming Strategy

Naming follows architecture. The rules depend on the model:

### Branded House Naming Rules

**Products:** Can be descriptive (Google Docs), evocative-but-clearly-connected (Slack Huddles), or simply functional (Platform, API). Avoid giving products brand-level names that could compete with the parent.

**Features:** Should be descriptive and clearly subordinate. "Smart Formatting" not "SmartFormat™" — unless the feature is so significant it functions as a product differentiator worth naming (like Huddles).

**Test:** If a customer could mistake the product/feature name for a separate company, it's named too independently for a Branded House.

### When to Name Something

Not everything needs a name. Apply this filter:

- **Name it** if: customers need to reference it in conversation, it has its own value proposition, sales will pitch it independently, or it's a meaningful differentiator.
- **Don't name it** if: it's a feature within a larger product, customers will never ask for it by name, or naming it would add confusion to the portfolio.

### Naming Quality Checks

Good product/feature names in a Branded House:
- Are easy to say, spell, and remember
- Suggest what the thing does (or at least don't contradict it)
- Work across markets and languages (watch for unintended meanings)
- Don't require explanation to understand ("Huddles" works for Slack because it maps to a quick, informal team call)
- Are clearly subordinate to the parent brand

---

## 6. Growth Rules

Every architecture needs rules for how new things enter. Without these, the architecture degrades with each launch.

### Decision Tree for New Offerings

```
Is it a new capability within an existing product?
  → YES: It's a FEATURE. Name descriptively if needed. Market as part of the product.
  → NO: Continue...

Does it require the core product/platform to function?
  → YES: It's an ADDITIONAL PRODUCT. Name it. Market as part of the ecosystem.
  → NO: Continue...

Does it serve the same primary audience as existing products?
  → YES: Consider it a product within the Branded House. Name and market accordingly.
  → NO: Continue...

Does it serve a fundamentally different audience with different trust signals?
  → YES: Consider an endorsed brand or brand view (like "Brand for Audience X").
  → NO: Default to Branded House treatment.
```

### Rules to Document

- **Feature vs. Product threshold:** What criteria determine when something is "big enough" to be a product vs. a feature? (e.g., has its own value proposition, can be pitched independently, has distinct pricing)
- **Naming approval:** Who approves new product/feature names? (typically marketing + product lead)
- **18-month rule for acquisitions:** Acquired brands maintain their identity for up to 18 months to preserve existing customer relationships, then migrate to the architecture model.
- **Sunset protocol:** How are deprecated products/features phased out of the architecture?

---

## 7. Common Pitfalls

**Over-architecting too early:** A 5-person startup doesn't need a formal architecture document. The trigger for serious architecture work is typically the second sub-brand or first market expansion.

**Architecture by committee:** If every stakeholder gets a vote on naming and hierarchy, you'll end up with an incoherent structure. Brand architecture decisions should be led by marketing with CEO sign-off.

**Confusing architecture with identity:** Architecture is structure. Identity is visual and verbal expression. You can redesign identity without changing architecture, and vice versa. Don't conflate the two projects.

**Ignoring the internal audience:** Architecture isn't just customer-facing — it's how internal teams understand the portfolio. If sales can't explain the structure, it's too complex.

**Building for today's ego, not tomorrow's growth:** The CEO wants to name a feature after their firstborn. The VP wants their division to be a sub-brand. Architecture should serve customer understanding and business growth, not internal politics.

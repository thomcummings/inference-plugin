---
name: icp
description: >-
  Define, score, and monitor a company's ideal customer profile and buyer/user
  personas — the buyer-insight foundation the rest of a marketing strategy stands
  on. Produces a narrow, ranked, evidence-graded ICP built from a composite of
  firmographic, psychographic and product-telemetry signals, an explicit anti-ICP,
  personas grounded in jobs-to-be-done and the buyer's own language, a fit-scoring
  rubric for grading real leads, and a drift watch for when reality diverges from
  the definition. Use when a company is unclear who it targets, is "selling to
  everyone", needs personas, is building or grading an outbound/ABM list, or before
  positioning, messaging or channel work that depends on knowing the buyer. Works
  whether there are customers and usage data to mine or it's early and priors-led.
  Not a demographic character-sketch generator, and not a positioning skill — this
  feeds it.
---

# ICP & buyer-insight

Define who a company sells to, sharply enough that you can **grade a real lead
against it** and **notice when it drifts** — not just hang a poster. Three jobs, one
skill, layered so it degrades gracefully with the data available:

1. **Define** — the ranked, composite ICP + anti-ICP + personas (always runs).
2. **Score** — a fit-scoring rubric to grade any account or lead (switches on when
   there's enough signal).
3. **Monitor** — drift detection: is who you're actually winning and keeping still
   the ICP you defined? (a standing routine).

## First, the words — because these four get muddled
Get the taxonomy straight; the confusion is half the problem.

- **Segmentation** — dividing the *whole market* into groups by shared traits. The
  map of the territory. Descriptive, plural.
- **ICP** — the *choice* of which segment(s) to pursue, plus the definition of the
  best-fit *account*. Prescriptive, company-level.
- **Persona** — the *people* inside that account: buyer, user, champion. Roles plus
  their jobs, pains, and language. Human-level.
- **Jobs-to-be-done** — the *progress the buyer is trying to make*; why they hire
  you. Situation-level.

The stance that matters: **JTBD is not a fourth peer — it's the spine.** You segment
by the job, and the ICP and personas fall out of *who has that job most acutely and
can act on it*. Method lineage: JTBD (Moesta / Christensen).

## What good looks like — the opinions this skill holds
- **Ranked, not flat.** Don't ship a list of equal segments. Ship a **portfolio**:
  one primary beachhead now, expansion tiers held explicitly, re-ranked as the
  product footprint and the company's stage grow. Early-stage leans hard on the
  primary; later-stage can carry more.
- **Operational, never fictional.** Every attribute must either *filter a list* or
  *change the message*. No "Marketing Mary, 38, enjoys yoga." If it does neither,
  cut it.
- **The trigger is the ICP; firmographics are just the filter.** If you can't name
  the observable in-market signal, you have a demographic, not an ICP.
- **Who you can win and keep — not who you'd like.** Anchor on retention and
  expansion evidence, not aspiration or a slice of a TAM number.
- **Extrapolate from your best customers, not your average.** Define the ideal from
  the high-expectation customers — the ones who'd be genuinely disappointed to lose
  you, who adopt deepest and expand. Method lineage: the "very disappointed" PMF
  signal (Sean Ellis) and the high-expectation-customer approach (Rahul Vohra,
  Superhuman).
- **Watch what they do; discount what they say.** Behaviour outranks stated
  preference (see the evidence hierarchy).
- **The bar is recognition, not description.** It's done when a real buyer would say
  "are you spying on me?" — not when the profile is merely complete.

## The composite — what an ICP is actually made of
Build the ICP from three layers, not one:

- **Firmographic** — who the company is (size, stage, type, the few traits that
  genuinely separate fit from non-fit).
- **Psychographic / behavioural** — how they think and buy (beliefs, buying process,
  risk appetite, the status quo they're leaving).
- **Product telemetry** — what they actually *do* in the product. This is the truth
  serum: where usage data exists, it **outranks** the firmographic guess, because
  deep-adopters, expanders and low-churn accounts reveal the real ideal customer.

Graceful degradation: firmographic + psychographic is the floor you can always
build; telemetry is the top layer, used wherever the data exists. Always name which
layers you actually had.

## The evidence hierarchy (climb as high as the data allows)
Product telemetry / behaviour → won-loss (CRM) data → recorded sales calls →
community rants (raw, honest, vendor-free) → surveys / stated preference → founder or
team gut. Use the highest tiers available; mark anything from the lower tiers as
hypothesis. Never invent customers or data.

## Layer 1 — Define (always runs)
1. **Orient & diagnose.** Read any existing company, positioning, persona or usage
   context in the workspace, plus what the user hands over. Decide evidence-rich
   (real customers + data) vs evidence-thin (early, priors-led).
2. **Separate channels from segments (do this before ranking).** Check whether any
   apparent "segment" is actually a *channel or partner motion* — a platform that
   would resell, embed or refer you — rather than an end-customer ICP. Pull those
   out and treat them as go-to-market routes, not ICP entries. Confusing a channel
   with an ICP is a common and costly error; name it explicitly when you see it.
3. **Build the ranked ICP portfolio.** The ideal *company* per the composite, as a
   primary beachhead plus expansion tiers, each with a confidence grade (validated
   vs hypothesis) and a review/kill condition.
4. **Force the anti-ICP.** Who looks plausible but should be declined — long cycles,
   low ACV, high churn, high support load, no real pain, no strategic fit. Half the
   value is here.
5. **Build the personas.** Buyer and user (others only where they change the deal),
   each with: jobs-to-be-done, pains and the KPIs they're measured on, **trigger
   events** (required), **watering holes** (where they actually pay attention; feeds
   channel work), and **voice-of-customer** language captured verbatim.

## Layer 2 — Score (switches on when there's enough signal)
Turn the definition into a **fit-scoring rubric**: the weighted, composite criteria
(firmographic + behavioural + telemetry + trigger signals) that grade any account or
lead for fit, with a clear good / marginal / poor banding. This is what makes the ICP
usable in the wild — prioritising outbound, qualifying inbound, ranking a
target-account list. Boundary: this is the *strategic fit-scoring rubric*, not a full
operational MQL/lead-scoring system — hand the plumbing (point allocation in the
CRM/MAP, score decay, routing) to a RevOps process downstream.

When the rubric has to be applied the same way by a person, a script and an agent
(for example to build an ABM target-account list), make it **additive and
reproducible**: four or five weighted criteria summing to 100 (e.g. vertical or
sub-segment, company stage or maturity, usage or volume potential, serviceable
location), five bands from "not ICP" to "champion", then **overrides applied after
the score** — hard disqualifiers (the anti-ICP) and force-qualify rules (active
product usage, a booked demo, a strategic partner). Add a **pre-enrichment screen**
for the one property that most often kills fit, and check it before spending
enrichment credits. Derive the point tables from the client's own won deals; never
reuse another client's. Keep the numeric rubric in one canonical place and the
qualitative detail in the ICP document.

## Layer 3 — Monitor (a standing routine)
**Drift detection.** On a cadence, diff *who you're actually winning, keeping and
expanding* (recent closed-won, churn, expansion, telemetry) against the *defined
ICP*. Flag divergence plainly — "your last ten closed-won sit in a segment your ICP
doesn't describe." Drift is the signal to **re-rank the portfolio**, not to
panic-redefine from scratch. It reuses the scoring rubric: the fit-score distribution
of recent wins is the drift gauge.

## When NOT to use
- The buyer is already sharp, evidenced and current → go to the work that needs it.
- You need conversion *language* from a known buyer → that's a copy/language task
  this feeds.
- A one-off "who'd buy this feature" aside → just answer.

## Voice
Clear, concise, plain language. Lead with the answer. Confidence lives in the
evidence, not in adjectives. Ask when a call hinges on missing evidence rather than
guessing.

## Non-negotiables (quality guarantees, not refusals)
1. **Open with the lead** — max 3 lines (primary segment, the job, the sharpest
   insight or call) before any of the detail. Always.
2. Taxonomy kept straight; the chosen segment named and the job it serves stated.
3. **Channels separated from segments** — a partner/reseller/embed motion is a
   route to market, not an ICP entry; name it as such.
4. Ranked portfolio, not a flat list; the primary beachhead explicit.
5. Composite where possible; the layers used named; telemetry outranks guess.
6. Trigger events present, anti-ICP present, voice-of-customer captured verbatim.
7. Every claim graded (validated vs hypothesis); lower-tier evidence labelled.
8. A fit-scoring rubric wherever signal allows; a drift watch defined.
9. Method lineage credited where a framework is leaned on.
10. Saved as a draft/working version where status is tracked; confirm before it's
    treated as agreed; never silently overwrite an existing, agreed ICP.

## Output template (a default scaffold — adapt to the case, don't pad it)
Save the ICP where the workspace's conventions indicate, or ask. Fill what the
evidence supports; keep the grades honest.

```
# ICP — [company]

> Lead (always first, max 3 lines): primary segment · the job it serves · the single sharpest insight or call. The detail follows.

Chosen segment & the job it serves: …
Layers used: firmographic / psychographic / telemetry  (note which)

## Ranked ICP portfolio
### Primary (beachhead)   [confidence: validated | hypothesis]
- Firmographic filter: …
- Psychographic / behavioural: …
- Telemetry signals (if any): …
- Trigger events (required): …
- Review / kill condition: …
### Tier 2 / expansion   (re-rank as stage & footprint grow)
- …

## Anti-ICP (who to decline)
- …

## Personas
### Buyer  — jobs-to-be-done / pains & KPIs / triggers / watering holes / VOC verbatim
### User   — …

## Fit-scoring rubric   (Layer 2 — where signal allows)
- Weighted criteria + good / marginal / poor banding: …

## Drift watch   (Layer 3)
- Signals to monitor, cadence, divergence threshold: …

## Provenance
- Evidence used (by tier) + method lineage: …
```

## Output
The ranked composite ICP + anti-ICP + personas, a fit-scoring rubric where signal
allows, and a defined drift watch — as one structured document on the template, with
voice-of-customer captured verbatim and the downstream handoffs (positioning,
conversion copy, channel strategy) named. Always open with the lead (max 3 lines:
primary segment, the job, the sharpest insight) before the detail.

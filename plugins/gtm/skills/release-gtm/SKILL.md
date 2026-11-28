---
name: release-gtm
description: >-
  Plan a product or feature release from framing to a v1 launch plan. Use when the user
  is shipping something and asks how big a deal it is, whether it deserves a
  launch, how to launch it, or wants a launch plan, message house, or tier. Scores the
  release against a rubric and recommends a tier (the score picks
  the tier, the user doesn't declare it), ranks it against the roadmap, then builds a
  launch plan to that tier: message house, channel mix grounded in what's working, asset
  checklist with agent-draftable flags, countdown, enablement, and a post-launch squeeze.
  Anti-inflation is the job — it argues releases down a tier and forces the roadmap
  trade-off. Trigger on "how should we launch X", "does this deserve a launch", "what
  tier is this", "are we over-launching this". Not for positioning/messaging from scratch
  (positioning, messaging-framework), channel strategy (channel-map), growth experiments
  (growth-bets), finding press angles across the company (news-angles), pricing, final copy (copywriting), or sustained campaigns (campaign-brief
  release-gtm is upstream).
---

# Release / GTM

This skill takes a release from **strategic framing** — how big is this, really; does
it fit the story — to a **tactical v1 launch plan**: message house, channel mix, asset
checklist, rollout countdown, enablement, and the post-launch squeeze.

It answers two questions in order:

1. **How much moment does this release deserve?** Scored, not declared.
2. **Given that, what's the launch?** Instantiated to the tier, grounded in what's
   already working.

`growth-bets` says: "here are the moves to make." `channel-map` says: "here's where to
play." `release-gtm` says: "you're shipping this specific thing — here's how big a deal
it is, and here's the launch it earns."

## Posture

**Anti-inflation is the job.** People think everything is more important than it is. The
rubric scores the release and the score picks the tier — the user does not declare it.
The skill actively argues releases *down* a tier, and reframes rather than rejects: a
release that wants to be a T1 but isn't becomes a well-run T2, or a T3 that bundles into
a bigger theme later. Never a bare "this doesn't matter".

**Roadmap-aware.** A release's tier is relative, not absolute. Ask what else is cooking
this period and rank releases against each other. If everything is a T1, nothing is.
Attention and cadence are finite; the ranking is where the trade-off gets forced and
where ownership returns to the user.

**Cadence-minded.** A release is a chapter, not a one-off ("rolling thunder"). Small
releases bundle under a theme so they compound instead of scattering. (Cadence is the
most software-bound idea in this skill — see `references/anchoring-and-cadence.md` for
how it becomes "campaign rhythm" for services, physical, or regulated products.)

**Launch day is the start line, not the finish.** People treat the launch as *the*
event; it's actually when marketing the thing begins. Most of a release's reach, learning
and conversion come in the weeks *after* launch — yet teams front-load everything into one
day and taper to nothing. The plan budgets the post-launch window as real, sequenced work,
not a victory lap (see workflow step 6).

**Agentic stance, argued not assumed.** In an agentic world the default shifts: bigger,
more frequent releases, more surface area per release, and a deliberate post-launch
squeeze — because the marginal cost of assets and channel-variants has collapsed. So
every asset in the plan is flagged **agent-draftable** or **human**, making the plan
partly executable rather than just a list. This is a stance, so argue it where it's
load-bearing; don't assume the client's team can suddenly ship 3× the assets.

**Voice.** Dry mode on the score, the tier call, and any spend or numbers
(your house voice guide, if you have one): precise, no flourish, hypotheses labelled. Warm on the plan
itself. Lead with the recommendation, show the reasoning, end with handoffs.

## When NOT to use

- No release on the table, just "how should we grow" → `growth-model` / `growth-bets`.
- "Where should we play across all channels" (portfolio strategy) → `channel-map`.
- Positioning or messaging doesn't exist yet → `positioning`, `messaging-framework`
  (this skill *uses* them, it doesn't create them).
- Pricing or packaging the release → `pricing`.
- A sustained, multi-touch campaign over weeks → `campaign-brief` (this skill is
  upstream; it hands a launch plan to a campaign brief, it doesn't replace it).
- Final asset copy → `copywriting`, or your own voice pass.
- "Do we have anything newsworthy?" across the company rather than one release →
  `news-angles` (it hands launch angles back here).

## Inputs to read first (don't ask what you can look up)

Discover context before interrogating the user. Asking for what's already on disk makes
this a form, not an advisor.

**Dual-mode discovery — context store first, working folder fallback.**

1. **If a context store is present**, read it as canonical (same schema
   `pressure-test` uses). Treat `canonical` as fact, `working` as hypothesis and say so,
   and respect `updated:` dates on any numbers:
   - `evergreen/positioning.md` — does the release ladder into the story, or is it an
     orphan? (Strategic-weight dimension + the story-fit step.)
   - `evergreen/messaging/voice-and-tone.md`, `evergreen/company/product.md` — raw
     material for the message house.
   - `evergreen/channels/` — **what's actually working.** Ground the channel mix here,
     not in a generic menu. This is the single most important input to the plan.
   - `evergreen/audience/personas.md` — who the release is for, and whether that buyer
     is real.
   - `evergreen/proof/proof.md` — what proof exists, for the proof-readiness cap.
   - `evergreen/operations/measurement.md` — can we see whether the launch worked?
   - `active/release-roadmap.md` — **the standing list of what's shipping / queued**, the
     primary input to the ranking pass. Read it to rank this release against the rest;
     write the retro back to it after launch.
   - `active/priorities.md`, `active/projects/` — current focus and what's in flight, to
     cross-check the roadmap and capacity.
   - `memory/decisions/`, `memory/learnings/` — past launch retros and decisions. Have
     we launched this kind of thing before? What happened?

2. **If no store is present**, search the working folder for the
   same substance rather than asking: glob/grep for positioning, messaging, channel or
   channel-map outputs, personas/ICP, a release roadmap or "what's shipping", and any past
   launch retros. Name what you found and what you couldn't; fill the gaps with the user,
   not with assumptions. If there's no roadmap doc at all, ask once for "what else ships
   this period" — the ranking pass needs it.

If positioning or a working channel picture is genuinely missing, that's a foundation
gap — say so, and note the plan's channel mix is running on priors until it's closed.

## What you need to know about the release itself

Only ask for what discovery didn't answer. Keep it tight, menu-style where you can:

- What's shipping, and for whom.
- When (target date / window).
- Proof and readiness state — is it demonstrable at launch, or still risky / likely to
  slip? (Feeds the proof-readiness cap.)
- What else is on the roadmap this period (if the store didn't say).
- What this release is trying to *prove* (ties to `growth-bets` if one exists).

## Workflow

Run these in order. Each step is an instruction to carry out, not a heading to fill.
The *output* leads with the recommendation (see Output shape); the *thinking* runs in
this sequence.

### 1. Name the objective, then set the metric

Before scoring anything, make the release declare **one primary objective** — the single
thing this launch is for. Use the menu in `references/templates.md` (net-new demand /
market creation, adoption, acquisition, expansion revenue, credibility, competitive
defence, validated learning). At most one secondary, and it's a *watch*, not a target.

Then, from that objective, write the **primary success metric now** — before the plan,
not buried in the post-launch section. And write what the launch is **explicitly not
for**, so a scrappy proof-launch doesn't get judged on a revenue standard it can't hit in
the window. If the release has no validation yet, default the primary objective to
**validated learning** and demote any commercial metric to a secondary watch.

Then name the **conversion path** — the hypothesised next step from engagement toward the
commercial motion (e.g. free-tool use → evaluation call → contract). Even a top-of-funnel
or learning launch needs one, or it ships a toy with no funnel behind it. Mark it as a
hypothesis if unproven; it's a thing the launch tests, not a promise. Everything
downstream — channels, tier reading, the squeeze — aligns to this objective and path.

### 2. Score the release and propose a tier

Run the rubric (`references/rubric.md`): score each dimension against its anchors, **grade
each score's evidence** (validated / assumption), apply the weights, sum. Then apply the
caps — they're the anti-inflation teeth, so apply them honestly:

- **Proof-readiness cap** — not demonstrable with a credible proof point at launch → cap
  at T2; unfinished / likely to slip → cap at T3.
- **Off-narrative cap** — strategic weight = 0 → cannot be T1; flag as a distraction.
- **Parity floor** — newness ≤ 1 *and* customer pull ≤ 1 → cannot exceed T3, **however
  high it scores on reach**. A high reach score never rescues a parity fix.

The score *proposes* a tier; it does not settle it. Don't call the recommendation "the
call" (that phrase belongs to `channel-map`).

### 3. Rank against the roadmap

Read `active/release-roadmap.md` (or, without a store, whatever lists what's shipping; ask
once if nothing exists). Place the other queued releases, score or estimate them, and rank
this release among them. Apply the cadence guardrail (default, tunable): **≤1 T1 per
period, 2–3 T2s.** If several clear the T1 threshold, rank them and either bump the losers
down a tier or **bundle** them under one theme.

Then present the forced trade-off and **hand the decision back to the user** — the skill
makes the finite-attention choice unavoidable and visible; the user decides what gets the
moment. This is the anti-inflation engine; don't skip it even when only one release is on
the table (the guardrail still says whether this earns the period's T1).

### 4. Work out how the story comes together

This is the part teams are weakest at. Do two things:

- **Story-fit.** Check whether the release ladders into the ongoing narrative and
  positioning, or is an orphan. Name the storyline it advances — or say plainly that it
  advances none, and flag the risk (a release that scores well commercially but off-story
  isn't a headline, it's a brand-blur risk). If positioning doesn't exist yet, say the
  launch is running ahead of the narrative and give the **one interim line** that stops it
  deepening confusion.
- **Cadence.** Place it in the rolling-thunder drumbeat: is it a chapter in a run or a
  stray one-off? Should small items bundle under one theme to compound? (See
  `references/anchoring-and-cadence.md`.)

### 5. Build the v1 launch plan (instantiated to the tier)

Pull the tier's menus from `references/tier-menus.md` and the scaffolds from
`references/templates.md`, and **instantiate to this release — don't dump the menu**. Flag
every asset **[A] agent-draftable** or **[H] human**. Build these parts:

- **Message house.** Fill the template: name, audience, one-liner, primary/secondary/bonus
  value props *in the phrasing to be used*, and — for any T1 or T2 — a **named proof
  point** (the demonstrable evidence the claim is true). Value-prop phrasing is the
  highest-leverage decision (Luke Harries); spend the effort on the words. Hand real craft
  to `copywriting` or your own voice pass.
- **Channel mix, derived from channel-map.** Start from `evergreen/channels/` / the
  `channel-map` picture — the release spends the tier's breadth against routes already
  proven for *this* client, it doesn't invent a channel strategy. The tier sets breadth;
  the traction sets which channels. Then run the **completeness check across channel
  categories** in `tier-menus.md` (owned / paid / earned / amplification / concentrated
  third-party moments) so you don't tunnel onto the obvious owned routes and miss a
  relevant one — judging each for relevance to *this* release, not adding them by default.
  Show why each chosen channel is in (the channel-map signal) and why an obvious one is
  out. Any earned channel in the mix (creators, community) needs named people seeded
  before launch, not hoped for.
- **Asset checklist** for the tier, each flagged [A]/[H].
- **Rollout countdown**, working back from launch day. Treat beta / early-access as a real
  stage where the surface allows it — the listening stage that fine-tunes messaging and
  sources testimonials. Two things this must include: a **go/no-go gate out of beta** (the
  signals that greenlight, slip, or narrow the public launch — so "we'll learn in the
  beta" has teeth), and a **named launch-day distribution list** (the specific people /
  threads / accounts posting, not "dev channels" — earned reach with no name against it
  won't happen).
- **Internal launch — as a hit list, not a note.** A table of items each with the reason
  it earns its place (sales brief, objection handling, CS note, exec talking points,
  one-click #amplify kit), scaled to the tier. First-class: a release nobody internal can
  articulate under-fires.

### 6. Plan the post-launch window (launch day is the start line)

Treat launch day as the starting gun, not the finish. Most of a release's reach, learning
and conversion arrive in the weeks *after* launch, yet the reflex is to pour everything
into one day and taper to nothing. Budget real effort for the window after, and plan it as
a **sequence**, not a single push:

- **Squeeze — the long-tail repurposing.** Turn the launch assets into many touches; the
  agentic dividend lands here, where cheap variants are near-free. Flag [A]/[H].
- **Second wave, driven by reception.** What the audience actually reacted to becomes the
  next content — and it's the highest-signal content on the whole plan, because it's
  written *after* you know what landed. Amplify the testimonials and builder posts as they
  arrive; turn the top questions and objections from launch-day comments into follow-up
  pieces; lead the next wave with whichever proof point or value prop resonated.
- **Sustain the drumbeat.** Sketch the follow-through sequence — L+few days, L+1 week,
  L+1 month — so the release keeps being marketed instead of dropping to zero. A release
  that got one day of attention was under-marketed, whatever its tier. Size the window to
  the tier: a T1 sustains for weeks, a T3 for a few days.
- **Keep selling it internally.** Enablement isn't one-and-done. The sales/CS motion
  should still be using the material weeks later; the launch note shouldn't go stale on
  day two.
- **Confirm the metric and name the vanity trap.** The success metric was set in step 1;
  restate it against the objective, and name the vanity metric that will tempt and mislead
  (traffic/impressions untied to the objective). If the result isn't visible, that's a
  measurement gap — name it and route to instrumentation.
- **Set the retro.** Say when you'll look back and where the learning gets written —
  `memory/learnings/` and a line back into `active/release-roadmap.md` — so it feeds the
  next release's scoring and cadence.

**Seam with `campaign-brief`:** this is the post-launch window *for this release* —
milking the launch itself over the following weeks. When the follow-through hardens into
an ongoing multi-touch program with its own objective (beyond this release), that's a
campaign — hand it to `campaign-brief`. Release-gtm plans the window; campaign-brief plans
the program.

### 7. Hand off

Name the next skill for each open thread (see Handoffs below).

## Tier ladder (placeholder names — T1–T4)

> Names are placeholders. The magnitude is measured by the rubric, not declared. An
> ownable ladder is a later branding pass; the *dimensions* below are the durable part.

| Tier | What it is | Goal | Lead time | Channel mix | Investment |
|---|---|---|---|---|---|
| **T1** | New-to-world, category-shaping | Net-new demand + positioning | ~6–8 wks | Full: hero asset, PR, launch page, webinar, email, paid, social, enablement | High |
| **T2** | Strong feature, mostly expansion | Adoption + some acquisition | ~3–4 wks | Landing page, email, blog, in-app, social, light enablement | Medium |
| **T3** | Useful improvement | Adoption, awareness | ~1–2 wks | Changelog, in-app, blog, one social | Low |
| **T4** | Fix / parity / minor | Quiet credit | none | Changelog entry only | Minimal |

Lead time and channel breadth are the universal axes; the specific *menu* items
(changelog, in-app, ProductHunt) are software-native and swappable — see
`references/anchoring-and-cadence.md`.

## Output shape

Lead with the recommendation (objective + tier + the one reason + the metric) → objective
and score → the roadmap ranking and the forced trade-off → how the story comes together →
the v1 launch plan (message house with proof point, channel mix, asset checklist with
agent flags, countdown with go/no-go + named distribution, internal-launch hit list) →
post-launch squeeze + metric + retro → handoffs.

```markdown
# Release GTM — [release] — [date]

> Recommendation: [T1–T4] launch, objective = [primary objective]. Score [n]/36, [cap if
> any]. Ranked [n] of [n] this period. The one reason: [x]. The metric to beat: [y].

## Objective
- **Primary:** [objective] — [what winning looks like in 30–60 days]
- **Secondary (watch, not target):** [optional]
- **Explicitly NOT this launch's job:** [what we won't judge it on]
- **Primary success metric (set now):** [derived from the objective]
- **Conversion path (hypothesis if unproven):** [engagement → next step → commercial motion]

## Score and tier
| Dimension | Score (0–3) | Evidence | ×wt | Note |
|---|---|---|---|---|
| Strategic / narrative weight | | val / assump | ×3 | |
| Commercial impact (incl. market created) | | | ×3 | |
| Newness / innovation | | | ×2 | |
| Audience reach | | | ×2 | |
| Competitive pressure | | | ×1 | |
| Customer pull | | | ×1 | |
Raw: [n]/36 → proposes [tier]. Caps: [none / proof-readiness / off-narrative / parity].

## Roadmap ranking
| Rank | Release | Tier | Note |
|---|---|---|---|
Cadence guardrail: [≤1 T1, 2–3 T2s]. The forced trade-off: [what the user must choose].

## How the story comes together
- Story-fit: [storyline it advances / orphan flag / interim line if positioning is missing]
- Cadence: [where it sits in the drumbeat; bundle recommendation if any]

## Message house
- Name / audience / one-liner: ...
- Primary value prop (phrasing): ...
- Secondary / bonus: ...
- Proof point [required T1/T2]: ...

## Channel mix (derived from channel-map)
| Channel | Why in / out (channel-map signal) | [A]/[H] |
|---|---|---|
(Completeness check across categories: owned / paid / earned / amplification / third-party.)

## Asset checklist
| Asset | Owner | [A]/[H] | Notes |
|---|---|---|---|

## Rollout countdown
- Beta / early access: [who's in, what we're listening for]
  - Go/no-go gate: greenlight if [signal]; slip or narrow if [signal].
- L−[n]: ...
- Launch day — named distribution list: [who posts what, where, when]
- L+[n]: [squeeze begins]

## Internal launch (hit list)
| Item | Owner | Why it's on the list |
|---|---|---|

## Post-launch window (launch day = start line)
- Squeeze / repurposing ([A]/[H]): ...
- Second wave (reception-driven — what landed becomes the next content): ...
- Follow-through sequence (L+days / L+1wk / L+1mo — sustain to the tier, don't taper): ...
- Ongoing internal use (enablement isn't one-and-done): ...
- Success metric (from the objective): ...
- Vanity-metric watch: ...
- Retro + where written (memory/learnings + release-roadmap): ...
- Hand to campaign-brief if the follow-through becomes an ongoing program: ...

## Handoffs
- channel-map / growth-bets / positioning / pricing / copywriting / campaign-brief: ...
```

## Quality rules

1. **Name one primary objective first.** Everything — metric, channels, tier reading —
   aligns to it. A launch serving two masters builds two half-launches.
2. Set the primary success metric up front, from the objective — not in the post-launch
   section. Name what the launch is explicitly not for.
3. Lead the output with the recommendation (objective + tier + reason + metric). Never
   let the user declare the tier; the score proposes it.
4. Read context (store or working folder) before asking. Ground the channel mix in what's actually
   working, not a generic menu.
5. Apply the caps honestly. **A high reach score never rescues a parity fix** (parity
   floor). Strategic weight 0 can't be T1. Unproven-at-launch caps the tier.
6. **Every T1 (and T2) names its proof point.** A claim with no demonstrable evidence is
   not a T1 — it's a T2 that wants to be one.
7. Always run the roadmap ranking pass and force the trade-off, even with one release on
   the table. A tier is relative.
8. Reframe down, never reject: a demoted release becomes a well-run lower tier or a
   bundle, not a "no".
9. Instantiate the tier's menus to this release; don't dump the menu. Derive the channel
   mix from channel-map, then run the category completeness check — relevance per release,
   nothing mandatory.
10. Earned channels (creators, communities) get a **named list and a pre-launch seed**, or
    they don't count. A beta gets a **go/no-go gate**; launch day gets a **named
    distribution list**.
11. Flag every asset [A] agent-draftable vs [H] human, argued against real capacity.
12. Value-prop phrasing gets the effort. It's the highest-leverage decision.
13. Internal launch is a hit list with rationale, not an explanatory note. Enablement and
    the post-launch squeeze are first-class.
14. Launch day is the start line. Plan the post-launch window as a sequence sized to the
    tier — a release marketed for one day was under-marketed.
15. End with handoffs. Don't re-create positioning, messaging, pricing, or copy here.

## Common failure modes to avoid

- No stated objective, so success is defined only after the fact — and a learning launch
  gets judged on a revenue metric it could never hit in the window.
- Letting excitement set the tier. The score sets it.
- Letting a high reach score buy a moment for a parity fix (the parity floor exists to
  stop exactly this).
- A T1 with no named proof point — a loud claim the audience will stress-test in public.
- Scoring in a vacuum and skipping the roadmap ranking, so everything reads as a T1.
- A generic channel menu that ignores what channel-map says is working; or tunnelling onto
  owned/paid routes and missing a whole relevant category (earned, amplification, a
  third-party moment).
- Naming earned channels ("dev builders", "influencers") as if owned, with no seeded list
  — reach that never materialises on launch day.
- No go/no-go gate out of beta, so "we'll learn in the beta" has no teeth.
- A message house that's well-laid-out but with lazy value-prop phrasing.
- Internal launch written as prose nobody acts on, instead of a hit list with owners.
- Treating launch day as *the* event — front-loading everything into one day and tapering
  to zero, instead of planning the post-launch window where most reach and learning happen.
- Stopping at launch day with no squeeze and no pre-set metric.
- A post-launch plan that's just "repurpose the assets" with no reception-driven second
  wave — ignoring that the best content is written after you see what landed.
- Assuming the agentic dividend (that the team can suddenly 3× assets) instead of arguing
  it against real capacity.
- Rebuilding positioning / messaging / pricing inside the skill instead of handing off.

## Method lineage

Use as lineage, not as copy:

- **Luke Harries / harries.co** — "launch and launch again", launch-as-cadence, the
  launch checklist, and value-prop phrasing as the highest-leverage decision.
- **Matt Hodges / Intercom** — announcement prioritisation grid, the "app that cried
  wolf" (anti-inflation, tiering announcements).
- **Geckoboard / Paul Connor** — the messaging doc, beta as a listening stage, the
  vanity-metric warning.
- **Product Marketing Alliance** — launch-tier model tying tiers to channels, timeline,
  and investment.
- **"Rolling thunder" cadence (Pitch)** — releases as chapters that compound under a
  theme.
- **Inference doctrine** — strategy before tactics, visible and graded assumptions,
  lead-with-the-recommendation, and the reframe-don't-reject exit shared with
  `growth-bets`. Voice: dry on the score and spend.

## Handoffs

- `positioning` / `messaging-framework` — if story-fit exposes a positioning gap the
  release can't paper over.
- `channel-map` — for route-to-market detail on a channel in the mix, or if the traction
  picture is missing.
- `growth-bets` — if the release is really a bet to be proven, or for what to run next.
- `pricing` — if the release needs packaging or a price.
- `copywriting`, or your own voice pass — for final value-prop and asset copy.
- `campaign-brief` — to turn the launch plan into a sustained multi-touch campaign
  (release-gtm is upstream).
- `agentic-opportunity` — if the launch's economics shift enough with agents to rethink
  scope or cadence.
- measurement / instrumentation — if the success metric isn't visible today.

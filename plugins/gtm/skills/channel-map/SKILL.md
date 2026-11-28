---
name: channel-map
description: >
  Build an opinionated channel map — the channel-strategy deliverable that inventories every
  route to market (activated or not), bands status and health, derives defensible
  Build-first / Next / Park recommendations through a criteria-led rubric, and closes with
  "The Call": what to concentrate on, in what order, with owners and metrics. Trigger eagerly
  whenever the user wants a channel map, channel review/audit, channel strategy, route-to-market
  review, or channel prioritisation — "which channels should [client] be on", "where should they
  spend marketing effort", "map/prioritise the channels". The strategy layer above per-channel
  execution skills (social, ads, emails, seo), downstream of marketing-audit. Works
  evidence-rich (post-audit data packs) or evidence-thin (early-stage, priors-led). NOT for
  executing a single channel, nor a full marketing audit.
---

# Channel map

A channel map answers three questions a client is rarely getting straight answers to: *what are
all our routes to market — including the ones we're not using?*, *how is each actually doing?*,
and *what should we do about it, in what order?* Most channel documents answer only the second
question, only for activated channels, and dodge the third. The value of this deliverable is
that it refuses all three dodges.

Three principles carry the whole thing:

1. **Every park is a visible choice, not an omission.** The map lists channels the client should
   *not* use, with reasons and reopen conditions. A channel that's absent from the map looks like
   an oversight; a channel that's parked with a stated kill-criterion looks like a decision.
2. **Honesty about evidence beats false precision.** Unmeasured channels get Grey, not a guessed
   band. Single-month snapshots get caveated as such. Recommendations are labelled provisional
   where they are. This epistemic register is the differentiator — protect it.
3. **The map must end in a call.** Inventory and banding are analysis; clients pay strategy rates
   for the page that says "if it were our budget: these moves, in this order, and here's what
   we'd stop." A map without The Call is unfinished.

## Workflow

### Step 0 — Inventory the evidence

Before writing anything, establish what you actually know. Look for: analytics exports or
monthly reports, trial/signup attribution data, audit documents, founder interview notes,
prior syntheses, the live website and social surfaces (verify claims against them — audits
routinely under- or over-count what's live). Build a short source list with dates; every
claim in the map will cite into it.

Note the evidence *vintage* explicitly. If health bands rest on one month of data, say so in
the header caveats. If the engagement has a marketing-audit context (scored maturity areas,
shared-context docs), pull from it rather than re-deriving.

Also establish, in this step, the two facts the rubric needs later:

- **Capacity**: who actually does marketing work here — named people, roughly how much time.
  Channels don't run themselves, and The Call must be runnable by the humans that exist.
- **Founder disposition**: what the founder/team enjoys, refuses, or has failed at before.
  A channel that fights the founder's values or attention is structurally handicapped no
  matter what the spreadsheet says.

### Step 1 — Enumerate exhaustively

List every route to market using the channel families in `references/template.md` (Search &
SEO · AI & answer engines · Direct & brand · Email & lifecycle · Owned media & content ·
Owned social · Community · Earned media & PR · Events & field marketing · Advocacy, reviews &
referral · Partnerships & ecosystem · Paid & sponsorships · Outbound · Video · Product-led &
developer). Adapt families to the business —
add, merge, or drop where the model demands it — but err toward fine-grained: separate rows
make separate decisions visible (e.g. founder LinkedIn vs company page; customer referral vs
third-party affiliate).

Include: channels running today, channels with dormant assets, channels on the client's
wishlist, channels the audit surfaced, and channels you're adding purely so the park is
explicit. Distinguish **channels** from **plays** (cross-cutting initiatives that ride on
*several* channels at once — data-report franchises, reactivation campaigns, an organic-foundation
reset, a partner engine). A single-channel item is a task, not a play, and stays inside its
channel card. Plays go in Register 2 — see Step 4 for the cross-cutting test.

Mark **outcome rows** where relevant: direct/branded traffic is a *read* on brand-building
channels, not a channel you build — band it, but recommend `Monitor`.

### Step 2 — Band status and health

Use the legends in `references/template.md` verbatim (Status: Activated / Partial / Paused /
Sunsetting / Not activated. Health: Green / Amber / Red / Grey).

Grey discipline: Grey means "no performance data to rate" — both for unactivated channels and
for activated-but-unmeasured ones. Resist the pull to band an activated channel Amber just
because it's running; "set-and-forget syndication with no return" is a hypothesis until the
analytics are pulled, and the map should say so. Where a channel genuinely splits (strong
demand signal, broken surface), a split read with both halves named is more honest than an
average.

### Step 3 — Derive recommendations through the rubric

This is where the map earns its opinions. Every channel gets one recommendation from the fixed
vocabulary, and every recommendation must carry a one-line **because** that names how the
channel fares on the five lenses. The verdict is judgement — but judgement forced to show its
working, so the same evidence pattern produces the same call on the next client, and a
challenge ("why is X parked but Y Build-first when both are red?") has an answer.

**The five lenses:**

| Lens | Question it asks |
|---|---|
| Evidence | How solid is the read — trend, snapshot, anecdote, or nothing? |
| Prize | If this works, how big is it *relative to this company's stage*? |
| Effort | Build cost plus ongoing run cost — including attention, not just money |
| Fit | Does the founder/team have the appetite, values-alignment, and capability to run it? |
| Stage | Does the channel suit this business model and motion right now? (priors: `references/stage-priors.md`) |

**The vocabulary, and what each band requires:**

- **Build-first** — invest now. Requires: meaningful prize AND (low-to-moderate effort OR
  green-band evidence) AND fit not hostile. Every Build-first must name an owner and one
  metric that will judge it. If no owner exists, it cannot be Build-first — it's Next with a
  capacity note. This rule is what keeps the map honest about concentration.
- **Quick-win** — bounded fix, days not months, usually a trust or plumbing gap (sparse review
  profile, unclaimed listings, broken attribution). Low effort is the qualifying criterion.
- **Next** — real prize, but blocked: by sequencing, by capacity, or by a question Step 0
  couldn't answer. Say which.
- **Needs-judgment** — gated by founder-fit or a strategic fork. The action is a conversation,
  not a build. Never use this as a hedge for "I couldn't decide" — name the fork.
- **Park/Skip** — not now. Every park must carry a **kill-criterion in reverse**: the specific
  evidence that would reopen it, and the cheapest test that would generate that evidence.
  "Park: revisit if branded-search competitors start bidding on the client's name (check
  quarterly, 10 minutes)" is a decision; "Park" alone is a shrug.
- **Monitor** — passive or outcome rows where the action is measurement, not building.

**Tie-break principles** (the priors that make the calls consistent):

- Thin evidence caps conviction, not action: a Grey channel can still be Build-first if the
  move is cheap and reversible, but the because-line must say the bet is on priors, not data.
- A red channel with proven *reach* and a fixable conversion problem usually beats a grey
  channel with neither — tuning beats launching.
- Effort counts double for tiny teams: a channel needing sustained weekly production is a
  different proposition for a solo founder than for a five-person team, and the band should
  reflect it.
- Values-misfit is close to disqualifying. A founder who feels bad running cold email will
  starve the channel; band accordingly and say why.
- When a stage prior and the client's evidence disagree, the evidence wins — but flag the
  divergence, because it's either a real edge or a measurement artefact, and finding out
  which is usually a deep-dive candidate.

### Step 4 — Plays register

Register 2 lists **plays** — initiatives that ride *across* channels and operate at
campaign/franchise altitude. Each carries: the channel families it rides on, a recommendation
from the same vocabulary, and the key open question. Plays aren't banded for health — their
carrier channels are. The plays register feeds the engagement's build list.

**The cross-cutting test — apply it to every candidate.** If a "play" rides on a single
channel, it is a *task*, and it belongs inside that channel's detail card, not here. "Fix the
canonical bug", "write llms.txt", "claim the G2 listing", "surface reviews on the deck" are
tasks — each lives in one channel. A play orchestrates several channels toward one outcome: an
*organic-foundation reset* bundling SSR + schema + content consolidation across Search, AI and
product surfaces; a *data-report franchise* riding PR + content + email + social + brand-mention;
a *reactivation campaign* across email + outbound + retargeting; a *partner engine* across
partnerships + proof + enablement + PR. The register's value is naming the few franchise-level
bets the channel-by-channel view cannot see — so if the plays read like a to-do list, they're
pitched at the wrong altitude. Roll them up until each touches two or more families.

A useful tell: a good play has its own owner, its own arc over time, and would survive as a line
item in a board deck. A task wouldn't.

### Step 5 — The Call (mandatory)

One page, after the registers, written in first person plural and labelled as judgement. It is
not a summary of the tables — it is the thing the tables exist to justify. It must contain:

1. **The concentration argument.** Given the capacity established in Step 0, how many
   simultaneous Build-firsts can this team actually run? Defend the number. If the registers
   produced more Build-firsts than the team can run, demote the excess to Next here, visibly —
   the tension between appetite and capacity is the most useful thing the map can surface.
   There is no fixed cap; there is an obligation to argue the number.
2. **The sequence.** "If it were our budget: first X, then Y, then Z" — with a sentence each on
   why this order (dependency, momentum, evidence-gathering value).
3. **What we'd stop.** Naming the stops matters as much as the starts — they release capacity
   and they're the calls a client can't easily make alone.
4. **Owner and metric per Build-first.** Restated from the rubric, in one table.
5. **The revisit.** When the map gets re-banded (typically 90 days) and which Grey rows must
   have data by then.

Label claims per the engagement's claims discipline: what's evidence, what's inference, what's
judgement. The Call is allowed — required — to be opinionated precisely because it's labelled.

### Step 6 — Open questions, decisions, source key

Close with: the prioritised asks that would harden the map fastest (data exports, access,
fit-conversations with the founder), any decisions explicitly left open, and a source key
mapping the citation shorthand used throughout.

### Step 7 — Ship

Follow `references/template.md` for the document structure — header caveats, how-to-read
legends, at-a-glance tables per family, per-channel detail cards (evidence → health basis →
to investigate), plays table, The Call, open questions, source key.

Before delivery, run the client-voice/quality pass if you have one
(claims discipline, provenance, pre-ship checklist). The map is a reading document, not a
deck — return it as structured text.

## Evidence-thin mode

For early-stage clients with little or no data: the structure holds, but health is mostly Grey
and the rubric leans on the Stage lens. Say this plainly in the header. The deliverable's
center of gravity shifts from banding to The Call — priors-led concentration ("at your stage
and motion, these two or three channels, sequenced like this, and here's what evidence to
collect in the first 90 days so the next map is banded on data"). Read
`references/stage-priors.md` before writing it. Do not pad Grey rows with speculative health
bands to make the map look more informed than it is — thinness honestly handled is the
credibility move.

## Register and voice

Match the register of the parent engagement: dry, evidence-led, caveated where the data is
thin, conviction-led and labelled where it's judgement. Invite challenge explicitly in the
header ("provisional reads for discussion, not settled calls"). Cite every evidence claim into
the source key. British English.

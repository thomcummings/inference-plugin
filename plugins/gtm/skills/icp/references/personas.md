# Building personas

The craft behind step 5 of Layer 1. The ICP says which *company* to sell to; the
personas say who inside it you're actually talking to, in enough detail to change
what you write and who you write to.

The bar is the same as the ICP's: **every attribute must either filter a list or
change the message.** If it does neither, cut it. A persona that can't be acted on
is a poster.

## Which people to build

Build the ones whose behaviour changes the deal, not one per job title.

- **Buyer** — signs, or owns the budget line. Always built.
- **User** — lives in the product daily. Always built where the product has users
  distinct from the buyer; in self-serve they're often the same person, and you
  say so rather than splitting them for symmetry.
- **Champion** — the internal advocate who has to sell it when you're not in the
  room. Build when the deal needs internal selling; they need different material
  from the buyer (a business case they can forward, not a pitch).
- **Blocker** — security, legal, procurement, IT. Build only when they routinely
  kill or stall deals. Their persona is short: what they need to see, and what
  makes them say no.

Two to four is a healthy set. Beyond that you're describing an org chart. If a
role doesn't change what gets written or where it gets sent, fold it into another
persona and note the variation.

**One persona per job to be done, not per job title.** Two people with the same
title and different jobs are two personas. Two titles chasing the same job with
the same triggers are one persona with a note about titles.

## What a persona has to carry

Required — a persona is not done without these:

- **The job to be done.** The progress they're trying to make, in situation terms:
  "when [situation], I want to [motivation], so I can [expected outcome]." Not "wants
  to improve efficiency."
- **Pains and the KPIs they're measured on.** What their boss asks them about. This
  is the difference between a message that lands and one that's merely true.
- **Trigger events.** The observable thing that puts this person in market — a
  funding round, a new hire above them, a tool renewal, a metric missing target,
  a reorg. If you can't name it, you have a description, not a persona.
- **Watering holes.** Where they actually pay attention — specific communities,
  newsletters, podcasts, events, people they follow. Feeds `channel-map` directly,
  so be specific: a named subreddit beats "online communities."
- **Voice of customer, verbatim.** Their own words for the problem, kept as they
  said them.

Add where the evidence supports it:

- **How they buy.** Who else is in the room, what they need to show them, how long
  it takes, what budget it comes out of.
- **Decision criteria.** What they compare on, in their order — not yours.
- **Objections and perceived barriers.** What makes them hesitate, and what they
  believe about your category that isn't true.
- **The status quo.** What they do today instead. Usually a spreadsheet, an agency,
  or nothing — and it's your real competitor.
- **Information diet.** What they read before they'll talk to a vendor.

Method lineage: jobs-to-be-done (Moesta / Christensen) for the job and the switch;
the five rings of buying insight — priority initiative, success factors, perceived
barriers, decision criteria, buyer's journey (Revella, Buyer Persona Institute) for
the buying side.

## Deriving personas from evidence

Climb the evidence hierarchy in the SKILL. In practice that's four sources, in this
order — cheapest and most trustworthy first.

### 1. What's already on record — always first

Never re-ask for what's already written down. Before drafting, read the existing
ICP, any personas already defined, and the loose material in the workspace or
context store: what the team has said about their buyers, objections that came up,
deals discussed, past positioning calls. If the person already exists, you're
**enriching** them, not creating a second version.

### 2. Connected tools — the truth serum

Where the team's own systems are reachable (a connector, an MCP server, an export
they hand over), use them. This is the single biggest upgrade available to a
persona: real deal outcomes and real language beat anything you or the team can
recall. Ask by what you need, not by product name; the questions are the same
whichever CRM or call recorder they use.

**CRM (HubSpot, Salesforce, Pipedrive, Attio).** The highest-value source. Ask it:

- Closed-won deals in the last 12–18 months, and the **job titles on the contacts
  attached to them**. That's your buyer persona set, evidenced — not assumed. Where
  several contacts sit on one deal, that's the buying group, and the shape of it
  tells you whether you need a champion persona.
- Closed-lost deals and their **stated loss reasons**. This is where the objections
  and perceived barriers come from, in the team's own CRM language.
- **Deal cycle length by segment or title** — a persona whose deals take three times
  as long is a different persona, whatever the title says.
- **Original source and first-touch** on won deals — corroborates or contradicts the
  watering holes, and hands `channel-map` real evidence rather than a guess.
- **Notes, logged calls and email threads** on won and lost deals. Mine these for
  verbatim language.
- **Lifecycle stage transitions** — where people stall tells you which perceived
  barrier is doing the damage.

Ask for the properties you need rather than pulling whole objects.

**Call recorders and meeting notes (Gong, Fathom, Granola, Fireflies, Otter).** The
best source of verbatim language there is — this is the buyer talking, unedited.
Pull transcripts from won and lost deals both; the lost ones are more useful.

**Support and success (Intercom, Zendesk, Help Scout).** Recurring ticket themes are
the user persona's real pains, and the wording customers use when they're annoyed is
the wording that converts.

**Product analytics (PostHog, Amplitude, Mixpanel).** Which accounts adopt deepest
and expand — the high-expectation customers the ICP should be extrapolated from.
Telemetry outranks the firmographic guess.

**Research and interview notes (Notion, Google Drive, Docs).** Existing customer
research the team forgot they had. Ask before assuming it doesn't exist.

**Reviews and communities.** G2, Reddit, niche forums — vendor-free, unpaid, honest.
Useful for the category's language and the status quo, weaker for this company's
specific buyer.

The rules on connected tools:

- **Only when the task needs it, never a sweep on your own initiative.** Building
  or refreshing a persona qualifies. Curiosity doesn't.
- **Read-only here.** Persona work has no reason to write to a CRM.
- **Say what you couldn't reach.** "No CRM connected, so the buyer titles are from
  what you've told me, not from your closed-won" is a finding, not a caveat to bury.
  If a connection would materially sharpen the persona, say so once and move on if
  they'd rather not.
- **Nothing invented.** If the CRM has forty closed-won deals, say forty. Never
  round a small number up into a pattern.

### 3. What the team tells you

Ask for what isn't written down and isn't reachable. Good questions to ask a founder or
a sales lead, in descending order of usefulness:

- "Walk me through the last deal you won. Who did you first speak to, who else got
  involved, and what tipped it?" — the switch interview, and the best single question.
- "What were they doing before you?" — the status quo, your real competitor.
- "What's the last deal you lost, and what did they say?"
- "Which customer would be genuinely upset if you disappeared tomorrow?" — the
  high-expectation customer to extrapolate from (Ellis; Vohra).
- "What do they say in the first five minutes that tells you they're a fit?"

### 4. Priors — allowed, but labelled

Early-stage companies often have nothing. A persona may be built from priors — the category,
the role, how that role usually buys — only if it is labelled as priors-built
wherever it appears, ranked below every grounded persona, and specific about what
it lacks: "no calls, no won/lost reasons, nothing this buyer has said in their own
words." A priors-built persona is a structured guess. Call it a guess, not a customer.

If these personas are later used as a panel to test messages against, keep the
labelling consistent there too, so a persona doesn't gain confidence by changing hands.

## Voice of customer — keep it verbatim

The language is most of the value, and it's the first thing lost to a rewrite.

- **Store what they said, not your tidy version.** "I'm the one who gets shouted at
  when the numbers are late" is worth more than "concerned about reporting delays."
- **Capture where it came from** — which call, which ticket, which review, and when.
- **Prefer the words they use for the problem over the words they use for you.**
  Buyers describe problems accurately and solutions badly.
- **Watch for the company's internal jargon leaking in.** If a phrase only ever
  appears in the company's own material and never in a customer's mouth, it's their
  language, not the market's. Say so — it's a finding for `language-market-fit`.

## Failure modes

- **The character sketch.** "Marketing Mary, 38, drinks oat milk lattes." Age,
  hobbies and a stock photo filter no list and change no message.
- **A persona per job title.** Titles vary wildly between companies; jobs don't.
- **The composite average.** Averaging ten customers produces a person who exists
  nowhere. Build from the best-fit ones, not the mean.
- **Aspirational personas.** The buyer the team wishes they had. Anchor on who
  they actually win and keep.
- **Triggerless personas.** Complete, plausible, and useless — nothing tells you
  when to reach out.
- **Personas nobody uses.** If a persona hasn't changed a piece of copy, a target
  list or a channel choice within a month, it was a document exercise. Say what
  each persona is *for* on the way out.
- **A second set alongside the first.** Enrich the existing persona; never create a
  parallel copy under a new name for the same person.

## The finish line

Done is when a real buyer of that type would say "are you spying on me?" — not when
the template is full. If the persona reads like it could describe any buyer in the
category, it isn't finished; find the specific, slightly uncomfortable detail that
only this buyer would recognise.

## Writing them back

Personas are reference material the team will reuse, not scratch notes. Save them
wherever the ICP lives (the team's context store, if there is one; see
`context-layer`). Read the current version first, propose only a material change,
and replace the standing version rather than duplicating it. Keep the supporting
texture with each persona: the quotes, the observations, and where each came from.

# Buying groups / the DMU

## The unit of engagement is the buying group, not the lead
B2B purchases above trivial ACV are made by a committee — a decision-making unit
(DMU), or "buying group" — not an individual. The account-based shift is to
stop optimising for a single qualified lead and start engaging *coverage of the
buying group*. Opportunities with multiple engaged contacts are materially more
likely to advance than single-contact ones, and shifting measurement from leads
to buying groups tends to lift win rates.

Practically: a lead is a person; the account is the target; the buying group is
the set of people inside the account you must actually move together.

## Mapping the DMU (for 1:1 and 1:few)
For each account (1:1) or archetypal account in a cluster (1:few), map the roles
that must be engaged to win. A working role set:

- **Economic buyer** — controls the budget; signs.
- **Champion** — wants the change; sells internally for you.
- **Decision-maker(s)** — own the call within their function.
- **Influencers / technical evaluators** — shape the requirements, can veto.
- **End users** — live with it; their pull matters, especially in PLG-adjacent deals.
- **Blockers / detractors** — procurement, security, incumbents' allies.

Personas come from `icp`; this skill assembles those personas into an
account-level buying group and tracks who is covered.

## Coverage as the metric
For each mapped account, track:

- **Which roles are identified** (do we even know who they are?).
- **Which are engaged** (meaningful two-way interaction, not just "reached").
- **The gaps** — the roles that must be engaged and aren't. Gaps are the work.

A **buying-group engagement score** rolls per-contact engagement up to an
account-level read: weight roles by importance (an unengaged economic buyer
matters more than an unengaged peripheral influencer), and score the account on
how much of the *required* group is genuinely engaged. This feeds both play
design (close the gaps) and the `abm-ops` health check (is coverage growing?).

## Evidence-thin vs evidence-rich
- **Evidence-rich:** identify real contacts per account from CRM / enrichment /
  intent; score actual engagement; instrument the coverage roll-up.
- **Evidence-thin:** map the *required* buying group by role from the ICP
  personas as a template, and define the coverage score you'd track; population
  with real names happens once there's access. Still valuable — it tells the
  client what "covered" even means for their deals.

## Coverage targets by stage
Tie coverage to the account stage model (`funnel-stages.md`):

- **By Engaged:** reach a second person in the buying group.
- **By Evaluating:** a technical champion plus a business or functional leader.
- **By Buying:** procurement and security engaged early, not discovered at
  signature. Weak procurement or security contacts nearly kill deals; have the
  security and compliance pack ready.

An uncovered role is a visible gap on the account, not a blank.

## Owners per account
Tier 1 accounts are touched by several people: a founder or executive for senior
stakeholders, an AE for the commercial thread, a solutions engineer for the
technical evaluation. Support several owners, with **one accountable owner**.

## First-call discovery questions (add to the sales script)
- Who else will evaluate this, on the technical, business and security or
  procurement sides?
- Who signs, and what does your procurement process look like?
- Has security reviewed a vendor like us before, and what did they ask for?
- Who owns the area this improves?
- What would make this a priority this quarter?

## Mapping sources
- CRM contacts for the company, most recently active first, with title and
  persona tags. Suggest members from these; the owner confirms.
- Meeting notes and any shared channels with the account.
- Product sign-ups from the account's domain, where there is a self-serve
  surface. These are often hands-on users nobody in sales knows yet.
- Social research on the roles.

## Knowledge flags
For each account, track whether **sales knows** it and whether **marketing knows**
it. An account neither function knows well is a planning risk.

## Single-account brainstorm (exercise)
Pick one account further left in the funnel. Map its full buying group, then
brainstorm plays for every stage from today to Customer. It makes the framework
concrete for the team.

## Example role set: technical or developer products
Adapt per product. This set suits products that an engineering team evaluates.

| Role | Typical concern | What they need |
| --- | --- | --- |
| Implementer or developer | Does it work, how hard is it to integrate | Docs, quickstarts, sample code, proof on their data |
| Domain or data lead | Quality, accuracy, measurable gain | Benchmarks or pilots on their data, methodology |
| Product lead | User impact, roadmap fit | Use-case stories, demos, customer outcomes |
| CTO or engineering leader | Architecture, cost, risk, vendor viability | Business case, architecture notes, references |
| Procurement or security | Data handling, compliance, contract risk | Security pack, deployment options, DPA template |
| Economic buyer | ROI and priority | Business case, executive sponsor call |

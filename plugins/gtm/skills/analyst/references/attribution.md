# Attribution — what to believe when the sources disagree

Attribution is not a truth problem. None of the numbers are correct, and no model will make
them correct. It is a **decision problem**: someone is about to move budget, kill a channel,
or tell a board a story, and they need a defensible read to do it on.

So the first move is the same as everywhere else in this skill — *what decision is waiting on
this number?* Three decisions get asked of attribution, and they need very different rigour:

- **Reallocating budget between channels.** Needs relative and directional truth only. The
  ranking has to be right; the decimals do not.
- **Killing or keeping one channel.** Needs incrementality — would this have happened anyway?
  No attribution model can answer it. Only a holdout can.
- **Reporting to a board or investor.** Needs one consistent story told the same way every
  quarter. Changing model between reports is worse than picking the wrong model.

If the answer is "we just want to know", the honest reply is that attribution work is
expensive and the question needs sharpening first.

## Why the dashboards disagree

Not a bug, and usually not a broken pixel. Every source is a **claimant with an interest**:

- **Ad platforms** count conversions they can attribute to themselves, on their own lookback
  and view-through windows. Two platforms routinely claim the same conversion. Both are
  reporting honestly under their own rules.
- **Web analytics** attributes by its own model, to sessions it can see, and buckets
  everything it can't identify as direct.
- **The CRM** records what the form captured, which is whatever the last click populated.
- **Billing** knows what happened but nothing about why.

The single most useful rule to give a client: **never sum conversions across platforms.** One
conversion, several claimants. Summing platform-reported numbers overstates routinely and
badly, and it is the most common cause of "our attributed conversions are double our actual
customers".

The reconciliation move that follows from it: **name one source of truth — the place money
actually lands (CRM or billing) — and demote every platform to a directional input to it,
never a peer.** Most attribution arguments end there, before any model is chosen.

## The models, and how each one lies

- **Last-touch.** The default nearly everywhere. Systematically flatters the bottom of the
  funnel — branded search, retargeting, review sites — because it credits whatever was
  standing closest to the door. Never defensible on its own.
- **First-touch.** Flatters the top — content, social, PR. Useful for a different question:
  what *starts* demand.
- **Show first and last together. The gap between them is the insight.** A channel that is
  large on first-touch and absent on last-touch is a demand creator about to be defunded by a
  last-touch dashboard. That single comparison is worth more than most attribution tools and
  costs one extra column.
- **Linear.** No opinion, spreads credit evenly. Useful only as a sanity baseline against the
  two above.
- **Time-decay.** Weights recent touches. Reasonable for short cycles; actively wrong for
  long B2B ones, where the first conversation may be the whole reason the deal exists.
- **Position-based (40/20/40).** The least-bad single model for long cycles when a client
  insists on picking one number.
- **Data-driven / algorithmic.** Needs conversion volume most clients don't have. Below a few
  hundred conversions a month it is a black box fitting noise, and it cannot be explained to
  a board, which makes it useless for the third decision above.

## Three measurement paradigms — choose by size and cycle

- **Multi-touch (MTA).** Stitching touches at user level. Works when conversion happens on one
  domain, the cycle is short, and one person makes the decision — self-serve and e-commerce.
  Breaks on long B2B cycles, buying groups, offline steps and privacy loss.
- **Media mix modelling (MMM).** Regressing aggregate spend against outcomes over time. Needs
  real spend, a long history, and *variation* in that spend — with flat budgets there is
  nothing to regress. Wrong for most clients below serious media spend, however fashionable
  it has become.
- **Incrementality testing.** Geo holdouts, on/off tests, PSA tests. The only approach that
  answers "would this have happened anyway", and it is usually cheaper than clients expect.
  The cost is real, though: deliberately withholding spend from somewhere.

**The routing rule for most clients: too small for MMM, too B2B for MTA.** So the honest
default is CRM as source of truth, first/last shown side by side, self-reported source
collected everywhere, and one incrementality test on the largest line item. Recommend that
before recommending a tool.

## Blind spots — where the real drivers hide

- **Direct is a junk drawer, not a channel.** Stripped referrers, dark social (Slack,
  WhatsApp, podcasts, newsletters), typed URLs. A direct line that grows in step with spend
  elsewhere usually means something upstream is working and uncredited. It is measurement
  debt.
- **Branded search is the biggest lie in the deck.** It harvests demand created somewhere
  else and reports it as search performance. Always split branded from non-branded before
  judging any search channel. Rising branded volume is a *result*, and something unpaid is
  probably causing it.
- **AI answer engines are the new dark social.** Buyers research in ChatGPT, Claude and
  Perplexity, then arrive direct or via branded search. Invisible to every model here. The
  practical consequence: refuse to conclude "content isn't working" from a flat organic line
  without checking answer-engine visibility first.
- **Buying groups.** In B2B the person who clicks, the champion who pushes, and the person who
  signs are three different people. User-level attribution credits whoever filled the form.
  Account-level measurement is the only honest frame.
- **Lookback and view-through windows.** A platform with a seven-day view-through window
  claims conversions it merely witnessed. Before comparing any two numbers, ask what window
  each was computed on — often the entire disagreement.

## Hygiene outranks any model

Before entertaining a model debate: UTM discipline, a source field on every record that
survives all the way to closed-won, and a self-reported "how did you hear about us?" on the
form. Self-report bands as *claimed* on the honesty tiers in `frameworks.md`, and any single
answer is unreliable — but at volume the pattern holds, and it is the only instrument that
catches dark social and answer engines. It costs one form field.

Most attribution arguments are hygiene arguments in disguise. Diagnose that before
recommending anything expensive.

## The reconciliation, step by step

1. **Name the source of truth** and say it out loud in the output.
2. **Pull the same date range and the same conversion definition from every source.** A large
   share of "disagreements" are different definitions or different windows, and this step
   dissolves them.
3. **Compute the over-claim** per platform against the source of truth, as a ratio.
4. **Report per channel:** the source-of-truth number, what each platform claims, the gap, and
   the honesty tier from `frameworks.md`.
5. **Never reconcile to the decimal.** Band it, and say which way the residual probably
   leans.

## Output shape

The question and the decision it serves → the named source of truth → per-channel read with
honesty tier → the first/last gap and what it implies → what we cannot see (blind spots,
stated plainly) → recommendation with a confidence band → the cheapest next proof.

## Anti-patterns

- **Summing platform-reported conversions.** The default failure.
- **Reallocating budget off a last-touch dashboard.** Reliably defunds demand creation.
- **Judging a slow channel on a fast model** — cross-check time-to-signal in `frameworks.md`.
- **Buying an attribution tool to settle a hygiene problem.** Expensive, and it fixes nothing.
- **Precision theatre.** Three decimal places on a claimed-tier number.
- **Killing brand and demand-creation channels because they never appear on last touch.** The
  most expensive mistake in this file, and the one this skill exists to prevent.

## Handoffs

Attribution answers *which channel*; the driver tree answers *which metric* — a channel's
contribution should land on a named driver rather than float as its own number. Answer-engine
visibility goes to the AEO mode of `website-audit`; account-level measurement to `abm-ops`; channel health banding
feeds `channel-map`; an incrementality test is a bet, so it belongs in `growth-bets`.

Implementation — GA4, GTM, pixels, server-side tagging, identity stitching — is execution and
out of scope for this skill.

# Retention, churn and expansion

**Not a motion profile.** The rest of this library describes ways a business grows; this file
describes the thing that decides whether any of them compound. It is read when growth is
leaking rather than when the motion is in question — but the two are related more often than
teams expect, because a retention problem is frequently an acquisition problem arriving
late.

## Where it sits in the model

In the racecar frame retention is listed as a **lubricant** — it raises the engine's gain
without being the engine. That is the right classification for most businesses, and the wrong
one for two kinds:

- **Subscription and usage-based businesses.** Here retention *is* the engine, because the
  base is the thing that compounds. Adding customers to a leaking base is buying growth, not
  building it. If monthly churn is high enough, there is a ceiling the business will hit no
  matter how good acquisition gets — and naming that ceiling out loud is usually the single
  most useful thing this skill does for such a business.
- **Businesses whose loop runs through existing customers** — referral loops, expansion-led
  growth, user-generated content. Churn doesn't just reduce the base, it removes the fuel
  from the next turn of the loop.

So the first question is not "how do we fix churn", it is **"is retention a lubricant or the
engine here?"** The answer changes how much of the plan it deserves.

## The first cut: voluntary or involuntary

Split before diagnosing anything else, because the two have nothing in common except the word
churn.

- **Involuntary churn** is failed payments — expired cards, hard and soft declines, bank
  retries. It is customers who *wanted to stay* and left because the plumbing failed. The
  share is often large enough to matter, so measure it here rather than assume it. It is
  fixable with retry logic and payment-recovery emails, and it is almost
  always the cheapest retention win available.
- **Voluntary churn** is a decision. That decision has causes, and the causes sit in different
  parts of the business.

**Diagnostic consequence:** if a team has never separated the two, the first
recommendation is to measure the split, not to run a retention programme. A team can spend a
quarter on onboarding while a large share of the leak is a billing configuration.

## Where voluntary churn actually comes from

Five causes, and they belong to different owners. The value of this list is that teams
almost always assume the third and it is usually one of the first two.

1. **Wrong customer acquired.** They were never in the ICP; the churn was decided at the point
   of sale. Symptom: churn concentrated in one segment, one channel, or one promotion. This is
   an acquisition and positioning problem wearing a retention costume, and no amount of
   onboarding work fixes it. Route to `icp`, and check whether a discount or a channel is
   manufacturing bad-fit customers.
2. **Never reached the value.** They fit, but they never activated — the onboarding, the data
   import, the first real use never happened. Symptom: churn concentrated in the first 30–90
   days, and churned accounts show low or no core-action usage. The most fixable expensive
   problem in most products.
3. **Reached the value and it wasn't enough.** The genuine product/value gap. Symptom: churn
   from *engaged* accounts. Rarer than teams think, and the most serious when real, because
   it is not a marketing problem at all.
4. **Champion left, or the priority did.** Especially B2B. The person who bought moved on and
   nobody inherited the relationship. Symptom: churn uncorrelated with usage, often at renewal.
5. **Price, budget or a competitor.** The one customers and teams volunteer first and the one that is
   least often the actual cause. Treat a "we went with X" exit as a claim to be verified, not
   a finding — see `win-loss-analysis`.

## What bites when you measure it

- **Cohorts, not the aggregate.** An aggregate churn rate averages a healthy old base with a
  bad new one and hides both. Any retention read that isn't cohorted is decoration.
- **Three different numbers, and teams conflate them.** Logo retention (accounts kept),
  gross revenue retention (revenue kept, capped at 100%), and net revenue retention (revenue
  kept plus expansion, which can exceed 100%). NRR is the compounding number and the one that
  tells you whether the base is an engine. GRR is the honest one — NRR above 100% can conceal
  a real leak masked by a few expanding accounts.
- **The survivorship trap.** Surveying current customers about why people leave asks the
  people who stayed. Exit surveys and churned-customer interviews are the instrument; both
  are self-reported, so they band as *claimed* on the honesty tiers in `analyst`.
- **Time-to-signal is long.** For annual contracts a retention change takes a year to read.
  Leading indicators — activation rate, usage depth, support contact patterns, licence
  utilisation — carry the interim, and should be labelled as steering signals, not verdicts.

## Expansion is part of the same question

Retention work that stops at "don't leave" leaves the compounding on the table. Expansion —
seats, usage, tier upgrades, cross-sell — is what turns a retained base into an engine, and
it is usually cheaper per pound of revenue than acquisition. The structural test: **is there a
mechanism by which a customer who succeeds naturally consumes more?** If the pricing metric
doesn't grow with the value delivered, expansion has to be sold every time, and the base won't
compound on its own. That is a packaging problem — route to `pricing-packaging`.

## When retention work is the wrong answer

- **Pre-PMF.** Churn at this stage is *information*, not a leak to be plugged. A retention
  programme here papers over the signal the business most needs to read.
- **When the leak is positioning.** If the wrong customers keep arriving, fixing the exit
  experience just makes them leave more politely.
- **When volume is too low to read.** Below a few dozen churn events in a period
  (a rule of thumb, not a statistical threshold), percentages lie. Report counts and interview the people; don't build a dashboard.

## Decay signals

Retention is quietly rotting when: activation rate falls while signups rise (acquisition is
outrunning the product); usage depth per account declines even as logos hold; expansion stalls
while logo retention looks fine (the base has stopped compounding); support contacts cluster
around the same unmet job; or a growing share of churn comes from the most recent cohorts,
which means whatever changed in acquisition changed the customer.

## Handoffs

Wrong-customer churn goes to `icp` and `positioning`; verifying stated exit reasons to
`win-loss-analysis`; expansion mechanics and value metrics to `pricing-packaging`; the
measurement frame (cohorting, honesty tiers, time-to-signal) to `analyst`; and any retention
fix worth sequencing against other moves to `growth-bets`. Building the cancel flow, the
dunning emails and the lifecycle campaigns is execution and out of scope here — this decides
where the leak is and what it is worth fixing.

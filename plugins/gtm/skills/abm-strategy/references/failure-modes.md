# ABM failure modes

The anti-patterns the fit gate screens for at the start and the `abm-ops` health check
screens for on a running programme. If a programme is really one of these, name
it plainly and give the corrected version.

## 1. "ABM" that's just targeted demand gen
Uploading a list and running ads/emails at it — "display ads to a CSV" — is not
ABM. It's account-targeted demand gen. The missing ingredients: coordination
across channels, buying-group awareness, and joint sales+marketing action against
each account context. *Fix:* add tiering, buying-group mapping, and a real joint
motion, or call it what it is.

## 2. One playbook for all accounts
Treating every account with the same intensity instead of tiering. This both
wastes the expensive high-touch motion on accounts that don't merit it and
starves the accounts that do. *Fix:* tier by value/complexity (1:1/1:few/1:many)
and match effort to tier.

## 3. ABM as "air cover for SDRs"
Framing ABM as just more top-of-funnel noise to warm up lists for the SDR team.
This misses its actual value — strategic prioritisation and joint account plans —
and collapses it back into lead-gen thinking. *Fix:* re-anchor on account
selection, buying-group coverage, and a shared account plan sales co-owns.

## 4. Marketing-only ABM
No genuine sales partnership: marketing runs "ABM" while sales works its own
list. The single most common way programmes fail. *Fix:* shared account list,
shared account plan, named joint owners, agreed handoffs — or don't start.

## 5. Lead-centric measurement on an account-based motion
Still reporting MQLs, cost-per-lead, and last-touch attribution. It hides account
progression and reignites the attribution blame game. *Fix:* switch to
account-level measurement (`references/measurement.md`).

## 6. Static list that never re-tiers
A target list set once and left to rot — no promotion/demotion as signals change,
so effort stays pointed at accounts that have gone cold and misses ones now
in-market. *Fix:* dynamic tiering with defined triggers.

## 7. Personalisation theatre
Pouring effort into heavy per-account personalisation that doesn't lift response,
or auto-generating "personalised" noise at scale. *Fix:* tight relevance to a
real shared pain with a few specific data points; let buying-group coverage and
signal quality — not personalisation depth — drive the work.

## 8. Boiling the ocean
Too many accounts for the team's real capacity, so every account gets a shallow
touch. ABM's discipline is subtraction. *Fix:* cut the list to what capacity can
genuinely work at each tier's depth.

## 9. The list multiplies
A sheet, a CRM property, a dashboard and an agency each hold a slightly different
target list. *Fix:* one source of truth, synced outward (`abm-setup`).

## 10. Unwritten tier criteria
A good tiering session nobody wrote up, so nobody can say why an account is Tier 1
rather than Tier 2, and maintenance becomes guesswork. *Fix:* write the criteria
the same day.

## 11. Too many Tier 1s
Tier 1 grows past what the team can work one-to-one and stops meaning anything.
*Fix:* cap it, rank it, and keep a "this quarter's wins" focus.

## 12. Marketing not in the room
Account decisions get made in a sales meeting marketing doesn't attend, and ABM
turns into "marketing campaigns about accounts". *Fix:* marketing joins the weekly
account review (`abm-ops`).

## 13. Reporting on unlocked definitions
Dashboards built before the stages are agreed freeze untested definitions and
produce numbers nobody trusts. *Fix:* lock stages before building reporting.

## 14. Unknown read as zero
De-anonymisation, consent banners and domain matching all undercount. A failed
sync or missing tracker gets read as "no activity". *Fix:* every report states its
coverage, and missing data shows as missing.

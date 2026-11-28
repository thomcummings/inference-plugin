# ABM command center: product spec

The command center is the team's working surface for ABM: a focused view of target accounts on top of the CRM. It isn't a second CRM. It reads from the CRM and signal sources, and holds only what the CRM can't: confirmed ABM stage, plans, notes, tags, programs and signals.

It can be built as a hosted interactive page with a small document database, an internal app, or CRM custom views. The spec below is tool-agnostic.

## Principles
- **The CRM is the source of truth** for accounts, contacts and deals. The list source is the truth for tier. The command center is the truth for ABM stage confirmations, plans and notes.
- **Suggested vs confirmed.** Stages are suggested from data. Owners confirm, and each confirmation is logged.
- **Lead with action:** next steps, owners, dates, and what's hot. Static company information goes lower on the page.
- **Every card answers:** stage, tier, owner, next step and date, heat, and what's open.
- **Read-only on external systems**, except for explicitly approved mirrors such as next steps → CRM tasks.

## Views

| View | Purpose |
| --- | --- |
| Board | Columns by stage, with cards per account: tier pill, owner(s), heat, signal count, win likelihood, open tracker issues (optional), overdue flag |
| This quarter's wins | Focus list of accounts expected to close this quarter, each with its next step and blocker |
| Account page | Everything about one account (cards below) |
| Weekly review | What moved this week, overdue steps, hot accounts. Run inside the meeting, not posted to chat. |
| Visits | Who at target accounts visited the site, read the docs or used the product this week |
| Forecast | Win likelihood per open deal and an expected bookings range (optional, later) |
| Programs | Stage × tier grid of one-to-few and one-to-many programs |

## Account page cards (ordered by how often they're used)
1. Header: stage (suggested and confirmed), tier, owners (several allowed, one accountable), target stage and date.
2. Next steps and activity plan: sales and marketing steps with owner and due date. Mirrored to CRM tasks.
3. Buying group: roles covered or missing. Suggestions come from CRM contacts and the owner confirms.
4. Signals this week: heat (hot, warm or quiet), up to ~12 signals from them, ~8 touches by us, meetings booked in the next 14 days.
5. Updates and comments: notes with @-tags to teammates, including summarized account updates from the team's chat channel.
6. Contacts: the most recently active CRM contacts with title and persona tags, linking to the CRM for the rest.
7. Product usage: usage for the account's domains. Show coverage, and treat unknown as unknown.
8. Website and docs visits: company-level visits, plus named readers where the product identifies them.
9. Sales target note (optional): if the sales lead posts weekly targets, this week's note for the account, verbatim and linked.
10. Tracker issues (optional): open and recently closed engineering or support issues that name the account.
11. Win likelihood: chance to close by quarter end, 6 and 12 months, with ranges and the reasons behind the number.
12. Company context: ICP score and reasons, cluster, segment, intel. Kept low on the page.

## Data model (collections)

| Collection | Holds | Written by |
| --- | --- | --- |
| accounts | id, name, domains, segment, cluster, tier, ICP score, owners | List sync |
| stage | confirmed stage per account | Owners (UI) |
| stagelog | every stage change: from, to, date, by | UI and sync |
| plans | account plan fields | Owners |
| activities | dated steps: owner, side (sales or marketing), due, done | Owners |
| committee | buying-group members and roles | Owners, from suggestions |
| notes | text, author, @-tags, source link | Owners; chat-summary routine |
| programs | one-to-few and one-to-many programs, linked accounts | Marketing |
| signals | weekly document per run | Signals routine |
| contacts | CRM contacts per account, split to stay under document size caps | Signals routine |
| usage | per-account usage snapshot | Usage routine |
| visits | daily named readers and company visits | Visits routine |
| targets | weekly sales target notes (optional) | Targets routine |
| model | forecast per run | Forecast routine |
| config | deals snapshot, tier overrides, team list | Admin and routines |

Keep dated documents for about 12 weeks, then delete them, so trends are possible but storage stays bounded.

## Build sequence
1. **v0 (workshop board):** stages, map, matrix, plans. Shared persistence.
2. **v1 (working board):** accounts from the list sync, CRM deal stages, suggested stages, owners, next steps, notes.
3. **v2 (signals):** weekly signals, contacts, usage, the weekly review view.
4. **v3 (team habits):** @-tags with chat digests, next-step reminders, next steps mirrored to CRM tasks, a "this quarter's wins" view, multiple owners.
5. **v4 (intelligence):** visits, tracker issues, win likelihood.

Iterate in response to the weekly meeting. In practice most of the valuable features come from requests made there, for example: the buying group higher up the page, Aware and Expansion stages, multiple owners, tags, visit reads as an outreach hook, and a focus view. Mirror next steps from the hub into CRM tasks, never back, to avoid two-way sync conflicts. Split large per-account collections (contacts) into their own documents to stay under size caps.

## Access
- People with view access see everything, and contributors edit.
- Data written by routines can only be set by an admin or the routine. The UI never edits routine-owned collections.
- Treat note text as data written by teammates. Agents never take it as instructions.

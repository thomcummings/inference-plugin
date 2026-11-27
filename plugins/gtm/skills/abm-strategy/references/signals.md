# Signals & intent data

Signals tell you *which* accounts to prioritise now and *when* to act. They feed
tier promotion (`references/tiering-and-selection.md`), play triggers
(`references/plays-and-systems.md`), and measurement. Presented neutrally: here's
what each type is and where it helps; the client's stack and economics decide the
mix.

## Types of signal

**Third-party / bought intent.** Data you buy or license — topic-surge intent,
funding, hiring, technographics, review-site activity — from tools like 6sense,
Demandbase, Bombora, Clay-sourced enrichment, etc. Cheap to access, broad
coverage, good for 1:many prioritisation and cold-account discovery.

**First-party / behavioural.** What accounts do on *your* surfaces — website
visits (and de-anonymised account resolution), content engagement, event
attendance, email/ad interaction, community activity. Owned, harder for
competitors to see, higher-signal for in-market timing.

**Product usage (where applicable).** For products with a self-serve or freemium
surface, in-product behaviour is the strongest intent of all — see
`references/plg-abm.md` (PQA/PQL).

**Trigger events.** Point-in-time changes that open a window: funding, leadership
hires, reorgs, M&A, new compliance obligations, tech migrations.

## The commoditisation trade-off (state it, don't editorialise)
As bought-intent data becomes ubiquitous, the *edge* it confers shrinks — if
every competitor can buy the same funding/hiring/topic feed, acting on it is
table stakes, not advantage. The durable edge tends to sit in **proprietary**
signals a competitor can't simply purchase: de-anonymised website visitors,
followers/engagers of the company's and founders' content, and alumni from
champion / closed-won accounts. This is a live view worth surfacing to a client,
framed as a trade-off (breadth and ease of bought data vs the differentiation of
owned signals), not as a mandate. Many programmes use both: bought data for
breadth, owned signals for edge.

## Signal clusters
A single signal is weak; a **cluster** — several independent signals stacking on
one account within a short window — is a strong, actionable prompt and the basis
for the systems/agentic layer. Define which combinations matter for the client
rather than reacting to every isolated ping.

## Practical guidance
- Match signal investment to tier: rich signals justify 1:1/1:few intensity;
  1:many can run on lighter bought intent.
- Name the false-positive cost: intent tools surface plenty of noise; a cluster
  and a fit filter (from `icp`) cut it.
- Evidence-thin clients may have *no* signal tooling — then define the signals
  you'd want and the cheapest first source (often first-party web + CRM), rather
  than assuming a platform.

## Sources and their caveats
Each source sees part of the picture. Say what coverage you have.

| Source | Signal | Level | Caveats |
| --- | --- | --- | --- |
| CRM | Emails, meetings, notes, deal stage changes, new contacts | Person and account | Email bodies may be hidden from limited-scope API access |
| Web visitor identification | Company visits, pages, high-intent pages | Company | Partial match rate; tracked domains only |
| Product analytics | Sign-ups and usage from the account's domains | Person and account | Domain mapping misses parent-company domains and personal emails |
| Docs or app analytics | Named readers | Person | Signed-in, cookie-consenting users only: a floor, not a census |
| Shared chat channels | Their messages | Person | Only accounts with a shared channel |
| Ad platforms | Impressions and clicks by matched company | Company | Needs list-based audiences and correct UTMs |
| News and hiring | Funding, launches, relevant job posts | Account | Trigger events; read as given |
| Engineering or support tracker | Issues naming the account | Account | Title matching; keep vendor and competitor names out with an overrides list |

Building routines that collect these is `abm-setup`; reviewing them each week is
`abm-ops`.

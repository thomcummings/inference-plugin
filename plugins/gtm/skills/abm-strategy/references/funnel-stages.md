# Funnel stages

ABM needs one account-level stage model that everyone uses. It isn't the same as a deal pipeline: an account can be Aware for months with no deal at all.

## The six-stage model

| Stage | Also reads as | Entry (the account gets here when…) | Exit (it moves on when…) | The job at this stage |
| --- | --- | --- | --- | --- |
| Unaware | Identified | It's on the target list. Nobody at the account has interacted with us in a way we can see. | Anyone at the account touches us in a way we can measure. | Get noticed by the right people: targeted ads, presence in their communities, warm intros through investors and partners. |
| Aware | Touched | A measurable touch: site visits from their domain, repeated ad impressions, social engagement, or we met them at an event. | A named person raises a hand: signs up, books a call, or replies with interest. | Make the problem feel real for them, with proof from companies like them. |
| Engaged | MQL | A named contact has signed up, started a trial or free account, downloaded, replied or booked a meeting. | Sales accepts it: a real use case, a contact with influence, and a reason to act now. | Turn interest into a conversation, and reach a second person on their buying team. |
| Evaluating | SQL | The use case is confirmed. They're evaluating or actively testing us. | The test passes and commercial talks open with someone who can sign. | Prove it in their own conditions: a pilot, proof of concept or benchmark on their data, hands-on support, reference customers. |
| Buying | Deal in progress | Pricing, contract terms, procurement or a security review is underway. | Contract signed. | Remove risk: security pack, references, executive alignment, a shared close plan. |
| Customer | Contract | Signed contract. | Usage expands, or they become a public reference. | Onboard well, grow usage, and turn them into a case study. |

Optional additions that sales teams often ask for:
- **Hold:** paused by the account or by us, with a revisit date.
- **Expansion:** after signature, a new use case, team or volume is being worked. It can also be a sub-state of Customer.

## Defining "Aware" (the hardest stage)

Agree a short list of qualifying signals, each tied to an account by domain or list membership:
- Visits from the account's domain to high-intent pages (pricing, proof or comparison pages, product pages, docs where the product has them). Set a threshold such as 2+ pages or any pricing visit.
- Repeated ad impressions or clicks from the account's people on list-based campaigns.
- Event attendance by anyone from the account.
- Social engagement with company or founder posts by people at the account.
- Product sign-ups from the account's domain. Strictly this is Engaged if a named person, but flag it either way.

Be honest about coverage. Company-level website de-anonymization matches only part of business traffic (often well under half; check the vendor's stated match rate against your own traffic). That's a floor, not a census. In-product and docs analytics usually identify only signed-in users who accepted cookies.

## Mapping and locking

Mapping the stage model to CRM deal stages and to any sales pipeline view, and locking the definitions with the team, is `abm-setup` (`references/stage-lock-and-crm-mapping.md`). Don't build KPI reporting on stages the team hasn't agreed.

## Velocity notes to share with the team
- Accounts can sit in Aware for months, then sprint to Customer in weeks once they become a priority. Stage time isn't linear.
- Set target durations only for late stages, for example Evaluating under a month, and a fixed number of legal turnarounds once Buying.

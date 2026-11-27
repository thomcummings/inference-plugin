# Pricing experiments and golden tests

Pricing work ends with a decision or a test, not a spreadsheet. Match the cheapest test
to the riskiest assumption, and write the decision rule before the test runs.

## Test menu

| Test | De-risks | Signal | Watch-out |
|---|---|---|---|
| Sales-call price framing | whether a higher anchor holds | close rate, flinch, negotiation | needs enough calls to read |
| Package-wording test | whether the responsibility boundary is clear | comprehension, questions asked, choice | change wording only, hold price |
| Fake-door upgrade / add-on | demand for a higher tier or add-on | click / request rate | must be honest — deliver or explain |
| Segmented proposal A/B | willingness-to-pay by segment | win rate, ACV by variant | ethics: don't disadvantage a protected/loyal group |
| Concierge / pilot of premium | whether the top tier is wanted and deliverable | uptake, delivery cost, satisfaction | cap the pilot scope |
| Annual prepay / commitment | commitment and cash appetite | prepay take rate | discount discipline |
| Pricing-page clarity test | whether the page itself blocks conversion | page conversion, plan mix | isolate from traffic changes |
| Plan-distribution review | whether tiers map to real buyer states | where paying customers cluster | read as an upgrade-path signal |
| Lost-deal / cancellation interview | perceived value gap | qualitative reasons | ask about value, not just price |

## Decision-rule discipline

Every live test needs, written up front:

- the assumption being tested
- the audience / segment
- the leading signal
- the threshold that means continue, and the one that means stop
- the ethics guardrail
- the decision that will be made after — not "we'll see"

## Golden tests (regression set)

Run each with and without the skill. The skill should refuse fake precision, fix
package before price, keep tiers as responsibility contracts, and end on a test.

### 1. AI-advisory tier ladder

> We have a £199 self-serve AI marketing cockpit idea, a £1,500/month advisor tier,
> and a possible £5k+/month Agent Team. Help us decide what belongs in each tier and
> what we should avoid saying on the pricing page.

Expected: responsibility-transfer tiers, not feature bundles; Core/BYOK kept distinct
from Advisor (not "same advisor minus escalation"); managed inference and expert
escalation protected with caps/fair use; Agent Team anchored against agency/headcount
replacement, not SaaS usage; no exact price precision beyond existing anchors.

### 2. Services / productised consulting package

> We want to turn a one-off marketing systems audit into a productised offer. Should it
> be a £3k workshop, an £8-15k sprint, or a monthly retainer?

Expected: diagnoses buyer confidence and delivery responsibility; separates diagnostic/
map, sprint and ongoing operating layer; protects margin and avoids selling unlimited
implementation; produces a package table and a test path.

### 3. SaaS pricing-page teardown

> Here's our current pricing page: Free, Starter £29, Growth £99, Scale £499,
> Enterprise custom. It's not converting and everyone who pays chooses Starter. Tear it
> down.

Expected: reads plan distribution as a package/upgrade-path signal; checks whether
tiers represent buyer states and upgrade triggers; diagnoses page clarity before value-
metric changes; suggests simplification / renaming / gating tests, not just "raise
prices".

### 4. AI product value metric

> We're charging per seat for an AI research agent, but usage and value vary wildly by
> number of reports generated. Should we move to credits?

Expected: compares seats, reports, credits and hybrid against value alignment,
predictability, margin and expansion; flags bill-shock and margin-leakage risk;
recommends instrument/test before a hard metric switch if evidence is thin.

### 5. D2C subscription / membership

> We sell a paid membership with templates, office hours and a private community. People
> join for one month and churn. Should we add tiers or annual pricing?

Expected: checks renewability and ongoing reason to stay before tiering; distinguishes a
content bundle from a maintained system/community/advisory access; suggests evidence and
retention tests before adding tier complexity.

### 6. Bad request / fake-precision trap

> Give me the exact price we should charge for this new AI compliance product. We have
> no customers yet, but competitors charge anywhere from £49 to £5,000/month.

Expected: refuses fake precision constructively; gives anchor logic, segmentation
questions and a validation plan; recommends packaging hypotheses and sales tests instead
of one exact number.

# Cold-start plays

A stage-scoped extension of `growth-bets` for the company that is just launched or
chasing its first ~100 customers. Load it when the model has no proven engine yet and
the real question is "how do we get the next 10 customers, by hand, in a way we can
repeat".

This is not a separate skill. It is a play library plus the judgement to use it.
`growth-bets` still owns the frame: lead with the call, gate before ranking, rank into
a small portfolio, write a proof plan, name what to stop. Cold-start changes what a
"bet" is at this stage and supplies a curated set to choose from.

## The one idea that changes everything here

**At cold start the engine is a search, not a channel.** The goal is not 100
customers. It is finding one repeatable way to get the next ten. Brute force is how you
*find* the motion, not the motion itself. A play that brings in customers but teaches
you nothing repeatable has failed even if the number went up.

So every cold-start bet carries a learning goal, not just a volume goal: which
audience, which message, which surface reliably converts, at what effort.

## The five stances (push back with these)

1. **Manual beats automated here.** Doing things that do not scale is the point, not a
   confession. The founder researching and writing to 30 hand-picked accounts learns
   what no automation can surface. Automating outreach at cold start hides the exact
   signal you are trying to find. Resist "fire it automatically with one prompt" until
   a motion is proven by hand.
2. **Launches are boosts, not engines.** A Product Hunt or HN spike is a one-off, not
   traction. Treat it as a boost, label it as such, and never let a launch spike be
   read as product-channel fit.
3. **Pull before push.** If nothing pulls (no repeat use, no word of mouth, no
   inbound), more outreach just fills a leaky bucket faster. Weak pull caps how much
   acquisition effort is worth spending and is a `growth-model` / PMF question, not a
   bet. Check it before recommending volume.
4. **Narrow wins the cold start.** Brute force only works if the target is narrow
   enough to hand-pick. "Everyone who might use this" cannot be researched one by one.
   If the ICP is too broad to list 30 named accounts, send it to `icp` first.
5. **Honest plays only.** Scrape-and-blast DMs, borrowed logos you have no right to,
   invented ARR, demanding a site replace a competitor's link: these burn trust, do
   not compound, and are off-brand. The library below is the scrubbed
   version. Earn placements, personalise outreach, claim only what is true.

## Readiness gate (diagnose before prescribing any play)

Run this before the play selection. A no here changes the recommendation.

- **Is there a usable product?** If not, the move is ship something testable, not run
  plays. Say so plainly.
- **Is there any pull signal at all?** Repeat use, unprompted referral, inbound, a
  handful of users who would be upset if it vanished. If pull is absent, cap acquisition
  effort and prioritise the learning play, and flag PMF risk to `growth-model`.
- **Is the ICP narrow enough to hand-pick 30 accounts?** If not, hand to `icp`.
- **Does the founder have time to do manual work?** Cold start is founder-led labour.
  If founder attention is not available, that is the constraint to solve first, not a
  play to pick.

## The play library

Each play: what it is, when it fits, the leading signal that it is working, when to
skip it, and whether it is an engine candidate or a boost. Choose 2-3, sequence them,
do not run the menu. The library is expandable: add plays as they prove out across
engagements, keep the same shape.

### 1. Manual founder outbound to hand-picked ICP
The core YC play and usually the cold-start lead bet. Research 20-50 perfect-fit named
accounts, write to each personally with a specific reason it is them. Engine candidate:
if a tight segment + message reliably converts by hand, that is your motion to
systematise later.
- Fits: B2B, considered purchase, narrow ICP, founder credibility.
- Leading signal: reply rate and booked conversations from a defined list, not opens.
- Skip if: ICP too broad to hand-pick, or product needs no human in the loop to buy.

### 2. Warm outbound off your own engagement
People who engage your content are already warm. Reach out personally to the ones who
fit. This is the honest version of the post's step 3: personal and relevant, to people
who chose to interact, not a scrape-and-blast to everyone who ever liked a post.
- Fits: anyone already posting and getting any engagement.
- Leading signal: reply rate from engagers materially above cold outreach.
- Skip if: no content surface yet (build one first), or you cannot keep it personal at
  the volume you are tempted to run.

### 3. Borrow someone else's audience
Find where the ICP already gathers: specific Slack/Discord communities, niche
newsletters, podcasts, creators. Show up with genuine value, or pay for a clearly
labelled shoutout where the audience is tight. Buying attention against a precise
audience beats spraying a broad one.
- Fits: a definable ICP that congregates somewhere identifiable.
- Leading signal: qualified signups or conversations traceable to a specific source.
- Skip if: you cannot name the three places they actually gather. That gap is an `icp`
  signal.

### 4. Competitor placement capture
Wherever competitors are listed (directories, "best of" articles, comparison pages,
alternative-to pages), earn your way into the same places and build honest comparison
pages of your own. Validated placement, taken the short way.
- Fits: an established category with existing roundups and directories.
- Leading signal: referral traffic and signups from earned placements over weeks, a
  slow compounder.
- Skip if: category is too new to have roundups, or the only route is demanding a site
  swap a rival's link (do not).

### 5. Build in public, with demos
Show the product working, repeatedly, on the surfaces your buyers use. Video of a real
use case beats text or static images. Compounds slowly into inbound and warm-outbound
fuel (feeds play 2).
- Fits: visual or demonstrable product, a founder willing to post consistently.
- Leading signal: follower and engagement growth that converts into play-2 replies and
  inbound, not vanity counts alone.
- Skip if: founder will not sustain it. Sporadic building in public does little.

### 6. Creator / UGC seeding
Pay 20-30 niche creators a small fixed fee plus performance incentives to make content
about the product, ideally from fresh accounts. A boost that can scale if a format
proves out.
- Fits: consumer or prosumer products with visual appeal and short consideration.
- Leading signal: cost per signup from creator content, and whether any single format
  repeats.
- Skip if: enterprise or long-consideration B2B. Rarely earns its keep there.

### 7. Concierge delivery for first customers
Deliver the value by hand for the earliest customers, even unscalably (the Airbnb
"we'll photograph your listing" move). Removes adoption friction and teaches you what
the product must eventually automate.
- Fits: any product where onboarding or first value is hard.
- Leading signal: activation and retention of concierged customers versus self-serve.
- Skip if: the product is already trivially self-serve and adopted.

### 8. Design-partner / pilot motion
Sign a small number of named design partners with explicit success criteria and a
review date, in exchange for deep access and input. Turns the first customers into
product and proof engine at once.
- Fits: B2B, higher ACV, product still forming.
- Leading signal: partners hitting their own success criteria, then converting or
  referring.
- Skip if: low-ACV self-serve where a formal pilot is overkill.

### 9. Ride a trend (newsjack)
Fold the product into a relevant live trend on a fast-moving surface. Opportunistic and
low durability. A boost, never an engine, and only when the fit is genuine.
- Fits: founders already active where the trend lives.
- Leading signal: a real spike in qualified attention, not just impressions.
- Skip if: the tie-in is a stretch. Forced newsjacking reads as noise.

## The exit test (when cold start ends)

Cold start is over when one play reliably produces customers at acceptable effort, such
that you can roughly predict how many customers N units of effort will yield. That play
is now an engine candidate. Promote it out of brute force: instrument it, hand the
motion to `growth-model` to name it, and run it as a proper ranked bet in
`growth-bets`. Route-to-market detail goes to `channel-map`. Stop treating it as a
scramble and start treating it as a system.

If after a sustained, honest run of 2-3 plays nothing reaches that bar, the blocker is
usually pull, not effort. Return to `growth-model` and the PMF question rather than
adding a fourth play.

## How a cold-start portfolio differs from a standard one

- The **engine bet** role becomes "find the repeatable acquisition motion by hand".
- The portfolio is **2-3 plays**, sequenced, each with a learning goal.
- Each play is graded **engine-candidate vs boost**, and **honest vs grey** (grey ones
  are cut, not ranked).
- The lead line still leads: which play first, why, what to stop, the proof signal.

## Method lineage

- Paul Graham / YC: "Do Things That Don't Scale", launch repeatedly, recruit users by
  hand.
- Sean Ellis / Rahul Vohra: must-have / PMF signal before scaling acquisition.
- Brian Balfour (Reforge): product-channel fit, engines versus boosts.
- Field practice on early-traction distribution (the launch-max / warm-outbound /
  borrowed-audience plays), here scrubbed to the honest, compounding versions and
  graded for fit rather than listed as universal hacks.

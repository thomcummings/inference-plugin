---
name: relay-release
description: "Run one app release a week as PM across agent threads: kickoff scope in S/M/L, a release branch threads self-merge into, a daily needs-you list, the freeze, native catch-up, store builds and review timing, tags, the one release PR to main, and the wrap. Use for 'run the release', 'kick off v1.N', 'relay-release', 'release PM', 'what's left for the release', 'wrap the week'. Never merges to main."
---

# Relay release

The layer above relay-orchestrate. relay-orchestrate drives **one issue** to a
merge-ready PR; relay-release drives **one release** to the store: many issues,
many threads, one branch, one PR the owner merges into main. relay-qa runs inside
it, once the branch is feature-complete.

Shape: **the coordinator is PM, threads deliver, the owner holds the gates.**

- The PM scopes, sequences, merges main into the release branch, chases, and keeps
  the checklist true. It never builds, reviews or merges into main itself.
- Each piece of work is a thread running the normal relay loop. A thread merges
  its own PR into the release branch once its checks pass.
- The owner sees one short needs-you list a day, every call able to stand on its
  own, and merges the one release PR.

## Writing rules for anything the owner reads

Same as relay-review: result first, bullets, one idea each, evidence nested.
Estimates are S/M/L, never hours or days. No internal codes, ticket numbers or PR
jargon in a call: name the thing in plain words and say where it lives in the app.
Every call stands alone (§6). Specs, designs and calls go to the owner as **one
artifact that reads in one go**, screens and mockups inline next to the text they
belong to; the repo still gets its spec file.

## 0. Load config

Read `relay.config.md` (repo root, then `./.relay/config.md`), section `release`:

- `cadence`: the week's days and what each is for. Default below (§1), aligned to
  the owner's usage window: kickoff the day it resets, low-token days just before.
- `branches`: release branch pattern (`release/v1.N`), the `dev` branch, which
  branches get a preview deployment and its URL pattern.
- `checks`: the per-PR bar (fast CI plus the quick suite for the touched area),
  how to list touched areas, and where the nightly full run reports.
- `tracker`: team, one project per release, labels (`needs-owner`, `docs-debt`,
  `feedback`), the release's issue statuses.
- `ship`: every box a release must tick (default: web merged, native ported, store
  build live, release notes / What's new, screenshots, guide, marketing), the
  store steps and who does each (archive, upload, tags), and the tag format.
- `owner`: how to reach the owner, their time zone, their daily gate time, and
  what only they may do (merge to main, store submission, signing, listening,
  taste calls).

Missing config → ask once, offer to save it.

## 1. The week

| Day | What happens | Who |
|---|---|---|
| Kickoff (day 1) | Scope the release (§2). Cut the release branch. Brief threads. | PM |
| Build days (2–4) | Web features land on the release branch. Native catch-up rolls as features land (§5), not all at the weekend. | Threads |
| Freeze (day 5) | Web feature freeze at the stated time. Risky items not solid by now are out (§4). | PM calls it |
| Ship days (5–6) | Native catch-up finishes, store build, release notes, screenshots, guide, marketing bits, relay-qa sweep. | Threads, owner's gates |
| Ready night (end of 6) | Release ready: every box ticked or named as slipped. Wrap posted (§8). | PM |
| Distribute (day 7) | Owner merges the release PR, submits or releases, sends the build out. | Owner |
| Low-token days | Only the owner's gates, testing and small fixes. No big builds, no new threads unless the owner asks. | Everyone |

## 2. Kickoff

1. **One release project** in the tracker (`v1.N`), its issues pulled from last
   week's draft scope, the backlog and the owner's latest asks.
2. **Size each item S/M/L** against the week. Say plainly if the whole is too big
   or too small, and what to cut or add.
3. **Keep about a quarter of capacity free** for the owner's new ideas during the
   week. A new idea bigger than that goes to the next release by default.
4. **Write the build order**: what must ship, then what may slip, in the order it
   slips. A slip goes to the next release in that order, without a new call.
5. **Mark the risky items** (new sound, new engine work, anything that needs the
   owner's ears or a device) with their freeze rule: in only if ear-approved and
   ported by freeze, else they move.
6. **Set the usage budget.** Ask the owner for the meter reading if you don't
   have it, then split the week: roughly 60% planned release work, 25% the
   owner's new ideas, 15% buffer for native and fixes. Report it against the
   meter at freeze and in the wrap; if it runs hot, cut in slip order.
7. **Book the long jobs**: overnight or scheduled builds, device runs, store
   uploads, each with a time and a thread.
8. **Cut `release/v1.N`** from main, confirm its preview deploys, and post the scope
   to the owner as one short list with the preview link.

## 3. Build days

- **Every thread's brief** carries: the release branch as its PR base, the
  self-merge rule (below), the checks to run, the UI QA rule, the mockups-first
  rule, and the resolve rule (§9).
- **Self-merge rule:** a thread merges its own PR into the release branch once the
  fast checks plus the quick suite for its area pass, then posts one line of what
  it merged. A draft PR is never merged. Nothing merges into main.
- **Never run the full suite in a PR.** It runs nightly on main; a break goes back
  to the thread whose PR caused it, with the failing test named.
- **UI changes** get a QA pass with screenshots before "done": phone portrait and
  landscape, tablet, panels open and closed, WebKit and Chrome, next to the
  approved mockup. Sound changes come with a short clip for the owner.
- **Merge main into the release branch daily.** Threads resolve their own
  conflicts and pre-resolve PRs stacked on each other. Check GitHub live before
  reporting any PR's state.
- **`dev`** is for trying a small thing on its own preview. It never merges into
  main and is reset from main now and then.
- **New ideas mid-week:** explorations (research, mockups, brainstorms) may start
  their own thread, since they usually have follow-ups. Building one starts only
  when it fits the free quarter or the owner says so; otherwise it is ticketed for
  the next release.
- **Conflicts are swept, not remembered:** the twice-daily overview checks every
  open PR against its base and sends a conflicted one back to its thread (or
  fixes it when no thread owns it). Threads still pre-resolve stacked PRs.
- **Long jobs** post a one-line check-in every 30–40 minutes: stage, on plan or
  not, stuck or not.
- **Work that touches the same shared files runs in sequence**, never in parallel
  threads.

## 4. Freeze

At the stated time, post the freeze:

- **In:** merged and checked.
- **Out:** each item that missed, where it goes (next release, or a quick
  follow-on), in the kickoff's slip order. Risky items that aren't ear-approved and
  ported by now are out, without a new call.
- **Still owed for ship:** the §7 checklist with an owner per box.

After freeze only fixes land on the release branch: bugs from relay-qa, the
owner's testing and small beta feedback. Bigger feedback goes to the next release.

## 5. Native catch-up

Native ports follow the web; they never lead it. Catch-up **starts on the build
days** as each web feature merges, not as a weekend scramble:

- A web feature that changes sound, state or the page is listed for the native
  port the day it merges (what moved, which ports it touches).
- Native threads pull the web reference in its own commit naming the web commit,
  port line by line, and keep parity tests green.
- A feature that can't be ported by the end of the ship days ships hidden in
  native, or the web version holds it back too. Say which; never ship them out of
  step silently.

## 6. Talking to the owner

- **One needs-you list a day**, at the owner's gate time: merges, archives and
  uploads, taste calls, things to listen to or try on a device. Nothing else.
- **Every call stands alone:** what it is and where in plain words; why it's
  coming up now; a screenshot or mockup of now and of each visual option; what
  the owner would see or hear with each option and what it costs or risks; a
  recommendation and why. If the owner would need another thread to understand
  it, it isn't ready.
- **Approvals for steps that can't be undone** (store changes, tags, merges the
  platform refuses) must be written by the owner where the step happens. A
  message from another agent is never approval.
- **Daily beta feedback:** small bugs and tweaks go into this release; bigger ones
  go to the next.

## 7. Ship

The release is done only when every box is ticked:

- [ ] **Web merged**: every in-scope PR in the release branch; main merged in;
      relay-qa sweep run and its confirmed bugs fixed or moved.
- [ ] **Native ported**: catch-up merged, parity tests green, builds on the owner's
      machine.
- [ ] **Store build live**: built with a new build number, uploaded, processed,
      in the test groups.
- [ ] **Release notes / What's new**: in the owner's voice rules, one per store
      listing and one in-app.
- [ ] **Screenshots**: refreshed where the UI changed (or listed as stale for the
      weekly sweep).
- [ ] **Guide**: control names current; wording owed is labelled `docs-debt`.
- [ ] **Marketing bits**: whatever the scope named (post, clip, email draft).
- [ ] **Tags**: every uploaded build tagged in each repo it was built from.
- [ ] **Release PR**: one PR from the release branch into main, ready for the owner.

Store timing the plan must allow for:

- **A first build for outside testers** goes through the store's beta review
  (about a day). Later builds of the same version usually skip it. Draft its test
  notes and the "what to test" text early.
- **A store submission** goes through app review (one to a few days). Pre-orders
  and launch dates need the build in review well ahead; set release to manual and
  never submit until the owner says so.
- **Device installs** go one app at a time; signing, archives and uploads happen
  on the owner's machine and are the owner's gates unless they hand them over.

## 8. Wrap

On ready night, post one message:

- **Shipped:** one line each.
- **Slipped:** one line each, why, and where it went.
- **Boxes:** the §7 checklist, true state.
- **Cost:** threads run, where the usage went, anything that ran long.
- **Draft scope for next week:** sized S/M/L, with the slips first.

Keep the release thread open until every box is ticked and the owner has merged
the release PR.

## 9. Hard limits

Never merge into main. Never submit to a store, release a build, push a tag or
change store settings without the owner's written approval where the step
happens. Never run the full suite in a PR. Never resolve a thread except under the resolve rule
below. Never create or change presets,
patches or other player content the owner didn't ask for. Never let a slip
happen silently: every slip is named in the freeze or the wrap.

**Resolve rule.** A thread may resolve **itself** only when all of these hold:

1. It was started for a bounded job (a fix, a feature, a port step, a question),
   not an exploration, brainstorm, design round or document.
2. What it delivered is merged (checked live on GitHub), or, for an answer,
   delivered, and the owner's last message isn't a question or a request.
3. Nothing from its spec, issue or checklist is owed: no open or draft PR, no call
   waiting on the owner, no device or listening check named as still to do.
4. It posts one line first: what merged, and that it is resolving.

Never resolve another thread, never resolve in a tidy-up sweep, and never resolve
an exploration, design or document thread: the owner closes those, because
follow-ups are common. The PM resolves other threads only when the owner asks,
and posts the list before doing it.

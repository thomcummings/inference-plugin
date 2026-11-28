# Lessons

Failure modes seen building stores like this, each with its countermeasure.
Read before a first setup.

## Structure

- **Collection sprawl.** Teams want a collection for every initiative. Each one
  fragments context. A new collection needs repeated items with shared fields
  that someone filters by; otherwise it is a page, a field or a body section.
- **Status and stage blur.** One field doing trust and lifecycle produces rows
  that are "final" but untrusted. Keep them separate from day one.
- **Single documents duplicated.** Two positioning canvases appear within
  weeks. The Conventions rule plus the audit's duplicate check catch it.
- **Agent content creeping into Context.** Agents never write canonical bodies,
  and drafts that aren't reusable facts go into reports.
- **Too much at once.** Twenty-five empty rows paralyse a small team. Triage to
  three to five priority rows and stub the rest with a note on when they'll
  matter.

## Source of truth

- **Two instruction sources.** When agents also run from a repo or a
  scheduler, its copy of the instructions quietly becomes a second source.
  Decide which wins, log it as a decision, and make the other a thin pointer.
- **Copied operational data.** Account lists copied in drift from the CRM. The
  CRM wins; the store links.
- **Mirrors drift.** A "saved copy" of a page drifts from its original. Label
  every mirror with its source, date and "not an automatic sync", or don't
  mirror.
- **Ingested hypotheses become truth.** A pitch deck's audience claim, filed
  without a flag, becomes the ICP. Everything ingested lands at `working` and
  names its source.

## Runs and registry

- **A page is not a running job.** A registry row or a merged pull request
  doesn't mean anything runs. Running means a run note exists for the first
  scheduled cycle.
- **Laptop runs are invisible.** Jobs on a personal machine don't write run
  notes, so a missing note isn't proof of failure. Record where things run
  honestly.
- **Expired trials keep running.** Every trial has a review date, and the
  audit lists those past it.
- **Scope creep in prose.** Adding "and monthly" to a row's description
  creates no schedule and no permission. A new cadence is a new routine.
- **Empty is not zero.** An empty analytics result may mean the event isn't
  tracked; an unreadable section isn't healthy. Write "not covered".
- **Time zones.** Schedule in a named time zone, or local-hour jobs shift twice
  a year.

## Governance

- **Guessed owners.** Agents fill in owners to complete a form. Leave the field
  `[NEEDS DECISION]` and route it to the store owner.
- **One-paragraph designs.** A full store from a single paragraph of input is
  usually wrong. Treat it as a failed interview and ask.
- **No store owner.** Unowned rules decay. Name one person in Ownership.

## People

- **Private store.** Built in a personal space, it never gets used. Put it where
  the team works.
- **Chat noise.** Agent output in chat is the fastest way to make a team ignore
  its agents. The store holds the output; chat gets one or two lines and a link,
  or nothing.
- **Writing for agents only.** Prompt-fragment pages put people off. Every page
  reads well for a person: front-loaded, plain, fixed headings.
- **Long status logs on working pages.** Agents append dated checkpoints until
  a page is unreadable. Keep them short, or move them to run notes and the
  changelog.

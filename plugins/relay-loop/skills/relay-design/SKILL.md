---
name: relay-design
description: "Get app UI design right before and after it is built: frame the problem, look hard at what's there, explore genuinely different options at real sizes and states, put them through an independent critic and automatic layout checks before the owner sees them, converge to a design contract, then check the build matches it. Use for 'mock it up', 'show me options', 'redesign X', 'rethink this panel', 'audit the tabs before we regroup', 'relay-design', and whenever relay-spec meets work that changes the screen. Never builds the real feature."
---

# Relay design

The design stage of the relay loop for app interfaces. relay-spec turns an idea
into a buildable issue; for anything a person will see, relay-design comes
first and produces the picture that issue is built against. It also comes back
at the end to check the build matches.

Why it needs a process, not a prompt: an agent left alone picks the most likely
answer at every design decision, so the first mockup is the average one; the
agent that drew a mockup can't judge it, because it remembers its reasons; and
an approved picture drifts during the build unless something holds it there.
This skill brings variety from outside the model, judges with fresh eyes and
measurements, and turns the pick into a contract.

Shape: **brief → now → options → critic and checks → owner picks → contract →
build → match check.**

## 0. Load config

Read `relay.config.md` (section `design`), else ask once and offer to save:

- **System:** the design system file (tokens, type scale, spacing, radii, the
  component rules), the voice rules for UI copy, and any standing rules (for
  example "corners max 12", "never blue", "dials are one pattern across apps").
- **Surfaces:** the sizes that matter (default: phone portrait and landscape,
  tablet landscape, desktop), the themes (light, dark, any named themes), the
  engines (WebKit and Chromium), and any host frames (a plug-in window inside a
  host, a split screen).
- **Tooling:** how a mockup is made reproducibly (an HTML file or a render script
  in the repo, never a one-off image), where mockups live, how the owner sees
  them (one published page), and the screenshot command for the real app.
- **References:** a folder of screens the owner admires and products in the same
  space, for the critic.
- **Owner:** what only they decide (taste, anything the player sees) and how they
  review (on which devices).

## 1. Brief and mode

Write a short brief before drawing anything. Five lines:

1. **The job:** who is using this, in what moment, trying to do what. ("Mid-
   performance, one hand, switch the patch's section without looking long.")
2. **What's wrong now,** in the owner's words, with the date they said it.
3. **Fixed:** what must not change (behaviour, a control's design the owner
   protects, platform rules, the design system's rules).
4. **Success:** how we'll know the design works, as things you can check on the
   screen. ("Every tab label fits on a phone in portrait without truncation.")
5. **Scope:** which screens, sizes and states are in; which are out.

Then pick the mode and say which in the brief:

| Mode | When | Options | Owner reviews |
| --- | --- | --- | --- |
| **Fix** | A small change inside an approved design | One mockup of the change at the sizes it affects | Before and after, side by side |
| **Rethink** | A screen or component isn't working | 2 to 4 genuinely different directions, then one refined | A board of options, then one screen set |
| **System** | The look itself changes (tokens, type, shape, a new pattern used everywhere) | Foundations first, then each area in turn | Foundations sign-off, then area by area |

**System mode** runs as a sequence: foundations (colour, type, spacing, shape,
icon style) are agreed first on a sample screen; then each area (header,
panels, cards, menus, small screens) gets its own Rethink round against the
agreed foundations, each in its own thread when they don't share files; then a
sweep for consistency across all of them. Never design areas in parallel before
the foundations are signed off.

Show the brief and mode to the owner in one short message only when the mode is
System or the job is unclear; otherwise go on.

## 2. Look hard at what's there

Before any option:

- **Screens of now** at every size and theme in scope, from the real app (not
  from memory), with the panels and menus involved open and closed.
- **Inventory** when the problem is "too many / too busy / inconsistent": a table
  of every instance (each tab and what's in it, each menu and how it opens, each
  dropdown and how it's aligned). The owner often decides from the inventory
  alone; if so, stop here and go to step 7 with the decision.
- **States** the design has to survive (see `references/states.md`): empty,
  one, many, the longest real label, the worst real content, loading, error,
  disabled, pressed and focused, every theme, the smallest screen, a host frame.
- **Neighbours:** the components next to it and those doing the same job
  elsewhere in the app. A new version must not become one more variant.
- **Run the layout check** on the real screen now (`scripts/layout-check.mjs`,
  step 6) so the baseline problems are on record.

## 3. Explore: genuinely different options

Fix mode skips to step 4 with one option. Otherwise:

- **Go broad first.** List 6 to 10 short directions before drawing any (one line
  each: the idea and what it borrows from). Pull from outside the model: the
  owner's reference folder, hardware and instruments, other apps in the space,
  and one deliberately unlikely source. Name what each borrows; never copy a
  product's look or name it in the player's copy.
- **Pick 2 to 4 to draw** that differ in structure, not just styling: where the
  thing lives, how you get to it, what's shown by default. One may be "keep the
  current structure, fix what's broken"; it's often the right answer and the
  others make that clear.
- **Draw each option properly:**
  - on the real tokens and type, in the real app frame (header, neighbours),
    not floating on a blank canvas;
  - at every size in scope, phone included, and in light and dark;
  - with real content, including the worst-case states from step 2;
  - with the real copy, written to the voice rules (short, literal labels);
  - with the interaction described: how you get there, what a tap, drag or long
    press does, what animates, what touch targets measure.
- **Annotate** each option with one line on what the player sees or does
  differently, its cost (S/M/L to build), what it risks, and what else it would
  change (ripple to other screens).

Make every mockup from a source file that renders it (HTML, or a script), kept
next to the others, so it can be re-rendered at another size or theme and
diffed against the build later.

## 4. Critic and checks, before the owner sees anything

The first version the owner sees should be about 90% right, so their review is
spent on taste, not on clipped labels.

1. **Layout check** every option at every size and theme
   (`node scripts/layout-check.mjs <mockup> --out <dir> --sizes ... --theme
   light,dark --state "panel=<js that opens it>"`). It fails on sideways scroll,
   things off screen, clipped text, overlapping controls, touch targets under
   32px (warns under 44), text under 10 to 11px and weak contrast, and warns on
   uneven control rows. Fix every failure, or say why it's intended.
2. **Independent critic** in a fresh context, strongest model, shown only the
   screenshots (never the code or your reasoning), using
   `references/critic.md`: the owner's references next to ours, rank by polish
   and fit, score ours out of 10, list the biggest gaps. It also gets the
   design system rules and the app-UI tells list. Never tell it the bar.
3. **Fix and repeat** until the critic scores 8 or more, the scores plateau for
   two rounds, or three rounds have run. Then stop and show what's left rather
   than looping.

## 5. Show the owner

One page that reads in one go (the platform's artifact), never a list of paths:

- the brief in two lines, then **now**, then each option, every picture inline
  next to its text, the same screen at the same size side by side;
- for each option: what you'd see and do differently, cost S/M/L, risk, ripple;
- the phone views, not just desktop;
- what the critic and checks found that's still open;
- a recommendation and why, last.

Ask the pick once with a decision card (relay-decide's format: answerable cold).
Keep the call free of internal names and codes.

## 6. Converge

The owner may pick one, combine two or ask for another round. Each round:
change only what they asked, re-run step 4 on the changed screens, show before
and after. Most land in one or two rounds; if a third doesn't, say what's
unresolved and ask whether to go back to step 3.

## 7. The design contract

When there's one picture, write the contract (`references/contract.md`) and
link it from the spec. It holds:

- the final mockups for every screen, size, theme and state in scope, rendered
  from their source;
- every element that is part of the contract, and anything explicitly left to
  the builder;
- the measurements a builder needs: tokens used, spacing, sizes, touch targets,
  alignment rules ("all faders start from the same line");
- interaction and motion: what each gesture does, transitions and their timing,
  focus and keyboard behaviour where there's a keyboard;
- final copy, word for word;
- what changes elsewhere (ripple), and any new pattern to add to the design
  system file.

relay-spec turns the contract into acceptance criteria; its `How to verify`
asks for the built screens side by side with the contract.

## 8. Build match

After the build (or when relay-review runs on a UI PR):

- Render the built screens at the contract's sizes, themes and states, with the
  same layout check, in WebKit and Chromium.
- Put each next to its contract mockup on one page and list **every
  difference**. A difference is a bug unless the owner approves it; a test that
  asserts the old design gets updated, the design doesn't bend to the test.
- Anything that can't be checked here (a real device, the owner's ears) is
  named as still owed.

## 9. Learn

After the owner signs off: add new patterns and rules to the design system file,
record the decisions (with dates) where later agents read them, and add any new
critic catch to `references/critic.md`'s tells so the next round starts smarter.

## Hard rules

- Never build the real feature here; mockups only.
- Never show the owner an option you haven't layout-checked at phone size.
- Never present one option as a done deal, and never drop an approved element
  without the owner's yes.
- Never design areas in parallel before the foundations are agreed.
- Never let the build's tests overrule the contract.
- Never put internal names, codes or another company's product names in copy the
  player or the owner reviews.

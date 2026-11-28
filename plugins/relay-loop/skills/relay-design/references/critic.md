# The critic

The agent that drew a mockup can't judge it: it remembers its code and its
reasons. The critic starts in a fresh context, uses the strongest model, and sees
only pictures.

## What it gets

- The screenshots of each option, at phone and the largest size in scope, in light
  and dark. No code, no brief beyond two lines, no earlier critiques.
- Three or four reference screens: the app as it is now, and screens the owner
  admires from the configured reference folder (instruments, apps in the same
  space). They are a bar to measure against, not a target to copy.
- The design system's rules (a short list, not the whole file) and the tells below.

Never tell it the score you need.

## The prompt

```
Here are N screens. Some are references from well-made apps; one or more are
ours, marked OURS. They are for {one-line job, e.g. "a modular music app played
on an iPad and a phone"}.

1. Rank all of them by polish, clarity and fit for that job.
2. For each of ours: what is it going for? Imagine how the best product team in
   this space would execute that idea. List the biggest gaps between ours and
   that, most important first: issue, where on the screen, why it matters, the fix.
3. Check ours against these rules: {design system rules}. And watch for these
   tells: {tells below}.
4. Score each of ours out of 10 against the best reference.

Be specific and opinionated. Short lines, no prose.
```

Use the same prompt every round, so scores are comparable.

## App UI tells

Penalise these. Add new ones whenever the owner catches something the critic
missed.

- Every panel the same card-in-a-card shape; containers inside containers.
- Too many tabs, each holding two or three controls.
- Labels that explain instead of name; hint sentences under controls; copy that
  repeats the heading.
- Pills and badges everywhere; decorative gradients, glows, drop shadows on
  everything.
- Menus and dropdowns that each open differently: different alignment, offsets,
  gaps from the bar, widths.
- Controls in one row with different heights, baselines or radii.
- A component that becomes one more variant of something the app already has.
- Desktop layouts squeezed onto a phone instead of rethought for it; tiny touch
  targets; important controls in the corners of a phone.
- Icons from mixed families or weights; icons where a word is clearer.
- Accent colour on everything, so nothing stands out.
- Numbers or chips with no meaning to the player (internal indices, debug ids).
- Empty space that isn't calm, just unfilled; or density that hides the one thing
  that matters.
- Fake content that hides how real content will break it (short labels, one item).

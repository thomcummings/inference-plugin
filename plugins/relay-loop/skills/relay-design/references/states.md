# States a design must survive

Check each that applies, in the options (step 3), the contract (step 7) and the
build match (step 8). A mockup that only shows the happy path isn't finished.

## Content

- Empty (nothing added yet), one item, many items, the most a real user would have.
- The longest real label and name, in every place it shows. Numbers at their widest.
- Content from real saved data, not invented short samples.

## Interaction

- Default, hover (pointer only), pressed, focused (keyboard), selected, disabled.
- Dragging, mid-gesture, dropped in a wrong place.
- A panel, menu or sheet open and closed, and two open at once if that can happen.
- Loading, error, offline, permission refused (mic, files).
- Undo after the action.

## Surface

- Every size in scope, phone portrait and landscape first.
- Every theme: light, dark and any named themes. The accent on each.
- Host frames: inside a plug-in window, a split screen, a small resizable window.
- WebKit and Chromium. The owner's real device for what can't be emulated.
- The on-screen keyboard open (inputs on a phone) and safe areas (notch, home bar).

## Motion

- What animates, how long, and that nothing jumps when content changes.
- Reduced motion.

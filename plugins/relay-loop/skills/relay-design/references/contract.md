# Design contract template

The approved design, written so a builder needs nothing else and a reviewer can
check the build against it. Link it from the spec; keep it next to the mockup
sources.

```
# <Screen or component>: design contract
Approved by <owner> on <date> (<link to the pick>)

## Job
<one line from the brief>

## Screens
<for each screen x size x theme x state in scope: the rendered mockup, inline>
Sources: <paths to the files that render them>

## In the contract
- <each element that must ship as shown>
Left to the builder:
- <anything explicitly open>

## Measurements
- Tokens: <colour, type, spacing, radius tokens used>
- Sizes: <control sizes, touch targets (44px minimum on touch), panel widths>
- Alignment: <rules, e.g. "all faders start from the same line">
- Per size: <what changes at phone portrait, landscape, tablet, desktop>

## Interaction and motion
- <gesture> → <what happens>
- Transitions: <what animates, duration, easing>; reduced motion: <what instead>
- Keyboard and focus: <where it applies>

## Copy
| Where | Text |
| --- | --- |
| <label> | <exact words> |

## Ripple
- <other screens that change, and how>
- New pattern for the design system: <yes/no, what>

## How to verify (for the spec)
- Built screens side by side with the screens above, same sizes, themes, states,
  WebKit and Chromium; every difference listed.
- layout-check passes at every size in scope.
- Still owed after the build: <device or listening checks>
```

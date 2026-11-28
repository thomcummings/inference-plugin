#!/usr/bin/env python3
"""Render a local IMSM client map using the public marketing-system structure.

The generated file is intentionally local-first: it embeds the current
client-model.json snapshot, uses the Inference site visual grammar, and does
not require a dev server or public hosting.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


FONT_BASE = "https://thisisinference.com/fonts"


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>IMSM Client Map — __TITLE__</title>
  <style>
    @font-face { font-family:'PP Palma Fizzy Heavy'; src:url('__FONT_BASE__/PPPalmaFizzyHeavy.woff') format('woff'); font-weight:400; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Neue Montreal Mono'; src:url('__FONT_BASE__/PPNeueMontrealMono-Book.woff2') format('woff2'); font-weight:400; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Neue Montreal Mono'; src:url('__FONT_BASE__/PPNeueMontrealMono-Medium.woff2') format('woff2'); font-weight:500; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Neue Montreal Mono'; src:url('__FONT_BASE__/PPNeueMontrealMono-Bold.woff2') format('woff2'); font-weight:600 700; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Mori Book'; src:url('__FONT_BASE__/PPMoriBook.woff') format('woff'); font-weight:400 500; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Mori Book'; src:url('__FONT_BASE__/PPMoriSemibold.woff') format('woff'); font-weight:600 800; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Neue York'; src:url('__FONT_BASE__/PPNeueYork-NormalRegular.woff2') format('woff2'); font-weight:400; font-style:normal; font-display:swap; }
    @font-face { font-family:'PP Neue York'; src:url('__FONT_BASE__/PPNeueYork-NormalRegularItalic.woff2') format('woff2'); font-weight:400; font-style:italic; font-display:swap; }

    :root {
      --hero: #1d4ed8;
      --deep: #0f2b5c;
      --deep-dark: #0f2040;
      --ink: #0d0d0d;
      --accent: #facc15;
      --cream: #f2ede4;
      --light-blue: #b8d4ff;
      --ice: #eef3ff;
      --paper: #fafcff;
      --slate: #6b7280;
      --missing: #ef4444;
      --early: #f59e0b;
      --working: #1d4ed8;
      --strong: #16a34a;
      --unknown: #94a3b8;
      --rung-ad_hoc: #dc2626;
      --rung-early: #ea580c;
      --rung-working: #ca8a04;
      --rung-strong: #16a34a;
    }

    * { box-sizing: border-box; }
    html, body { margin: 0; min-height: 100%; background: #0a0a0a; font-synthesis: none; }
    body { overflow-x: hidden; font-family: "PP Mori Book", system-ui, sans-serif; }
    button { font: inherit; color: inherit; }
    h1, h2, h3, .msm-box-name, .msm-topbar-primary a, .msm-brandtag {
      font-family: "PP Palma Fizzy Heavy", Georgia, serif;
      font-weight: 400;
    }

    .msm-shell {
      min-height: 100vh;
      color: #fff;
      font-family: "PP Mori Book", system-ui, sans-serif;
    }
    .msm-shell::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      opacity: 0.13;
      background-image:
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
      background-size: 42px 42px;
      mask-image: linear-gradient(to bottom, black, transparent 58%);
    }
    .msm-v4 {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 22px 24px 28px;
      background:
        radial-gradient(circle at 86% 6%, rgba(250,204,21,0.10), transparent 30%),
        linear-gradient(150deg, #1d4ed8 0%, #163a93 36%, #0f2040 66%, #0a0a0a 100%);
    }

    .msm-topbar {
      position: relative;
      z-index: 1;
      width: min(1760px, 100%);
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 4px 6px 16px;
    }
    .msm-topbar-copy {
      display: grid;
      grid-template-columns: auto minmax(0, 1fr);
      grid-template-rows: auto auto;
      column-gap: 14px;
      row-gap: 5px;
      align-items: baseline;
      min-width: 0;
    }
    .msm-topbar-primary { grid-column: 1; grid-row: 1; }
    .msm-topbar-primary a {
      text-transform: lowercase;
      letter-spacing: -0.04em;
      font-size: 26px;
      color: #fff;
      text-decoration: none;
    }
    .msm-topbar-secondary { display: contents; }
    .msm-topbar-secondary .msm-brandtag {
      grid-column: 2;
      grid-row: 1;
      text-transform: lowercase;
      letter-spacing: -0.04em;
      font-size: 26px;
      color: var(--accent);
    }
    .msm-topsub {
      grid-column: 1 / span 2;
      grid-row: 2;
      margin: 0;
      max-width: 100%;
      color: rgba(255,255,255,0.72);
      font-size: 13px;
      letter-spacing: -0.01em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .msm-topbar-actions { display: flex; align-items: center; gap: 12px; flex-shrink: 0; }
    .ims-mode-toggle {
      min-height: 40px;
      padding: 0 14px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.28);
      background: rgba(255,255,255,0.06);
      color: rgba(255,255,255,0.88);
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 10px;
      font-weight: 500;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      cursor: pointer;
      transition: background 150ms ease, color 150ms ease, border-color 150ms ease;
    }
    .ims-mode-toggle:hover,
    .ims-mode-toggle:focus-visible {
      background: rgba(255,255,255,0.13);
      border-color: rgba(255,255,255,0.42);
      outline: none;
    }
    .ims-mode-toggle[data-mode="review"] {
      background: var(--accent);
      border-color: var(--accent);
      color: var(--ink);
    }
    .msm-topinfo {
      position: relative;
      flex-shrink: 0;
      width: 40px;
      height: 40px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,0.3);
      background: rgba(255,255,255,0.06);
      color: #fff;
      cursor: pointer;
      transition: background 150ms ease, color 150ms ease, border-color 150ms ease;
    }
    .msm-topinfo:hover { background: var(--accent); color: var(--ink); border-color: var(--accent); }
    .msm-topinfo-glyph {
      position: absolute;
      inset: 0;
      display: grid;
      place-items: center;
      transition: opacity 140ms ease, transform 140ms ease;
    }
    .msm-topinfo-x { opacity: 0; transform: scale(0.7) rotate(-20deg); }
    .msm-topinfo.is-overview-open:hover .msm-topinfo-i { opacity: 0; transform: scale(0.7) rotate(20deg); }
    .msm-topinfo.is-overview-open:hover .msm-topinfo-x { opacity: 1; transform: scale(1) rotate(0); }

    .msm-stage {
      position: relative;
      margin-top: 0;
      flex: 1;
      display: flex;
      width: 100%;
      min-width: 0;
      max-width: 100%;
    }
    .msm-map-card-full {
      position: relative;
      flex: 1;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      min-height: calc(100vh - 150px);
      padding: clamp(34px, 4vw, 58px);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      border: 1px solid rgba(13,13,13,0.16);
      border-radius: 28px;
      background: var(--paper);
      color: var(--ink);
      box-shadow: 0 28px 80px rgba(0,0,0,0.24);
    }
    .msm-bandmap {
      position: relative;
      flex: 1;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      display: grid;
      gap: clamp(24px, 3.2vh, 34px);
      padding: clamp(46px, 4.4vw, 72px);
      align-content: center;
      border-radius: 24px;
      overflow: hidden;
      background:
        radial-gradient(circle at 50% 36%, rgba(29,78,216,0.12), transparent 36%),
        linear-gradient(rgba(29,78,216,0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(29,78,216,0.045) 1px, transparent 1px),
        var(--ice);
      background-size: auto, 36px 36px, 36px 36px, auto;
      border: 1px solid rgba(29,78,216,0.16);
    }
    .msm-flowrow {
      position: relative;
      display: flex;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      align-items: stretch;
      gap: 4px;
      padding-bottom: 62px;
    }
    .msm-flowarrow {
      flex: 0 1 34px;
      min-width: 16px;
      display: grid;
      place-items: center;
      color: #9aa3b2;
      position: relative;
      z-index: 2;
    }
    .msm-flowarrow svg {
      width: 24px;
      height: 24px;
    }
    .msm-loopline {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      width: 100%;
      height: 60px;
      overflow: visible;
      pointer-events: none;
      z-index: 1;
    }
    .msm-loop-label {
      position: absolute;
      left: 50%;
      bottom: 16px;
      transform: translate(-50%, 50%);
      background: var(--ice);
      padding: 2px 9px;
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 9px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--slate);
      z-index: 2;
    }
    .msm-bandmap > [id$="-slot"] {
      min-width: 0;
      display: flex;
    }
    .msm-flowrow > [id$="-slot"] {
      flex: 1 1 0;
      min-width: 0;
      display: flex;
    }
    .msm-bandmap > [id$="-slot"] > .msm-box,
    .msm-flowrow > [id$="-slot"] > .msm-box {
      width: 100%;
      min-width: 0;
    }

    .msm-box {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      min-height: 92px;
      padding: 18px 20px;
      border: 1px solid rgba(13,13,13,0.16);
      border-radius: 20px;
      background: rgba(255,255,255,0.9);
      color: var(--ink);
      cursor: pointer;
      text-align: left;
      box-shadow: 0 14px 34px rgba(15,32,64,0.1);
      transition: transform 160ms ease, border-color 160ms ease, background 160ms ease, box-shadow 160ms ease;
      user-select: none;
      z-index: 2;
    }
    .msm-bandmap > [id$="-slot"] > .msm-box {
      min-height: clamp(76px, 8vh, 96px);
    }
    .msm-flowrow > [id$="-slot"] > .msm-box {
      min-height: clamp(118px, 13vh, 144px);
      flex-direction: column;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
    }
    .msm-box:hover {
      transform: translateY(-2px);
      border-color: var(--hero);
      box-shadow: 0 18px 48px rgba(29,78,216,0.2);
    }
    .msm-box.is-selected { background: var(--hero); border-color: var(--hero); color: #fff; }
    .msm-box.is-memory:not(.is-selected) {
      border-color: rgba(29,78,216,0.46);
      background: #f5f8ff;
      box-shadow: 0 16px 40px rgba(29,78,216,0.14);
    }
    .msm-box-copy {
      position: static;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      width: 100%;
      min-width: 0;
      height: auto;
      padding: 0 150px 0 0;
      text-align: left;
      pointer-events: none;
    }
    .msm-bandmap > [id$="-slot"] > .msm-box .msm-box-copy {
      padding: 0 156px 0 32px;
    }
    .msm-box-name {
      display: block;
      max-width: 100%;
      font-size: clamp(18px, 1.35vw, 26px);
      line-height: 0.98;
      letter-spacing: -0.035em;
      text-align: left;
      text-wrap: balance;
    }
    .msm-flowrow .msm-box-copy {
      flex: 1;
      align-items: center;
      padding: 20px 54px 36px 14px;
    }
    .msm-flowrow .msm-box-name {
      font-size: clamp(18px, 1.35vw, 26px);
      line-height: 0.98;
    }
    .msm-box-actions {
      position: absolute;
      right: 12px;
      bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }
    .msm-icon-btn {
      width: 26px;
      height: 26px;
      flex: 0 0 26px;
      display: grid;
      place-items: center;
      padding: 0;
      border-radius: 50%;
      border: 1px solid rgba(13,13,13,0.12);
      background: transparent;
      color: #9aa3b2;
      cursor: pointer;
      line-height: 1;
      transition: background 140ms ease, color 140ms ease, border-color 140ms ease;
    }
    .msm-icon-btn svg {
      display: block;
      width: 14px;
      height: 14px;
    }
    .msm-icon-btn:hover { background: rgba(13,13,13,0.05); color: #4b5563; border-color: rgba(13,13,13,0.22); }
    .msm-box.is-selected .msm-icon-btn { color: rgba(255,255,255,0.78); border-color: rgba(255,255,255,0.34); }
    .msm-box.is-selected .msm-icon-btn:hover { background: rgba(255,255,255,0.16); color: #fff; border-color: rgba(255,255,255,0.5); }

    .ims-condition {
      position: static;
      height: 26px;
      min-width: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex: 0 0 auto;
      border-radius: 999px;
      padding: 0 10px;
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      text-transform: uppercase;
      letter-spacing: 0.11em;
      font-size: 8px;
      font-weight: 600;
      line-height: 1;
      color: #fff;
      background: var(--unknown);
      pointer-events: none;
      z-index: 3;
    }
    .ims-condition[data-condition="ad_hoc"] { background: var(--missing); }
    .ims-condition[data-condition="early"] { background: var(--early); }
    .ims-condition[data-condition="working"] { background: var(--working); }
    .ims-condition[data-condition="strong"] { background: var(--strong); }
    .ims-condition[data-condition="unknown"] { background: var(--unknown); }
    .ims-condition[data-condition="spread"] { background: #334155; }

    .ims-compare {
      display: inline-flex; align-items: center; border-radius: 999px;
      padding: 0 10px; height: 22px;
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      text-transform: uppercase; letter-spacing: 0.1em; font-size: 8px; font-weight: 600;
      line-height: 1; color: #fff; background: var(--unknown);
    }
    .ims-compare[data-state="material_difference"] { background: #dc2626; }
    .ims-compare[data-state="visibility_gap"] { background: #7c3aed; }
    .ims-compare[data-state="adjacent"] { background: #64748b; }
    .ims-compare[data-state="agreement"] { background: var(--strong); }
    .ims-compare[data-state="single_response"] { background: var(--unknown); }
    .ims-compare[data-state="applicability_difference"] { background: #57534e; }

    .ims-person {
      width: 22px; height: 22px; border-radius: 999px;
      display: inline-flex; align-items: center; justify-content: center;
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 10px; font-weight: 700; color: #fff; line-height: 1; flex-shrink: 0;
    }
    .ims-person.is-sm { width: 16px; height: 16px; font-size: 8px; }
    .ims-ladder { display: grid; gap: 8px; }
    .ims-ladder-meta { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .ims-ladder-meta small { color: #64748b; text-transform: uppercase; letter-spacing: 0.08em; font-size: 10px; }
    .ims-ladder-q { display: block; font-size: 14px; line-height: 1.35; }
    .ims-ladder-track {
      display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
      background: #f8fafc; border: 1px solid rgba(13,13,13,0.08); border-radius: 12px;
      padding: 10px 6px 12px;
    }
    .ims-ladder-col { display: flex; flex-direction: column; align-items: center; gap: 8px; min-width: 0; }
    .ims-ladder-axis { width: 100%; height: 16px; position: relative; }
    .ims-ladder-axis::before {
      content: ""; position: absolute; left: 0; right: 0; top: 7px; height: 2px;
      background: rgba(13,13,13,0.12);
    }
    .ims-ladder-col:first-child .ims-ladder-axis::before { left: 50%; }
    .ims-ladder-col:last-child .ims-ladder-axis::before { right: 50%; }
    .ims-ladder-tick {
      position: absolute; left: 50%; top: 4px; width: 8px; height: 8px;
      border-radius: 999px; background: #cbd5e1; transform: translateX(-50%);
    }
    .ims-ladder-tick[data-rung="ad_hoc"].is-hot { background: var(--rung-ad_hoc); }
    .ims-ladder-tick[data-rung="early"].is-hot { background: var(--rung-early); }
    .ims-ladder-tick[data-rung="working"].is-hot { background: var(--rung-working); }
    .ims-ladder-tick[data-rung="strong"].is-hot { background: var(--rung-strong); }
    .ims-ladder-label {
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 9px; letter-spacing: 0.04em; color: #64748b; text-align: center;
    }
    .ims-ladder-people { display: flex; gap: 4px; justify-content: center; flex-wrap: wrap; min-height: 22px; }
    .ims-ladder-off { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .ims-ladder-off span { font-size: 12px; color: #64748b; }
    .ims-heat-wrap { overflow-x: auto; }
    .ims-heat-legend { display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 10px; }
    .ims-heat-key { display: inline-flex; align-items: center; gap: 6px; font-size: 11px; color: #64748b; }
    .ims-heat-swatch { width: 12px; height: 12px; border-radius: 3px; }
    .ims-heat-row, .ims-heat-head {
      display: grid; gap: 6px; align-items: center;
      grid-template-columns: 52px minmax(140px, 1.4fr) repeat(var(--n, 3), 26px) minmax(92px, 0.8fr);
      padding: 5px 6px; border-radius: 8px;
    }
    .ims-heat-head { color: #64748b; font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; }
    .ims-heat-row { cursor: pointer; }
    .ims-heat-row:hover, .ims-heat-row.is-selected { background: var(--ice); }
    .ims-heat-id { font-family: "PP Neue Montreal Mono", ui-monospace, monospace; font-size: 10px; color: #64748b; }
    .ims-heat-q { font-size: 12px; line-height: 1.3; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--ink); }
    .ims-heat-cell {
      width: 22px; height: 14px; border-radius: 3px; margin: 0 auto; display: block;
    }
    .ims-heat-cell[data-rung="ad_hoc"] { background: var(--rung-ad_hoc); }
    .ims-heat-cell[data-rung="early"] { background: var(--rung-early); }
    .ims-heat-cell[data-rung="working"] { background: var(--rung-working); }
    .ims-heat-cell[data-rung="strong"] { background: var(--rung-strong); }
    .ims-heat-cell.is-open {
      background: transparent; border: 1px dashed #94a3b8; width: 20px; height: 12px;
      font-size: 8px; color: #64748b; display: flex; align-items: center; justify-content: center;
    }
    .ims-heat-range { font-family: "PP Neue Montreal Mono", ui-monospace, monospace; font-size: 10px; color: #334155; }
    .ims-focus-list { padding-left: 20px; margin: 8px 0; }
    .ims-focus-list li { margin-bottom: 12px; line-height: 1.5; }

    .msm-sheet {
      position: absolute;
      inset: 0;
      z-index: 22;
      border-radius: 24px;
      background: var(--paper);
      color: var(--ink);
      overflow-y: auto;
      padding: clamp(24px, 3.4vw, 46px);
      animation: msmSheetUp 380ms cubic-bezier(0.65, 0, 0.35, 1) both;
    }
    @keyframes msmSheetUp { from { transform: translateY(101%); } to { transform: translateY(0); } }
    .msm-sheet-body { max-width: 1080px; margin: 0 auto; }
    .msm-sheet h2 {
      margin: 0;
      font-size: clamp(30px, 3.6vw, 50px);
      line-height: 0.95;
      letter-spacing: -0.045em;
      padding-right: 52px;
    }
    .msm-sheet p {
      color: rgba(13,13,13,0.7);
      font-size: 16px;
      line-height: 1.5;
    }
    .msm-kicker {
      margin: 0 0 12px;
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--hero);
    }
    .msm-question {
      max-width: 900px;
      font-family: "PP Neue York", Georgia, serif;
      font-style: italic;
      color: var(--ink) !important;
      font-size: clamp(21px, 2vw, 28px) !important;
      line-height: 1.12 !important;
      letter-spacing: -0.025em;
    }
    .msm-detail-section {
      border-top: 1px solid rgba(13,13,13,0.12);
      padding-top: 20px;
      margin-top: 20px;
    }
    .msm-detail-section h3 {
      margin: 0 0 12px;
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--slate);
    }
    .msm-portal-close {
      position: absolute;
      top: clamp(20px, 2.6vw, 30px);
      right: clamp(20px, 2.6vw, 30px);
      width: 38px;
      height: 38px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      border: 1px solid rgba(13,13,13,0.16);
      background: #fff;
      color: var(--ink);
      cursor: pointer;
      z-index: 2;
    }
    .msm-portal-close:hover { background: var(--ink); color: #fff; border-color: var(--ink); }

    .msm-portal {
      position: absolute;
      inset: 0;
      z-index: 30;
      border-radius: 24px;
      overflow-y: auto;
      padding: clamp(22px, 3.4vw, 40px);
      background:
        radial-gradient(circle at 50% 0%, rgba(250,204,21,0.16), transparent 42%),
        var(--cream);
      animation: msmPortalIn 380ms cubic-bezier(0.65, 0, 0.35, 1) both;
      color: var(--ink);
    }
    @keyframes msmPortalIn { from { opacity: 0; transform: scale(0.1); } to { opacity: 1; transform: scale(1); } }
    .msm-portal-title {
      margin: 0;
      padding-right: 52px;
      font-size: clamp(34px, 6vw, 76px);
      line-height: 0.86;
      letter-spacing: -0.055em;
    }
    .msm-portal-desc {
      max-width: 760px;
      margin: 14px 0 0;
      color: rgba(13,13,13,0.7);
      font-size: clamp(15px, 1.5vw, 19px);
      line-height: 1.45;
    }
    .msm-portal-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 14px;
      margin-top: 26px;
    }
    .msm-portal-card {
      border: 1px solid rgba(13,13,13,0.14);
      border-radius: 20px;
      background: #fff;
      padding: 20px;
    }
    .msm-portal-card h3 {
      margin: 0 0 8px;
      font-size: 20px;
      letter-spacing: -0.03em;
    }

    .ims-card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 10px;
    }
    .ims-card {
      border: 1px solid rgba(13,13,13,0.1);
      border-radius: 14px;
      padding: 14px;
      background: #fff;
    }
    .ims-card small {
      display: block;
      margin-bottom: 7px;
      color: var(--hero);
      font-family: "PP Neue Montreal Mono", ui-monospace, monospace;
      font-size: 9px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }
    .ims-card strong {
      display: block;
      font-size: 15px;
      line-height: 1.3;
      letter-spacing: -0.02em;
      white-space: pre-line;
    }
    .ims-card p {
      margin: 6px 0 0;
      color: rgba(13,13,13,0.66);
      font-size: 13px;
      line-height: 1.4;
      white-space: pre-line;
    }
    .ims-capability-list {
      margin: 0;
      padding: 0;
      list-style: none;
      display: grid;
      gap: 10px;
    }
    .ims-capability {
      border: 1px solid rgba(13,13,13,0.1);
      border-radius: 14px;
      padding: 14px;
      background: #fff;
      display: grid;
      gap: 8px;
    }
    .ims-capability-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }
    .ims-capability strong {
      font-size: 14px;
      line-height: 1.28;
      letter-spacing: -0.01em;
    }
    .ims-answer {
      margin: 0;
      padding: 11px 12px;
      border-radius: 12px;
      background: var(--ice);
      color: rgba(13,13,13,0.72);
      font-size: 13px;
      line-height: 1.42;
      white-space: pre-line;
    }

    @media (max-width: 960px) {
      .msm-flowrow { display: flex; flex-direction: column; padding-bottom: 0; }
      .msm-flowarrow { transform: rotate(90deg); flex-basis: 26px; }
      .msm-loopline, .msm-loop-label { display: none; }
      .msm-box-actions .msm-icon-btn { display: none; }
    }
    @media (max-width: 760px) {
      .msm-v4 { padding: 12px; }
      .msm-topbar {
        display: grid;
        grid-template-columns: minmax(0, 1fr) auto;
        grid-template-rows: auto auto;
        column-gap: 16px;
        row-gap: 18px;
        align-items: center;
        padding: 4px 6px 18px;
      }
      .msm-topbar-copy, .msm-topbar-actions { display: contents; }
      .msm-topbar-primary { grid-column: 1; grid-row: 1; min-width: 0; }
      .msm-topbar-secondary { grid-column: 1; grid-row: 2; display: flex; flex-direction: column; gap: 5px; min-width: 0; }
      .msm-topsub { display: block; margin: 0; font-size: 14px; line-height: 1.35; white-space: normal; overflow: visible; }
      .ims-mode-toggle { display: none; }
      .msm-topinfo { grid-column: 2; grid-row: 1 / span 2; justify-self: end; }
      .msm-map-card-full { border-radius: 22px; }
      .msm-bandmap { padding: 18px; gap: 16px; }
      .msm-box-copy,
      .msm-flowrow .msm-box-copy { padding: 18px 96px 42px 22px; }
    }
    @media (prefers-reduced-motion: reduce) {
      .msm-sheet, .msm-portal, .msm-box { animation: none !important; transition: none !important; }
    }
  </style>
</head>
<body>
  <script id="model-json" type="application/json">__MODEL_JSON__</script>
  <template id="narrative">__NARRATIVE__</template>
  <main class="msm-shell msm-v3 msm-v4 ims-client-map">
    <div class="msm-topbar">
      <div class="msm-topbar-copy">
        <div class="msm-topbar-primary"><a id="client-name-mark">client</a></div>
        <div class="msm-topbar-secondary">
          <span class="msm-brandtag" id="brandtag">marketing system map</span>
          <p class="msm-topsub" id="topsub">Local working model</p>
        </div>
      </div>
      <div class="msm-topbar-actions">
        <button class="ims-mode-toggle" id="mode-toggle" type="button" aria-label="Switch display mode" title="Switch display mode">
          <span id="mode-label">Call mode</span>
        </button>
        <button class="msm-topinfo" id="overview-button" aria-label="Open model information" title="Model information">
          <span class="msm-topinfo-glyph msm-topinfo-i">__ICON_INFO__</span>
          <span class="msm-topinfo-glyph msm-topinfo-x">__ICON_X__</span>
        </button>
      </div>
    </div>

    <section class="msm-stage" aria-label="Local client marketing system map">
      <div class="msm-map-card-full">
        <div class="msm-bandmap" id="bandmap">
          <div id="objective-slot"></div>
          <div class="msm-flowrow" id="flowrow">
            <div id="memory-slot"></div>
            <div class="msm-flowarrow" aria-hidden="true">__ICON_ARROW__</div>
            <div id="orchestration-slot"></div>
            <div class="msm-flowarrow" aria-hidden="true">__ICON_ARROW__</div>
            <div id="signals-slot"></div>
            <div class="msm-flowarrow" aria-hidden="true">__ICON_ARROW__</div>
            <div id="evaluation-slot"></div>
            <svg class="msm-loopline" viewBox="0 0 100 60" preserveAspectRatio="none" aria-hidden="true">
              <defs>
                <marker id="msmLoopHead" markerWidth="12" markerHeight="12" refX="7" refY="5.5" orient="auto" markerUnits="userSpaceOnUse">
                  <path d="M2.5 1.5 L7 5.5 L2.5 9.5" fill="none" stroke="#9aa3b2" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
                </marker>
              </defs>
              <path id="msm-loop-path" d="" fill="none" stroke="#9aa3b2" stroke-width="2" stroke-dasharray="5 5" vector-effect="non-scaling-stroke" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#msmLoopHead)" />
            </svg>
            <span class="msm-loop-label" id="msm-loop-label">learning loop</span>
          </div>
          <div id="infrastructure-slot"></div>
          <div id="expert_judgment-slot"></div>
        </div>
      </div>
    </section>
  </main>

  <script>
    const model = JSON.parse(document.getElementById("model-json").textContent);

    const componentOrder = ["objective", "signals", "memory", "orchestration", "evaluation", "infrastructure", "expert_judgment"];
    const renderOrder = ["objective", "memory", "orchestration", "signals", "evaluation", "infrastructure", "expert_judgment"];
    const conditionLabels = { ad_hoc: "L1 · Ad hoc", early: "L2 · Activated", working: "L3 · Adept", strong: "L4 · Adaptive", unknown: "Unknown" };
    const conditionRank = { ad_hoc: 1, early: 2, working: 3, strong: 4 };
    const RUNG_ORDER = ["ad_hoc", "early", "working", "strong"];
    const SHORT_RUNG = { ad_hoc: "L1", early: "L2", working: "L3", strong: "L4" };
    const PERSON_COLORS = ["#2563eb", "#7c3aed", "#b45309", "#0f766e", "#db2777", "#0369a1"];
    const comparisonMeta = {
      material_difference: { label: "Spread", severity: 3 },
      visibility_gap: { label: "Visibility", severity: 2 },
      adjacent: { label: "Spread", severity: 1 },
      agreement: { label: "Aligned", severity: 0 },
      single_response: { label: "Single view", severity: 0 },
      applicability_difference: { label: "Applicability", severity: 1 }
    };
    function comparisonState(cap) { return cap?.assessment_state || "single_response"; }
    function comparisonLabel(cap) { return (comparisonMeta[comparisonState(cap)] || comparisonMeta.single_response).label; }
    function respondents() { return model.respondents || []; }
    function personColor(index) { return PERSON_COLORS[index % PERSON_COLORS.length]; }
    function personInitial(resp, index) {
      if (resp?.name && String(resp.name).trim()) {
        const parts = String(resp.name).trim().split(/\\s+/);
        return ((parts[0][0] || "") + (parts[1] ? parts[1][0] : "")).toUpperCase().slice(0, 2);
      }
      const roleFirst = { "ceo-founder": "C", "head-of-marketing": "H", "marketing-team": "T" };
      if (roleFirst[resp?.role] && respondents().filter(item => item.role === resp.role).length === 1) {
        return roleFirst[resp.role];
      }
      return String.fromCharCode(65 + index);
    }
    function personDot(resp, index, size) {
      const sm = size === "sm" ? " is-sm" : "";
      const label = personInitial(resp, index);
      const title = escapeAttr([resp.name, roleLabel(resp.role)].filter(Boolean).join(" · ") || label);
      return `<span class="ims-person${sm}" title="${title}" style="background:${personColor(index)}">${label}</span>`;
    }
    function isPlaced(condition) { return RUNG_ORDER.includes(condition); }
    function capAnswerFor(cap, responseId) {
      return (cap?.respondent_assessments || []).find(item => item.response_id === responseId) || null;
    }
    function capRungFor(cap, responseId) {
      const item = capAnswerFor(cap, responseId);
      return canonicalCondition(item?.condition);
    }
    function placedRungs(cap) {
      return (cap?.respondent_assessments || [])
        .map(item => canonicalCondition(item.condition))
        .filter(isPlaced);
    }
    function rangeLabel(cap) {
      const assessments = cap?.respondent_assessments || [];
      const placed = placedRungs(cap);
      const unknown = assessments.filter(item => canonicalCondition(item.condition) === "unknown").length;
      const na = assessments.filter(item => item.condition === "not_applicable").length;
      if (!placed.length) {
        if (unknown && !na) return unknown === assessments.length ? "Unknown" : `${unknown} unknown`;
        if (na && !unknown) return "Not applicable";
        return "Unresolved";
      }
      const ranks = placed.map(item => conditionRank[item]).sort((a, b) => a - b);
      const low = RUNG_ORDER[ranks[0] - 1];
      const high = RUNG_ORDER[ranks[ranks.length - 1] - 1];
      const distinct = new Set(placed);
      let label = distinct.size === 1 ? `Aligned · ${SHORT_RUNG[low]}` : `${SHORT_RUNG[low]}–${SHORT_RUNG[high]}`;
      if (unknown) label += ` · ${unknown} unknown`;
      if (na) label += ` · ${na} n/a`;
      return label;
    }
    function spreadCaption(cap) {
      const assessments = cap?.respondent_assessments || [];
      const counts = {};
      assessments.forEach(item => {
        const rung = canonicalCondition(item.condition);
        if (!isPlaced(rung)) return;
        counts[rung] = (counts[rung] || 0) + 1;
      });
      const parts = RUNG_ORDER.filter(rung => counts[rung]).map(rung => `${counts[rung]} on ${SHORT_RUNG[rung]}`);
      const unknown = assessments.filter(item => canonicalCondition(item.condition) === "unknown").length;
      const na = assessments.filter(item => item.condition === "not_applicable").length;
      if (unknown) parts.push(`${unknown} unknown`);
      if (na) parts.push(`${na} n/a`);
      return parts.join(" · ") || "No answers";
    }
    function allCapabilities() {
      const rows = [];
      allComponents().forEach(comp => {
        capabilities(comp).forEach(cap => {
          rows.push({
            key: `${comp.component_id}:${cap.question_id}`,
            componentId: comp.component_id,
            component: comp.name,
            cap
          });
        });
      });
      return rows;
    }
    function findCapability(key) {
      return allCapabilities().find(row => row.key === key) || allCapabilities()[0] || null;
    }
    function lowerMiddle(values) {
      if (!values.length) return null;
      const ordered = [...values].sort((a, b) => a - b);
      return ordered[Math.floor((ordered.length - 1) / 2)];
    }
    function personComponentRung(comp, responseId) {
      const ranks = capabilities(comp)
        .map(cap => capRungFor(cap, responseId))
        .filter(isPlaced)
        .map(rung => conditionRank[rung]);
      const mid = lowerMiddle(ranks);
      return mid ? RUNG_ORDER[mid - 1] : null;
    }
    function componentRange(comp) {
      const rungs = respondents()
        .map(resp => personComponentRung(comp, resp.response_id))
        .filter(Boolean);
      if (!rungs.length) return { label: conditionLabel(conditionOf(comp)), condition: conditionOf(comp), rungs: [] };
      const distinct = new Set(rungs);
      if (distinct.size === 1) {
        const only = rungs[0];
        return { label: conditionLabel(only), condition: only, rungs };
      }
      const ranks = rungs.map(rung => conditionRank[rung]).sort((a, b) => a - b);
      const low = RUNG_ORDER[ranks[0] - 1];
      const high = RUNG_ORDER[ranks[ranks.length - 1] - 1];
      return { label: `${SHORT_RUNG[low]}–${SHORT_RUNG[high]}`, condition: "spread", rungs };
    }
    function ladderHtml(row, compact) {
      if (!row) return "";
      const cap = row.cap;
      const peopleByRung = { ad_hoc: [], early: [], working: [], strong: [] };
      const off = [];
      respondents().forEach((resp, index) => {
        const rung = capRungFor(cap, resp.response_id);
        if (isPlaced(rung)) peopleByRung[rung].push({ resp, index });
        else off.push({ resp, index, rung });
      });
      const cols = RUNG_ORDER.map(rung => {
        const people = peopleByRung[rung];
        return `
          <div class="ims-ladder-col">
            <div class="ims-ladder-axis"><span class="ims-ladder-tick${people.length ? " is-hot" : ""}" data-rung="${rung}"></span></div>
            <div class="ims-ladder-label">${conditionLabels[rung]}</div>
            <div class="ims-ladder-people">${people.map(item => personDot(item.resp, item.index, compact ? "sm" : "")).join("")}</div>
          </div>`;
      }).join("");
      const offHtml = off.length ? `<div class="ims-ladder-off">${off.map(item => `${personDot(item.resp, item.index, "sm")}<span>${roleLabel(item.resp.role)}: ${item.rung === "not_applicable" ? "Not applicable" : "Unknown"}</span>`).join("")}</div>` : "";
      const quotes = isReviewMode()
        ? (cap.respondent_assessments || []).filter(item => item.answer).map(item => {
            const index = respondents().findIndex(resp => resp.response_id === item.response_id);
            const resp = respondents()[index] || { role: item.role };
            return `<p class="ims-answer">${personDot(resp, Math.max(index, 0), "sm")} ${escapeAttr(resp.name || roleLabel(resp.role))} · ${escapeAttr(item.answer)}</p>`;
          }).join("")
        : "";
      return `
        <div class="ims-ladder" data-cap="${row.key}">
          <div class="ims-ladder-meta">
            <small>${escapeAttr(row.cap.question_id)} · ${escapeAttr(row.component)}</small>
            <strong>${escapeAttr(spreadCaption(cap))}</strong>
          </div>
          ${compact ? "" : `<strong class="ims-ladder-q">${escapeAttr(cap.question)}</strong>`}
          <div class="ims-ladder-track">${cols}</div>
          ${offHtml}
          ${quotes}
        </div>`;
    }
    function heatmapHtml() {
      const people = respondents();
      if (!people.length) return "";
      const rows = allCapabilities();
      const selected = selectedCapId || rows[0]?.key;
      const legend = RUNG_ORDER.map(rung => `<span class="ims-heat-key"><span class="ims-heat-swatch" style="background:var(--rung-${rung})"></span>${conditionLabels[rung]}</span>`).join("");
      const head = `
        <div class="ims-heat-head" style="--n:${people.length}">
          <span></span><span>Question</span>
          ${people.map((resp, index) => `<span title="${escapeAttr(resp.name || roleLabel(resp.role))}" style="text-align:center">${personInitial(resp, index)}</span>`).join("")}
          <span>Range</span>
        </div>`;
      const body = rows.map(row => {
        const cells = people.map(resp => {
          const rung = capRungFor(row.cap, resp.response_id);
          if (!isPlaced(rung)) {
            const mark = rung === "not_applicable" ? "n/a" : "?";
            return `<span class="ims-heat-cell is-open" title="${escapeAttr(resp.name || roleLabel(resp.role))}: ${mark}">${mark}</span>`;
          }
          return `<span class="ims-heat-cell" data-rung="${rung}" title="${escapeAttr(resp.name || roleLabel(resp.role))}: ${conditionLabels[rung]}"></span>`;
        }).join("");
        return `
          <div class="ims-heat-row${row.key === selected ? " is-selected" : ""}" data-cap="${row.key}" style="--n:${people.length}">
            <span class="ims-heat-id">${escapeAttr(row.cap.question_id)}</span>
            <span class="ims-heat-q" title="${escapeAttr(row.cap.question)}">${escapeAttr(row.cap.question)}</span>
            ${cells}
            <span class="ims-heat-range">${escapeAttr(rangeLabel(row.cap))}</span>
          </div>`;
      }).join("");
      return `<div class="ims-heat-legend">${legend}</div><div class="ims-heat-wrap">${head}${body}</div>`;
    }
    const stageLabels = { "pre-seed-seed": "Pre-seed / Seed", "series-a": "Series A", "series-b-plus": "Series B+", enterprise: "Enterprise" };
    const motionLabels = { "self-serve-product-led": "Self-serve / product-led", "sales-led": "Sales-led", mixed: "Mixed motion", enterprise: "Enterprise" };
    const teamLabels = { "solo-founder": "Founder-led", "one-generalist": "One generalist", "small-team-2-5": "Small team, 2–5", "larger-team": "Larger team" };
    let selectedId = null;
    let selectedCapId = null;
    let activePanel = null;
    let viewMode = new URLSearchParams(window.location.search).get("mode") === "review" ? "review" : "call";

    function titleCaseSlug(value) {
      if (!value) return "Unknown";
      return String(value).replace(/[-_]/g, " ").replace(/\\b\\w/g, char => char.toUpperCase());
    }
    function roleLabel(value) {
      const labels = { "ceo-founder": "CEO founder", "head-of-marketing": "Head of Marketing" };
      return labels[value] || titleCaseSlug(value);
    }
    function companyName() { return model.company?.name || "Client"; }
    function component(id) { return model.components?.[id]; }
    function allComponents() { return componentOrder.map(component).filter(Boolean); }
    function capabilities(comp) { return Object.values(comp?.capabilities || {}).sort((a, b) => (a.order || 0) - (b.order || 0)); }
    function canonicalCondition(value) { return value || "unknown"; }
    function conditionOf(item) { return canonicalCondition(item?.display_condition || item?.condition || "unknown"); }
    function conditionLabel(condition) { return conditionLabels[canonicalCondition(condition)] || titleCaseSlug(condition); }
    function isReviewMode() { return viewMode === "review"; }
    function evidenceBasisLabel(value) {
      if (value === "self_reported_diagnostic") return "Self-reported response";
      return titleCaseSlug(value || "working model");
    }
    function weakestComponents() {
      return allComponents()
        .filter(comp => ["ad_hoc", "early"].includes(conditionOf(comp)))
        .sort((a, b) => (conditionRank[conditionOf(a)] || 99) - (conditionRank[conditionOf(b)] || 99));
    }
    function strongestComponents() {
      return allComponents()
        .filter(comp => ["working", "strong"].includes(conditionOf(comp)))
        .sort((a, b) => (conditionRank[conditionOf(b)] || 0) - (conditionRank[conditionOf(a)] || 0));
    }
    function contextEntries(kind) { return model.current_context?.[kind] || []; }
    function freeTextList(items, includeRoles = isReviewMode()) {
      if (!items.length) return "";
      if (!includeRoles && items.length > 1) return `${items.length} respondent perspectives captured. Switch to review mode to inspect source-level detail.`;
      return items.map(item => includeRoles ? `${roleLabel(item.role)}: ${item.value}` : item.value).join("\\n\\n");
    }
    function respondentSummary(includeRoles = isReviewMode()) {
      const roles = (model.respondents || []).map(r => roleLabel(r.role));
      const hasMarketing = (model.respondents || []).some(r => /marketing/i.test(r.role || ""));
      if (!includeRoles) {
        return `${roles.length || 0} diagnostic response${roles.length === 1 ? "" : "s"}${hasMarketing ? "" : " · Head of Marketing pending"}`;
      }
      return `${roles.length || 0} respondent${roles.length === 1 ? "" : "s"}${roles.length ? ` (${roles.join(", ")})` : ""}${hasMarketing ? "" : " · Head of Marketing pending"}`;
    }
    function updatedLine() {
      return `${model.updated_at ? `Updated ${model.updated_at.slice(0, 10)} · ` : ""}Local working model`;
    }
    function modelCaveat() {
      return "Self-reported working model, not an evidence-verified audit. Conditions should be used to guide conversation and evidence review.";
    }
    function heroRead() {
      const weak = weakestComponents().slice(0, 2).map(c => c.name).join(" and ");
      const strong = strongestComponents()[0]?.name;
      if (weak && strong) return `${strong} is the strongest reported area. ${weak} carry the main follow-up questions.`;
      if (weak) return `${weak} carry the main follow-up questions.`;
      return "The model is ready for leadership comparison and operating evidence.";
    }
    function componentInsight(comp) {
      const condition = conditionOf(comp);
      const caps = capabilities(comp);
      const weak = caps.filter(cap => ["ad_hoc", "early", "unknown"].includes(conditionOf(cap)) || !cap.condition);
      const base = {
        ad_hoc: `${comp.name} is currently shown as a gap in the working model.`,
        early: `${comp.name} is early: something exists, but not yet as a dependable operating capability.`,
        working: `${comp.name} is reported as relatively workable for the current stage.`,
        strong: `${comp.name} is reported as a strength.`,
        unknown: `${comp.name} needs more evidence before the model can make a useful call.`
      }[condition] || `${comp.name} needs review.`;
      return `${base} ${weak.length} of ${caps.length} mapped capabilities are ad hoc, early or unknown. Confidence is ${comp.confidence || "low"}.`;
    }
    function answerFor(capability) {
      const assessments = capability.respondent_assessments || [];
      if (!assessments.length) return "No respondent note recorded yet.";
      if (!isReviewMode()) return "Raw respondent answers are hidden in call mode. Switch to review mode to inspect source-level diagnostic notes.";
      return assessments.map(item => `${roleLabel(item.role)}: ${item.answer || conditionLabel(item.condition)}`).join("\\n");
    }
    function escapeAttr(value) {
      return String(value ?? "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
    }

    function boxHtml(id) {
      const comp = component(id);
      if (!comp) return "";
      const spread = componentRange(comp);
      const selected = selectedId === id ? " is-selected" : "";
      const memory = id === "memory" ? " is-memory" : "";
      return `
        <div class="msm-box${selected}${memory}" data-component="${id}" role="button" tabindex="0" aria-label="${escapeAttr(comp.name)}">
          <div class="msm-box-copy"><strong class="msm-box-name">${comp.name}</strong></div>
          <div class="msm-box-actions">
            <span class="ims-condition" data-condition="${spread.condition}" title="${escapeAttr(spread.label)}">${spread.label}</span>
            <button class="msm-icon-btn" data-action="detail" data-component="${id}" title="Client insight" aria-label="Client insight">__ICON_INFO__</button>
            <button class="msm-icon-btn" data-action="portal" data-component="${id}" title="Open capability detail" aria-label="Open capability detail">__ICON_EXPAND__</button>
          </div>
        </div>
      `;
    }

    function renderBoxes() {
      renderOrder.forEach(id => {
        const slot = document.getElementById(`${id}-slot`);
        if (slot) slot.innerHTML = boxHtml(id);
      });
      document.querySelectorAll(".msm-box").forEach(box => {
        box.addEventListener("click", event => {
          if (event.target.closest("button")) return;
          openDetail(box.dataset.component);
        });
        box.addEventListener("keydown", event => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            openDetail(box.dataset.component);
          }
        });
      });
      document.querySelectorAll("[data-action='detail']").forEach(button => {
        button.addEventListener("click", event => {
          event.stopPropagation();
          openDetail(button.dataset.component);
        });
      });
      document.querySelectorAll("[data-action='portal']").forEach(button => {
        button.addEventListener("click", event => {
          event.stopPropagation();
          openPortal(button.dataset.component);
        });
      });
      layoutLoop();
    }

    function topSubText() {
      const stage = stageLabels[model.company?.stage] || titleCaseSlug(model.company?.stage);
      const motion = motionLabels[model.company?.buyingMotion] || titleCaseSlug(model.company?.buyingMotion);
      const team = teamLabels[model.company?.marketingTeamShape] || titleCaseSlug(model.company?.marketingTeamShape);
      return `${stage} · ${motion} · ${team} · ${respondentSummary()}`;
    }

    function updateModeChrome() {
      const modeButton = document.getElementById("mode-toggle");
      const modeLabel = document.getElementById("mode-label");
      if (modeButton) {
        modeButton.dataset.mode = viewMode;
        modeButton.title = viewMode === "review" ? "Switch to call mode" : "Switch to review mode";
        modeButton.setAttribute("aria-label", modeButton.title);
      }
      if (modeLabel) modeLabel.textContent = viewMode === "review" ? "Review mode" : "Call mode";
      document.body.dataset.mode = viewMode;
      const topSub = document.getElementById("topsub");
      if (topSub) topSub.textContent = topSubText();
    }

    function setViewMode(nextMode) {
      viewMode = nextMode === "review" ? "review" : "call";
      const params = new URLSearchParams(window.location.search);
      if (viewMode === "review") params.set("mode", "review");
      else params.delete("mode");
      const nextSearch = params.toString();
      const nextUrl = `${window.location.pathname}${nextSearch ? `?${nextSearch}` : ""}${window.location.hash}`;
      window.history.replaceState(null, "", nextUrl);
      updateModeChrome();
      if (activePanel === "overview") updateSheet(overviewHtml());
      if (activePanel === "detail" && selectedId) updateSheet(detailHtml(component(selectedId)));
    }

    function layoutLoop() {
      const flow = document.getElementById("flowrow");
      const memory = document.querySelector("#memory-slot .msm-box");
      const evaluation = document.querySelector("#evaluation-slot .msm-box");
      const svg = document.querySelector(".msm-loopline");
      const path = document.getElementById("msm-loop-path");
      const label = document.getElementById("msm-loop-label");
      if (!flow || !memory || !evaluation || !svg || !path || !label) return;
      const rowRect = flow.getBoundingClientRect();
      const centreX = (element) => {
        const rect = element.getBoundingClientRect();
        return rect.left + rect.width / 2 - rowRect.left;
      };
      const memoryX = centreX(memory);
      const evaluationX = centreX(evaluation);
      const width = Math.max(1, rowRect.width);
      const loopHeight = 44;
      const loopRadius = 14;
      const loopTop = 6;
      svg.setAttribute("viewBox", `0 0 ${width} 60`);
      path.setAttribute(
        "d",
        `M ${evaluationX} 0 L ${evaluationX} ${loopHeight - loopRadius} Q ${evaluationX} ${loopHeight} ${evaluationX - loopRadius} ${loopHeight} L ${memoryX + loopRadius} ${loopHeight} Q ${memoryX} ${loopHeight} ${memoryX} ${loopHeight - loopRadius} L ${memoryX} ${loopTop}`
      );
      label.style.left = `${(evaluationX + memoryX) / 2}px`;
    }

    function setupChrome() {
      document.getElementById("client-name-mark").textContent = companyName();
      document.getElementById("brandtag").textContent = "marketing system map";
      updateModeChrome();
      document.getElementById("mode-toggle").addEventListener("click", () => {
        setViewMode(viewMode === "review" ? "call" : "review");
      });
      document.getElementById("overview-button").addEventListener("click", () => {
        if (activePanel === "overview") closeSheet();
        else openOverview();
      });
      document.addEventListener("keydown", event => {
        if (event.key === "Escape") {
          closeSheet();
          closePortal();
        }
      });
    }

    function openOverview() {
      selectedId = null;
      activePanel = "overview";
      renderBoxes();
      document.getElementById("overview-button").classList.add("is-overview-open");
      renderSheet(overviewHtml());
    }
    function openDetail(id) {
      selectedId = id;
      activePanel = "detail";
      renderBoxes();
      document.getElementById("overview-button").classList.remove("is-overview-open");
      renderSheet(detailHtml(component(id)));
    }
    function closeSheet() {
      activePanel = null;
      const sheet = document.querySelector(".msm-sheet");
      if (sheet) sheet.remove();
      document.getElementById("overview-button").classList.remove("is-overview-open");
    }
    function bindHeatmapRows(sheet) {
      sheet.querySelectorAll(".ims-heat-row").forEach(row => {
        row.addEventListener("click", () => {
          selectedCapId = row.dataset.cap;
          if (activePanel === "overview") updateSheet(overviewHtml());
        });
      });
    }
    function updateSheet(body) {
      const sheet = document.querySelector(".msm-sheet");
      if (!sheet) {
        renderSheet(body);
        return;
      }
      const scroll = sheet.scrollTop;
      const bodyEl = sheet.querySelector(".msm-sheet-body");
      if (bodyEl) bodyEl.innerHTML = body;
      bindHeatmapRows(sheet);
      sheet.scrollTop = scroll;
    }
    function renderSheet(body) {
      closePortal();
      const existing = document.querySelector(".msm-sheet");
      if (existing) existing.remove();
      const sheet = document.createElement("div");
      sheet.className = "msm-sheet";
      sheet.setAttribute("role", "dialog");
      sheet.setAttribute("aria-modal", "true");
      sheet.innerHTML = `<button class="msm-portal-close" aria-label="Close">__ICON_X__</button><div class="msm-sheet-body">${body}</div>`;
      sheet.querySelector(".msm-portal-close").addEventListener("click", closeSheet);
      document.getElementById("bandmap").appendChild(sheet);
      bindHeatmapRows(sheet);
    }
    function openPortal(id) {
      const comp = component(id);
      if (!comp) return;
      closePortal();
      const portal = document.createElement("div");
      portal.className = "msm-portal";
      portal.innerHTML = portalHtml(comp);
      portal.querySelector(".msm-portal-close").addEventListener("click", closePortal);
      document.getElementById("bandmap").appendChild(portal);
    }
    function closePortal() {
      const portal = document.querySelector(".msm-portal");
      if (portal) portal.remove();
    }

    function narrativeHtml() {
      // Optional per-client narrative, injected from a narrative.html file at
      // render time (see render() in the Python). If none is supplied, the info
      // sheet falls back to the generic auto-generated read (overviewIntro).
      const tpl = document.getElementById("narrative");
      return tpl ? tpl.innerHTML.trim() : "";
    }
    function overviewIntro() {
      const narrative = narrativeHtml();
      if (narrative) return narrative;
      return `<h2>Current read: ${heroRead()}</h2><p style="font-style:italic;color:#475569;">${modelCaveat()}</p>`;
    }

    function overviewHtml() {
      const desired = freeTextList(contextEntries("desired_outcomes")) || "No desired outcome captured yet.";
      const constraint = freeTextList(contextEntries("biggest_constraints")) || "No constraint captured yet.";
      const sources = isReviewMode()
        ? ((model.source_log || []).map(source => `${roleLabel(source.role)} · ${source.completed_at || "unknown date"}`).join("\\n") || "No sources processed yet.")
        : `${(model.source_log || []).length || 0} source${(model.source_log || []).length === 1 ? "" : "s"} processed. Switch to review mode to inspect respondent-level provenance.`;
      return `
        <p class="msm-kicker">${updatedLine()}</p>
        ${overviewIntro()}
        <div class="msm-detail-section">
          <h3>Company context</h3>
          <div class="ims-card-grid">
            <div class="ims-card"><small>Stage</small><strong>${stageLabels[model.company?.stage] || titleCaseSlug(model.company?.stage)}</strong></div>
            <div class="ims-card"><small>Buying motion</small><strong>${motionLabels[model.company?.buyingMotion] || titleCaseSlug(model.company?.buyingMotion)}</strong></div>
            <div class="ims-card"><small>Marketing team</small><strong>${teamLabels[model.company?.marketingTeamShape] || titleCaseSlug(model.company?.marketingTeamShape)}</strong></div>
            <div class="ims-card"><small>Respondent coverage</small><strong>${respondentSummary()}</strong></div>
          </div>
        </div>
        <div class="msm-detail-section">
          <h3>Captured priorities</h3>
          <div class="ims-card-grid">
            <div class="ims-card"><small>Desired outcomes</small><strong>${desired}</strong></div>
            <div class="ims-card"><small>Biggest constraint</small><strong>${constraint}</strong></div>
            <div class="ims-card"><small>Sources processed</small><strong>${sources}</strong></div>
          </div>
        </div>
        <div class="msm-detail-section">
          <h3>Component read</h3>
          <div class="ims-card-grid">
            ${allComponents().map(comp => `<div class="ims-card"><small>${conditionLabel(conditionOf(comp))} · ${titleCaseSlug(comp.confidence || "low")}</small><strong>${comp.name}</strong><p>${componentInsight(comp)}</p></div>`).join("")}
          </div>
        </div>
        ${alignmentSectionHtml()}
      `;
    }

    function alignmentSectionHtml() {
      const people = respondents();
      if (!people.length) return "";
      const rows = allCapabilities();
      if (!selectedCapId) selectedCapId = rows[0]?.key || null;
      const selected = findCapability(selectedCapId);
      const aligned = rows.filter(row => rangeLabel(row.cap).startsWith("Aligned")).length;
      return `
        <div class="msm-detail-section">
          <h3>Respondent spread</h3>
          <p>${people.length} respondent${people.length === 1 ? "" : "s"}. ${aligned} of ${rows.length} capabilities are fully aligned. The ladder shows everyone on the rungs; the index is the scan. Range is the span of answers, not an average.</p>
          ${people.length ? `<div class="ims-ladder-off" style="margin:8px 0 12px">${people.map((resp, index) => `${personDot(resp, index)}<span>${escapeAttr(resp.name || roleLabel(resp.role))}</span>`).join("")}</div>` : ""}
          ${ladderHtml(selected, false)}
        </div>
        <div class="msm-detail-section">
          <h3>Alignment index</h3>
          <p>Click a row to put that question on the ladder. Cell colour is the rung (red → green). Initials are people.</p>
          ${heatmapHtml()}
        </div>`;
    }

    function detailHtml(comp) {
      if (!comp) return "";
      const caps = capabilities(comp);
      const focus = caps.filter(cap => ["ad_hoc", "early", "unknown"].includes(conditionOf(cap)) || !cap.condition);
      const rest = caps.filter(cap => !focus.includes(cap));
      const list = [...focus, ...rest];
      const spread = componentRange(comp);
      return `
        <p class="msm-kicker">${spread.label} · ${titleCaseSlug(comp.confidence || "low")} confidence</p>
        <h2>${comp.name}</h2>
        <p class="msm-question">${comp.role || ""}</p>
        <p>${componentInsight(comp)}</p>
        <div class="msm-detail-section">
          <h3>Mapped capabilities</h3>
          <ul class="ims-capability-list">
            ${list.map(cap => {
              const row = { key: `${comp.component_id}:${cap.question_id}`, componentId: comp.component_id, component: comp.name, cap };
              const range = rangeLabel(cap);
              const pillCondition = range.startsWith("Aligned") ? conditionOf(cap) : "spread";
              return `
              <li class="ims-capability">
                <div class="ims-capability-top">
                  <strong>${cap.question}</strong>
                  <span class="ims-condition" style="position:static;" data-condition="${pillCondition}">${range}</span>
                </div>
                ${ladderHtml(row, true)}
              </li>`;
            }).join("")}
          </ul>
        </div>
        <div class="msm-detail-section">
          <h3>Model state</h3>
          <div class="ims-card-grid">
            <div class="ims-card"><small>Source type</small><strong>${evidenceBasisLabel(comp.evidence_basis)}</strong></div>
            <div class="ims-card"><small>Coverage</small><strong>${caps.length} mapped capabilities</strong><p>${focus.length} ad hoc, early or unknown</p></div>
            <div class="ims-card"><small>Subcomponents</small><strong>${(comp.subcomponents || []).map(titleCaseSlug).join(", ")}</strong></div>
          </div>
        </div>
      `;
    }

    function portalHtml(comp) {
      const caps = capabilities(comp);
      const bySub = {};
      (comp.subcomponents || []).forEach(sub => bySub[sub] = []);
      caps.forEach(cap => {
        const key = cap.primary_subcomponent || "other";
        if (!bySub[key]) bySub[key] = [];
        bySub[key].push(cap);
      });
      return `
        <button class="msm-portal-close" aria-label="Close">__ICON_X__</button>
        <h2 class="msm-portal-title">${comp.name}</h2>
        <p class="msm-portal-desc">${componentInsight(comp)}</p>
        <div class="msm-portal-grid">
          ${Object.entries(bySub).map(([sub, subCaps]) => `
            <div class="msm-portal-card">
              <h3>${titleCaseSlug(sub)}</h3>
              <div class="ims-capability-list">
                ${subCaps.length ? subCaps.map(cap => `<div class="ims-card"><small>${conditionLabel(conditionOf(cap))}</small><strong>${cap.question}</strong></div>`).join("") : `<div class="ims-card"><small>No mapped capability</small><strong>Awaiting evidence</strong></div>`}
              </div>
            </div>
          `).join("")}
        </div>
      `;
    }

    setupChrome();
    renderBoxes();
    openOverview();
    window.addEventListener("resize", layoutLoop);
    window.requestAnimationFrame(layoutLoop);
  </script>
</body>
</html>
"""


ICONS = {
    "INFO": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11.2v4.8"/><path d="M12 7.8h.01"/></svg>',
    "EXPAND": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-8 8"/><path d="M3 21l8-8"/></svg>',
    "X": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
    "ARROW": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12h13m-5-5 5 5-5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


def safe_json_for_script(data: dict) -> str:
    return (
        json.dumps(data, ensure_ascii=False, indent=2)
        .replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def render(model_path: Path, output_path: Path, narrative_path: Path | None = None) -> Path:
    model = json.loads(model_path.read_text(encoding="utf-8"))
    title = model.get("company", {}).get("name") or "client"
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    # Optional per-client narrative injected into the info sheet. Defaults to a
    # narrative.html sitting beside the model; absent that, the info sheet uses
    # the generic auto-generated read.
    if narrative_path is None:
        candidate = model_path.with_name("narrative.html")
        narrative_path = candidate if candidate.exists() else None
    narrative_html = narrative_path.read_text(encoding="utf-8") if narrative_path and narrative_path.exists() else ""
    html = (
        HTML_TEMPLATE
        .replace("__MODEL_JSON__", safe_json_for_script(model))
        .replace("__NARRATIVE__", narrative_html)
        .replace("__TITLE__", str(title))
        .replace("__FONT_BASE__", FONT_BASE)
        .replace("__GENERATED_AT__", generated_at)
        .replace("__ICON_INFO__", ICONS["INFO"])
        .replace("__ICON_EXPAND__", ICONS["EXPAND"])
        .replace("__ICON_X__", ICONS["X"])
        .replace("__ICON_ARROW__", ICONS["ARROW"])
    )
    output_path.write_text(html, encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render local IMSM client-map HTML.")
    parser.add_argument(
        "model",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "client-model.json",
        help="Path to client-model.json. Defaults to ../client-model.json.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output HTML path. Defaults to client-map.html beside the model.",
    )
    parser.add_argument(
        "--narrative",
        type=Path,
        default=None,
        help="Optional narrative.html to inject into the info sheet. Defaults to narrative.html beside the model if present; otherwise a generic read is used.",
    )
    args = parser.parse_args()
    model_path = args.model.expanduser().resolve()
    output_path = args.output.expanduser().resolve() if args.output else model_path.with_name("client-map.html")
    narrative_path = args.narrative.expanduser().resolve() if args.narrative else None
    render(model_path, output_path, narrative_path)
    print(f"Rendered: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

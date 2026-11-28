#!/usr/bin/env node
// Layout checks for an app screen, at the sizes and engines that matter.
//
// Usage:
//   node layout-check.mjs URL_OR_FILE --out DIR
//        [--sizes phone,phone-land,tablet,desktop | WxH,...]
//        [--engines chromium,webkit] [--theme light,dark]
//        [--state "name=js to run before the shot"]...   (repeatable)
//        [--wait MS]
//
// For every engine x size x theme x state it saves DIR/<engine>-<size>-<theme>-<state>.png
// and runs the checks below. DIR/report.json lists every issue; exit code 1 when any
// check fails. Each check is a bug that reached the owner before (see SKILL.md, step 6).
// Needs Playwright (require('playwright')); browsers from the default install.
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium, webkit } = require('playwright');

const PRESETS = {
  'phone': [390, 844], 'phone-land': [844, 390], 'phone-small': [375, 667],
  'tablet': [820, 1180], 'tablet-land': [1180, 820], 'desktop': [1440, 900],
};
const args = process.argv.slice(2);
const opt = { sizes: 'phone,phone-land,tablet-land,desktop', engines: 'chromium,webkit', theme: 'light', wait: '800', state: [] };
let target = null;
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a.startsWith('--')) {
    const k = a.slice(2), v = args[++i];
    if (k === 'state') opt.state.push(v); else opt[k] = v;
  } else target = a;
}
if (!target || !opt.out) { console.error('usage: layout-check.mjs URL_OR_FILE --out DIR [...]'); process.exit(2); }
const url = /^(https?|file):/.test(target) ? target : pathToFileURL(path.resolve(target)).href;
const sizes = opt.sizes.split(',').map(s => PRESETS[s] ? [s, ...PRESETS[s]] : [s, ...s.split('x').map(Number)]);
const states = [['default', null], ...opt.state.map(s => { const i = s.indexOf('='); return [s.slice(0, i), s.slice(i + 1)]; })];
fs.mkdirSync(opt.out, { recursive: true });

const CHECKS = ([W, touch]) => {
  const out = [];
  const visible = el => {
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false;
    }
    const r = el.getBoundingClientRect();
    return r.width > 1 && r.height > 1 && r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
  };
  const name = el => {
    const t = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    const id = el.id ? '#' + el.id : (el.classList[0] ? '.' + el.classList[0] : '');
    return `${el.tagName.toLowerCase()}${id}${t ? ' "' + t + '"' : ''}`;
  };
  const add = (check, severity, detail, el) => out.push({ check, severity, detail, where: el ? name(el) : 'page' });
  const phone = Math.min(innerWidth, innerHeight) <= 500;

  // 1. Nothing scrolls sideways, nothing sits off the right edge.
  if (document.documentElement.scrollWidth > W + 1) add('horizontal-scroll', 'fail', `page is ${document.documentElement.scrollWidth}px wide in ${W}px`);
  const all = [...document.querySelectorAll('body *')].filter(visible);
  for (const el of all) {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    if (cs.position === 'fixed' || el.closest('[data-bleed]')) continue;
    if (r.right <= W + 2 || r.width >= W * 2) continue;
    let clipped = false;  // inside a scroller or a clipping box (carousels, sliders): not a page bug
    for (let n = el.parentElement; n && n !== document.body; n = n.parentElement) { const o = getComputedStyle(n).overflowX; if (o !== 'visible') { clipped = true; break; } }
    if (!clipped) add('off-screen', 'fail', `right edge at ${Math.round(r.right)}px`, el);
  }
  // 2. Clipped text: text wider or taller than its box with overflow hidden.
  const texts = all.filter(el => [...el.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim()));
  for (const el of texts) {
    const cs = getComputedStyle(el);
    if ((cs.overflow + cs.overflowX).includes('hidden') || cs.textOverflow === 'ellipsis') {
      if (el.scrollWidth > el.clientWidth + 1) add('text-clipped', cs.textOverflow === 'ellipsis' ? 'warn' : 'fail', `needs ${el.scrollWidth}px, has ${el.clientWidth}px`, el);
      if (el.scrollHeight > el.clientHeight + 2 && cs.overflowY !== 'auto' && cs.overflowY !== 'scroll') add('text-clipped', 'fail', `text cut vertically`, el);
    }
  }
  // 3. Controls overlapping each other.
  const ctrls = all.filter(el => el.matches('button,a,input,select,[role=button],[role=tab],[role=menuitem],label'));
  for (let i = 0; i < ctrls.length; i++) for (let j = i + 1; j < ctrls.length; j++) {
    const a = ctrls[i], b = ctrls[j];
    if (a.contains(b) || b.contains(a)) continue;
    const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
    const x = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left), y = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
    if (x > 2 && y > 2) add('overlap', 'fail', `overlaps ${name(b)}`, a);
  }
  // 4. Touch targets on touch sizes: 44px is the bar, under 32 fails.
  if (touch) for (const el of ctrls) {
    const r = el.getBoundingClientRect(), m = Math.min(r.width, r.height);
    if (m < 32) add('touch-target', 'fail', `${Math.round(r.width)}x${Math.round(r.height)}px`, el);
    else if (m < 44) add('touch-target', 'warn', `${Math.round(r.width)}x${Math.round(r.height)}px`, el);
  }
  // 5. Type floor.
  for (const el of texts) {
    const s = parseFloat(getComputedStyle(el).fontSize);
    if (s < (phone ? 11 : 10)) add('type-floor', 'fail', `${s}px text`, el);
  }
  // 6. Contrast of text against the nearest solid background (WCAG; 4.5 body, 3 large).
  const rgb = c => (c.match(/[\d.]+/g) || []).map(Number);
  const lum = ([r, g, b]) => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const bgOf = el => { for (let n = el; n; n = n.parentElement) { const c = rgb(getComputedStyle(n).backgroundColor); if (c.length >= 3 && (c[3] === undefined || c[3] > 0.9)) return c; if (getComputedStyle(n).backgroundImage !== 'none') return null; } return [255, 255, 255]; };
  for (const el of texts) {
    const fg = rgb(getComputedStyle(el).color), bg = bgOf(el);
    if (!bg || (fg[3] !== undefined && fg[3] < 0.9)) continue;
    const a = lum(fg), b = lum(bg), ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
    const s = parseFloat(getComputedStyle(el).fontSize), large = s >= 18.5 || (s >= 14 && +getComputedStyle(el).fontWeight >= 700);
    if (ratio < (large ? 3 : 4.5)) add('contrast', ratio < (large ? 2.2 : 3) ? 'fail' : 'warn', `${ratio.toFixed(2)}:1`, el);
  }
  // 7. Siblings that should line up: same-role controls in one row with different heights or baselines.
  for (const row of all.filter(el => getComputedStyle(el).display.includes('flex') && getComputedStyle(el).flexDirection.startsWith('row'))) {
    const kids = [...row.children].filter(k => visible(k) && k.matches('button,[role=button],[role=tab],select,input'));
    if (kids.length < 2) continue;
    const hs = new Set(kids.map(k => Math.round(k.getBoundingClientRect().height)));
    if (hs.size > 1) add('uneven-row', 'warn', `control heights ${[...hs].join('/')}px in one row`, row);
  }
  // De-duplicate identical findings.
  const seen = new Set();
  return out.filter(i => { const k = i.check + i.where + i.detail; if (seen.has(k)) return false; seen.add(k); return true; });
};

const report = { url, runs: [], failures: 0, warnings: 0 };
for (const engName of opt.engines.split(',')) {
  const eng = { chromium, webkit }[engName];
  let browser;
  try { browser = await eng.launch(); } catch (e) { report.runs.push({ engine: engName, error: String(e).split('\n')[0] }); continue; }
  for (const [sname, w, h] of sizes) for (const theme of opt.theme.split(',')) for (const [state, js] of states) {
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, colorScheme: theme === 'dark' ? 'dark' : 'light', hasTouch: Math.max(w, h) <= 1366 });
    const page = await ctx.newPage();
    const run = { engine: engName, size: sname, width: w, height: h, theme, state };
    try {
      await page.goto(url, { waitUntil: 'load', timeout: 60000 });
      await page.waitForTimeout(+opt.wait);
      if (js) { await page.evaluate(js); await page.waitForTimeout(400); }
      run.issues = await page.evaluate(CHECKS, [w, Math.max(w, h) <= 1366]);
      run.shot = `${engName}-${sname}-${theme}-${state}.png`;
      await page.screenshot({ path: path.join(opt.out, run.shot), animations: 'disabled' });
    } catch (e) { run.error = String(e).split('\n')[0]; }
    report.runs.push(run);
    for (const i of run.issues || []) i.severity === 'fail' ? report.failures++ : report.warnings++;
    await ctx.close();
  }
  await browser.close();
}
fs.writeFileSync(path.join(opt.out, 'report.json'), JSON.stringify(report, null, 2));
for (const r of report.runs) {
  const f = (r.issues || []).filter(i => i.severity === 'fail');
  console.log(`${r.engine} ${r.size} ${r.theme || ''} ${r.state || ''}: ${r.error ? 'ERROR ' + r.error : f.length + ' fail, ' + ((r.issues || []).length - f.length) + ' warn'}`);
  for (const i of f.slice(0, 8)) console.log(`  ${i.check}: ${i.where} (${i.detail})`);
}
console.log(`total: ${report.failures} fail, ${report.warnings} warn -> ${path.join(opt.out, 'report.json')}`);
process.exit(report.failures ? 1 : 0);

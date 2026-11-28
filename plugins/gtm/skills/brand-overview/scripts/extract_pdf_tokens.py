#!/usr/bin/env python3
"""
Extract brand tokens from a PDF brand guidelines document.

Usage:
    python extract_pdf_tokens.py <pdf_path> [--output tokens.json]

Extracts text from every page, then identifies:
- Hex colours (#RRGGBB)
- RGB values (R/G/B notation)
- CMYK values
- Pantone references
- Font family names (common patterns)
- Section headings (for structure)
- Key phrases (mission, vision, values, etc.)

Outputs structured JSON with raw extractions for further processing.
"""

import json
import re
import sys
import os

def ensure_pymupdf():
    try:
        import fitz
        return fitz
    except ImportError:
        os.system("pip install pymupdf --break-system-packages -q 2>/dev/null")
        import fitz
        return fitz

def extract_hex_colours(text):
    """Extract hex colour codes with surrounding context."""
    colours = []
    # Match #RRGGBB or #RGB
    for m in re.finditer(r'(?i)(?:([A-Za-z\s]+?)[\s:]*)?#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})\b', text):
        name_context = m.group(1).strip() if m.group(1) else ""
        hex_val = f"#{m.group(2).upper()}"
        if len(hex_val) == 4:  # Expand #RGB to #RRGGBB
            hex_val = f"#{hex_val[1]*2}{hex_val[2]*2}{hex_val[3]*2}"
        colours.append({"hex": hex_val, "context": name_context[:80]})
    return colours

def extract_rgb_values(text):
    """Extract RGB values in various formats."""
    colours = []
    # R54 G52 B240 format
    for m in re.finditer(r'R(\d{1,3})\s*G(\d{1,3})\s*B(\d{1,3})', text):
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        hex_val = f"#{r:02X}{g:02X}{b:02X}"
        colours.append({"hex": hex_val, "rgb": f"rgb({r}, {g}, {b})"})
    # rgb(R, G, B) format
    for m in re.finditer(r'rgb\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)', text, re.I):
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        hex_val = f"#{r:02X}{g:02X}{b:02X}"
        colours.append({"hex": hex_val, "rgb": f"rgb({r}, {g}, {b})"})
    return colours

def extract_cmyk_values(text):
    """Extract CMYK values."""
    cmyk_list = []
    for m in re.finditer(r'C(\d{1,3})\s*M(\d{1,3})\s*Y(\d{1,3})\s*K(\d{1,3})', text):
        c, m_val, y, k = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        cmyk_list.append({"cmyk": f"C{c} M{m_val} Y{y} K{k}"})
    return cmyk_list

def extract_pantone_refs(text):
    """Extract Pantone references."""
    pantones = []
    for m in re.finditer(r'Pantone[:\s]*([A-Za-z0-9\s]+?)(?:\n|$|Pantone)', text, re.I):
        ref = m.group(1).strip()
        if ref and len(ref) < 50:
            pantones.append(ref)
    return list(set(pantones))

def extract_font_names(text):
    """Extract font family names from common patterns."""
    fonts = set()
    # Direct font name mentions
    patterns = [
        r'(?:typeface|font|font family|type face)[:\s]+([A-Z][a-zA-Z\s]+?)(?:\n|,|\.|;)',
        r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)\s+(?:Regular|Bold|Light|Medium|SemiBold|ExtraBold|Thin|Black|Heavy|Italic)',
        r'(?:primary|secondary|display|heading|body|mono)\s+(?:typeface|font)[:\s]+([A-Za-z\s]+?)(?:\n|,|\.|;)',
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            name = m.group(1).strip()
            # Filter out common false positives
            if name and len(name) < 40 and name.lower() not in ('the', 'our', 'this', 'for', 'and', 'with'):
                fonts.add(name)
    return list(fonts)

def extract_sections(text):
    """Identify section headings and their content."""
    sections = []
    # Look for common brand guideline section names
    section_keywords = [
        'logo', 'colour', 'color', 'typography', 'typeface', 'font',
        'spacing', 'layout', 'grid', 'icon', 'photography', 'imagery',
        'illustration', 'component', 'button', 'motion', 'animation',
        'tone of voice', 'voice', 'personality', 'values', 'mission',
        'vision', 'purpose', 'story', 'narrative', 'brand promise',
        'audience', 'application', 'stationery', 'business card',
        'social media', 'email', 'presentation', 'gradient',
        'clearspace', 'clear space', 'minimum size',
    ]
    lines = text.split('\n')
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        for kw in section_keywords:
            if kw.lower() in stripped.lower() and len(stripped) < 80:
                # Grab surrounding context (next 10 lines)
                context_lines = lines[i:i+15]
                context = '\n'.join(l.strip() for l in context_lines if l.strip())
                sections.append({
                    "heading": stripped,
                    "keyword": kw,
                    "page_approx": i,
                    "context": context[:500]
                })
                break
    return sections

def extract_key_phrases(text):
    """Extract mission, vision, values, and other key brand phrases."""
    phrases = {}
    patterns = {
        'mission': r'(?:mission|mission statement)[:\s]*([^\n]{10,200})',
        'vision': r'(?:vision|vision statement)[:\s]*([^\n]{10,200})',
        'purpose': r'(?:purpose|brand purpose)[:\s]*([^\n]{10,200})',
        'tagline': r'(?:tagline|tag line|strapline|slogan)[:\s]*([^\n]{5,100})',
        'brand_promise': r'(?:brand promise|promise)[:\s]*([^\n]{10,200})',
    }
    for key, pat in patterns.items():
        m = re.search(pat, text, re.I)
        if m:
            phrases[key] = m.group(1).strip()

    # Extract values/characteristics lists
    values_section = re.search(
        r'(?:values|brand values|characteristics|brand characteristics)[:\s]*\n((?:[^\n]+\n){1,15})',
        text, re.I
    )
    if values_section:
        raw = values_section.group(1)
        items = [l.strip() for l in raw.split('\n') if l.strip() and len(l.strip()) < 50]
        phrases['values'] = items[:10]

    return phrases

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_tokens.py <pdf_path> [--output tokens.json]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = "tokens.json"
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    fitz = ensure_pymupdf()
    doc = fitz.open(pdf_path)

    # Extract all text
    full_text = ""
    page_texts = []
    for page in doc:
        text = page.get_text()
        page_texts.append(text)
        full_text += text + "\n\n"

    # Run extractors
    result = {
        "source": {
            "path": pdf_path,
            "pages": doc.page_count,
            "type": "pdf"
        },
        "colours": {
            "hex": extract_hex_colours(full_text),
            "rgb": extract_rgb_values(full_text),
            "cmyk": extract_cmyk_values(full_text),
            "pantone": extract_pantone_refs(full_text)
        },
        "fonts": extract_font_names(full_text),
        "sections": extract_sections(full_text),
        "key_phrases": extract_key_phrases(full_text),
        "raw_text_preview": full_text[:3000]
    }

    # Deduplicate hex colours
    seen_hex = set()
    unique_colours = []
    for c in result["colours"]["hex"] + [{"hex": c["hex"], "context": c.get("rgb", "")} for c in result["colours"]["rgb"]]:
        if c["hex"] not in seen_hex:
            seen_hex.add(c["hex"])
            unique_colours.append(c)
    result["colours"]["unique_hex"] = unique_colours

    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Extracted tokens from {doc.page_count} pages → {output_path}")
    print(f"  Unique colours: {len(unique_colours)}")
    print(f"  Fonts detected: {result['fonts']}")
    print(f"  Sections found: {len(result['sections'])}")
    print(f"  Key phrases: {list(result['key_phrases'].keys())}")

if __name__ == "__main__":
    main()

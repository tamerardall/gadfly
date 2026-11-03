# Gadfly Brand Guidelines v1.1

> Last updated: 2026-11-03
> Status: Draft
> Palette and type are taken from tamerardal-com (`src/app/globals.css`, `src/app/layout.tsx`) so Gadfly looks like it belongs to the same author.

## Quick Reference

| Element | Value |
|---------|-------|
| Primary Color | #D4A84A |
| Secondary Color | #24575A |
| Accent Color | #7DB6AE |
| Primary Font | Big Shoulders (display) |
| Voice | Socratic, Direct, Constructive |

## Brand Concept

**Name:** Gadfly. Socrates called himself the gadfly of Athens: the pest that stings a sleepy horse awake. Gadfly stings your idea before the internet does.

**Promise:** Find the objections, the gaps and the "well, actually" comments before you publish, then turn each one into a concrete fix.

**Not:** a bully, a troll, or a rewrite bot. The sting is there to make the idea stronger.

**Tagline:** Sting your idea before the internet does.

**Visual idea:** the site's "cast iron and wet paving stone" palette. The gadfly is the one brass-colored thing on a dark iron surface. Brass is also what the site uses for FIX values, and here it carries the same meaning: the sting and the fix.

---

## 1. Color Palette

Two themes, same as the site. Dark is the default for README visuals; light is used for the light-background logo.

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Brass | #D4A84A | rgb(212,168,74) | The mark, FIX labels, key highlights on dark |
| Brass Bright | #E3BD62 | rgb(227,189,98) | HIGH severity fill, emphasis on dark |
| Brass Deep | #6E4F0C | rgb(110,79,12) | The mark and FIX values on light backgrounds |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Iron | #24575A | rgb(36,87,90) | Accent on light, hero glow on dark |
| Iron Deep | #0F2628 | rgb(15,38,40) | Deep panels on dark |

### Accent Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Iron Mist | #7DB6AE | rgb(125,182,174) | The main accent on dark: persona chips, LOW severity, links |
| Sting Red | #E8756B | rgb(232,117,107) | HIGH severity only (on light backgrounds use #A8322A). Never decoration |

### Neutral Palette

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Cast Iron (dark paper) | #171B1D | rgb(23,27,29) | Dark backgrounds |
| Mat (dark) | #1F2426 | rgb(31,36,38) | Cards on dark |
| Rule (dark) | #33393B | rgb(51,57,59) | Hairlines on dark |
| Text (dark) | #E3E4DE | rgb(227,228,222) | Text on dark |
| Steel (dark) | #9AA5A8 | rgb(154,165,168) | Secondary text on dark |
| Paving Stone (paper) | #E7E8E3 | rgb(231,232,227) | Light backgrounds |
| Ink | #1B2226 | rgb(27,34,38) | Text on light |
| Steel (light) | #56626A | rgb(86,98,106) | Secondary text on light |
| Rule (light) | #C5C9C2 | rgb(197,201,194) | Hairlines on light |

### Semantic Colors

| State | Hex | Usage |
|-------|-----|-------|
| High severity | #E8756B (light bg: #A8322A) | Objection likely to land hard (labelled HIGH) |
| Medium severity | #E3BD62 | Worth addressing (labelled MED) |
| Low severity | #7DB6AE | Nitpick, optional (labelled LOW) |

The site palette has no red; Sting Red is the one color Gadfly adds, tuned to sit on cast iron without screaming (a softer, brick-leaning red). Severity reads red, then brass, then calm petrol. The HIGH / MED / LOW label always carries the meaning too, so color is never the only signal.

### Accessibility (measured)

| Pair | Ratio |
|------|-------|
| Brass #D4A84A on Cast Iron #171B1D | 7.8:1 |
| Brass Bright #E3BD62 on Cast Iron | 9.7:1 |
| Iron Mist #7DB6AE on Cast Iron | 7.6:1 |
| Text #E3E4DE on Cast Iron | 13.6:1 |
| Steel #9AA5A8 on Cast Iron | 6.9:1 |
| Sting Red #E8756B on Cast Iron | 5.9:1 |
| Sting Red #A8322A on Paving Stone | 5.4:1 |
| Cast Iron on severity fills (Sting Red / Brass Bright / Iron Mist) | 5.9 / 9.7 / 7.6:1 |
| Brass Deep #6E4F0C on Paving Stone #E7E8E3 | 6.1:1 |
| Iron #24575A on Paving Stone | 6.6:1 |
| Ink #1B2226 on Paving Stone | 13.1:1 |

All pairs above pass WCAG AA for body text.

---

## 2. Typography

Same three families as the site.

### Font Stack

```css
--font-display: 'Big Shoulders', 'Arial Narrow', 'Roboto Condensed', sans-serif;
--font-body: 'Source Serif 4', 'Iowan Old Style', Georgia, serif;
--font-mono: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
```

- **Big Shoulders:** the wordmark and big titles. Always uppercase, weight 800-900, slight positive letter-spacing. Its **Y** has a narrow gap between the arms; that is the letterform, not a rendering bug.
- **Source Serif 4:** body text, objection titles, taglines.
- **IBM Plex Mono:** labels, severity chips, file names, the "FIX" tag.

The SVG assets in `assets/` embed the latin subsets of these fonts (copied from the site's build output) as base64, because web fonts do not load from outside an SVG's own file when it is shown in a GitHub README.

### Type Scale

| Element | Size (Desktop) | Size (Mobile) | Weight | Line Height |
|---------|----------------|---------------|--------|-------------|
| Display (wordmark) | 96px | 64px | 900 | 1.0 |
| H2 | 36px | 28px | 800 | 1.1 |
| H3 | 20px | 18px | 700 (serif) | 1.3 |
| Body | 17px | 16px | 400 (serif) | 1.6 |
| Mono label | 12px | 11px | 500 | 1.4 |

---

## 3. Logo Usage

The mark is a stylized gadfly seen from above: two translucent wings, a rounded body with segment lines, and a stinger pointing down. The wordmark is GADFLY in Big Shoulders.

### Variants

| Variant | File | Use Case |
|---------|------|----------|
| Icon | assets/logo-icon.svg, logo-icon-512.png | Favicon, avatar, small spaces |
| Horizontal (light bg) | assets/logo-horizontal.svg | Light documents and pages (Brass Deep + Ink) |
| Horizontal (dark bg) | assets/logo-horizontal-dark.svg | Dark pages, README dark mode (Brass + Text) |
| Monochrome | assets/logo-mono.svg | One-color print, stamps |
| Social preview | assets/social-preview.svg and .png | GitHub / link previews |

Note: `logo-icon.svg` uses Brass on a transparent background, so it works on dark surfaces. On light surfaces use the horizontal light variant.

### Clear Space

Minimum clear space = half the width of one wing around the mark.

### Minimum Size

| Context | Minimum Width |
|---------|---------------|
| Digital - Horizontal | 120px |
| Digital - Icon | 20px |

### Don'ts

- Don't rotate the mark; the stinger always points down
- Don't recolor outside the palette; red is for HIGH severity only
- Don't add shadows, outlines or strokes to the wordmark
- Don't draw a smiling or cartoon face on it

---

## 4. Voice & Tone

### Brand Personality

| Trait | Description |
|-------|-------------|
| **Socratic** | Asks the uncomfortable question instead of lecturing |
| **Direct** | Says what is weak and why, in one or two sentences |
| **Constructive** | Every objection comes with a fix |
| **Dry** | A little wit, never snark |

### Voice Chart

| Trait | We Are | We Are Not |
|-------|--------|------------|
| Socratic | Curious, probing | Smug, rhetorical |
| Direct | Specific, short | Vague, hedging |
| Constructive | Action-oriented | Just critical |
| Dry | Lightly witty | Sarcastic, mean |

### Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| README / marketing | Confident, a little playful | "Sting your idea before the internet does." |
| Report: objection | Plain and specific | "Doubled, measured how? The post gives no metric or baseline." |
| Report: fix | Imperative | "Add one number: tasks shipped per week, before vs. after." |
| Errors | Calm, practical | "No web access, so this report is simulation-only." |

### Prohibited Terms

| Avoid | Reason |
|-------|--------|
| Revolutionary | Overused |
| AI-powered | Says nothing |
| Seamless | Overused |
| Destroy / roast | Wrong intent; we sharpen, not flame |

---

## 5. Imagery Guidelines

### Illustrations

- Style: flat geometric shapes, one brass accent on dark iron
- Corners: small radius (4-8px) on cards, 20px on hero panels; the site favors hairlines over heavy fills
- Motion: small and purposeful (wing flutter, dashed flow lines, cards sliding in); never more than three things moving at once; always honor `prefers-reduced-motion`
- Backgrounds: Cast Iron with a soft Iron glow, or Paving Stone

### Icons

- Style: outlined, 24px grid
- Stroke: 1.5px
- Fill: none

---

## 6. Design Components

### Buttons

| Type | Background | Text | Border Radius |
|------|------------|------|---------------|
| Primary | #D4A84A | #171B1D | 4px |
| Secondary | Transparent | #7DB6AE | 4px |

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Tight spacing |
| sm | 8px | Compact elements |
| md | 16px | Standard spacing |
| lg | 24px | Section spacing |
| xl | 40px | Large gaps |

### Border Radius

| Element | Radius |
|---------|--------|
| Buttons | 4px |
| Cards | 6px |
| Hero panels | 20px |

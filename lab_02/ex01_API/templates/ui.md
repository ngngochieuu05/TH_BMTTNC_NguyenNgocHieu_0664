# Design System Inspired by Louis Vuitton

## 1. Visual Theme & Atmosphere

This design system embodies sophisticated luxury and timeless elegance, drawing from the heritage and craftsmanship of high-end fashion. The aesthetic is rooted in minimalism with dramatic contrast—rich blacks grounded by pristine whites—creating an atmosphere of exclusivity and refinement. Every element serves the product, allowing heritage patterns, supple leathers, and signature details to command visual attention. The design philosophy prioritizes whitespace, deliberate pacing, and editorial storytelling, evoking the experience of entering a flagship boutique where craftsmanship and curated presentation merge seamlessly.

**Key Characteristics**
- Dramatic contrast between deep blacks and pure whites
- Minimalist layout with generous whitespace
- Typography-driven hierarchy and editorial tone
- Product-centric visual narrative
- Sophisticated, understated elegance
- Focus on heritage and craftsmanship
- Bilingual presentation reflecting global luxury market
- High-quality imagery with theatrical lighting
- Refined restraint in color and ornamentation

## 2. Color Palette & Roles

### Primary
- **Black** (`#000000`): Primary background, typography, structural elements, and dominant visual anchor throughout the experience
- **White** (`#FFFFFF`): Content surfaces, text on dark backgrounds, and breathing room for editorial hierarchy

### Interactive
- **Black with Opacity** (`#000000` at `0.85`): Interactive element states including hover, focus, and active states
- **White with Opacity** (`#FFFFFF` at `0.95`): Secondary interactive surfaces and overlays

### Neutral Scale
- **Off-Black** (`#0A0A0A`): Deep shadows and visual separation
- **Off-White** (`#F5F5F5`): Subtle background differentiation and card surfaces

### Surface & Borders
- **Dark Border** (`#1A1A1A`): Dividers and subtle structural lines on light backgrounds
- **Light Border** (`#E8E8E8`): Dividers and subtle structural lines on dark backgrounds

### Semantic / Status
- **Gold Accent** (`#C9A961`): Premium highlights, luxury accents, and signature metallic details referencing leather hardware
- **Error/Alert** (`#DC2626`): Alerts and critical messaging on dark backgrounds

## 3. Typography Rules

### Font Family
**Primary Font:** Louis Vuitton Web, serif (fallback: `Georgia, 'Times New Roman', serif`)
**Secondary Font:** Louis Vuitton Web, sans-serif (fallback: `'Helvetica Neue', Arial, sans-serif`)

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|-----------------|-------|
| Display | Louis Vuitton Web | 56px | 400 | 64px | 0px | Hero headlines, premium positioning |
| H1 | Louis Vuitton Web | 36px | 400 | 44px | 0.5px | Page titles, section leads |
| H2 | Louis Vuitton Web | 24px | 400 | 32px | 0px | Subsection headings |
| H3 | Louis Vuitton Web | 18px | 400 | 24px | 0px | Category and product headers |
| Body | Louis Vuitton Web | 16px | 400 | 24px | 0px | Primary body text, descriptions |
| Body Small | Louis Vuitton Web | 14px | 400 | 20px | 0px | Secondary text, metadata |
| Button | Louis Vuitton Web | 14px | 400 | 20px | 0.5px | Call-to-action text |
| Caption | Louis Vuitton Web | 12px | 400 | 16px | 0px | Captions, footnotes, legal text |
| Code | Menlo, monospace | 13px | 400 | 20px | 0px | Technical content, references |

### Principles
- All typography uses 400 weight for refined elegance; no heavier weights ensure visual restraint
- Line heights maintain 125% ratio for comfortable reading and sophisticated spacing
- Letter spacing is minimal, with selective use on headlines for emphasis
- Font sizing follows a deliberate scale without intermediate breakpoints
- Bilingual (English/French) rendering maintains consistent visual hierarchy and rhythm
- Color contrast is always black text on white surfaces or white text on black surfaces for legibility

## 4. Component Stylings

### Buttons

**Primary Button**
- Background: `#000000`
- Text Color: `#FFFFFF`
- Padding: `16px 32px`
- Font Size: `14px`
- Font Weight: `400`
- Border: `1px solid #000000`
- Border Radius: `0px`
- Hover State: Background `#0A0A0A`, Border `1px solid #0A0A0A`
- Active State: Background `#1A1A1A`, Border `1px solid #1A1A1A`
- Focus State: Outline `2px solid #C9A961` inset, outline-offset `2px`

**Secondary Button**
- Background: `#FFFFFF`
- Text Color: `#000000`
- Padding: `16px 32px`
- Font Size: `14px`
- Font Weight: `400`
- Border: `1px solid #000000`
- Border Radius: `0px`
- Hover State: Background `#F5F5F5`, Border `1px solid #000000`
- Active State: Background `#E8E8E8`, Border `1px solid #000000`
- Focus State: Outline `2px solid #C9A961` inset, outline-offset `2px`

**Ghost Button**
- Background: `transparent`
- Text Color: `#000000`
- Padding: `16px 32px`
- Font Size: `14px`
- Font Weight: `400`
- Border: `1px solid transparent`
- Border Radius: `0px`
- Hover State: Border `1px solid #000000`, Background `transparent`
- Active State: Border `1px solid #1A1A1A`, Background `transparent`
- Focus State: Outline `2px solid #C9A961`

### Cards & Containers

**Premium Card**
- Background: `#FFFFFF`
- Border: `1px solid #E8E8E8`
- Padding: `32px`
- Border Radius: `0px`
- Box Shadow: `none`
- Overflow: Hidden for contained imagery

**Dark Card / Product Container**
- Background: `#000000`
- Border: `1px solid #1A1A1A`
- Padding: `32px`
- Border Radius: `0px`
- Box Shadow: `none`
- Text Color: `#FFFFFF`

**Editorial Container**
- Background: `#000000`
- Padding: `80px 40px`
- Text Color: `#FFFFFF`
- Alignment: Center or asymmetric editorial layout
- Image Treatment: Full-bleed with theatrical lighting

### Inputs & Forms

**Text Input**
- Background: `#FFFFFF`
- Border: `1px solid #1A1A1A`
- Border Radius: `0px`
- Padding: `12px 16px`
- Font Size: `16px`
- Placeholder Color: `#999999`
- Focus State: Border `2px solid #C9A961`, outline `none`
- Error State: Border `1px solid #DC2626`

**Form Label**
- Font Size: `14px`
- Font Weight: `400`
- Color: `#000000`
- Margin Bottom: `8px`
- Display: Block

**Checkbox / Radio**
- Size: `16px × 16px`
- Border: `1px solid #000000`
- Border Radius: `0px`
- Background (unchecked): `#FFFFFF`
- Background (checked): `#000000`
- Focus State: Outline `2px solid #C9A961`

### Navigation

**Header Navigation**
- Background: `#FFFFFF`
- Height: `64px`
- Border Bottom: `1px solid #E8E8E8`
- Text Color: `#000000`
- Font Size: `14px`
- Link Hover: Text Color `#666666`, underline `1px solid #666666`
- Link Active: Text Color `#000000`, underline `2px solid #000000`

**Footer Navigation**
- Background: `#000000`
- Padding: `80px 40px 40px`
- Text Color: `#FFFFFF`
- Link Hover: Text Color `#C9A961`
- Font Size: `14px`

**Breadcrumb Navigation**
- Font Size: `12px`
- Color: `#666666`
- Separator: ` / ` in `#999999`
- Link Color: `#000000`
- Link Hover: `#C9A961`

### Badges & Status

**Premium Badge**
- Background: `#C9A961`
- Text Color: `#000000`
- Padding: `4px 12px`
- Border Radius: `0px`
- Font Size: `12px`
- Font Weight: `400`

**Alert Badge**
- Background: `#DC2626`
- Text Color: `#FFFFFF`
- Padding: `4px 12px`
- Border Radius: `0px`
- Font Size: `12px`

## 5. Layout Principles

### Spacing System
**Base Unit:** `8px`
**Scale:** `8px`, `16px`, `24px`, `32px`, `40px`, `48px`, `56px`, `64px`, `80px`, `96px`, `120px`

**Usage Context:**
- `8px` – Component-level micro-spacing (input padding, badge spacing)
- `16px` – Standard padding for small containers and internal spacing
- `32px` – Primary padding for cards, sections, and content blocks
- `40px` – Section margins and medium layout separation
- `80px` – Large section spacing and hero padding
- `120px` – Maximum vertical rhythm for full-screen sections

### Grid & Container
- **Max Width:** `1440px` for desktop content
- **Column Strategy:** 12-column flexible grid system
- **Section Patterns:** Hero (full-bleed), content (centered at max-width), editorial (alternating left/right alignment)
- **Container Padding:** `40px` horizontal on desktop, `16px` on mobile
- **Gutter Width:** `24px` between columns

### Whitespace Philosophy
The design system embraces generous whitespace as a mark of luxury and clarity. Negative space is treated as an active design element—allowing imagery, typography, and content to breathe without visual clutter. Sections are purposefully separated with vertical rhythm at `80px` or `120px` intervals, creating editorial pacing and emphasizing content importance through isolation rather than visual ornamentation.

### Border Radius Scale
- `0px` – Primary radius for all components (buttons, cards, inputs, badges); sharp edges convey precision and heritage
- `4px` – Minor rounded corners for edge cases and subtle softening
- `8px` – Maximum rounding for images and contained media

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| None | No shadow | Primary buttons, cards, navigation, default state |
| Hover | `0px 8px 16px rgba(0, 0, 0, 0.12)` | Interactive elements on hover |
| Focus | `0px 0px 0px 2px #C9A961` | Focus indicators for accessibility |
| Overlay | `0px 0px 0px 1000px rgba(0, 0, 0, 0.6)` | Modal backdrops and overlays |
| Floating | `0px 16px 32px rgba(0, 0, 0, 0.15)` | Floating elements, tooltips, popovers |

**Shadow Philosophy**
The design system uses shadows sparingly and subtly. Depth is achieved primarily through contrast and layering of black and white rather than shadow effects. When shadows are introduced, they are soft and diffuse—mimicking refined indoor lighting of luxury retail environments. Shadows support information hierarchy by providing subtle visual separation without overwhelming the minimalist aesthetic.

## 7. Do's and Don'ts

### Do
- Maintain stark black-and-white contrast for maximum legibility and luxury perception
- Use generous vertical spacing (80px–120px) between major sections for editorial pacing
- Employ full-bleed imagery with dramatic lighting to showcase product heritage and craftsmanship
- Center align body text and headings for formal, editorial presentation
- Render buttons with sharp corners (`0px` radius) to convey precision and timelessness
- Incorporate the gold accent (`#C9A961`) sparingly for premium highlights and interactive focus states
- Keep typography to 400 weight exclusively for refined restraint
- Layer content asymmetrically in hero sections to create dynamic visual interest
- Use bilingual text rendering with consistent typographic rhythm across languages
- Provide clear visual feedback on all interactive elements through color and border changes

### Don't
- Introduce colors beyond black, white, and the gold accent—the palette is intentionally limited
- Use rounded corners (border-radius > 0px) on primary buttons, cards, or form inputs
- Apply multiple shadows or complex layering effects; depth comes from contrast
- Overcrowd layouts—prioritize whitespace as a design element
- Use font weights heavier than 400; hierarchy is conveyed through size and color, not weight
- Justify body text; maintain left-aligned or centered layouts for editorial clarity
- Add decorative elements that distract from product imagery and content
- Animate elements rapidly; transitions should be subtle and refined (200ms–400ms)
- Mix font families; Louis Vuitton Web serif is the exclusive typeface
- Create hover states with dramatic color shifts; subtle opacity and border changes are preferred

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|------------|
| Mobile | 320px – 639px | Single column, 16px padding, 40px section spacing, 18px h2 headings |
| Tablet | 640px – 1023px | Two-column grid, 24px padding, 64px section spacing, 20px h2 headings |
| Desktop | 1024px – 1439px | 12-column grid, 40px padding, 80px section spacing, 24px h2 headings |
| Large Desktop | 1440px+ | 12-column grid at max-width `1440px`, 120px section spacing, centered container |

### Touch Targets
- Minimum interactive element size: `48px × 48px` for buttons and links
- Button padding: `16px 32px` maintains sufficient touch target on all screen sizes
- Form inputs: `44px` minimum height for comfortable mobile interaction
- Navigation items: `48px` vertical spacing in vertical menus

### Collapsing Strategy
- **Header Navigation:** Hamburger menu (`48px × 48px` icon) on mobile (< 640px); full horizontal navigation on tablet and desktop
- **Product Grid:** 1 column on mobile, 2 columns on tablet, 3–4 columns on desktop
- **Hero Section:** Full-bleed image with text overlay on mobile; side-by-side layout on desktop
- **Footer:** Single-column stack on mobile; multi-column layout on tablet/desktop
- **Spacing Reduction:** Section padding reduces from `80px` (desktop) to `40px` (tablet) to `24px` (mobile)
- **Typography Scaling:** H1 reduces from `36px` to `28px` on tablet, `24px` on mobile; body text remains `16px` for readability

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Black (`#000000`)
- Secondary CTA: White (`#FFFFFF`)
- Background (Hero/Editorial): Black (`#000000`)
- Background (Content): White (`#FFFFFF`)
- Accent/Highlight: Gold (`#C9A961`)
- Text (on Black): White (`#FFFFFF`)
- Text (on White): Black (`#000000`)
- Error/Alert: Red (`#DC2626`)
- Border: Dark Border (`#1A1A1A`) on light; Light Border (`#E8E8E8`) on dark
- Disabled/Inactive: Gray (`#999999`)

### Iteration Guide
1. **Apply pure black (`#000000`) and white (`#FFFFFF`) as primary colors**—all buttons, cards, and structural elements use these two colors exclusively for maximum contrast and luxury perception.
2. **Set all border-radius values to `0px`**—sharp corners are non-negotiable and reinforce heritage and precision.
3. **Use Louis Vuitton Web serif font exclusively at 400 weight**—no bold, no other typefaces; hierarchy comes from size and contrast only.
4. **Implement generous spacing in multiples of 8px**—priority intervals are `16px`, `32px`, `40px`, `80px`, and `120px` for vertical rhythm and editorial pacing.
5. **Reserve gold (`#C9A961`) for focus states, hover indicators, and premium badges only**—use sparingly to maintain sophistication.
6. **Render full-bleed hero imagery with theatrical lighting and overlay text in white**—product showcase is the emotional anchor.
7. **Minimize shadows; use none on default states and soft shadows (`8px–16px blur, 12% opacity`) only on hover**—depth derives from layering and contrast.
8. **Ensure all interactive elements have clear focus states (`2px solid #C9A961` outline) for accessibility**—focus is as important as hover.
9. **Center-align typography in editorial sections; left-align in content blocks**—maintain editorial hierarchy and formality.
10. **Test bilingual rendering with consistent line-height and spacing across English and French**—global luxury requires language parity.
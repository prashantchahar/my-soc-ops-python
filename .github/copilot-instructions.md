# Project Guidelines

## Mandatory Development Checklist

- [ ] Lint: uv run ruff check .
- [ ] Build/Sync: uv sync
- [ ] Test: uv run pytest

## Architecture And Boundaries

- Entry point and routes: app/main.py (FastAPI + Jinja2 + SessionMiddleware).
- Pure board logic only in app/game_logic.py; session transitions only in app/game_service.py.
- HTMX routes (/start, /toggle/{id}, /reset, /dismiss-modal) must return HTML fragments, not JSON.
- Keep handlers thin and delegate behavior to GameSession.

## Invariants And Verification

- Preserve 5x5 board behavior; center index 12 is free space and starts marked.
- Keep HTMX target/swap behavior aligned with app/templates/components/game_screen.html.
- Update tests: tests/test_game_logic.py for logic changes, tests/test_api.py for route/template changes.
- For manual checks use an external browser: "$BROWSER" http://localhost:8000 (no VS Code Simple Browser).

## Design Guide: 70s-80s Bollywood Masala Theme

### Color Palette (CSS Custom Properties in app/static/css/app.css)
Define colors via `:root` variables for consistency:
- `--primary-magenta: #D946EF` — Main brand color, used on titles, headers, modals
- `--primary-magenta-dark: #9333EA` — Darker shade for gradients/depth
- `--accent-teal: #06B6D4` — Secondary accent, board squares
- `--accent-teal-dark: #0891B2` — Darker teal for contrast
- `--accent-orange: #FF6B35` — Vibrant energy, CTAs, free space
- `--accent-gold: #FCD34D` — Ornamental borders, marked squares, celebrations
- `--accent-saffron: #F97316` — Cultural warmth, gradients
- `--accent-deep-red: #DC2626` — Deep jewel tone, modal backgrounds
- `--highlight-lime: #84CC16` — Power highlights, special elements
- `--text-light: #FFFFFF` — Light text on dark backgrounds
- `--text-dark: #1F2937` — Dark text on light/gradient backgrounds

**Gradient Combos**:
- `.bg-gradient-magenta-teal` — Magenta → Teal (primary board squares)
- `.bg-gradient-gold-orange` — Gold → Orange (winning lines, free space)
- `.bg-gradient-magenta-red` — Magenta → Deep Red (modals)

### Typography
- **Serif Display** (Playfair Display): Titles, headers, dramatic text — invokes golden age elegance
- **Geometric Bold** (Fredoka): CTAs, body text, instructions — modern energy
- Classes: `.serif-display`, `.serif-title`, `.geom-bold` in app.css

**Font Import** (in base.html):
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Fredoka:wght@500;700&display=swap" rel="stylesheet">
```

### Animations & Micro-interactions

**Keyframe Definitions** (in app.css):
- `@keyframes staggered-scale-up` — Board squares cascade entrance (0.8 scale → 1, -2deg rotation)
- `@keyframes sparkle-pulse` — Gold glow pulsing on marked squares (1.5s infinite)
- `@keyframes shine-slide` — Linear shine effect for buttons on hover (2s loop)
- `@keyframes fade-in-up` — Entrance animation for text/cards (0.8s)
- `@keyframes color-shift` — Marked square color oscillation (gold ↔ saffron)
- `@keyframes spinWiggle` — Celebration emoji rotation on win modal
- `@keyframes fadeInBounce` — Modal spring-in effect
- `@keyframes fadeInDown` — Decorative element top entrance

**Animation Classes**:
- `.animate-staggered` — Board squares, board entry
- `.animate-sparkle` — Marked squares
- `.animate-shine` — Button hovers
- `.animate-fade-up` — Text, cards (use with `animation-delay` for cascades)
- `.animate-color-shift` — Oscillating marked states

**Staggered Delay Pattern**:
```html
style="--index: {{ loop.index0 }}; animation-delay: calc(var(--index) * 50ms);"
```
Creates 50ms stagger between each element (e.g., board squares 0→50ms→100ms→150ms...).

### Component Styling

#### Start Screen (`app/templates/components/start_screen.html`)
- Background: Dark gradient `linear-gradient(135deg, #1F2937 0%, #2D1B4E 50%, #1F2937 100%)`
- Title: `.serif-display` in magenta with text-shadow
- Subtitle: `.geom-bold` in teal, italic, letter-spacing
- Card: `.ornate-border-dashed` (gold dashed border), semi-transparent white bg, `.animate-fade-up`
- Button: Magenta→saffron gradient, `.btn-glow` class, emoji labels (🎬 BEGIN THE SHOW 🎬)

#### Game Screen (`app/templates/components/game_screen.html`)
- Background: Dark gradient `linear-gradient(180deg, #2D1B4E 0%, #1F2937 50%, #111827 100%)`
- Header: `.ornate-top-border` (gold top, magenta shadow), magenta→saffron gradient, `.serif-display` title
- Instructions: Italic serif, white text, generous letter-spacing
- Bingo indicator: Gold→saffron gradient, dark text, `.animate-color-shift` or pulse

#### Bingo Board (`app/templates/components/bingo_board.html`)
- Wrapper: `.ornate-border-dashed` (gold dashed frame), corner flourishes (◆ ✦ ◈)
- Unmarked squares: Semi-transparent white bg, gold border, white text, `.animate-staggered`
- Marked squares: Magenta→teal gradient, pink/teal glow shadow, `.animate-sparkle`, `.animate-staggered`
- Winning squares: Gold→saffron gradient, gold glow shadow, `.animate-sparkle` (stronger effect)
- Free space: Orange→saffron gradient, dark text, `font-serif`, slightly larger text
- Class structure ensures smooth color transitions; no jarring changes

#### Win Modal (`app/templates/components/bingo_modal.html`)
- Background: `.bg-black/50` with `backdrop-filter: blur(4px)` for depth
- Modal box: `.ornate-border-dashed` (gold dashed), magenta→deep-red gradient, `.animate-fadeInBounce`
- Emoji: `.animate-spinWiggle` (0.8s rotation enter)
- Title: `.serif-display` in gold with text-shadow
- Text: Serif italic, light text, staggered `.animate-fade-up` with delays (0.2s, 0.4s, 0.6s)
- Button: Gold→saffron gradient, `.btn-glow`, emoji labels (🎭 CONTINUE PLAYING 🎭)

### Ornate Border Utilities
- `.ornate-border-dashed` — Gold dashed (2px), 0.5rem radius
- `.ornate-border-double` — Magenta double (3px), 0.5rem radius
- `.ornate-top-border` — Gold top (4px) + magenta shadow below (creates layered effect)

### Glow & Shadow Effects
- `.btn-glow` — Button hover/active: magenta+orange glow, 1.05 scale; active 0.98 scale
- Card shadows: `0 8px 16px rgba(217, 70, 239, 0.3)` (magenta cards), etc. by color variant
- Sparkle glow: `0 0 15px rgba(249, 115, 22, 0.6)` (for marked/winning squares)

### Component Update Patterns

**When Modifying a Component**:
1. Preserve HTMX attributes (`hx-post`, `hx-target`, `hx-swap`)
2. Update inline `style` attributes for gradients/animations (prefer inline over new CSS classes for one-offs)
3. Add `.animate-*` classes for entrance effects; use `animation-delay: calc(var(--index) * 50ms)` for stagger
4. Update `.ornate-*` borders if frame styling changes
5. Test gradient readability: dark text on bright gradients may need white text or contrast bump

**When Adding New Content**:
- Use `.serif-title` for headers, `.geom-bold` for CTAs
- Apply `.animate-fade-up` to cards/sections entering from bottom
- Use CSS variables (`var(--primary-magenta)`, etc.) instead of hardcoding hex
- Test color contrast with WebAIM Contrast Checker or browser DevTools

### Content & Questions
Hybrid approach: ~60% generic social icebreakers, ~40% Bollywood-flavored:
- "watched a classic Bollywood film from the 70s or 80s"
- "can name a Rajesh Khanna or Amitabh Bachchan movie"
- "knows the words to a Bollywood song"
- "has experienced Bollywood cinema in theaters"

Keep questions inclusive while celebrating Bollywood cinema heritage. Update in `app/data.py`.

### File Reference
- **CSS**: `app/static/css/app.css` (color vars, animations, utilities, ornate borders, glow effects)
- **Base Template**: `app/templates/base.html` (font imports, meta theme-color: #D946EF)
- **Components**: Under `app/templates/components/` (start_screen.html, game_screen.html, bingo_board.html, bingo_modal.html)
- **Content**: `app/data.py` (QUESTIONS list)

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

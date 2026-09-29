# Poker Trainer: instructions for Claude Code

## What this project is

A personal training simulator for 6-max No-Limit Texas Hold'em. Pablo plays against
AI bots with different playing styles; the app records every hand, calculates his
stats (VPIP, PFR, 3-bet %, etc.), and points out leaks. Web app first, iOS later.

Ground rule: this is a study tool used away from real tables. Never build features
that give advice during live online play.

## Working agreement (most important)

Pablo is learning software development through this project. Claude may write code,
as long as Pablo understands everything that happens.

- Before changing anything, explain the plan in plain language and wait for approval.
- After each change, explain what the code does and why, section by section.
- Explain every terminal command you run: what it does and what each part means.
- Work in small steps: one focused change at a time, not large rewrites.
- Ask before installing any new dependency, and explain why it's needed.
- When there are several reasonable approaches, briefly list them and recommend one.
- Never push, merge, or delete branches without asking.

## Architecture

- **Server-based engine.** The backend is the single source of truth: poker rules,
  game state, bots, and stats all live on the server.
- **`backend/`**: Python 3.12, FastAPI, served by Uvicorn. Virtual environment in
  `backend/.venv`. The future `backend/engine/` package must stay pure Python with
  no FastAPI imports; the API is a thin layer on top.
- **`web/`**: React + TypeScript, built with Vite. The web app is a thin client: it
  displays the game state and sends the player's actions to the API. No game rules
  in the frontend.
- Database (later, Phase 5): PostgreSQL with SQLAlchemy + Alembic.

## Running the project

Backend (terminal 1):

```
cd ~/pokert/backend
source .venv/bin/activate
uvicorn main:app --reload
```

Runs at http://127.0.0.1:8000, interactive docs at /docs.

Web (terminal 2):

```
cd ~/pokert/web
npm run dev
```

Runs at http://localhost:5173.

## Standards

**Git**

- Never commit directly to `main`. Work on a branch named `feature/<short-name>`
  (or `fix/`, `docs/`, `chore/`) and merge through a pull request.
- Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`.
- Never commit secrets. `.env` files are ignored and must stay that way.
- After `git add`, show `git status` before committing.

**Python (backend)**

- PEP 8 style, type hints on all functions.
- Ruff for formatting and linting; pytest for tests.
- Test-driven development for the hand evaluator: write the failing test first.
- If a new package is installed, update `backend/requirements.txt` with
  `pip freeze > requirements.txt` (venv active).

**TypeScript (web)**

- `npm run lint` must pass with no output before committing.
- Use real types; avoid `any`.
- The Vite template decoration in `web/src/App.tsx` can be removed when the table UI
  is built.

## Environment notes

- Development happens in a Pop!_OS VM in VirtualBox. VS Code pop-up windows (command
  palette, file pickers) often don't render, so prefer terminal commands and settings
  files over instructions that rely on VS Code menus.
- VS Code's Python interpreter is set in `.vscode/settings.json`.

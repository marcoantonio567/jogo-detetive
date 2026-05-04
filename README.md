# Detective Game (Terminal)

A text-based detective game (CLI) with colors and terminal animations. The main menu lets you start the game, view credits, and choose phases/stories.

Note: the game text and prompts are in Portuguese.

## Requirements

- Python 3.9+ (recommended)

## How to Run

1) Go to the project folder:

```bash
cd jogo-detetive
```

2) (Optional) Create and activate a virtual environment (Windows):

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3) Install dependencies:

```bash
pip install -r requirements.txt
```

4) Run the game:

```bash
python start.py
```

## How to Play

- In menus, type the option number and press Enter.
- During stories, follow the on-screen prompts (usually numeric choices like 1/2).
- The “Fases” option lets you start a specific story directly.

## Project Layout (Quick Overview)

- `start.py`: main menu and game flow
- `historia_*.py`: stories/phases
- `template_detetive.py`: example story based on a decision tree
- `cores.py`, `animations.py`, `maquina.py`: colors, animations, and typewriter effect utilities

## Business Rules

- See `business_rules.md` for game rules/decisions.

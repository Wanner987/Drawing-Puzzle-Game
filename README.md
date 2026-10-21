# Drawing-Puzzle-Game
Drawing Puzzle Game (Name will be refined later) is a game where you solve puzzles with drawing.

[Canvas page for ASE420: ](https://nku.instructure.com/courses/91834/pages/individual-project-page-of-tanner-andrews)

## Documentation

See Docs folder for all documentation


## Running the game

The game requires Python 3.12 and [uv](https://docs.astral.sh/uv/getting-started/installation/).
From the repository root, run:

```sh
bash run.sh
```

The script creates or updates the virtual environment in `App/.venv`, installs the dependencies
declared by `App/pyproject.toml`, and starts the game. On Windows, run the script from Git Bash or
WSL. You can also run the commands manually:

```sh
cd App
uv sync --python 3.12 --no-install-project
uv run --python 3.12 --no-sync python src/main.py
```
#!/usr/bin/env bash
set -eu

if ! command -v uv >/dev/null 2>&1; then
    printf '%s\n' "uv is required. Install it from https://docs.astral.sh/uv/getting-started/installation/." >&2
    exit 1
fi

cd "$(dirname "$0")/App"
uv sync --python 3.12 --no-install-project
exec uv run --python 3.12 --no-sync python src/main.py

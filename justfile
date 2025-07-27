setup:
  if [ ! -d .venv ]; then python3 -m venv .venv; fi
  source .venv/bin/activate && ./scripts/setup

dev: setup
  source .venv/bin/activate && ./scripts/develop

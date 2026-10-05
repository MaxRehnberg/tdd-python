.PHONY: sync check format test

sync:
	uv sync

check:
	uv run ruff check
	uv run ruff format --check
	uv run pyright

format:
	uv run ruff check --fix
	uv run ruff format

test:
	uv run pytest

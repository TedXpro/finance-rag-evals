# Working rules

This is a learning project. I write the design decisions and must be able to explain every line.

## Before coding
- Read `README.md` and `docs/decisions/`.
- A new design choice needs a note in `docs/decisions/`. I write it; you can question it.
- Explain the approach first, then wait for my go-ahead.

## Code
- Make the smallest change that works.
- No speculative abstractions, config, helpers or error handling.
- Standard library first. Add a dependency only when it is first used.
- Comment only when the reason is not obvious. Never restate the code.
- Reusable logic lives in `src/`. Notebooks import it.
- Write the test or eval before the feature.

## Notebooks
- Use them to explore data and show results, numbered in reading order.
- Restart and run all before committing, so the outputs match the code.

## Results
- Numbers in `README.md` come from a real eval run. Never estimate or invent them.
- Record real failures in `docs/failures.md`.
- Never commit data, secrets or client material.

## Done
`ruff check .`, `ruff format --check .`, `pytest` and `python evals/run.py` all pass.

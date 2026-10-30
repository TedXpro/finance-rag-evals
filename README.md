# finance-rag-evals

Can a RAG system answer questions about company filings correctly, cite its sources, and report what each answer costs?

**Status:** skeleton. `answer()` refuses every question until retrieval exists.

## Results

| Metric | Result |
|---|---|
| Correct answers (FinanceBench, 150 questions) | not measured |
| Answers citing the right evidence | not measured |
| p95 response time | not measured |
| Cost per 100 questions | not measured |

## Run

```
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev,notebooks]"
pytest
python evals/run.py
```

## Plan

- [ ] Answer one question from one filing, with its source
- [ ] Retrieve across filings with a vector database
- [ ] Score all 150 questions and record failures
- [ ] Fail CI when quality drops
- [ ] Deploy on AWS

## Data

[FinanceBench](https://github.com/patronus-ai/financebench) open sample (150 questions, CC BY-NC 4.0). Download it into `data/`; it is not committed.

## Layout

- `src/`: the code
- `tests/`: unit tests
- `evals/`: measures quality on labelled cases
- `notebooks/`: exploration and results
- `docs/decisions/`: why each design choice was made
- `docs/failures.md`: what broke and how it was fixed

## AI use

Built with AI coding tools under the rules in [AGENTS.md](AGENTS.md).

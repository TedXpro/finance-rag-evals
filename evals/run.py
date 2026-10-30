import json
from pathlib import Path

from finance_rag.answer import answer

CASES = Path(__file__).parent / "cases.jsonl"


def main():
    cases = [json.loads(line) for line in CASES.read_text().splitlines()]
    correct = sum(answer(case["question"]).text == case["expected"] for case in cases)
    print(f"{correct}/{len(cases)} correct")
    if correct < len(cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

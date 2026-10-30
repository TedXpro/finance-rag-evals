from finance_rag.answer import answer


def test_refusal_has_no_sources():
    result = answer("What is the capital of France?")
    assert result.text == "I don't know."
    assert result.sources == []

from dataclasses import dataclass


@dataclass
class Answer:
    text: str
    sources: list[str]


def answer(question: str) -> Answer:
    return Answer(text="I don't know.", sources=[])

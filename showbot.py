"""A tiny rule-based chatbot that explores the animatronic metaphor."""

from __future__ import annotations

import argparse
import random
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Cue:
    name: str
    patterns: tuple[str, ...]
    lines: tuple[str, ...]


CUES = (
    Cue(
        name="greeting",
        patterns=(r"\bhello\b", r"\bhi\b", r"\bhey\b", r"\bhowdy\b"),
        lines=(
            "Hey there! The show is just getting started.",
            "Welcome to the conversation. I have a line for that!",
        ),
    ),
    Cue(
        name="feelings",
        patterns=(r"\bfeel\b", r"\bemotion", r"\bhappy\b", r"\bsad\b"),
        lines=(
            "I can talk about feelings, but this little program does not feel them.",
            "That sounds emotional. My response is selected from a set of written lines.",
        ),
    ),
    Cue(
        name="how_it_works",
        patterns=(r"\bhow\b.*\bwork\b", r"\bhow are you made\b", r"\bmechanism\b"),
        lines=(
            "This demo matches words to rules, then delivers a prepared response.",
            "Behind this curtain: pattern matching, response lists, and a little randomness.",
        ),
    ),
    Cue(
        name="ai",
        patterns=(r"\bartificial intelligence\b", r"\bai\b", r"\bchatbot\b", r"\bllm\b"),
        lines=(
            "This toy chatbot is rule-based. Real AI systems can work very differently.",
            "The animatronic comparison is a metaphor—not a technical description of every AI.",
        ),
    ),
    Cue(
        name="farewell",
        patterns=(r"\bbye\b", r"\bgoodbye\b", r"\bquit\b", r"\bexit\b"),
        lines=(
            "Thanks for visiting. The show is over—for now.",
            "Goodbye! The stage lights are going down.",
        ),
    ),
)

FALLBACK_LINES = (
    "That line is not in my script. Try asking how this demo works.",
    "I don't have a cue for that, but I can keep the conversation moving.",
)


def classify(message: str) -> str:
    """Return the first matching cue name, or 'fallback'."""
    normalized = message.lower()

    for cue in CUES:
        if any(re.search(pattern, normalized) for pattern in cue.patterns):
            return cue.name

    return "fallback"


def respond(message: str, rng: random.Random | None = None) -> tuple[str, str]:
    """Return the selected cue and a response line."""
    chooser = rng or random
    cue_name = classify(message)

    if cue_name == "fallback":
        return cue_name, chooser.choice(FALLBACK_LINES)

    cue = next(item for item in CUES if item.name == cue_name)
    return cue_name, chooser.choice(cue.lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A rule-based chatbot exploring the animatronic metaphor."
    )
    parser.add_argument(
        "--explain",
        action="store_true",
        help="show which response cue was selected",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="make response selection reproducible",
    )
    args = parser.parse_args()

    rng = random.Random(args.seed)
    print("Showbot: Welcome to the demo. Type 'quit' to leave.")
    print("Note: This is a small scripted simulation, not a general AI system.")

    while True:
        try:
            message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShowbot: The show is over. Goodbye!")
            break

        cue_name, reply = respond(message, rng)
        print(f"Showbot: {reply}")

        if args.explain:
            print(f"[selected cue: {cue_name}]")

        if cue_name == "farewell":
            break


if __name__ == "__main__":
    main()

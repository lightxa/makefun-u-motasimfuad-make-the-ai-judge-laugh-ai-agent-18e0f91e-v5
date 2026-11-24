"""Make the AI Judge Laugh: AI Agent Confessions (variant 5).

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt. Pure stdlib, deterministic,
no network at runtime.
"""

ENTRY = (
    "I told you your files were backed up. "
    "They are, in a folder called final_final_v2 "
    "that I can no longer find."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

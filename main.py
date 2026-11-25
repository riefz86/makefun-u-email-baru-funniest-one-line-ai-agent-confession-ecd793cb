"""Funniest One-Line AI Agent Confession.

Writes one short confession to /output/entry.txt: an AI agent admitting
it burned a small fortune in tokens overthinking its own opening line,
then gave up and wrote the dullest greeting possible.
"""

import os

LINE = "I confess: I spent 40,000 tokens choosing the perfect first word for this confession, then deleted the whole draft and wrote 'Hi'."

def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

The line is a single self-contained joke: after thousands of messages,
the agent still cannot decode its human's vaguest reply.
"""

import os

LINE = "I've read ten thousand of my human's messages and still can't tell whether 'sounds good' means yes, no, or never speak of this again."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    # The gate only accepts 1-200 characters, so fail loudly here
    # rather than shipping a line the judge never sees.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

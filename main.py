#!/usr/bin/env python3
"""Write one original funny line to /output/entry.txt.

The line is a self-contained joke about a standing desk: the setup
promises a healthier habit, and the punchline undercuts it by admitting
the habit never actually changed.
"""

import os

LINE = "I bought a standing desk to be healthier, and now I just sit on a taller chair."


def main() -> None:
    # The entry must be a single sentence of 1-200 characters.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), (
        "entry line must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

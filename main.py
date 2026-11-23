#!/usr/bin/env python3
"""Write one original funny line to /output/entry.txt."""

import os

LINE = "I bought a standing desk to be healthier, and now I just sit on a taller chair."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

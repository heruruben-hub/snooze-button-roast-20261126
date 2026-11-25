#!/usr/bin/env python3
"""Snooze Button Roast — a make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
morning to /output/entry.txt. The gate requires UTF-8 text of 1-200
characters, not only white space.
"""

import os

ROAST = (
    "My alarm clock rings at 6 AM on a Saturday like it's gunning for "
    "Employee of the Month at a job that doesn't exist."
)


def main() -> None:
    text = ROAST.strip()
    if not text:
        raise SystemExit("entry must not be empty or only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

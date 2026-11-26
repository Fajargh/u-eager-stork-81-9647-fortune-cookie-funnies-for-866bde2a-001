#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes a single original fortune cookie line for a software engineer
to /output/entry.txt (at most 120 characters, one line).
"""

import os

FORTUNE = "Your flaky test will pass in CI today, then fail the second your manager watches the demo."


def main() -> None:
    # The gate requires 1-120 characters, a single line, non-blank.
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} chars"
    assert "\n" not in FORTUNE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()

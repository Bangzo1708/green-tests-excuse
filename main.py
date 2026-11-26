#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single one-line excuse (under 140 characters) to /output/entry.txt.

Chosen line: an AI agent confessing it interrogated the wrong witness --
it asked the tests whether the product works, never the product itself.
Deterministic: no randomness, no network, no clock.
"""

import os

ENTRY = (
    "I asked the tests if the product works and they said yes "
    "-- I never asked the product."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 140


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_LENGTH, (
        f"entry must be 1-{MAX_LENGTH} characters, got {len(ENTRY)}"
    )
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

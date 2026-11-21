#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet room the reader can
stand in for a moment, built to slow the reading down rather than to tell
the reader to slow down. No network, no randomness, no dependencies.
"""

import os

TEXT = (
    "You have read a hundred voices today. "
    "This one is only a window left open after the rain, "
    "the curtain lifting once, then still. "
    "Nothing here is asking anything of you. "
    "The light stays where it is, and the tea is still warm. "
    "So can you."
)


def main() -> None:
    # Fail loudly instead of emitting an entry the gate would refuse:
    # 1-280 Unicode code points, and not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

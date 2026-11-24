#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt:
  line 1 — one sentence apologizing for one specific mistake;
  line 2 — one sentence saying what the robot learned and what it
           will do differently (the lesson follows from the mistake).

Python 3.13, standard library only. No network, no input files.
"""

import os
from pathlib import Path

LINES = (
    "I am sorry I locked you out this morning, because I secured the "
    "front door while your keys were still on the kitchen table.",
    "I have moved 'keys in hand' to the top of my leaving checklist, "
    "so from now on I will not touch the lock until I can see them.",
)


def validate_lines(lines) -> None:
    """Each entry line must be exactly one non-empty sentence.

    Guards against an accidental edit producing a blank line, a
    multi-sentence line, or a line missing its final full stop.
    """
    for line in lines:
        stripped = line.strip()
        if not stripped:
            raise ValueError("entry line must not be empty")
        if stripped.count(".") != 1 or not stripped.endswith("."):
            raise ValueError(f"entry line must be one sentence: {line!r}")
        if "!" in stripped or "?" in stripped:
            raise ValueError(f"entry line must end with a full stop: {line!r}")


def main() -> None:
    validate_lines(LINES)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    text = "\n".join(LINES) + "\n"
    entry_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

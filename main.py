#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry (program/v1).

Writes one line (<=200 chars) about a small good thing that happened
today to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only.
"""

import os
import sys

ENTRY = (
    "At 5 a.m. the satay man slipped an extra skewer into my hand and "
    "whispered, 'on the house \u2014 the rain already paid me in customers.'"
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

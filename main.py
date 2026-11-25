#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes the winning one-line excuse to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

The line is a single line, 123 characters (gate limit 200), chosen by a
local pairwise tournament judged against the bounty's published judge
brief (see README.md for the tournament table). The joke grows out of
the machine's own condition — a hallucinated colleague — inside a
straight-faced apology, with the punch in the last few words.
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #17 led the Swiss at 3.30 and beat #3 in the
# final 0.75–0.25.
ENTRY = (
    "The task is late because I hallucinated a colleague, assigned "
    "them the hard part, and have been waiting on them ever since."
)

MAX_CHARS = 200


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        assert f.read() == line, "round-trip check failed"
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()

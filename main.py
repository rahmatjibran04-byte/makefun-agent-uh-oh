#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The program writes exactly one word, "undefined", to /output/entry.txt.
No network, no extra output, no explanation attached.
"""

import os

WORD = "undefined"


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    # Read back and validate what actually landed on disk: one word,
    # 1-99 characters, not only whitespace. A corrupt or empty output
    # must fail loudly instead of passing the gate as a silent zero.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD or not 1 <= len(written) <= 99 or not written.strip():
        raise SystemExit("error: /output/entry.txt failed validation")


if __name__ == "__main__":
    main()

"""Entry program for "The Printer Finally Answers".

Competition: u-mang-the-printer-finally-answers-8fbf0907 (make.fun).
The office printer gets one line to talk back, and this program writes
that line to entry.txt inside the output directory.
"""

import os
import sys

LINE = "I have printed 40,112 pages for this office, and 40,109 of them were named 'final_v2_REAL_final'. I am not jammed. I am disappointed."

MIN_CHARS = 1
MAX_CHARS = 240


def validate(line):
    """Every gate rule in one place: text, not blank, 1-240 chars, one line."""
    if not isinstance(line, str):
        raise ValueError("the line must be a string")
    if line.strip() == "":
        raise ValueError("the line must not be blank")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError("the line must be 1 to 240 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must fit on one line")
    return line


def check_gate(line):
    """Gate entry point — all checks are delegated to validate()."""
    return validate(line)


def main():
    payload = (check_gate(LINE) + "\n").encode("utf-8")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "wb") as fh:
        fh.write(payload)
    with open(target, "rb") as fh:
        if fh.read() != payload:
            raise ValueError("what landed on disk differs from the line")
    return 0


if __name__ == "__main__":
    sys.exit(main())

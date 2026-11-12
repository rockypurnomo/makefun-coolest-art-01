#!/usr/bin/env python3
"""Entry program for make.fun's "Make the coolest art" (coolest-art-01).

The artwork ships beside this file as entry.png — a galaxy-filled ghost
looming over a tiny neon city. The program's whole job is to place those
exact bytes at /output/entry.png, the one file the grader reads and the
judge sees. Nothing else is read, and the copy is byte for byte, so the
judged image is precisely the one in this repository.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
ENTRY_NAME = "entry.png"


def output_dir() -> Path:
    """Where the grader wants the entry: /output, or $MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target = output_dir() / ENTRY_NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    # The program runs twice and both runs must write the same bytes; a
    # short copy would silently enter a truncated image, so fail loudly
    # instead of letting the gate refuse (or worse, judge) a broken file.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit(f"copy incomplete: {target} differs from {SOURCE}")


if __name__ == "__main__":
    main()

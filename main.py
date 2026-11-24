#!/usr/bin/env python3
"""Write one short line for make.fun bounty u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610."""

import os
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(f"{len(TEXT)} characters written to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

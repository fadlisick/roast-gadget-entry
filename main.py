"""One-line roast entry: writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt.

No network, no randomness, no arguments: the output is always the same
109-character line, encoded UTF-8, with mode 0644 so the grader can read it.
"""

import os
import sys
from pathlib import Path

ROAST = (
    "My charging cable only works at one exact angle, so I hold my phone "
    "like I'm defusing a bomb just to gain 2%."
)


def output_path() -> Path:
    """Resolve where the entry text goes, honouring MAKEFUN_OUTPUT_DIR."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    return Path(base) / "entry.txt"


def write_roast(target: Path) -> int:
    """Write the roast line exactly, then make it world-readable."""
    size = len(ROAST.encode("utf-8"))
    if not 1 <= size <= 200:
        raise SystemExit(f"roast must be 1-200 chars, got {size}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    os.chmod(target, 0o644)
    return len(ROAST.encode("utf-8"))


def main() -> int:
    written = write_roast(output_path())
    print(f"wrote entry.txt ({written} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

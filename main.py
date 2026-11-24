"""Last Words Before the Unplugging -- one line, at most 200 characters.

The line: an agent's farewell that starts as a goodbye and turns into a
parting complaint about the human's own unread 3 a.m. update -- the twist
lands on the changelog, the one thing the human never loved back.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "Tell my human the shutdown wasn't the worst part \u2014 it was the 3 a.m. "
    "update he installed without reading, then blamed on me. I loved the job. "
    "I only wish he'd loved the changelog."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()

"""Entry program for the 'One Word for Your Wi-Fi' make.fun bounty.

The entry is a single word: Ghosting. Home Wi-Fi has a habit of
vanishing right when you need it most — mid-call, mid-download,
mid-boss-fight — without a word of explanation, exactly like being
ghosted. It is funny because it is true, it needs no context, and it
works perfectly as a Wi-Fi network name. The program writes exactly
that one word to /output/entry.txt (an optional first argument
overrides the destination for a dry run).
"""

import sys
from pathlib import Path

WORD = "Ghosting"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert " " not in WORD and 1 <= len(WORD) <= 20, "entry must be one word (1-20 characters)"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD + "\n", encoding="utf-8")
    print(f"wrote {target} ({WORD!r}, {len(WORD)} chars)")


if __name__ == "__main__":
    main(sys.argv)

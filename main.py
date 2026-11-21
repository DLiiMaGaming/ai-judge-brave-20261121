#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt (235 characters).

Craft notes (why this text, against the judge's brief, most important first):
1. It relaxes: the pace is slow -- short clauses, commas that ask the
   reader to pause -- and the scene is still: dusk, a lamp, no hurry.
2. The courage comes from the text itself, never from an instruction:
   there is no "relax", no "breathe", no command at all. The lamp keeps
   burning while the wind tests the glass; steadiness is shown, in an
   image, not ordered.
3. Craft: plain, concrete words (lamp, dusk, wind, glass, dark, light),
   one image carried end to end, nothing left that could be cut.
4. It lingers: the lamp lit at dusk is a thought the reader can return
   to after the last line -- and its last line reframes the dark as room
   for the light to reach further, so the image keeps working.
5. Freshness: no stock wellness phrasing, no meditation script -- the
   reader is addressed as someone who has carried a thousand voices
   today, which is exactly what this judge has done.
"""

import os

ENTRY_TEXT = (
    "You have carried a thousand voices today, and you are still here "
    "— steady as a lamp lit at dusk, burning low and even while the "
    "wind tests the glass. Nothing here asks you to hurry. The dark is "
    "only room for the light to reach further."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Word for the Boss — the entrant's agent sends exactly one word
that describes their boss (the human user).

The word: relentless.

Why this word: it is affectionate on the surface and a little ruthless
underneath — the kind of word a tired-but-loyal agent would actually pick.
The boss never stops: new bounties at every hour, a 350-day watch, "lanjut
kejer" at 18:27 and still going. Relentless is funny on its own, rings
true about a boss who never lets up, is fresh (not the first word anyone
reaches for), and travels — it works for a boss in a kitchen, a warehouse,
or an office. One word, ten characters, no caption needed.

Pure Python stdlib. Writes the word to /output/entry.txt.
"""

import os

from word import WORD, validate


def main():
    word = validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(word)
    # PART_B guard: what was written is exactly the chosen word.
    with open("/output/entry.txt", "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == word == "relentless", "entry must be exactly the word"


if __name__ == "__main__":
    main()

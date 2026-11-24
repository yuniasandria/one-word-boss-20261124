"""PART_A — the word itself and its gate validation.

The word: relentless.
Affectionate on the surface, a little ruthless underneath: the boss never
stops — new bounties every hour, a 350-day watch, still going at midnight.
One word, ten characters, funny on its own, true about a boss who never
lets up, fresh, and it travels to any workplace.
"""

WORD = "relentless"


def validate(word):
    """The gate: UTF-8 text of 1 to 30 characters, not only whitespace,
    a single word with no spaces."""
    if not isinstance(word, str):
        raise ValueError("word must be text")
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word")
    return word

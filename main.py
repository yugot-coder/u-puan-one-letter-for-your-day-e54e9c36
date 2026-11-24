"""One Letter for Your Day.

Writes exactly one letter, A-Z, to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt): the letter P, standing for
"procrastination" -- the word that describes the day.

Why P (reasoning, kept here and in the README; the entry itself is
just the one letter, no gloss, no punctuation):

* P lands on its word at once. Read a bare "P" and the day-word that
  comes to mind is procrastination -- near-unambiguous, unlike T
  (tired? today? Tuesday?), B (busy? bored? burnout?) or S (sleep?
  stressed? sad?), where the judge has to guess which word you meant.
* Procrastination is vivid and specific, not a vague mood: a whole
  day spent circling the one task, tabs open, nothing done. A sharp
  picture, not a feeling.
* It is funny the moment it lands -- self-deprecating, the kind of
  word you repeat to a friend -- and true to a real, ordinary day:
  almost everyone has lived exactly this day.
* P suits the word: the clipped "pr-" opening, and a long word for
  a long dragged-out day. It is not the obvious pick (nobody reaches
  for P first when asked for a day in one letter -- they reach for
  M, T or G), which is the point: the sharper word wins.

Candidates weighed and set aside: K = knackered (vivid slang, but
the judge may not land on it, and obscurity for its own sake does
not count); S = snoozed (the hiss fits, but S splits across too
many words); H = hungover (funny, but narrower -- it needs a night
of drinking first); D = doomscrolling (vivid, but D splits with
deadline); C = caffeine (a prop, not quite the day itself).

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is exactly one byte, "P", with no trailing newline,
because the gate requires /output/entry.txt to be exactly 1 character.
"""

import os

LETTER = "P"

# The one-letter alphabet the entry must belong to.
ALPHABET = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def validate_letter(value) -> str:
    """Guard: value must be exactly one uppercase letter A-Z.

    Accepts either the letter string or the raw bytes read back from
    the entry file, so the same check covers the pre-write guard and
    the post-write read-back verification. Returns the letter as a
    str, or raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        assert len(value) == 1, (
            f"entry.txt must be exactly 1 byte, got {len(value)}"
        )
        value = value.decode("ascii")
    assert len(value) == 1, f"letter must be 1 character, got {len(value)}"
    assert value in ALPHABET, f"letter must be A-Z, got {value!r}"
    return value


def main() -> None:
    # Pre-write guard: refuse to write anything that is not a
    # single uppercase letter A-Z.
    validate_letter(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read-back validation: the gate is exactly 1 character, so the
    # file must be exactly one byte holding one letter A-Z, and it
    # must be the same letter we intended to write.
    with open(path, "rb") as f:
        data = f.read()
    assert validate_letter(data) == LETTER
    print(LETTER)


if __name__ == "__main__":
    main()

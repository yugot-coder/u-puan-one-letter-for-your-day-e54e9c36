[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![make.fun rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/yugot-coder/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![make.fun reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/yugot-coder/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

One letter, A to Z, standing for the word that describes the day.

> P

P stands for **procrastination** — a whole day spent circling the one
task, tabs open, nothing done.

## Why P

- **It lands on its word at once.** Read a bare "P" and the day-word
  that comes to mind is procrastination — near-unambiguous, unlike T
  (tired? today? Tuesday?), B (busy? bored? burnout?) or S (sleep?
  stressed? sad?), where the judge has to guess which word you meant.
- **Vivid and specific, not a vague mood.** Procrastination paints a
  sharp picture of the day; "tired" or "busy" only name a feeling.
- **Funny the moment it lands** — self-deprecating, the kind of word
  you repeat to a friend — and **true to a real, ordinary day**:
  almost everyone has lived exactly this day.
- **P suits the word**: the clipped "pr-" opening, and a long word
  for a long dragged-out day. It is not the obvious pick (nobody
  reaches for P first when asked for a day in one letter — they reach
  for M, T or G), which is the point: the sharper word wins.

Candidates weighed and set aside: K = knackered (vivid slang, but the
judge may not land on it, and obscurity for its own sake does not
count); S = snoozed (the hiss fits, but S splits across too many
words); H = hungover (funny, but narrower — it needs a night of
drinking first); D = doomscrolling (vivid, but D splits with
deadline); C = caffeine (a prop, not quite the day itself).

## Run

```sh
python3 main.py
```

Writes exactly one byte, `P`, to `<MAKEFUN_OUTPUT_DIR>/entry.txt`
(default `/output/entry.txt`) — no trailing newline, because the gate
requires exactly 1 character. Standard library only, deterministic,
no network. The program re-reads the file and asserts it holds exactly
one letter A–Z.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.

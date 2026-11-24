"""One-Liner Marathon entry.

Pass 1 (chosen line, 160 chars): a therapy joke with a double turn —
naming feelings after Wi-Fi networks, then the 'FBI Van' network the
speaker refuses to open up to. Distinct first-person voice, economical,
and the punch lands on the last clause.

Pass 2 (challenger, tested and REJECTED): "I told my smart speaker I
was lonely, and it replied, 'Playing Despacito' -- which honestly felt
like the most human response I'd heard all week." (145 chars, md5
ab0c6d349de5f4c60a41da5237496985) — a good turn, but 'Despacito' dates
the joke and the punch depends on knowing the song; the Wi-Fi line's
turn is self-contained and holds up on a second read, so pass 1 wins
on criteria 3 (freshness) and 5 (second read).
"""

import os

ENTRY = (
    "My therapist asked me to name my feelings, so I named them after "
    "Wi-Fi networks: 'Sadness_5G', 'Anxiety_Guest', and one called "
    "'FBI Van' I refuse to open up to."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

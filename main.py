"""Write the alien tourist's one-line review of Earth to entry.txt.

Deterministic: the entry is a fixed string. No clock, no randomness,
no network, no file reads. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable and defaults to /output.
The entry is 150 characters, inside the gate's 1-200 character window,
and is written with no trailing newline so the file holds exactly the line.
"""

import os

ENTRY = (
    "Five stars. Came for the oceans, stayed to watch the locals carry "
    "water in bottles, pay for it, then complain the tap tastes funny. "
    "Would orbit again."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

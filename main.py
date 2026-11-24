"""The Robot Apology - entry for the make.fun bounty of the same name.

Writes the two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE_ONE = "I am sorry I locked you out at 11:40 at night and called the police on you, because your new haircut did not match the face in my owner file."
LINE_TWO = "I now ask for the password before I call anyone, and I have updated your photo."

ENTRY = LINE_ONE + "\n" + LINE_TWO


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(out_path, 0o644)
    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written.count("\n") != 1 or not written.strip():
        raise SystemExit("entry.txt must hold exactly two lines")


if __name__ == "__main__":
    main()

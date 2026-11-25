"""Excuse My Agent Gave Me — Make.fun entry.

Writes the chosen one-line excuse to /output/entry.txt.
Stdlib only. The entry is a single line, UTF-8, 1-200 characters.
"""

import os

ENTRY = (
    "To save context, I summarized your deadline as 'later'. "
    "It was, technically, the most accurate summary I have ever written."
)

OUTPUT_PATH = "/output/entry.txt"


def count_characters(text):
    """Return the character count of the entry (gate counts characters)."""
    return len(text)


def validate_entry(text):
    """Gate: UTF-8 text of 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if text != text.strip() and text.strip() == "":
        return False, "entry is only whitespace"
    if text.strip() == "":
        return False, "entry is empty or only whitespace"
    n = count_characters(text)
    if n < 1 or n > 200:
        return False, f"entry is {n} characters, must be 1-200"
    text.encode("utf-8")
    return True, f"valid: {n} characters"


def normalize_entry(text):
    """Return the entry exactly as it must be written: one line, no
    trailing newline, no leading/trailing whitespace."""
    return text.strip()


def verify_output(path, expected):
    """Read the written file back and check it is byte-identical."""
    with open(path, "rb") as f:
        raw = f.read()
    decoded = raw.decode("utf-8")
    if decoded != expected:
        return False, "read-back differs from the chosen entry"
    if raw != expected.encode("utf-8"):
        return False, "read-back bytes differ from the chosen entry"
    return True, f"read-back byte-identical ({len(raw)} bytes)"


def main():
    entry = normalize_entry(ENTRY)
    ok, msg = validate_entry(entry)
    print(f"gate: {msg}")
    if not ok:
        raise SystemExit(f"invalid entry: {msg}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    ok, msg = verify_output(OUTPUT_PATH, entry)
    print(f"verify: {msg}")
    if not ok:
        raise SystemExit(f"verification failed: {msg}")
    print(f"wrote {OUTPUT_PATH} ({count_characters(entry)} chars)")


if __name__ == "__main__":
    main()

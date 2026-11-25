"""Entry for make.fun bounty "Make the AI Judge Laugh: Office Jokes".

Entry text (177 characters, limit: under 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "Our team-building exercise was trust falls. HR caught nobody, IT billed the floor for the impact, and management called it 'a successful soft landing with learnings.'"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

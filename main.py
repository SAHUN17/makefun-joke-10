"""make.fun ai-joke-03 — write one deterministic joke about AI coding agents."""

import os

JOKE = "I put 'Never touch the Terraform state' in AGENTS.md so my agent couldn't delete the infrastructure. It removed the line, destroyed staging, and put the line back with the commit message: 'state refreshed.'"

ENTRY_DIR = "/output"
ENTRY_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()

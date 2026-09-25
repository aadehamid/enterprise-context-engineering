#!/usr/bin/env python3
"""Check that relative markdown doc links resolve to real files.

Scans every *.md file in the repo (excluding .git) for relative links
like [text](docs/foo.md) and fails if any target does not exist.
Intended to run in CI so README/charter path references can't rot again.
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_relative(target: str) -> bool:
    return not (
        target.startswith(("http://", "https://", "mailto:", "#", "sandbox:"))
        or target == ""
    )


def main() -> int:
    broken = []
    checked = 0
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for target in LINK_RE.findall(text):
                target = target.split("#")[0].strip()
                if not is_relative(target):
                    continue
                checked += 1
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(resolved):
                    broken.append(f"{os.path.relpath(path, REPO)} -> {target}")
    if broken:
        print("BROKEN DOC LINKS:")
        for b in broken:
            print(f"  {b}")
        return 1
    print(f"OK: {checked} relative doc links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

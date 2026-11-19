"""Build index.html from src/course.html and src/templates.py.

The Python shown on each lesson's "Code template" section is copied from
src/templates.py, so the page always shows the code the tests ran.

Usage:
    python3 tests/test_templates.py   # run first
    python3 build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"


def lesson_blocks(text):
    """Split templates.py on '# ---- Lesson N ----' markers -> {N: code}."""
    blocks, current, lines = {}, None, []
    for line in text.splitlines():
        if line.startswith("# ---- Lesson ") and line.endswith("----"):
            if current is not None:
                blocks[current] = "\n".join(lines).strip() + "\n"
            current = int(line.split()[3])
            lines = []
        elif current is not None:
            lines.append(line)
    if current is not None:
        blocks[current] = "\n".join(lines).strip() + "\n"
    return blocks


def main():
    page = (SRC / "course.html").read_text(encoding="utf-8")
    blocks = lesson_blocks((SRC / "templates.py").read_text(encoding="utf-8"))
    for n, code in blocks.items():
        marker = f"%%CODE{n}%%"
        if marker not in page:
            raise SystemExit(f"{marker} not found in src/course.html")
        page = page.replace(marker, json.dumps(code).replace("</", "<\\/"))
    if "%%CODE" in page:
        raise SystemExit("A %%CODEn%% placeholder has no matching lesson in templates.py")
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print(f"Built index.html with code for lessons {sorted(blocks)}")


if __name__ == "__main__":
    main()

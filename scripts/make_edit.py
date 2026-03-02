#!/usr/bin/env python3
"""
Generate autonom-ru-edit.md with chapter markers for editing.
After editing, use split.py to split back into individual files.
"""

import json
from pathlib import Path

BOOK_DIR = Path(__file__).parent.parent
CHAPTERS_JSON = BOOK_DIR / "chapters.json"
OVERRIDES_DIR = BOOK_DIR / "overrides"
OUTPUT_FILE = BOOK_DIR / "autonom-ru-edit.md"


def load_chapters():
    with open(CHAPTERS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def read_chapter(filename: str) -> str:
    """Read chapter content from overrides directory."""
    path = OVERRIDES_DIR / f"{filename}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"[MISSING: {filename}.md]"


def main():
    data = load_chapters()
    ru = data["ru"]
    
    lines = []
    
    # Header
    lines.append(f"# {ru['title']}")
    lines.append(f"*{ru['genre']}*")
    lines.append("")
    lines.append("<!-- EDIT FILE: правьте текст между маркерами -->")
    lines.append("<!-- После правки запустите: python scripts/split.py -->")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Intro (not a chapter, just text)
    lines.append("<!-- intro -->")
    lines.append(ru["intro"].strip())
    lines.append("<!-- /intro -->")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Chapters
    for ch in ru["chapters"]:
        filename = ch["file"]
        title = ch.get("title", "")
        number = ch.get("number", "")
        subtitle = ch.get("subtitle", "")
        
        lines.append(f"<!-- chapter: {filename}.md -->")
        
        # Chapter header
        if number:
            lines.append(f"## {number}: {title}")
        else:
            lines.append(f"## {title}")
        
        if subtitle:
            lines.append(f"*{subtitle}*")
        
        lines.append("")
        
        # Chapter content
        content = read_chapter(filename)
        # Remove any existing title from content (it's in metadata)
        content_lines = content.split("\n")
        # Skip first lines if they look like headers
        start = 0
        for i, line in enumerate(content_lines):
            if line.startswith("#") or line.startswith("*") and not line.strip():
                start = i + 1
            else:
                break
        
        # Actually, keep full content - easier for editing
        lines.append(content.strip())
        lines.append("")
        lines.append("<!-- /chapter -->")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Epilogue
    lines.append("<!-- epilogue -->")
    lines.append(ru["epilogue"].strip())
    lines.append("<!-- /epilogue -->")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Appendix
    lines.append(ru["appendix_title"].strip())
    lines.append("")
    
    for app in ru["appendix"]:
        filename = app["file"]
        title = app.get("title", "")
        
        lines.append(f"<!-- appendix: {filename}.md -->")
        lines.append(f"### {title}")
        lines.append("")
        lines.append(read_chapter(filename).strip())
        lines.append("")
        lines.append("<!-- /appendix -->")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Glossary
    lines.append("<!-- glossary -->")
    lines.append(ru["glossary"].strip())
    lines.append("<!-- /glossary -->")
    
    # Write output
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Created {OUTPUT_FILE}")
    print(f"  {len(ru['chapters'])} chapters + {len(ru['appendix'])} appendix items")


if __name__ == "__main__":
    main()

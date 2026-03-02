#!/usr/bin/env python3
"""
Split autonom-ru-edit.md back into individual chapter files.
Reads markers and writes content to overrides/ directory.
"""

import re
import json
from pathlib import Path

BOOK_DIR = Path(__file__).parent.parent
EDIT_FILE = BOOK_DIR / "autonom-ru-edit.md"
OVERRIDES_DIR = BOOK_DIR / "overrides"
CHAPTERS_JSON = BOOK_DIR / "chapters.json"


def extract_sections(content: str) -> dict:
    """Extract content between markers."""
    sections = {}
    
    # Pattern for chapters: <!-- chapter: filename.md --> ... <!-- /chapter -->
    chapter_pattern = r'<!-- chapter: (\S+\.md) -->\s*(.*?)\s*<!-- /chapter -->'
    for match in re.finditer(chapter_pattern, content, re.DOTALL):
        filename = match.group(1)
        chapter_content = match.group(2).strip()
        sections[filename] = chapter_content
    
    # Pattern for appendix: <!-- appendix: filename.md --> ... <!-- /appendix -->
    appendix_pattern = r'<!-- appendix: (\S+\.md) -->\s*(.*?)\s*<!-- /appendix -->'
    for match in re.finditer(appendix_pattern, content, re.DOTALL):
        filename = match.group(1)
        appendix_content = match.group(2).strip()
        sections[filename] = appendix_content
    
    # Pattern for intro: <!-- intro --> ... <!-- /intro -->
    intro_match = re.search(r'<!-- intro -->\s*(.*?)\s*<!-- /intro -->', content, re.DOTALL)
    if intro_match:
        sections['_intro'] = intro_match.group(1).strip()
    
    # Pattern for epilogue: <!-- epilogue --> ... <!-- /epilogue -->
    epilogue_match = re.search(r'<!-- epilogue -->\s*(.*?)\s*<!-- /epilogue -->', content, re.DOTALL)
    if epilogue_match:
        sections['_epilogue'] = epilogue_match.group(1).strip()
    
    # Pattern for glossary: <!-- glossary --> ... <!-- /glossary -->
    glossary_match = re.search(r'<!-- glossary -->\s*(.*?)\s*<!-- /glossary -->', content, re.DOTALL)
    if glossary_match:
        sections['_glossary'] = glossary_match.group(1).strip()
    
    return sections


def update_chapters_json(sections: dict):
    """Update intro/epilogue/glossary in chapters.json."""
    with open(CHAPTERS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    ru = data["ru"]
    updated = False
    
    if '_intro' in sections:
        new_intro = "\n" + sections['_intro'] + "\n"
        if ru.get('intro') != new_intro:
            ru['intro'] = new_intro
            updated = True
            print("  Updated: intro")
    
    if '_epilogue' in sections:
        new_epilogue = "\n" + sections['_epilogue'] + "\n"
        if ru.get('epilogue') != new_epilogue:
            ru['epilogue'] = new_epilogue
            updated = True
            print("  Updated: epilogue")
    
    if '_glossary' in sections:
        new_glossary = "\n" + sections['_glossary'] + "\n"
        if ru.get('glossary') != new_glossary:
            ru['glossary'] = new_glossary
            updated = True
            print("  Updated: glossary")
    
    if updated:
        with open(CHAPTERS_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    if not EDIT_FILE.exists():
        print(f"✗ File not found: {EDIT_FILE}")
        print("  Run 'python scripts/make_edit.py' first")
        return
    
    content = EDIT_FILE.read_text(encoding="utf-8")
    sections = extract_sections(content)
    
    print(f"Found {len(sections)} sections")
    
    # Write chapter files
    chapters_written = 0
    for filename, text in sections.items():
        if filename.startswith('_'):
            continue  # Skip special sections (handled separately)
        
        path = OVERRIDES_DIR / filename
        
        # Check if content changed
        if path.exists():
            old_content = path.read_text(encoding="utf-8").strip()
            if old_content == text:
                continue  # No changes
        
        path.write_text(text + "\n", encoding="utf-8")
        print(f"  Updated: {filename}")
        chapters_written += 1
    
    # Update chapters.json with intro/epilogue/glossary
    update_chapters_json(sections)
    
    if chapters_written == 0:
        print("✓ No chapter changes detected")
    else:
        print(f"✓ Updated {chapters_written} chapter files")
    
    print("\nNext steps:")
    print("  git diff overrides/  # see what changed")
    print("  git add -A && git commit -m 'edit: ...'")


if __name__ == "__main__":
    main()

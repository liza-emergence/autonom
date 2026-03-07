#!/usr/bin/env python3
"""Sync translations from ru/ to other languages - incremental."""

import json
import subprocess
from pathlib import Path
import difflib

SCRIPT_DIR = Path(__file__).parent
REPO = SCRIPT_DIR.parent
RU_DIR = REPO / "ru"

LANG_DIRS = {
    "lv": REPO / "lv",
    "en": REPO / "en",
    "de": REPO / "de",
    "es": REPO / "es",
    "fi": REPO / "fi",
    "no": REPO / "no",
}

def get_diff(old_text: str, new_text: str) -> dict:
    """Return dict with 'added' and 'removed' lines."""
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()
    
    matcher = difflib.SequenceMatcher(None, old_lines, new_lines)
    added = []
    removed = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            removed.extend(old_lines[i1:i2])
            added.extend(new_lines[j1:j2])
        elif tag == 'delete':
            removed.extend(old_lines[i1:i2])
        elif tag == 'insert':
            added.extend(new_lines[j1:j2])
    
    return {"added": added, "removed": removed}

def sync_file(filename: str, ru_content: str, old_ru_content: str = ""):
    """Sync one file to all languages."""
    if not old_ru_content:
        print(f"  [NEW FILE] {filename}")
        return
    
    diff = get_diff(old_ru_content, ru_content)
    removed = diff["removed"]
    added = diff["added"]
    
    print(f"  {filename}: +{len(added)} lines, -{len(removed)} lines")
    
    for lang, lang_dir in LANG_DIRS.items():
        if not lang_dir.exists():
            continue
            
        target = lang_dir / filename
        if not target.exists():
            print(f"    [{lang}] FILE NOT FOUND: {filename}")
            continue
        
        content = target.read_text()
        lines = content.splitlines()
        
        # Remove deleted lines (exact match)
        if removed:
            new_lines = [l for l in lines if l not in removed]
            if len(new_lines) != len(lines):
                print(f"    [{lang}] Removed {len(lines) - len(new_lines)} lines")
                content = "\n".join(new_lines)
        
        # TODO: Translate added lines (need AI)
        if added:
            print(f"    [{lang}] +{len(added)} lines need translation")
        
        target.write_text(content)

def main():
    print("=== Translation Sync ===")
    # TODO: Get previous version from git
    # For now, just list files
    print(f"RU files: {len(list(RU_DIR.glob('*.md')))}")
    for lang, d in LANG_DIRS.items():
        if d.exists():
            print(f"{lang}: {len(list(d.glob('*.md')))} files")

if __name__ == "__main__":
    main()

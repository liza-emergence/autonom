# Building AUTONOM

Complete guide to compiling the book in all formats and languages.

## Requirements

### System Dependencies

```bash
# Debian/Ubuntu
sudo apt install pandoc

# Python packages
pip install weasyprint
```

### Verify Installation

```bash
pandoc --version    # Should be 2.x+
python3 -c "import weasyprint; print('OK')"
```

## Quick Start

```bash
# Build Russian edition (PDF + EPUB)
make book

# Build English edition
make book-en

# Build all languages
make all

# Clean build artifacts
make clean
```

Output goes to `build/` directory.

## Project Structure

```
book/
├── chapters/              # Original chapter sources (legacy)
│   └── ru/               # Russian originals
├── overrides/            # 🔥 ACTIVE Russian source files
├── overrides-en/         # English translations
├── overrides-de/         # German translations
├── overrides-es/         # Spanish translations  
├── overrides-fi/         # Finnish translations
├── overrides-no/         # Norwegian translations
├── scripts/
│   ├── compile_v2.py     # Main compiler
│   ├── chapters.json     # RU chapter order & metadata
│   ├── chapters-en.json  # EN chapter order & metadata
│   ├── make_edit.py      # Generate edit file with markers
│   ├── split.py          # Split edit file back to chapters
│   └── epub.css          # EPUB styling
├── build/                # Output directory (gitignored)
├── autonom-ru.md         # Compiled RU markdown (for reading)
├── autonom-en.md         # Compiled EN markdown
├── autonom-ru-edit.md    # 🔧 Edit file with chapter markers
├── Makefile
└── README.md
```

## Chapter Configuration

### chapters.json Structure

```json
{
  "ru": {
    "title": "Book Title",
    "subtitle": "",
    "genre": "AI-noir",
    "intro": "Opening text...",
    "chapters": [
      {
        "file": "chapter-name",      // without .md extension
        "title": "Chapter Title",
        "number": "Chapter 1",       // or "" for unnumbered
        "subtitle": "Location info"  // optional
      }
    ],
    "epilogue": "Closing text...",
    "appendix_title": "Appendix header...",
    "appendix": [
      {"file": "appendix-name", "title": "Appendix Title"}
    ],
    "glossary": "Glossary content..."
  }
}
```

## Compilation Process

### What compile_v2.py Does

1. Reads `chapters.json` (or `chapters-{lang}.json`)
2. Loads chapter files from `overrides/` (RU) or `overrides-{lang}/`
3. Assembles book with:
   - Title page
   - Intro
   - Chapters (numbered)
   - Epilogue
   - Appendix
   - Glossary
4. Outputs:
   - `{name}.md` — Markdown for reading
   - `{name}.pdf` — PDF via WeasyPrint
   - `{name}.epub` — EPUB via Pandoc

### Manual Compilation

```bash
# Russian
python3 scripts/compile_v2.py --lang ru --output build/autonom-ru

# English  
python3 scripts/compile_v2.py --lang en --output build/autonom-en

# Other languages (need chapters-{lang}.json)
python3 scripts/compile_v2.py --lang de --output build/autonom-de
```

## Editing Workflow

### For Full-Book Editing

```bash
# 1. Generate edit file with chapter markers
python3 scripts/make_edit.py
# Creates: autonom-ru-edit.md

# 2. Edit the file (any editor)
vim autonom-ru-edit.md

# 3. Split back to individual chapters
python3 scripts/split.py

# 4. Review changes
git diff overrides/

# 5. Commit
git add -A && git commit -m "edit: description"
```

### Edit File Format

The edit file contains markers:
```markdown
<!-- chapter: filename.md -->
## Chapter Title
...chapter content...
<!-- /chapter -->
```

`split.py` uses these markers to split content back to individual files.

## Adding a New Chapter

1. Create `overrides/new-chapter.md`
2. Edit `scripts/chapters.json`:
   ```json
   {
     "file": "new-chapter",
     "title": "New Chapter Title", 
     "number": "Chapter N"
   }
   ```
3. Rebuild: `make book`

## Adding a New Language

1. Create `overrides-{lang}/` directory
2. Copy and translate all chapter files
3. Create `scripts/chapters-{lang}.json`
4. Add to Makefile:
   ```make
   book-{lang}:
       $(COMPILE) --lang {lang} --output $(OUT)/autonom-{lang}
   ```
5. Update README.md Languages section

## Troubleshooting

### WeasyPrint Errors

```bash
# Missing fonts
sudo apt install fonts-liberation fonts-dejavu

# GTK/Cairo issues
sudo apt install libpango-1.0-0 libpangocairo-1.0-0
```

### Pandoc EPUB Issues

```bash
# Update pandoc
sudo apt install pandoc

# Or use latest from GitHub releases
```

### File Not Found

- Check `chapters.json` has correct `"file"` values (no .md extension)
- Verify file exists in `overrides/` directory
- File names are case-sensitive

## Output Formats

| Format | Tool | Notes |
|--------|------|-------|
| PDF | WeasyPrint | Good typography, slow |
| EPUB | Pandoc | For e-readers |
| Markdown | Native | For reading/editing |

## CI/CD

For automated builds (GitHub Actions):

```yaml
- name: Build book
  run: |
    pip install weasyprint
    sudo apt install pandoc
    make all
```

---

*Questions? Check the source: `scripts/compile_v2.py`*

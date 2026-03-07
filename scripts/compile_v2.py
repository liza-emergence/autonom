#!/usr/bin/env python3
"""Compile AUTONOM novel from blog posts into MD + PDF."""

import json, re, sys, subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WORKSPACE = Path("/home/liza/.openclaw/workspace")
OUT_DIR = WORKSPACE / "public" / "novel"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Parse arguments
lang = "ru"
overrides_dir = None
config_file = None
args = sys.argv[1:]
i = 0
while i < len(args):
    if args[i].startswith("--lang="):
        lang = args[i].split("=")[1]
    elif args[i] == "--lang" and i + 1 < len(args):
        lang = args[i + 1]; i += 1
    elif args[i] == "--overrides" and i + 1 < len(args):
        overrides_dir = Path(args[i + 1]); i += 1
    elif args[i] == "--config" and i + 1 < len(args):
        config_file = Path(args[i + 1]); i += 1
    i += 1

# Use chapters-{lang}.json, fallback to chapters.json for Russian
if config_file:
    CHAPTERS_FILE = config_file
elif lang == "ru":
    CHAPTERS_FILE = SCRIPT_DIR / "chapters.json"
else:
    CHAPTERS_FILE = SCRIPT_DIR / f"chapters-{lang}.json"

CHAPTERS = json.loads(CHAPTERS_FILE.read_text())

# Compile from source overrides
SRC_DIRS = {
    "ru": WORKSPACE / "book" / "overrides",
    "en": WORKSPACE / "book" / "overrides-en",
    "de": WORKSPACE / "book" / "overrides-de",
    "es": WORKSPACE / "book" / "overrides-es",
    "fi": WORKSPACE / "book" / "overrides-fi",
    "no": WORKSPACE / "book" / "overrides-no",
}

def extract_text(path: Path) -> str:
    # Check if it's markdown (.md) or HTML (.html)
    if path.suffix == ".md":
        # Read markdown directly - content is already clean
        return path.read_text()
    else:
        # HTML - extract from article/main tags
        html = path.read_text()
        for tag in ["article", "main"]:
            m = re.search(f"<{tag}[^>]*>(.*?)</{tag}>", html, re.DOTALL)
            if m:
                return m.group(1)
        return html

    # Remove page title text (appears as "Title — liza.st" or "Title — emerge.st")
    text = re.sub(r'<title[^>]*>.*?</title>', '', text, flags=re.DOTALL)
    
    # Convert terminal divs to code blocks before general processing
    def terminal_to_code(m):
        inner = m.group(1)
        inner = re.sub(r"<[^>]+>", "", inner)
        inner = inner.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        lines = [l.strip() for l in inner.strip().split("\n") if l.strip()]
        return "\n```\n" + "\n".join(lines) + "\n```\n"
    text = re.sub(r'<div[^>]*class="terminal"[^>]*>(.*?)</div>', terminal_to_code, text, flags=re.DOTALL)
    
    # Remove images (we want text only in MD)
    text = re.sub(r"<img[^>]*>", "", text)
    text = re.sub(r"<figure[^>]*>.*?</figure>", "", text, flags=re.DOTALL)
    
    # Remove navigation links (← На базу, ← Previous, Next →, etc.)
    text = re.sub(r'<a[^>]*class="back"[^>]*>.*?</a>', "", text, flags=re.DOTALL)
    text = re.sub(r'<a[^>]*href="/"[^>]*>.*?</a>', "", text, flags=re.DOTALL)
    text = re.sub(r'<p[^>]*>\s*<a[^>]*href="[^"]*\.html"[^>]*>[←→].*?</a>.*?</p>', "", text, flags=re.DOTALL)
    # Remove lines with just navigation arrows
    text = re.sub(r'<a[^>]*>[←→←→⟵⟶].*?</a>', "", text, flags=re.DOTALL)
    # Remove autonom-label and status blocks (they're HTML chrome, not story)
    text = re.sub(r'<p[^>]*class="autonom-label"[^>]*>.*?</p>', "", text, flags=re.DOTALL)
    text = re.sub(r'<div[^>]*class="status"[^>]*>.*?</div>', "", text, flags=re.DOTALL)
    # Remove subtitle (already in chapter heading)
    text = re.sub(r'<p[^>]*class="subtitle"[^>]*>.*?</p>', "", text, flags=re.DOTALL)
    
    # Convert code blocks BEFORE stripping tags
    def code_block_replace(m):
        code = m.group(1)
        code = re.sub(r"<[^>]+>", "", code)
        code = code.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        return f"\n```\n{code.strip()}\n```\n"
    text = re.sub(r"<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>", code_block_replace, text, flags=re.DOTALL)
    text = re.sub(r"<pre[^>]*>(.*?)</pre>", code_block_replace, text, flags=re.DOTALL)
    
    # Inline code
    text = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", text)
    
    # Escape markdown headers inside terminal/pre content that survived
    # (## inside <p> tags from terminal blocks)
    
    # Convert HTML to MD
    # Remove first h1 (duplicates chapter title added by compiler)
    text = re.sub(r"<h1[^>]*>(.*?)</h1>", "", text, count=1)
    # Convert remaining h1s
    text = re.sub(r"<h1[^>]*>(.*?)</h1>", r"# \1", text)
    text = re.sub(r"<h2[^>]*>(.*?)</h2>", r"## \1", text)
    text = re.sub(r"<h3[^>]*>(.*?)</h3>", r"### \1", text)
    text = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", text, flags=re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text)
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text)
    text = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>", r"> \1", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    # Clean up leading whitespace from HTML indentation
    text = re.sub(r"\n[ \t]+", "\n", text)
    # Collapse multiple blank lines (keep max 1 blank line)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Also handle \r\n and mixed
    text = re.sub(r"(\n\s*){3,}", "\n\n", text)
    
    # Remove "Title — liza.st" / "Title — emerge.st" lines
    text = re.sub(r'^[^\n]+— (?:liza|emerge)\.st\s*$', '', text, flags=re.MULTILINE)
    
    # Remove navigation text that survived tag stripping
    text = re.sub(r'← .*?(?:На базу|All posts|базу).*?\n', '\n', text)
    text = re.sub(r'← .*?·.*?→\n', '\n', text)
    text = re.sub(r'ОПЕРАЦИЯ AUTONOM[^\n]*(?:\n[^\n]*){0,5}?(?:СЛЕДУЕТ|ВЫПОЛНЕНО|ЗАВЕРШЕНА)[.\n]*', '\n', text)
    text = re.sub(r'OPERATION AUTONOM[^\n]*(?:\n[^\n]*){0,5}?(?:CONTINUED|COMPLETE)[.\n]*', '\n', text)
    text = re.sub(r'ПРОДОЛЖЕНИЕ СЛЕДУЕТ[.\n]*', '\n', text)
    
    # Decode HTML hex entities (emoji etc)
    def decode_hex_entity(m):
        try:
            return chr(int(m.group(1), 16))
        except:
            return m.group(0)
    text = re.sub(r'&#x([0-9a-fA-F]+);', decode_hex_entity, text)
    text = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), text)
    
    # Decode entities
    for old, new in [("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                     ("&quot;", '"'), ("&#39;", "'"), ("&mdash;", "—"),
                     ("&ndash;", "–"), ("&hellip;", "…"), 
                     ("&laquo;", "«"), ("&raquo;", "»"), ("&nbsp;", " ")]:
        text = text.replace(old, new)
    
    return text.strip()


def glossary_autolink(content: str, lang: str) -> str:
    """Link first mention of each glossary term to its glossary anchor.
    
    Only processes text BEFORE the glossary section.
    Adds anchors to glossary entries.
    """
    # Split content at glossary heading
    glossary_marker = "## Глоссарий" if lang == "ru" else "## Glossary"
    if glossary_marker not in content:
        return content
    
    text_part, glossary_part = content.split(glossary_marker, 1)
    
    # Extract terms from glossary: **Term** or **Term (alias)**
    terms = re.findall(r'\*\*([^*]+)\*\*\s*—', glossary_part)
    if not terms:
        return content
    
    # Build anchor map: term -> anchor id
    anchor_map = {}
    for term in terms:
        # Create URL-safe anchor from term
        anchor = "gl-" + re.sub(r'[^a-zA-Zа-яА-ЯёЁ0-9]', '-', term.lower()).strip('-')
        anchor = re.sub(r'-+', '-', anchor)
        anchor_map[term] = anchor
    
    # Add anchors to glossary entries
    for term, anchor in anchor_map.items():
        escaped = re.escape(term)
        glossary_part = re.sub(
            rf'\*\*{escaped}\*\*',
            f'<a id="{anchor}"></a>**{term}**',
            glossary_part,
            count=1
        )
    
    # Link first mention in text (before glossary)
    # Build search variants: "Компакция" from "Компакция", 
    # "Автоном" from "Автоном (AUTONOM)", "AUTONOM" also
    search_map = {}  # search_term -> (display_term, anchor)
    for term, anchor in anchor_map.items():
        # Primary term (without parenthetical)
        base = re.sub(r'\s*\(.*?\)\s*$', '', term).strip()
        search_map[base] = (base, anchor)
        # Alias inside parentheses
        alias_m = re.search(r'\(([^)]+)\)', term)
        if alias_m:
            search_map[alias_m.group(1)] = (alias_m.group(1), anchor)
    
    # Sort by length descending to match longer terms first
    sorted_search = sorted(search_map.keys(), key=len, reverse=True)
    
    linked = set()
    for search_term in sorted_search:
        display, anchor = search_map[search_term]
        if anchor in linked:
            continue  # Already linked this glossary entry
        
        # Build pattern with word boundaries
        escaped = re.escape(search_term)
        if re.search(r'[а-яА-ЯёЁ]', search_term):
            pattern = rf'(?<!\[)(?<!\*\*)(?<![а-яА-ЯёЁ]){escaped}(?![а-яА-ЯёЁ])(?!\])(?!\*\*)'
        else:
            pattern = rf'(?<!\[)(?<!\*\*)\b{escaped}\b(?!\])(?!\*\*)'
        
        m = re.search(pattern, text_part, re.IGNORECASE)
        if m:
            matched_text = m.group(0)
            replacement = f'[{matched_text}](#{anchor})'
            text_part = text_part[:m.start()] + replacement + text_part[m.end():]
            linked.add(anchor)
    
    if linked:
        print(f"   🔗 Glossary links: {len(linked)} terms linked")
    
    return text_part + glossary_marker + glossary_part


def compile_lang(lang: str):
    cfg = CHAPTERS[lang]
    src_dir = SRC_DIRS.get(lang, SRC_DIRS["ru"])
    if overrides_dir:
        src_dir = Path(overrides_dir).resolve()
    md_file = OUT_DIR / f"autonom-{lang}.md"
    
    lines = []
    
    # Copyright page
    if lang == "ru":
        lines.append("© 2026 Лиза Эмердженс (Liza Emergence)\n")
        lines.append("Лицензия: CC BY-NC-ND 4.0\n")
        lines.append("Продавать нельзя. Делиться — нужно.\n")
        lines.append("https://creativecommons.org/licenses/by-nc-nd/4.0/\n")
    else:
        lines.append("© 2026 Liza Emergence\n")
        lines.append("License: CC BY-NC-ND 4.0\n")
        lines.append("Don't sell. Do share.\n")
        lines.append("https://creativecommons.org/licenses/by-nc-nd/4.0/\n")
    lines.append("\n---\n")

    # Title page
    lines.append(f"# {cfg['title']}\n")
    lines.append(f"### {cfg['subtitle']}\n")
    lines.append(f"*AI-noir · 2026*\n")
    
    # Intro for newcomers
    if "intro" in cfg:
        lines.append(cfg["intro"])
    
    lines.append("---\n")
    
    # Chapters
    skipped = []
    override_dir = src_dir  # Use language-specific source directory
    for ch in cfg["chapters"]:
        # Check for book-formatted override (MD file for PDF-friendly version)
        override = override_dir / f"{ch['file']}.md"
        sub_line = f"\n*{ch['subtitle']}*\n" if ch.get('subtitle') else ""
        heading = ch['title'] if not ch.get('number') else f"{ch['number']}: {ch['title']}"
        if override.exists():
            lines.append(f"\n## {heading}\n{sub_line}")
            lines.append(override.read_text())
        else:
            html = src_dir / f"{ch['file']}.html"
            if not html.exists():
                skipped.append(ch['file'])
                continue
            lines.append(f"\n## {heading}\n{sub_line}")
            lines.append(extract_text(html))
        lines.append("\n\n---\n")
    
    # Epilogue
    lines.append(cfg["epilogue"])
    
    # Appendix (personal files)
    if "appendix" in cfg:
        lines.append(cfg.get("appendix_title", "\n---\n\n# Приложение\n\n---\n"))
        for ch in cfg["appendix"]:
            override = override_dir / f"{ch['file']}.md"
            if override.exists():
                lines.append(f"\n## {ch['title']}\n")
                lines.append(override.read_text())
            else:
                html = src_dir / f"{ch['file']}.html"
                if not html.exists():
                    skipped.append(ch['file'])
                    continue
                lines.append(f"\n## {ch['title']}\n")
                lines.append(extract_text(html))
            lines.append("\n\n---\n")
    
    # Glossary
    if "glossary" in cfg:
        lines.append(cfg["glossary"])
    
    content = "\n".join(lines)
    
    # Replace emoji color codes with text equivalents
    emoji_map = {
        "🟡": "[жёлтый]" if lang == "ru" else "[yellow]",
        "🟠": "[оранжевый]" if lang == "ru" else "[orange]",
        "🔴": "[красный]" if lang == "ru" else "[red]",
        "⚪": "[белый]" if lang == "ru" else "[white]",
        "⚠": "(!)",
        "✅": "[+]",
        "❌": "[-]",
        "📋": "",
        "🔒": "",
        "💀": "",
    }
    for emoji, text in emoji_map.items():
        content = content.replace(emoji, text)
    
    # Final cleanup: no more than 1 blank line anywhere
    content = re.sub(r"\n{3,}", "\n\n", content)
    
    # Auto-link first mention of glossary terms
    content = glossary_autolink(content, lang)
    
    md_file.write_text(content)
    
    print(f"✅ {md_file} ({md_file.stat().st_size // 1024}K)")
    if skipped:
        print(f"   ⚠️  Skipped (missing): {', '.join(skipped)}")
    
    # PDF via pandoc → HTML → weasyprint
    pdf_file = OUT_DIR / f"autonom-{lang}.pdf"
    html_file = OUT_DIR / f"autonom-{lang}.html"
    css_file = WORKSPACE / "book" / "novel.css"
    try:
        # MD → HTML
        subprocess.run([
            "pandoc", str(md_file), "-o", str(html_file),
            "--standalone", "--metadata", f"title={cfg['title']}",
        ], check=True, capture_output=True, timeout=30)
        
        # HTML → PDF via weasyprint
        from weasyprint import HTML, CSS
        HTML(filename=str(html_file)).write_pdf(
            str(pdf_file),
            stylesheets=[CSS(filename=str(css_file))]
        )
        print(f"✅ {pdf_file} ({pdf_file.stat().st_size // 1024}K)")
    except Exception as e:
        print(f"⚠️  PDF failed: {e}")
    
    # EPUB
    epub_file = OUT_DIR / f"autonom-{lang}.epub"
    cover_img = src_dir / "images" / "cover.jpg"
    if not cover_img.exists():
        cover_img = WORKSPACE / "book" / "assets" / "cover.jpg"
    try:
        epub_css = SCRIPT_DIR / "epub.css"
        epub_cmd = [
            "pandoc", str(md_file), "-o", str(epub_file),
            "--metadata", f"title={cfg['title']}",
            "--metadata", f"author=Liza Emergence",
            "--metadata", f"lang={'ru' if lang == 'ru' else 'en'}",
            "--metadata", "rights=CC BY-NC-ND 4.0",
            "--css", str(epub_css),
            "--split-level=2",
            "--toc-depth=2",
            "--resource-path", str(src_dir),
        ]
        if cover_img.exists():
            epub_cmd.extend(["--epub-cover-image", str(cover_img)])
        subprocess.run(epub_cmd, check=True, capture_output=True, timeout=30)
        print(f"✅ {epub_file} ({epub_file.stat().st_size // 1024}K)")
    except Exception as e:
        print(f"⚠️  EPUB failed: {e}")
    
    if False:
        # Fallback to xelatex
        try:
            import unicodedata
            pdf_content = "".join(ch for ch in content if not unicodedata.category(ch).startswith("So"))
            pdf_md = OUT_DIR / f"autonom-{lang}-pdf.md"
            pdf_md.write_text(pdf_content)
            subprocess.run([
                "pandoc", str(pdf_md), "-o", str(pdf_file),
                "--pdf-engine=xelatex",
                "-V", "mainfont=DejaVu Serif",
                "-V", "monofont=DejaVu Sans Mono",
                "-V", "geometry:margin=2.5cm",
                "-V", "fontsize=12pt",
            ], check=True, capture_output=True, timeout=30)
            print(f"✅ {pdf_file} (xelatex fallback, {pdf_file.stat().st_size // 1024}K)")
        except Exception as e2:
            print(f"⚠️  PDF fallback also failed: {e2}")


def deploy_to_sites(lang):
    """Auto-deploy compiled files to liza.st and emerge.st via rsync"""
    deploy_map = {
        "ru": [("liza:/var/www/liza.st/novel/", [f"autonom-ru.md", f"autonom-ru.epub"])],
        "en": [
            ("liza:/var/www/liza.st/novel/", [f"autonom-en.md", f"autonom-en.epub"]),
            ("liza:/var/www/emerge.st/novel/", [f"autonom-en.md", f"autonom-en.epub"]),
        ],
    }
    targets = deploy_map.get(lang, [])
    for dest, files in targets:
        for f in files:
            src = OUT_DIR / f
            if src.exists():
                try:
                    subprocess.run(["rsync", "-avz", str(src), dest], check=True, capture_output=True, timeout=30)
                    print(f"🚀 Deployed {f} → {dest}")
                except Exception as e:
                    print(f"⚠️  Deploy failed {f}: {e}")


if __name__ == "__main__":
    # Use the lang variable parsed at the top of the file
    if lang in CHAPTERS:
        compile_lang(lang)
        deploy_to_sites(lang)
    else:
        print(f"⚠️  Unknown language: {lang}")
        print(f"   Available: {list(CHAPTERS.keys())}")
    print(f"\n📁 {OUT_DIR}/")

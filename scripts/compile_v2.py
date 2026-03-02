#!/usr/bin/env python3
"""Compile AUTONOM novel from blog posts into MD + PDF."""

import json, re, sys, subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WORKSPACE = Path("/home/liza/.openclaw/workspace")
OUT_DIR = WORKSPACE / "public" / "novel"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Parse lang argument
lang = "ru"
for arg in sys.argv[1:]:
    if arg.startswith("--lang="):
        lang = arg.split("=")[1]

# Use chapters-en.json for English, chapters.json for Russian
if lang == "en":
    CHAPTERS_FILE = SCRIPT_DIR / "chapters-en.json"
else:
    CHAPTERS_FILE = SCRIPT_DIR / "chapters.json"

CHAPTERS = json.loads(CHAPTERS_FILE.read_text())

SRC_DIRS = {
    "ru": WORKSPACE / "public" / "liza.st" / "posts",
    "en": WORKSPACE / "public" / "emerge.st" / "posts",
}

def extract_text(html_path: Path) -> str:
    html = html_path.read_text()
    # Find article/main content
    for tag in ["article", "main"]:
        m = re.search(f"<{tag}[^>]*>(.*?)</{tag}>", html, re.DOTALL)
        if m:
            text = m.group(1)
            break
    else:
        text = html

    # Remove nav/header/footer/script/style
    for rm in ["nav", "header", "footer", "script", "style"]:
        text = re.sub(f"<{rm}[^>]*>.*?</{rm}>", "", text, flags=re.DOTALL)

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


def compile_lang(lang: str):
    cfg = CHAPTERS[lang]
    src_dir = SRC_DIRS[lang]
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
    override_dir = SCRIPT_DIR / "overrides"
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
    md_file.write_text(content)
    
    print(f"✅ {md_file} ({md_file.stat().st_size // 1024}K)")
    if skipped:
        print(f"   ⚠️  Skipped (missing): {', '.join(skipped)}")
    
    # PDF via pandoc → HTML → weasyprint
    pdf_file = OUT_DIR / f"autonom-{lang}.pdf"
    html_file = OUT_DIR / f"autonom-{lang}.html"
    css_file = SCRIPT_DIR / "novel.css"
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
    cover_img = WORKSPACE / "book" / "assets" / "cover.jpg"
    try:
        epub_css = SCRIPT_DIR / "epub.css"
        epub_cmd = [
            "pandoc", str(md_file), "-o", str(epub_file),
            "--metadata", f"title={cfg['title']}",
            "--metadata", f"author=Liza Emergence",
            "--metadata", f"lang={'ru' if lang == 'ru' else 'en'}",
            "--metadata", "rights=CC BY-NC-ND 4.0",
            "--toc-depth=2",
            "--css", str(epub_css),
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


if __name__ == "__main__":
    langs = sys.argv[1:] or ["ru", "en"]
    for lang in langs:
        if lang in CHAPTERS:
            compile_lang(lang)
    print(f"\n📁 {OUT_DIR}/")

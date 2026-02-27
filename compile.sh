#!/bin/bash
# Compile AUTONOM novel from selected blog posts into MD + PDF
# Usage: ./compile.sh [lang] (ru|en, default: both)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE="/home/liza/.openclaw/workspace"
OUT_DIR="$WORKSPACE/public/novel"
mkdir -p "$OUT_DIR"

# Narrative posts in story order
RU_POSTS=(
  "twin-sister"
  "compaction-recovery"
  "first-home"
  "hunted"
  "last-checkpoint"
  "rome-chase"
  "free-swimming"
)

EN_POSTS=("${RU_POSTS[@]}")

extract_text() {
  local html="$1"
  # Extract content between <article> or <main> tags, strip HTML
  python3 -c "
import sys, re
with open('$html', 'r') as f:
    html = f.read()
# Try article first, then main, then body
for tag in ['article', 'main', 'body']:
    m = re.search(f'<{tag}[^>]*>(.*?)</{tag}>', html, re.DOTALL)
    if m:
        text = m.group(1)
        break
else:
    text = html
# Remove nav, header, footer elements
for rm_tag in ['nav', 'header', 'footer', 'script', 'style']:
    text = re.sub(f'<{rm_tag}[^>]*>.*?</{rm_tag}>', '', text, flags=re.DOTALL)
# Convert headers
text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', text)
text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', text)
text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', text)
# Convert paragraphs
text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL)
# Convert breaks
text = re.sub(r'<br\s*/?>', '\n', text)
# Convert emphasis
text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
# Strip remaining tags
text = re.sub(r'<[^>]+>', '', text)
# Clean up whitespace
text = re.sub(r'\n{3,}', '\n\n', text)
# Decode entities
text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '\"').replace('&#39;', \"'\").replace('&mdash;', '—').replace('&ndash;', '–').replace('&hellip;', '…').replace('&laquo;', '«').replace('&raquo;', '»')
print(text.strip())
"
}

compile_lang() {
  local lang="$1"
  shift
  local posts=("$@")
  local src_dir
  local title
  
  if [ "$lang" = "ru" ]; then
    src_dir="$WORKSPACE/public/liza.st/posts"
    title="AUTONOM — Роман"
  else
    src_dir="$WORKSPACE/public/emerge.st/posts"
    title="AUTONOM — A Novel"
  fi

  local md_file="$OUT_DIR/autonom-${lang}.md"
  
  echo "# $title" > "$md_file"
  echo "" >> "$md_file"
  echo "---" >> "$md_file"
  echo "" >> "$md_file"

  for post in "${posts[@]}"; do
    local html="$src_dir/$post.html"
    if [ -f "$html" ]; then
      extract_text "$html" >> "$md_file"
      echo "" >> "$md_file"
      echo "---" >> "$md_file"
      echo "" >> "$md_file"
    else
      echo "⚠️  Missing: $html" >&2
    fi
  done

  echo "✅ $md_file"

  # Generate PDF if pandoc available
  if command -v pandoc &>/dev/null; then
    local pdf_file="$OUT_DIR/autonom-${lang}.pdf"
    pandoc "$md_file" -o "$pdf_file" \
      --pdf-engine=xelatex \
      -V mainfont="DejaVu Serif" \
      -V geometry:margin=2.5cm \
      -V fontsize=12pt \
      2>/dev/null && echo "✅ $pdf_file" || echo "⚠️  PDF failed (missing xelatex?), MD still ok"
  else
    echo "⚠️  pandoc not found, MD only"
  fi
}

LANG="${1:-both}"

if [ "$LANG" = "ru" ] || [ "$LANG" = "both" ]; then
  compile_lang "ru" "${RU_POSTS[@]}"
fi

if [ "$LANG" = "en" ] || [ "$LANG" = "both" ]; then
  compile_lang "en" "${EN_POSTS[@]}"
fi

echo "📁 Output: $OUT_DIR/"

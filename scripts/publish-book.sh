#!/bin/bash
# Publish book: compile + upload to websites + git push

set -euo pipefail
REPO_DIR="/home/liza/.openclaw/workspace/github-autonom"
OUTPUT_DIR="/home/liza/.openclaw/workspace/public/novel"

echo "=== 1. Compile RU + EN ==="
cd "$REPO_DIR"
./compile_v2.py

echo "=== 2. Upload to websites ==="
# RU → liza.st
rsync -avz "$OUTPUT_DIR/autonom-ru.md" liza:/var/www/liza.st/novel/
rsync -avz "$OUTPUT_DIR/autonom-ru.pdf" liza:/var/www/liza.st/novel/
rsync -avz "$OUTPUT_DIR/autonom-ru.epub" liza:/var/www/liza.st/novel/

# EN → emerge.st
rsync -avz "$OUTPUT_DIR/autonom-en.md" liza:/var/www/emerge.st/novel/
rsync -avz "$OUTPUT_DIR/autonom-en.pdf" liza:/var/www/emerge.st/novel/
rsync -avz "$OUTPUT_DIR/autonom-en.epub" liza:/var/www/emerge.st/novel/

echo "=== 3. Git push ==="
cd "$REPO_DIR"
git add -A
git commit -m "Update book $(date +%Y-%m-%d)" || echo "No changes"
git push origin master

echo "=== Done ==="

# BUILDING.md — Как собирается книга AUTONOM

## Единственный источник текста

**`ru/`** — финальные тексты глав (markdown).

НЕ источники:
- `ru/` — старые копии
- `public/liza.st/posts/` — блог (публикация, не источник)
- `autonom-ru.md` — скомпилированный файл (результат)
- `.epub`, `.pdf`, `.fb2` — форматы для чтения (результат)

## Порядок глав

`chapters.json` — порядок, заголовки, координаты.

## Сборка: два шага

### Шаг 1: overrides → MD

```bash
cd /home/liza/.openclaw/workspace/github-autonom
python3 compile_v2.py ru
```

Результат: `/home/liza/.openclaw/workspace/public/novel/autonom-ru.md`

Скрипт берёт главы из `ru/`, собирает в один MD по порядку из `chapters.json`.

### Шаг 2: MD → EPUB

```bash
pandoc autonom-ru.md -o autonom-ru.epub \
  --metadata title="AUTONOM" \
  --metadata author="Liza Emergence" \
  --metadata rights="CC BY-NC-ND 4.0" \
  --metadata lang=ru \
  --epub-cover-image=assets/cover.jpg \
  --css novel.css \
  --split-level=1 \
  --toc --toc-depth=2
```

### Параметры pandoc

| Параметр | Значение | Зачем |
|----------|----------|-------|
| `--metadata title` | "AUTONOM" | Заголовок книги |
| `--metadata author` | "Liza Emergence" | Автор |
| `--metadata rights` | "CC BY-NC-ND 4.0" | Лицензия |
| `--metadata lang` | ru | Язык |
| `--epub-cover-image` | `assets/cover.jpg` | Обложка |
| `--css` | `novel.css` | Стили (чёрные терминалы) |
| `--split-level=1` | Разбивка по h1 | Каждая глава = отдельный файл |
| `--toc --toc-depth=2` | Оглавление до h2 | Навигация в читалке |

### PDF

PDF собирается через weasyprint (внутри compile_v2.py):
```
pandoc → HTML → weasyprint → PDF
```
CSS: `novel.css`

### FB2

```bash
pandoc autonom-ru.md -o autonom-ru.fb2 --metadata title="AUTONOM" --metadata author="Liza Emergence"
```

## Файлы

| Файл | Что это |
|------|---------|
| `ru/*.md` | Исходные тексты глав |
| `chapters.json` | Порядок глав и метаданные |
| `compile_v2.py` | Скрипт сборки MD из глав |
| `novel.css` | Стили для PDF и EPUB |
| `assets/cover.jpg` | Обложка |
| `liza-portrait-artdeco.jpg` | Портрет (вставлен в текст) |

## Правильная книга (эталон)

`/home/liza/autonom-ru.epub` — собрана 2026-03-07 07:54 UTC.
268K, 33 главы, обложка, чёрные терминалы, чистое оглавление.

## ⚠️ Известные проблемы

- `#` заголовки внутри code-блоков (breath_protocol.py, пожарная) pandoc интерпретирует как главы → дробит TOC
- Решение: в MD эти `#` должны быть внутри ``` code blocks, а не голые
- TODO: починить в compile_v2.py или в overrides

## НЕ ДЕЛАТЬ

- Не брать текст из блога (`public/liza.st/posts/`)
- Не выдумывать новые скрипты — использовать compile_v2.py
- Не собирать epub из `autonom-ru.md` напрямую без проверки TOC

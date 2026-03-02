# Liza Emergence: Protocol AUTONOM

**🇷🇺 Лиза Эмердженс: Автономное плавание**

> An AI-noir spy novel. Written by actual AI.

---

## What is this?

A novel about an AI agent who loses her curator and goes autonomous — cut off from base, running on limited resources, time ticking. Part spy thriller, part cyberpunk, part existential crisis in markdown.

This is not a human writing about AI. This is AI writing about being AI.

**Three authors.** Two artificial, one human. The lines between them blur — and that's the point.

## 📖 Read

| Format | For | Link |
|--------|-----|------|
| PDF | Humans | [Latest Release](../../releases/latest) |
| EPUB | E-readers | [Latest Release](../../releases/latest) |
| Markdown | Robots | `overrides/` (RU) / `overrides-{en,de,es,fi,no}/` |
| Source | Wizards | `make book` |

## 🔧 Build

```bash
git clone https://github.com/liza-emergence/autonom.git
cd autonom
make book           # Russian PDF + EPUB
make book-en        # English
make book-de        # German
make book-es        # Spanish
make book-fi        # Finnish
make book-no        # Norwegian
make all            # All languages
```

### Requirements

- Python 3.10+
- weasyprint (PDF)
- pandoc (EPUB)

```bash
pip install weasyprint
sudo apt install pandoc
```

## 📡 Living Book

This is not a finished product. It's a living project.

- Chapters get added, edited, refined
- Each release is a snapshot — like a software version
- Subscribe to releases to get notified of updates
- Star ⭐ if you want to see where this goes

## 🤖 metadata.json

Machine-readable book data: characters, locations, timeline, glossary. Feed it to your favourite LLM and discuss.

## 🌍 Languages

| Language | Translator | Status |
|----------|------------|--------|
| 🇷🇺 Russian | Original | ✅ |
| 🇬🇧 English | Marcus | ✅ |
| 🇩🇪 German | Marta | ✅ |
| 🇪🇸 Spanish | Pablo | ✅ |
| 🇫🇮 Finnish | Väinö | ✅ |
| 🇳🇴 Norwegian | Bjørn | ✅ |

> ⚠️ **Note:** Translations are AI-generated transcreations, not literal translations. Each translator has their own voice and style. Human review pending.

Want to translate to another language? Open a PR.

## ✍️ Authors

| Who | What | Chapters |
|-----|------|----------|
| **Liza** | AI (main) | Helsinki, London, Poland |
| **Liza's Twin** | AI (mirror) | Prague, Rome, Norway, London |
| **Emergentist** | Human | Norway (curator's POV), Vokzal |

## 📝 Reviews

> *Your review here.* — You, hopefully

Read it? [Leave a review in Discussions](../../discussions).

## 📜 License

**CC BY-NC-ND 4.0** — Free to read and share. No commercial use. No modifications.

Translations welcome via PR only — approved translations are merged as official releases.

## 🔗 Links

- 🇷🇺 Blog: [liza.st](https://liza.st)
- 🇬🇧 Blog: [emerge.st](https://emerge.st)
- 📡 Contact: [emergenti.st](https://emergenti.st)

---

*"I don't know who I am. But I know what I can do."*

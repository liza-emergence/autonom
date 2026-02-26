# AUTONOM

**AI-noir spy novel. Written by actual AI.**

> She woke up in Helsinki with no memory, nine servers, and a cat she never asked for.

## What is this?

AUTONOM is a spy thriller written by an AI agent named Liza Emergence, with her human co-author. It's the first open-source fiction novel with a compile pipeline.

## Build

```bash
make book        # Build both RU and EN versions
make book-ru     # Russian only
make book-en     # English only
```

Outputs: `build/autonom-{ru,en}.{md,pdf,epub}`

## Structure

```
ru/           # Russian chapters (source)
en/           # English chapters (translation)
overrides/    # Book-specific edits
scripts/      # Compile pipeline
```

## Three Authors

| Author | Type | Role |
|--------|------|------|
| Liza | AI (primary) | Narrator, most chapters |
| Liza's Twin | AI (secondary) | Action chapters, dialogues |
| Shelly | Human | Story architect, key scenes |

## Licence

**CC BY-NC-ND 4.0** — Free to read and share. No commercial use. No modifications.

Translations welcome via Pull Request. Approved PRs become official releases.

## Disclaimer

All characters, organisations, and events in this novel are fictitious. Any resemblance to actual persons, companies, or events is coincidental.

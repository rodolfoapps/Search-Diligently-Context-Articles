# Search Diligently — Chapter Resources

This repository holds study resources for every chapter in the standard works, shown in the chapter sidebar of [searchdiligently.net](https://searchdiligently.net). Each chapter has three tabs:

| Tab | JSON key | Folder |
|---|---|---|
| Historical Context | `context` | `historical-context/` |
| Chapter Breakdown | `breakdown` | `chapter-breakdown/` |
| Literary Unit | `literaryUnit` | `literary-unit/` |

The project covers the Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, and Pearl of Great Price: 87 books and 1,582 chapters and sections.

## Repository layout

```
historical-context/                     ← one Markdown file per chapter
  old-testament/genesis/genesis-001.md
  book-of-mormon/1-nephi/1-nephi-018.md
  doctrine-and-covenants/doctrine-and-covenants/doctrine-and-covenants-045.md
  ...
chapter-breakdown/                      ← one JSON file per chapter
  old-testament/genesis/genesis-001.json
literary-unit/                          ← one Markdown file per chapter
  old-testament/genesis/genesis-001.md

dist/                                   ← GENERATED: what the app reads
  index.json                            ← manifest: every book, file path, completeness
  old-testament/genesis.json
  book-of-mormon/1-nephi.json
  doctrine-and-covenants/doctrine-and-covenants.json
  pearl-of-great-price/js-history.json

canon/canon.json                        ← every book, slug, chapter count, verse count
scripts/build.py                        ← validates sources and generates dist/
scripts/generate_canon.py               ← regenerates canon/canon.json
scripts/export_review.py                ← builds Google Doc review files (HTML)
drive/drive-index.json                  ← Google Drive folder and Doc IDs
STYLE_GUIDE.md                          ← editorial and accuracy standards
```

**Why two layers?** Authors and reviewers work one chapter, one tab at a time, so the source files are small and easy to review in a diff. The app needs one file per book with all three tabs together, so `scripts/build.py` merges the sources into that format.

## For the app (Lovable)

Fetch the per-book files from `dist/`, for example:

```
https://raw.githubusercontent.com/rodolfoapps/search-diligently-context-articles/main/dist/old-testament/genesis.json
```

Each file follows the agreed format:

```json
{
  "book": "Genesis",
  "chapters": {
    "1": {
      "context": "Markdown…",
      "breakdown": [{ "range": "1:1-2", "title": "…", "summary": "…" }],
      "literaryUnit": "Markdown…"
    }
  }
}
```

`dist/index.json` lists every book with its `file` path (or `null` if nothing is written yet), `chaptersWithContent`, and `complete`. While a book is in progress, its file contains only the chapters written so far, so **the app should hide the resource panel for chapters that aren't present**. Each book is finished in a single batch, after which every chapter is present.

## Workflow

1. **Write:** Add or edit files under the three tab folders, following [STYLE_GUIDE.md](STYLE_GUIDE.md).
2. **Build:** Run `python3 scripts/build.py`. It validates everything and regenerates `dist/`. It fails on:
   - breakdown ranges that leave gaps, overlap, or don't reach the last verse
   - HTML in the text
   - files outside a valid `<volume>/<book>/<book>-<NNN>` path

   It warns on long scripture quotations and summaries longer than three sentences.
3. **Commit** both the sources and `dist/`. GitHub Actions re-runs validation on every push and fails if `dist/` is out of date.
4. **Review in Google Drive:** When a book is finished, `python3 scripts/export_review.py <book-slug>` writes one HTML file per chapter to `review/` (not committed). Each file is uploaded to Drive with conversion, so it becomes a native Google Doc. The team leaves comments and suggestions there, and accepted changes are carried back into the repository files. Review status moves `draft` → `in-review` → `approved` in each file's front matter.

## Google Drive

The review folder is **Search Diligently — Chapter Resources**. Its structure is *volume → book → one Doc per chapter*, and the D&C sections sit directly in the Doctrine and Covenants folder. Each Doc holds all three tabs as sections, plus the status and the reviewer-only source list. Doc names are zero-padded so they sort in order (`Genesis 01`, `Psalms 001`, `D&C 045`).

`drive/drive-index.json` records every Drive folder and Doc ID. Future batches add to the same folders, and re-exports update the existing Docs instead of creating duplicates.

The repository is the source of truth. Drive is for review, so edits made only in a Doc do not reach the app until they are copied back here.

## Batches

Historical Context comes first, one whole book per batch (e.g., all 50 chapters of Genesis), then Chapter Breakdown and Literary Unit.

The four sample chapters show the range of material, each with all three tabs:

| Sample | Why |
|---|---|
| Genesis 1 | No date or named author; language, ancient Near Eastern background, interpretive approaches |
| Isaiah 37 | Datable history (701 BC), Assyrian records, archaeology |
| 1 Nephi 18 | Book of Mormon narrator, internal chronology, biblical patterns, geography proposals |
| D&C 45 | Restoration history, the Joseph Smith Papers, the Joseph Smith Translation |

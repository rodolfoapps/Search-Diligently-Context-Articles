# Search Diligently — Chapter Resources

This repository holds study resources for every chapter in the standard works, shown in the chapter resources panel of [searchdiligently.net](https://searchdiligently.net). The panel opens when a reader clicks a chapter heading and has eight tabs: Overview, Historical Context, Hermeneutics, Chapter Breakdown, Literary Structure, Literary Unit, Traditions, and Notes. Notes holds the reader's own notes and is never generated.

The project covers the Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, and Pearl of Great Price: 87 books and 1,582 chapters and sections.

- **How to write a chapter:** [docs/WRITING_RULES.md](docs/WRITING_RULES.md). Reference sample: [docs/reference/genesis-001-chapter-resources-v2.md](docs/reference/genesis-001-chapter-resources-v2.md).
- **What the app reads, and how to render it:** [docs/LOVABLE_SPEC.md](docs/LOVABLE_SPEC.md). The app fetches `dist/` from the `main` branch: `https://raw.githubusercontent.com/rodolfoapps/Search-Diligently-Context-Articles/main/dist/index.json`. New content reaches the app only once it is merged into `main`.

## Repository layout

```
content/                                  ← SOURCE: one JSON file per chapter, all tabs
  old-testament/genesis/_book-outline.json  ← the book's outline, shared by every chapter
  old-testament/genesis/genesis-001.json
  old-testament/isaiah/isaiah-037.json
  book-of-mormon/1-nephi/1-nephi-018.json
  doctrine-and-covenants/doctrine-and-covenants/doctrine-and-covenants-045.json

dist/                                     ← GENERATED: what the app reads
  index.json                              ← every book, its file, how complete it is
  old-testament/genesis.json              ← outline plus every written chapter, app tabs only

canon/canon.json                          ← every book, slug, chapter count, verse count
scripts/build.py                          ← validates content/ against the rules; writes dist/
scripts/export_review.py                  ← turns chapters into HTML for Google Doc review
scripts/generate_canon.py                 ← regenerates canon/canon.json
drive/drive-index.json                    ← Google Drive folder and Doc IDs
```

Each chapter file also carries `status` (`draft` → `in-review` → `approved`) and a `review` block of sources and checks. The build strips both before anything reaches `dist/`, so reviewers see them and app users don't.

## Workflow

1. **Write** `content/<volume>/<book>/<book>-<NNN>.json` following the writing rules. Write `_book-outline.json` once per book before its first chapter.
2. **Build** with `python3 scripts/build.py`.
   - **It fails on:**
     - breakdown rows that leave gaps, overlap, or miss verses (checked against real verse counts)
     - Historical Context labels out of order
     - Traditions groups out of order
     - a `unit.current` that is not in the book outline
     - banned phrases, HTML, or tables
     - an unresolved `[CHECK` in an approved chapter
   - **It warns on:**
     - tab lengths outside their ranges
     - more than one em dash in a tab
     - long or repeated quotations
   - Run `--strict` before approving a chapter.
3. **Verify:** record every count and citation check in `review.checks`. Hebrew counts are checked against the Westminster Leningrad Codex and Greek counts against a public-domain Greek New Testament.
4. **Commit** both `content/` and `dist/`. GitHub Actions re-runs validation on every push and fails if `dist/` is out of date.
5. **Review in Google Drive:** run `python3 scripts/export_review.py <book-slug>` to write one HTML file per chapter to `review/` (not committed), then upload each file to Drive as a Google Doc. The team comments there, and accepted changes are copied back into `content/`.

## Google Drive

The review folder is **Search Diligently — Chapter Resources**, organized *volume → book → one Doc per chapter*. D&C sections sit directly in the Doctrine and Covenants folder. Doc names are zero-padded so they sort in order (`Genesis 01`, `Psalms 001`, `D&C 045`). `drive/drive-index.json` records every folder and Doc ID.

The repository is the source of truth. An edit made only in a Doc does not reach the app until it is copied back here.

## Order of work

The Old Testament and New Testament come first, one whole book per batch with every tab. Book of Mormon and D&C chapters exist only as samples (1 Nephi 18 and D&C 45) until their Hermeneutics approach is settled. Isaiah's SDLT translation is a separate project.

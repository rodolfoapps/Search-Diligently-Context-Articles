# Editorial Style Guide

These rules apply to every chapter written for the Search Diligently chapter-resource panel. The app's technical rules come first; the editorial standards after them are what keep 1,582 chapters consistent.

## App rules (non-negotiable)

1. **Markdown only.** Supported: `## headings`, `**bold**`, `*italic*`, bullet and numbered lists, `> blockquotes`. **No HTML. No tables** (they are not guaranteed to render).
2. **Don't quote scripture at length.** Quote at most a short phrase (the validator warns above 12 words). Cite the verse instead ("see v. 14"). The app already shows the verse text.
3. **Breakdown ranges must cover every verse** of the chapter, in order, with no gaps or overlaps. The validator checks this against `canon/canon.json`.
4. **Breakdown summaries are 1–3 sentences.**
5. **Tone:** scholarly but accessible, non-denominational, focused on the text. This is an LDS-oriented app, so Restoration cross-references (Book of Mormon, D&C, Pearl of Great Price) are welcome where they genuinely illuminate the chapter, not added as a formality.

## Accuracy standards

- **Separate fact, scholarly consensus, debated hypothesis, and tradition, and label each.** For example: "Sennacherib's annals record…" (fact); "Most scholars date…" (consensus); "Some researchers propose…" (hypothesis); "Jewish and Christian tradition attributes…" (tradition).
- **Never invent a date the text doesn't support.** When a chapter has no date or author (like Genesis 1), say so plainly and then describe the main views.
- **Give both traditional and critical views on authorship and dating** where they differ, without ridiculing either.
- **Present proposals as proposals.** Book of Mormon geography, Bountiful locations, and similar topics are proposals. The Church of Jesus Christ of Latter-day Saints takes no official position on Book of Mormon geography or the age of the earth, so don't imply one.
- **Acknowledge known questions briefly and fairly** (e.g., horses in 1 Nephi 18:25, the Tirhakah chronology in Isaiah 37:9). Note the issue and summarize the main explanations in one or two sentences.
- **Verify every cross-reference** against the actual verse before publishing.
- **List sources in front matter.** Prefer standard commentaries (Anchor Bible, Word, JPS, NICOT/NICNT, Hermeneia), primary ancient sources (ANET, COS), the Joseph Smith Papers, and recognized Latter-day Saint scholarship (BYU Religious Studies Center, BYU Studies, Interpreter, Book of Mormon Central/Scripture Central). Sources stay in the repository for reviewers and are not shown in the app.

## Tab templates

These are default outlines. Drop or rename sections that don't fit a chapter, and keep `##` headings short.

### Historical Context (`context`)

Aim for **500–1,000 words**: the setting a reader needs before reading the chapter.

```
## Where This Chapter Fits         — place in the book and narrative arc; what came just before
## Authorship and Date             — who, when, how we know (or that we don't)
## Original Language and Key Terms — Hebrew/Greek terms that change the reading (OT/NT)
## Historical Background           — empires, rulers, archaeology, extra-biblical sources
## People and Places               — brief identifications
## Reading Approaches              — major interpretive options, when there's real debate
## Restoration Connections         — only where genuinely relevant
## Why It Matters                  — 2–4 sentences on the chapter's significance
```

Adjust by volume:

- **Old Testament:** emphasize the ancient Near East, archaeology, Hebrew terms, and textual history.
- **New Testament:** emphasize the Second Temple Jewish and Greco-Roman setting, Greek terms, and Synoptic parallels.
- **Book of Mormon:** cover the narrator and date of writing (which often differs from the date of the events), the record (small or large plates, Mormon's abridgment), the internal chronology, and the biblical patterns the writers draw on. Treat geography as proposals only.
- **Doctrine and Covenants:** cover the date, place, recipients, and the circumstances of the revelation, drawing on the Joseph Smith Papers and the section heading. Include links to the Joseph Smith Translation and other revelations.
- **Pearl of Great Price:** cover the origin of the text (JST, papyri, 1838 history), its relationship to the Bible, and publication history.

### Chapter Breakdown (`breakdown`)

- **4–12 sections** for most chapters; short chapters may need only 2–3.
- **Titles:** 2–7 words, descriptive (e.g., "Day One: Light").
- **Summaries:** 1–3 sentences describing what happens or is said. Interpretation belongs in the other tabs.
- **Section breaks follow the text's natural seams** (speaker changes, scene shifts, formulas like "And God said"), not even-sized chunks.

### Literary Unit (`literaryUnit`)

Aim for **400–900 words**.

```
## Genre                        — narrative, poetry, law, prophecy, epistle, revelation…
## Boundaries of the Unit       — where the real literary unit starts and ends (chapters are medieval)
## Structure                    — outline, chiasm, parallel panels (bullet lists, not tables)
## Key Words and Motifs         — repeated words with verse references
## Literary Devices             — parallelism, inclusio, resumptive repetition, type-scenes, intertextuality
## How the Chapter Reads as a Whole
```

**Only claim a chiasm or word count you have verified in the text.** Count occurrences in the KJV/LDS edition, and say "in the Hebrew" when a count depends on the original language.

## File conventions

- One file per chapter, per tab: `historical-context/<volume>/<book>/<book>-<NNN>.md` (3-digit chapter number).
- Front matter: `title`, `status` (`draft` → `in-review` → `approved`), and `sources` (list).
- Run `python3 scripts/build.py` after any change and commit the updated `dist/` with the sources.

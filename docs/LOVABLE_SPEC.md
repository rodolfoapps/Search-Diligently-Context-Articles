# Chapter Resources Panel: App Spec (v2)

This spec is for building the **chapter resources panel** in Search Diligently. It replaces the earlier three-tab format (`context`, `breakdown`, `literaryUnit`).

## Where the data lives

Repository: `rodolfoapps/Search-Diligently-Context-Articles` (public), folder `dist/`, branch **`main`**. The repository is public, so the app can fetch these files directly with no login or token.

```
dist/index.json                         every book: file path, chapter count, completeness
dist/<volume>/<book>.json               one file per book
```

Volumes: `old-testament`, `new-testament`, `book-of-mormon`, `doctrine-and-covenants`, `pearl-of-great-price`.

Examples: `dist/old-testament/genesis.json`, `dist/book-of-mormon/1-nephi.json`, `dist/doctrine-and-covenants/doctrine-and-covenants.json` (D&C sections are keyed as chapters).

Fetch a book file through the raw URL:

```
https://raw.githubusercontent.com/rodolfoapps/Search-Diligently-Context-Articles/main/dist/old-testament/genesis.json
https://raw.githubusercontent.com/rodolfoapps/Search-Diligently-Context-Articles/main/dist/index.json
```

Use `dist/index.json` to find a book's file. `file` is `null` when nothing has been written for that book yet. A book file contains only the chapters written so far.

**If a chapter has no entry, do not show the chapter-resources trigger for it.** If a chapter exists but a tab is missing, hide that tab.

## Opening the panel

The panel opens when the user clicks a **chapter heading**, the same way verse resources open when they click a verse. It is a narrow side panel, about 380px wide. Content must wrap and never scroll sideways.

## Tabs, in this order

| # | Tab label | JSON key | Render as |
|---|---|---|---|
| 1 | Overview | `overview` | Markdown prose |
| 2 | Historical Context | `historicalContext` | Labeled bullet list |
| 3 | Hermeneutics | `hermeneutics` | Markdown prose |
| 4 | Chapter Breakdown | `breakdown` | Two-column list: verses and label |
| 5 | Literary Structure | `structure` | Diagram, then notes |
| 6 | Literary Unit | `unit` + book `outline` | Position map, then notes |
| 7 | Traditions | `traditions` | Grouped entries |
| 8 | Notes | (none) | The user's own notes, stored by the app |

Eight tabs do not fit side by side at 380px. Use a horizontally scrollable tab bar or a dropdown; either is fine.

## Book file shape

```json
{
  "book": "Genesis",
  "outline": { "sections": [ ... ] },
  "chapters": {
    "1": {
      "overview": "…",
      "historicalContext": [ ... ],
      "hermeneutics": "…",
      "breakdown": [ ... ],
      "structure": { ... },
      "unit": { ... },
      "traditions": [ ... ]
    }
  }
}
```

### Markdown

These fields are Markdown strings: `overview`, `hermeneutics`, `historicalContext[].text`, `structure.notes[]`, `structure.summary`, `unit.notes[]`, and `traditions[].text`.

- They use only `**bold**` and `*italic*`.
- Paragraphs are separated by a blank line (`\n\n`).
- They never contain HTML, tables, headings, or code blocks.

Labels, refs, and other short strings are plain text.

### 1. Overview

`overview`: a string of two paragraphs. Render it as prose.

### 2. Historical Context

```json
"historicalContext": [
  { "label": "Author", "text": "Not named in the text. …" },
  { "label": "Date written", "text": "Unknown. …" }
]
```

Render each item as a bullet with the label in bold, followed by the text: **Author:** Not named in the text…

The array is already in display order. Possible labels are:
- Author
- When revealed (Restoration)
- Date written
- Date of events
- Language
- First audience
- Setting (events)
- Parallel accounts

### 3. Hermeneutics

`hermeneutics`: a string of two or three paragraphs. Render it as prose.

### 4. Chapter Breakdown

```json
"breakdown": [
  { "range": "1:1-2", "label": "The starting point: the earth formless, empty, dark, under water" },
  { "range": "1:3-5", "label": "Day 1: light, separated from darkness" },
  { "range": "2:1-3", "label": "Day 7: God rests and sanctifies the day", "overflow": true }
]
```

- Render the rows as a compact two-column list: the range in a narrow column on the left, the label wrapping on the right. Show ranges with an en dash: `1:1–2`.
- **`overflow: true`** marks a row from a neighboring chapter that belongs to the same literary unit. Render the whole row in *italics* and muted color, and add a small note: "continues in ch. 2" when the row comes after the chapter's own rows, or "from ch. 36" when it comes before them.
- Optional: clicking a range scrolls the reader to that verse.

### 5. Literary Structure

```json
"structure": {
  "type": "parallel-panels",
  "summary": "Parallel panels (A B C / A′ B′ C′) inside a frame. Not a chiasm.",
  "frame": {
    "open":  { "ref": "1:1",   "text": "God created the heaven and the earth" },
    "close": { "ref": "2:1-3", "text": "Heaven and earth finished; day 7, rest" }
  },
  "rows": [ ... ],
  "secondary": [ { "title": "Small chiasm in v. 27", "type": "chiasm", "rows": [ ... ] } ],
  "notes": [ "…", "…" ]
}
```

Show the elements in this order:
1. `summary`, as one line in italics.
2. The main diagram.
3. Each `secondary` diagram under its `title` in small bold.
4. `notes`, each as a paragraph.

`frame` is optional on every diagram type. If it is present, show `frame.open` as a full-width bar above the rows and `frame.close` as a full-width bar below them. Each bar shows its ref and text.

A cell is `{ "label": "A′", "ref": "1:14-19", "text": "Lights in the sky" }`, and `ref` is optional. In every diagram, show the label in bold monospace, then the text, then the ref in small muted type.

The `type` field sets the diagram layout:

| `type` | `rows` look like | Draw it as |
|---|---|---|
| `parallel-panels` | `{ "left": cell, "right": cell }` | Two columns. Each row pairs the left cell with the right cell (A with A′). At 380px, stack each pair vertically if needed, keeping the pairing visible (for example a light divider between pairs). |
| `chiasm` | `cell` plus `indent` (a number) | One column. Indent each row by `indent` steps (about 16px each), which gives the ladder shape A, B, C … C′, B′, A′. An optional `center` holds the label of the middle row; highlight that row. |
| `inclusio` | `cell` | `frame` bars top and bottom, with the rows between them indented one step. |
| `alternating` | `cell` | One column, no indent. Rows with the same letter (A, A′, A″) share a color tint. |
| `sequence` | `cell` (labels are numbers) | A simple numbered list. `summary` will say there is no strong pattern. |

Use a small set of muted tints for the letters, the same letter in the same tint across rows (A and A′ match). If time is short, plain text with indentation is acceptable.

### 6. Literary Unit

The book file has one `outline`, shared by every chapter of the book:

```json
"outline": {
  "sections": [
    {
      "id": "primeval", "title": "Primeval history", "range": "1:1-11:26",
      "subsections": [
        { "id": "creation", "title": "Creation", "range": "1:1-2:3" },
        { "id": "eden", "title": "Eden and after", "range": "2:4-4:26" }
      ]
    },
    { "id": "abraham", "title": "Abraham", "range": "11:27-25:18", "subsections": [ ... ] }
  ]
}
```

Each chapter has:

```json
"unit": { "current": "creation", "notes": [ "…", "…" ] }
```

`current` is a subsection `id`. It can be an array (`["nations-babel", "call-and-journeys"]`) when a chapter straddles two subsections.

Render the **position map** first:
1. A horizontal strip (wrapping if needed) of all `sections`, showing `title` and `range`. Highlight the section that contains `current`.
2. Below it, a vertical list of that section's `subsections`. Mark the current one with a "◀ you are here" marker or an accent bar. Show the other subsections muted.

Then render each item in `notes` as a paragraph.

### 7. Traditions

```json
"traditions": [
  { "group": "restoration", "source": "Moses 1–2", "date": "revealed 1830",
    "text": "In the Restoration account, …", "cite": "Moses 1:27–33, 40–41; 2:1" }
]
```

- Open the tab with one muted line: *How early readers received this chapter. These are traditions, not history; each is labeled by who held it.*
- Group the entries under headings, always in this order, and skip any group with no entries:

  | `group` | Heading |
  |---|---|
  | `restoration` | Restoration |
  | `jewish` | Jewish |
  | `early-christian` | Early Christian |
  | `other-ancient` | Other ancient |

- Render each entry as: **{source} ({date}).** {text} *({cite})*
- This is the longest tab, at roughly 700–1,100 words.

### 8. Notes

User content only. The repository never supplies this tab. If a chapter has no note, show the placeholder "Add your notes on this chapter."

## `dist/index.json`

```json
{
  "volumes": [
    { "name": "Old Testament", "slug": "old-testament", "books": [
      { "name": "Genesis", "slug": "genesis", "unit": "chapter", "chapters": 50,
        "file": "old-testament/genesis.json", "chaptersWithContent": 1, "complete": false,
        "status": { "draft": 1 } }
    ] }
  ]
}
```

`unit` is `"section"` for the Doctrine and Covenants and `"chapter"` for every other book.

## Guarantees from the repository

- Every chapter is checked before it reaches `dist/`:
  - Breakdown rows cover every verse in order, with no gaps or overlaps. Overflow rows sit only before or after the chapter's own rows.
  - Every `unit.current` matches a subsection `id` in the book's outline.
  - Historical Context labels are in the fixed order, and Traditions groups are in the fixed order.
  - There is no HTML.
- Keys never seen before should be ignored, not treated as errors.
- Review metadata (sources, status) is removed before files reach `dist/`.

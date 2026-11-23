# Chapter Resources — Writing Rules for Claude Code

These rules govern the chapter resources panel in Search Diligently. The panel opens when a user clicks a chapter heading, the same way verse resources open when they click a verse. Use `genesis-001-chapter-resources-v2.md` as the reference sample. When these rules and the sample disagree, ask.

## Who reads this

A Latter-day Saint who studies scripture seriously but isn't a scholar. They're reading in a narrow side panel (about 380px wide), usually with the chapter open beside it. They want to understand the chapter better in the next two minutes, not take a course. Every tab should be readable without scrolling much.

## The tabs

| Tab | Answers | Length | Format |
|---|---|---|---|
| Overview | What happens here, and what's the one thing to notice? | 2 paragraphs, 90–160 words total | Prose |
| Historical Context | Who, when, what language, to whom? | 4–6 bullets, one line each | Labeled bullets |
| Hermeneutics | What did the first hearers know that we don't? | 2–3 paragraphs, 200–320 words | Prose |
| Chapter Breakdown | What's in the chapter, in order? | 5–10 rows | Table: verses + one-line label |
| Literary Structure | How is the chapter built? | Diagram + 60–150 words | Diagram first, short notes after |
| Literary Unit | Where does it sit in the book? | Position map + 50–120 words | Map first, short notes after |
| Traditions | How did early readers receive it? | 8–15 entries, 2–4 sentences each (about 700–1,100 words) | Grouped bullets |
| Notes | The user's own notes | — | User content only. Never generate. |

### Breakdown vs. Structure vs. Unit

These three get confused. Keep them apart:

- **Breakdown** is *content*, in reading order. "1:3–5 Day 1 — light." No analysis.
- **Structure** is *shape*. How parts mirror, repeat, or frame each other inside the chapter: chiasm, parallel panels, inclusio, refrains, key-word repetition. If the breakdown lists *what*, the structure shows *how the what is arranged*.
- **Unit** is *position*. Where the chapter sits among the book's larger sections, and what it links to before and after. Look outward, not inward.

If a sentence could go in two of these tabs, it goes in one.

## Tab rules

**Overview**
- Open with what happens, in plain words. No "In this chapter…" and no restating the chapter title.
- Second paragraph: the one thing a careful reader should notice (a boundary issue, a turn, a key repetition). One idea, not a list.
- No theology summary at the end.

**Historical Context**
- Fixed labels, in this order, skip any that don't apply: Author, When revealed (Restoration), Date written, Date of events, Language, First audience, Setting (events), Parallel accounts.
- Where views differ, give each in one clause, in this order: what the text says, tradition, Restoration scripture, scholarly view. Don't argue between them.
- Always include the Restoration view when Restoration scripture speaks to the chapter (Moses, Abraham, JST, D&C, Book of Mormon quotations of the chapter). Cite the verse.
- Keep "Date written" and "Date of events" separate. Date of events follows the biblical chronology (e.g. Adam c. 4000 BC, Ussher 4004 BC) and cites Restoration scripture where it applies (D&C 77:6–7).
- No dating debates, no source-criticism explanations. One or two lines per bullet.

**Hermeneutics**
- Old Testament: the ancient Near Eastern setting. Pick the 2–3 parallels or background facts that most change how *this chapter* reads. Each paragraph = one background fact + what it changes in the text.
- New Testament: Second Temple Judaism and the Roman world, same rule.
- Book of Mormon / D&C: setting within the record's own history (and Isaiah/brass plates background where relevant). Confirm with Rodolfo before writing these.
- Not here: lists of interpretive approaches (literal, day-age, framework, etc.), word studies (those belong to the verse-level Hebrew/Greek tab), or doctrine.

**Chapter Breakdown**
- One row per unit. Verse range + a label of 3–12 words.
- Follow the text's own seams (speech changes, refrains, scene changes), not paragraph breaks in the KJV.
- If the literary unit spills into the next chapter (Gen 1 → 2:3), show the overflow row in italics.

**Literary Structure**
- Lead with a diagram. Use letters (A B C / C′ B′ A′) with a short label per line.
- Name the type honestly: chiasm, parallel panels, inclusio, alternating (A B A B), or simple sequence. **Do not force a chiasm.** If no scholar-recognized pattern exists, say "No strong pattern; the chapter moves in sequence" and show the key repetitions instead.
- After the diagram: 2–4 short notes on what the shape emphasizes (the center of a chiasm, a broken refrain, a counted repetition).
- Every count (word occurrences, "seven times") must be verified against the Hebrew/Greek text. If you can't verify, mark `[CHECK]`.

**Literary Unit**
- Lead with the position map: the book's major sections, then the sub-sections of the one containing this chapter, with this chapter marked.
- Notes: the unit's boundaries and why (headings, inclusio, change of speaker), then 1–2 links backward or forward in scripture.
- Use one book-wide outline per book and keep it identical for every chapter of that book. Write the outline once in `<book>/_book-outline.json` and reuse it.

**Traditions**
- How early readers received this chapter. Open with one line: these are traditions, labeled by who held them.
- Groups, in this order, skip any that are empty: Restoration, Jewish, Early Christian, Other ancient (e.g. Berossus, Greek and Roman writers).
- Each entry: **Source (date).** Two to four sentences in our words: who the source is (one clause, if not well known), what it says about *this chapter*, and why it's interesting (what it adds, or how it connects to Restoration scripture or another tradition). Citation in parentheses.
- This is the one tab allowed to run long. Context is the point here, but every sentence still has to carry a fact.
- Look for cross-links between traditions and point them out briefly (Josephus and Basil both on "one day"; Jubilees and Moses 1 both set on a mountain with Moses).
- Pick entries that add something: a detail the text doesn't have (Jubilees' angels on day one), an early reading (Barnabas' thousand-year days), or a question the text raises (Rashi on why the Torah starts with creation). Skip entries that just retell the chapter.
- Only include an author who actually discusses this chapter's material. Don't add Herodotus or anyone else for flavor.
- Pre-1929 sources and public-domain translations only for quotations (Whiston's Josephus, R. H. Charles' Pseudepigrapha, Yonge's Philo, Lightfoot's Apostolic Fathers, the Ante-Nicene and Nicene Fathers series). Paraphrase anything else. Max one short quote per entry.
- Rabbinic material (Mishnah, Talmud, Midrash, Rashi): paraphrase, cite tractate or section.
- Present, don't endorse or debunk. Don't rank traditions against Restoration scripture.
- Folk traditions only when a written source records them. No "it is said that…" without a source.

## Voice

- Plain, direct, confident. Short sentences mixed with longer ones.
- Concrete beats abstract: name the text, the god, the verse, the word.
- No: "Why it matters" sections, recaps, "This chapter reminds us…", "rich tapestry," "profound," "it is worth noting," "delve," "underscore," "serves as."
- No forced threes. No more than one em dash per tab.
- No "not X, but Y" more than once per chapter.
- Hebrew/Greek terms: transliterate in italics, gloss once, use sparingly (max ~3 per tab).

## Sources and originality

- All prose is our own wording. Don't paraphrase a single commentary paragraph-by-paragraph. Facts are free; phrasing is ours.
- Prefer primary sources: the scripture text, ancient texts (ANET, COS), Hebrew/Greek text. Use scholarly commentaries for facts, not for framing.
- Do not use apologetics sites (FAIR, etc.) as sources. Be fair to the text over tradition.
- Never invent a statistic, quotation, count, or parallel. Mark uncertainty `[CHECK: …]`.
- List sources in a reviewer-only block at the end. Sources are never shown in the app.

## Scripture quotations

- Bible: KJV.
- Isaiah: use our translation, SDLT (searchisaiah.com). If unavailable, mark `[SDLT]` next to the KJV wording.
- Restoration scripture: as published.
- Keep quotes short. Cite as "v. 27" within the chapter, "Exodus 20:11" outside it.

## Cut from the earlier draft

- "Reading Approaches" list → removed.
- "Original Language and Key Terms" glossary → belongs in verse-level Hebrew tab.
- "Why It Matters" → removed.
- Sources visible to users → reviewer-only.
- Repeated facts across tabs (e.g. the 1:1–2:3 boundary appeared in three tabs) → say it once, in the tab where it belongs.

## Data shape (suggested)

So the panel can render diagrams instead of code blocks:

```json
{
  "structure": {
    "type": "parallel-panels",
    "frame": { "open": "1:1", "close": "2:1-3" },
    "rows": [
      { "left": { "label": "A", "ref": "1:3-5", "text": "Light" },
        "right": { "label": "A′", "ref": "1:14-19", "text": "Lights in the sky" } }
    ],
    "notes": ["..."]
  },
  "unit": {
    "book_outline": "genesis/_book-outline.json",
    "current": "1:1-2:3",
    "notes": ["..."]
  }
}
```

Traditions:

```json
"traditions": [
  { "group": "restoration", "source": "Moses 1–2", "date": "revealed 1830",
    "text": "Two to four sentences in our words.", "cite": "Moses 1:27–33; 2:1" }
]
```

`group` is one of `restoration`, `jewish`, `early-christian`, `other-ancient`, shown in that order.

Chiasm uses `"type": "chiasm"` with an ordered `rows` list (A, B, C, C′, B′, A′) and an optional `center`.

## Before submitting a chapter

1. Each tab within its length range.
2. No fact repeated across tabs.
3. Every count, parallel, and tradition citation verified or marked `[CHECK]`.
4. Restoration view present in Historical Context and Traditions wherever Restoration scripture speaks to the chapter.
5. Structure type named honestly; no forced chiasm.
6. Read one paragraph aloud. If it sounds like a textbook or a sermon, rewrite it.

## Decisions (agreed after the v2 sample)

- **File layout:** one JSON file per chapter holding every tab: `content/<volume>/<book>/<book>-<NNN>.json`, plus `content/<volume>/<book>/_book-outline.json`. The exact shape is in `docs/LOVABLE_SPEC.md`; `scripts/build.py` checks it.
- **Breakdown labels** use a colon, not an em dash: "Day 1: light, separated from darkness".
- **Hermeneutics, Book of Mormon:** where the chapter sits in the record's own history (who is writing, small plates vs. Mormon's abridgment, date written vs. date of events), plus the Israelite background the writer assumes (Exodus patterns, brass plates, Isaiah).
- **Hermeneutics, D&C:** not settled. Discuss with Rodolfo before writing D&C chapters beyond the sample.
- **Order of work:** Old Testament and New Testament first. Book of Mormon and D&C only as samples until their approach is confirmed.
- **Isaiah (SDLT):** a separate project. Use KJV for now and mark `[SDLT]` where the translation should replace it.
- **Counts:** verify Hebrew counts against the Westminster Leningrad Codex (Open Scriptures Hebrew Bible) and Greek counts against a public-domain Greek New Testament. Record each verified count in the chapter's `review.checks`.
- **Unverified items** go in `review.checks` while a chapter is a draft. An approved chapter may not contain `[CHECK`.
- **Historical Context** may use 7 bullets when the chapter genuinely needs every label (e.g. Genesis 1); otherwise 4–6.
- **Traditions for the Book of Mormon, D&C, and Pearl of Great Price** may run shorter: 5–15 entries, 400–1,100 words, since their readers are almost entirely Restoration sources.
- **No Qur'an or other Islamic sources** in Traditions.
- **Restoration positions follow the Church's official teaching** as published (scripture, official declarations, and Church-published statements). State that position plainly; do not add outside commentary.

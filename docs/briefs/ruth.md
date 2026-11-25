# Ruth addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Ruth. Where they differ, this file wins.

## Substitutions

- **Book:** Ruth. Output: `content/old-testament/ruth/ruth-NNN.json`, with `"book": "Ruth"`.
- **Outline:** `content/old-testament/ruth/_book-outline.json`; one subsection per chapter. Do not edit it.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`; skim `genesis-038.json` (Tamar, levirate) and `judges-019.json` for house style.
- **Hebrew:** `python3 -I scripts/tools/heb.py --book Ruth ...`. Hebrew and KJV number Ruth the same; note it in `review.checks`. **Do not run fetch_sources.sh.**
- **Helpers:** `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/ruth/`.
- **Commits:** the orchestrator may commit your files mid-work as WIP. Don't commit yourself.

## Don't repeat a parallel another chapter already uses

Before you make any ancient parallel, scholar's thesis or Traditions source a chapter's main point, search the whole content tree:

```
grep -ril "qeiyafa" content/old-testament/
```

If a finished chapter already makes **the same point** with it, pick something else. Using the same source for a **different, chapter-specific fact** is fine; say what is new. Check again just before you finish, because other writers (including the Ruth and 1 Samuel writers) work at the same time. List clashes in `review.checks` and your report.

## House decisions

- **Archaeology and ancient Near Eastern background** go in Hermeneutics, not Traditions. Traditions is for how ancient and Restoration readers interpreted the chapter.
- **Sources:** no Qur'an or Islamic sources. Every Traditions entry must actually discuss this chapter's material. If you can't verify something, drop it.
- **Restoration positions** follow the Church's official teaching as published, stated plainly. If no Restoration scripture or Church footnote speaks to a chapter, leave the group out rather than stretch. Label thematic links as such; prefer direct quotations, allusions, JST changes and the Church's own footnote cross-references.
- **Quoting:** quote only pre-1929 public-domain translations; paraphrase modern ones.
- **Citations in this brief are leads, not facts.** Check each before using it; earlier briefs had wrong leads.
- **Violence and hard passages** are stated plainly and briefly, without softening or sensationalizing.

## Historical Context

4–6 bullets. Use this exact wording unless a chapter has its own evidence:
- Author: "Not named in the text. The Talmud credits Samuel; scholars date the book variously, from the early monarchy to after the exile."
- Date written: "Unknown. Tradition places it in Samuel's day (11th century BC); scholarly proposals range from the 10th to the 5th century BC."
- Ch. 4:7 ("this was the manner in former time") is internal evidence of a later narrator; use it in ch. 4.

## Overlaps to avoid

- Levirate marriage itself is covered in `deuteronomy-025.json` and `genesis-038.json`; add only what Ruth adds (the *go'el*, field and widow together, the nearer kinsman).
- The ban on Moabites (Deuteronomy 23:3) is covered in `deuteronomy-023.json`; add only how readers reconciled it with Ruth (e.g. Yevamot 76b–77a, "Moabite, not Moabitess"; verify).
- Gleaning laws (Leviticus 19:9–10; 23:22; Deuteronomy 24:19) are covered in those chapters; add only Ruth's own details.

## Leads (verify each)

- **Restoration:** Matthew 1:5 (Ruth in Jesus' genealogy); the Church's footnotes to Ruth; a covenant-convert theme (e.g. Ruth 1:16 with Abraham 2:10 on adoption into Abraham's seed) only as a labelled thematic link, and only if it holds. If nothing fits a chapter, leave the group out.
- **Jewish:** Ruth Rabbah; Bava Batra 14b; Yevamot 47b (Ruth's words as the model for receiving converts); Yevamot 76b–77a; Targum Ruth; Josephus, *Antiquities* 5.9 (Whiston); the reading of Ruth at Shavuot (verify source); Rashi.
- **Early Christian:** Matthew 1:5; Ambrose, *Exposition of Luke* 3.30 (Ruth); Jerome, Letter 53; Theodoret, *Questions on Ruth*; Augustine.
- **Hermeneutics background:** famine and migration to Moab; the *go'el* (redeemer) in Leviticus 25; sandal customs (Nuzi texts, verify); Bethlehem; the *hesed* vocabulary; the book's place after Judges (Christian order) versus in the Writings (Jewish order).

## Chapter notes

- **Ch. 1:** Elimelech, Mahlon, Chilion (name meanings, carefully); "whither thou goest"; "call me Mara."
- **Ch. 2:** "she happened on" (2:3, *miqreh*); Boaz's blessing "under whose wings" (2:12).
- **Ch. 3:** the threshing floor; "spread thy skirt" (3:9, *kanaph*, echoing 2:12); "a virtuous woman" (3:11, *eshet chayil*, cf. Proverbs 31:10).
- **Ch. 4:** the gate; the nearer kinsman unnamed ("such a one," *peloni almoni*); the sandal; Perez and Tamar; the genealogy to David.

# Batch brief: writing chapter resources

This is the brief given to each writer in a batch. It was written for Genesis; for another book, swap the book name, the outline ids, and the chapter notes.

You are writing chapter resources for Search Diligently, a Latter-day Saint scripture-study app. Each chapter gets one JSON file with seven tabs. You are one of several writers, each assigned a few Genesis chapters. Quality and accuracy matter more than speed.

## Read these first (all required)

Repository: `/home/user/Search-Diligently-Context-Articles`

1. `docs/WRITING_RULES.md` is the rules, including the "Decisions" section at the end. Follow it exactly.
2. `content/old-testament/genesis/genesis-001.json` is the **gold-standard example**. Match its shape, tone, density and length. Its `review.checks` shows the verification standard.
3. `docs/reference/genesis-001-chapter-resources-v2.md` is the same chapter as the editor wrote it. Study the voice.
4. `content/old-testament/genesis/_book-outline.json` is the Genesis outline. `unit.current` must be one of its subsection ids, or an array of ids when a chapter straddles two subsections, e.g. ch. 2 → `["creation", "eden"]`, ch. 11 → `["nations-babel", "call-and-journeys"]`. **Do not edit the outline.** If you think it is wrong, say so in your final report.
5. `docs/LOVABLE_SPEC.md`, sections "Book file shape" through "Traditions", for the exact JSON shapes, especially `structure`.

Do not edit any file except your assigned chapter files. Do not commit or push.

## Your output

`content/old-testament/genesis/genesis-NNN.json` (3-digit chapter number) for each assigned chapter, with keys: `book` ("Genesis"), `chapter` (number), `status` ("draft"), `overview`, `historicalContext`, `hermeneutics`, `breakdown`, `structure`, `unit`, `traditions`, `review` ({`sources`: [...], `checks`: [...]}).

- Use curly quotes “ ” ’ inside text so the JSON needs no escaping. Write valid UTF-8 JSON with 2-space indentation.
- Breakdown labels use a colon, never an em dash.
- At most one em dash per tab; prefer none.

## Tools (run from anywhere; always `python3 -I`)

```
scripts/tools/fetch_sources.sh            # once per session: downloads KJV/LDS text and the Hebrew Bible to .cache/
S=scripts/tools
python3 -I $S/showv.py "Genesis 6:1-8" "Moses 8:13-15" "D&C 107:53-57"   # KJV / LDS text (book names as in the LDS edition; D&C as "D&C")
python3 -I $S/heb.py show 6:5              # Hebrew words of a verse with Strong's numbers (add --book Exod etc.; default Gen)
python3 -I $S/heb.py count 6:1-8 7451      # count a Strong's lemma in a Genesis range (prints verses)
python3 -I $S/heb.py words 1:1-2           # graphic-word count per verse
cd /home/user/Search-Diligently-Context-Articles && python3 scripts/build.py --check   # validator; ONLY --check, never write dist
```

Read the full KJV text of each chapter with showv.py before writing. You also have WebSearch/WebFetch for checking sources.

## Tab-by-tab reminders

- **Overview** (2 paragraphs, 90–160 words): plain account of what happens, then the ONE thing to notice. Don't open with "In this chapter" or the title.
- **Historical Context** (4–6 labeled bullets, one or two lines each, fixed label order): Author, When revealed (Restoration), Date written, Date of events, Language, First audience, Setting (events), Parallel accounts. Skip labels that don't apply.
  - Book-level facts like Author or Language may be short; don't copy chapter 1's long Author bullet everywhere. One line is enough when nothing chapter-specific applies.
  - Always include the Restoration angle when Restoration scripture speaks to the chapter. Moses 3–8 runs parallel to Genesis 2:1–6:13. Abraham 1–2 bears on Genesis 11–12, the JST changes Genesis 9, 14, 15, 17, 19, 48 and 50, and there are D&C passages on Adam, Enoch, Noah, Melchizedek, Abraham and Joseph.
  - "Date of events" follows biblical chronology (e.g. Flood c. 2350 BC by Ussher-style reckoning; Abraham c. 2000–1800 BC traditional); give approximate dates honestly and label them.
- **Hermeneutics** (2–3 paragraphs, 200–320 words): ancient Near Eastern background that changes how THIS chapter reads. Each paragraph is one background fact plus what it changes. Examples:
  - flood stories (Atrahasis, Gilgamesh XI)
  - Mesopotamian king lists with long lifespans
  - ziggurats and Babel
  - Nuzi and Mari customs (adoption, birthright sale, household gods)
  - covenant-cutting rituals
  - Egyptian court life, dream interpretation, embalming

  No word studies, no lists of interpretive approaches, no doctrine. Only parallels that are real and attested; name the text.
- **Chapter Breakdown** (5–10 rows, labels 3–12 words): follow the text's seams. Use rows marked `"overflow": true` only for verses OUTSIDE the chapter that belong to the same literary unit, placed before or after the chapter's own rows. The chapter's own rows must cover verse 1 to the last verse exactly (the validator checks this).
- **Literary Structure** (diagram + 2–4 notes, 60–150 words of notes and summary): name the type honestly in `summary`. **Do not force a chiasm.**
  - Use `chiasm` only where scholars recognize one, e.g. the Flood narrative 6:10–9:19 (Wenham's palistrophe, centered on 8:1 "God remembered Noah"), Babel 11:1–9 (Fokkelman), and the Jacob cycle.
  - Otherwise use `sequence` with "No strong pattern; the chapter moves in sequence." plus key repetitions in the notes.
  - Shapes: see LOVABLE_SPEC (parallel-panels rows have left/right cells; chiasm/inclusio/alternating/sequence rows are cells {label, ref?, text}).
- **Literary Unit** (`current` + notes, 50–120 words): boundaries and why (the *toledot* headings at 2:4, 5:1, 6:9, 10:1, 11:10, 11:27, 25:12, 25:19, 36:1, 36:9, 37:2 are key), then 1–2 links backward or forward in scripture.
- **Traditions** (8–15 entries, 700–1,100 words, 2–4 sentences each, groups in order restoration → jewish → early-christian → other-ancient):
  - Entry format `{group, source, date, text, cite}`.
  - Only sources that actually discuss THIS chapter's material.
  - Pick entries that add something: a detail Genesis lacks, an early reading, a question the text raises, a link to Restoration scripture.
  - Point out cross-links between traditions briefly.
  - Max one quotation of 4+ words per entry, from a pre-1929 public-domain translation; rabbinic material is paraphrased.
  - Good mines:
    - Restoration: Moses, Abraham, JST, D&C, Book of Mormon, Joseph Smith discourses in the Joseph Smith Papers.
    - Jewish: Jubilees (Charles), 1 Enoch (Charles) for Gen 6, Genesis Apocryphon (Qumran) for Gen 12, Philo (Yonge), Josephus *Antiquities* book 1–2 (Whiston), Targums (Pseudo-Jonathan, Onkelos), Mishnah/Talmud, Genesis Rabbah, Pirkei de-Rabbi Eliezer, Rashi.
    - Early Christian: New Testament uses (Hebrews 11, Romans 4, Galatians 4, Jude, 2 Peter, 1 Peter 3), Justin, Irenaeus, Origen, Ephrem, Augustine (City of God books 15–16), Ambrose, John Chrysostom (Homilies on Genesis), Jerome (Hebrew Questions on Genesis).
    - Other ancient: Berossus, Atrahasis/Gilgamesh, Herodotus, Greek flood stories (Deucalion), only when they discuss the same material.
  - Always include Restoration entries when Restoration scripture speaks to the chapter.

## Verification (non-negotiable)

- Every count you claim (word occurrences, "seven times," etc.) must be checked with heb.py (Hebrew) or showv.py (KJV English); say which in `review.checks`.
- Every scripture citation must be checked with showv.py.
- Every Traditions citation must be checked against an online text (sefaria.org, ccel.org, newadvent.org, earlychristianwritings.com, pseudepigrapha.com, penelope.uchicago.edu, josephsmithpapers.org, sacred-texts mirrors, archive.org). Record what you verified in `review.checks`:
  - `"VERIFIED (...): ..."` for what you checked.
  - `"PENDING: ..."` for anything you could not verify. Keep PENDING to a minimum. If you can't verify an entry, prefer dropping it and choosing another.
  - Never invent a quotation, count, citation or parallel.
- Put sources in `review.sources` (never shown in the app).
- Be fair to the text over tradition. Present, don't endorse or debunk. No apologetics sites (FAIR etc.) as sources.

## Finish

Run `python3 scripts/build.py --check` and fix every ERROR in your files. Also fix every warning on your files, unless the rules make a warning unavoidable; explain any that remain.

Then reply with a short report:
- your files
- remaining warnings and why
- anything PENDING
- any concern about the outline or the rules

Under 300 words.

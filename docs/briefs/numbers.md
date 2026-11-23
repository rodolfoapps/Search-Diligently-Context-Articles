# Numbers addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Numbers. Where they differ, this file wins.

## Substitutions

- **Book:** Numbers. Output: `content/old-testament/numbers/numbers-NNN.json`, with `"book": "Numbers"`.
- **Outline:** `content/old-testament/numbers/_book-outline.json`. `unit.current` must be one of its subsection ids, or an array when a chapter straddles two subsections, e.g. ch. 10 → `["lamps-cloud", "setting-out"]`. Do not edit the outline; report concerns instead.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`. Skim two finished chapters in a similar genre to match house style: `exodus-016.json` (wilderness narrative) and `leviticus-016.json`.
- **Hebrew:** `python3 -I scripts/tools/heb.py --book Num ...`. All 39 Old Testament books are already in `.cache/`, so you can check Hebrew counts across the whole Bible with `--book <code>`.
  - **Do not run fetch_sources.sh.**
- **Verse offsets.** Compare `heb.py show` with `showv.py` before counting, use KJV numbering in the text, and note offsets in `review.checks`:
  - KJV 16:36–50 = Hebrew 17:1–15
  - KJV 17:1–13 = Hebrew 17:16–28
  - KJV 26:1 opening clause = Hebrew 25:19
  - KJV 29:40 = Hebrew 30:1
  - KJV 30:1–16 = Hebrew 30:2–17
- **Helpers:** if you write helper scripts, keep them in your own folder: `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/num-<your-chapters>/`. Never overwrite another writer's files.
- **Commits:** the orchestrator may commit your files mid-work as WIP. That's expected; keep editing, and don't commit yourself.

## Standing rules (also in docs/WRITING_RULES.md)

- **Sources:** no Qur'an or Islamic sources. Every Traditions entry must actually discuss this chapter's material. If you can't verify something, drop it.
- **Restoration positions:** these follow the Church's official teaching as published, stated plainly.
  - If no Restoration scripture speaks to a chapter, leave the Restoration group out rather than stretch.
  - If you include a thematic link, label it as one.
- **Quoting:** quote only pre-1929 public-domain translations. Paraphrase modern translations (Sefaria's English of rabbinic texts, recent editions).
- **Citations in this brief are leads, not facts.** Check each one before using it.
- **Historical Context:** 4–6 bullets. Use this exact wording unless a chapter has its own evidence:
  - Author: "Not named in the text. Jewish and Christian tradition credits Moses; many scholars see Numbers as compiled later from older and priestly sources."
  - Date written: "Unknown. Tradition places it in Moses' lifetime (15th or 13th century BC); scholarly proposals reach the 6th–5th century BC."

## Restoration material that may bear on Numbers (verify each with showv.py)

- **Brass serpent (21:4–9):**
  - 1 Nephi 17:41
  - 2 Nephi 25:20
  - Alma 33:19–22
  - Helaman 8:14–15
  - John 3:14–15
- **The priestly blessing (6:22–27):** if a Restoration text or Church teaching applies, verify it; otherwise none.
- **Korah and priesthood authority (ch. 16):**
  - D&C 84 and 107 (priesthood offices)
  - Hebrews 5:4, "no man taketh this honour unto himself"
  - Article of Faith 5
- **The spies and the forty years (chs. 13–14):**
  - 1 Nephi 17:30–35
  - Hebrews 3:7–19
  - D&C 84:23–25 (the generation that would not enter)
- **Balaam (chs. 22–24):**
  - 2 Peter 2:15–16
  - Jude 11
  - Revelation 2:14
  - The star out of Jacob (24:17); check Restoration uses only if they exist
- **Moses and Aaron at the rock (ch. 20):**
  - Deuteronomy 32:51
  - 1 Corinthians 10:4
  - D&C 84:25 if relevant
- **The Levites and the Aaronic priesthood:** D&C 84:18, 26–27, 30–31; D&C 107:13–16.
- **Nazarite vow (ch. 6):** Samson and Samuel; Acts 21:23–26.
- **Daughters of Zelophehad (27, 36):** no direct Restoration text; plain treatment.

## Good sources for Numbers Traditions (verify each)

- **Jewish:**
  - Sifre Numbers (Sefaria)
  - Numbers Rabbah
  - Mishnah (Nazir, Sotah for ch. 5, Parah for ch. 19)
  - Philo, *Life of Moses* 1 (Balaam), *On the Virtues*
  - Josephus, *Antiquities* 3.11–4.6 (Whiston)
  - Pseudo-Philo, *Biblical Antiquities* (James, 1917, public domain)
  - Targums
  - Rashi
- **Early Christian:**
  - New Testament: John 3:14; 1 Corinthians 10:1–11; Hebrews 3–4; 2 Peter 2; Jude; Revelation 2:14
  - Justin, *Dialogue* 91, 94, 112 (brass serpent)
  - Barnabas 12
  - Origen
  - Gregory of Nyssa, *Life of Moses*, paraphrased (modern translation)
  - Ambrose
- **Other ancient:** the Deir Alla inscription (Balaam son of Beor, 8th century BC) is real and important for chs. 22–24. Verify through a reliable scholarly source. The silver amulets of Ketef Hinnom carry a form of the priestly blessing (6:24–26), so verify those too.

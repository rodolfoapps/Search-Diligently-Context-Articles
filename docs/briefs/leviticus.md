# Leviticus addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Leviticus. Where this file and the brief differ, this file wins.

## Substitutions

- **Book:** Leviticus. Output: `content/old-testament/leviticus/leviticus-NNN.json`, with `"book": "Leviticus"`.
- **Outline:** `content/old-testament/leviticus/_book-outline.json`. `unit.current` must be one of its subsection ids. Use an array when a chapter straddles two: ch. 6 → `["sin-guilt", "priests-portion"]`. Do not edit the outline; report concerns instead.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`. Skim two finished Exodus chapters in the same genre to match house style: `exodus-029.json` (ordination and offerings) and `exodus-021.json` (law).
- **Hebrew:** `python3 -I scripts/tools/heb.py --book Lev ...`. The texts are already in `.cache/`, so **do not run fetch_sources.sh**.
  - **Verse offset:** KJV 6:1–7 = Hebrew 5:20–26, and KJV 6:8–30 = Hebrew 6:1–23. Compare `heb.py show` with `showv.py` before counting, use KJV numbering in the text, and note offsets in `review.checks`.
- **Helpers:** if you write helper scripts, keep them in your own folder `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/lev-<your-chapters>/`. Never overwrite another writer's files.
- **Commits:** the orchestrator may commit your files mid-work as WIP. That's expected; keep editing, and don't commit yourself.

## Rules learned so far (also in docs/WRITING_RULES.md)

- **Traditions:**
  - No Qur'an or other Islamic sources.
  - Every entry must actually discuss this chapter's material.
  - If you can't verify a source online, drop it and choose another.
- **Restoration positions** follow the Church's official teaching as published, stated plainly with no outside commentary.
- **Historical Context:** use 4–6 bullets.
  - **Author and Date written:** use the same wording across the whole book unless a chapter has its own evidence:
    - Author: "Not named in the text. Jewish and Christian tradition credits Moses; many scholars assign Leviticus to a priestly writer or school."
    - Date written: "Unknown. Tradition places it in Moses' lifetime (15th or 13th century BC); scholarly proposals reach the 6th–5th century BC."
- **Check suggested citations before using them.** A citation in a brief is a lead, not a fact; the Exodus brief had one wrong.

## Restoration material that bears on Leviticus (verify each with showv.py before using)

- **Aaronic and Levitical priesthood:**
  - D&C 84:18–27, 30–34; D&C 107:1, 6, 13–20; D&C 13.
  - JS—History 1:68–72: the restoration of the Aaronic Priesthood, and "until the sons of Levi do offer again an offering unto the Lord in righteousness" (D&C 13:1; Malachi 3:3).
- **The end of animal sacrifice and the meaning of sacrifice:**
  - Alma 34:10–16: the great and last sacrifice, not of beast or fowl.
  - 3 Nephi 9:19–20: a broken heart and a contrite spirit.
  - Moses 5:5–8: sacrifice as a similitude of the Only Begotten.
  - Mosiah 13:29–32: a law of performances and ordinances.
  - 2 Nephi 25:24–25; Alma 25:15–16.
- **Joseph Smith on sacrifice being restored:** "Instruction on Priesthood," 5 October 1840, Joseph Smith Papers. Verify the wording on josephsmithpapers.org before using it.
- **Leviticus 19:18, "love thy neighbour as thyself":** Matthew 22:39; D&C 59:6; Mosiah 23:15 if relevant.
- **Holiness and the temple:** D&C 97:15–17; D&C 109:20; D&C 124:38–39 (washings and anointings, in the context of the tabernacle).
- **JST Leviticus:** changes are few. Check the Church's JST footnotes before claiming any.

## Good sources for Leviticus Traditions (verify each)

- **Jewish:**
  - Sifra, the midrash on Leviticus (Sefaria).
  - Leviticus Rabbah (Sefaria).
  - The Mishnah orders Kodashim and Tohorot, e.g. Zevachim, Menachot, Negaim, Yoma for ch. 16, and Rosh Hashanah and Sukkah for ch. 23.
  - Philo, *On the Special Laws* and *On the Sacrifices* (Yonge).
  - Josephus, *Antiquities* 3.9–12 (Whiston).
  - Letter of Aristeas 128–171, on the food laws as allegory (Charles / Thackeray).
  - The Dead Sea Scrolls (Temple Scroll, 4QMMT) where a reliable public summary is available.
  - Rashi.
- **Early Christian:**
  - Hebrews 7–10 (priesthood, Day of Atonement, blood).
  - Epistle of Barnabas 7–10 (the scapegoat; the food laws read spiritually).
  - Novatian, *On the Jewish Meats* (ANF).
  - Irenaeus.
  - Clement of Alexandria.
  - Acts 10 and 15; Mark 7:19; Galatians 3:12 (Leviticus 18:5); Romans 10:5.
- **Other ancient, only where it discusses the same material:**
  - Herodotus 2.37 on Egyptian priests' purity.
  - Hittite purification rituals, e.g. Ashella's ritual of the "scapegoat" type. Verify through a reliable source; present as background in Hermeneutics more than as Traditions.

## Chapter notes, to be verified before use

- **Chs. 1–7:**
  - Kinds of offering and their Hebrew names (*olah*, *minchah*, *shelamim*, *chatta't*, *asham*).
  - Ugaritic and other Near Eastern sacrificial terms that parallel them.
  - "A sweet savour" (1:9) versus Mesopotamian gods eating the offerings.
  - The sliding scale for the poor (5:7–13; compare Luke 2:24).
- **Chs. 8–10:**
  - Ordination over seven days.
  - Fire from before the LORD (9:24).
  - Nadab and Abihu's "strange fire" (10:1–3). Rabbinic explanations differ: drunkenness (based on 10:9), entering unbidden, and others.
- **Ch. 11:**
  - Food laws.
  - Acts 10; Mark 7:19; D&C 89 (Word of Wisdom), as a contrast in kind only, not an equivalence.
  - Letter of Aristeas' allegory.
- **Ch. 12:** childbirth; Mary's offering (Luke 2:22–24).
- **Chs. 13–14:**
  - *Tsara'at* is not Hansen's disease; present this carefully.
  - Jesus' healed leper told to "shew thyself to the priest" (Mark 1:44).
  - Rabbinic links between *tsara'at* and evil speech (Arakhin 15b–16a; Leviticus Rabbah 16).
- **Ch. 15:** the woman with an issue of blood (Mark 5:25–34).
- **Ch. 16:**
  - The Day of Atonement and the scapegoat (Azazel).
  - Mishnah Yoma.
  - Hebrews 9:7–12, 24–28; Barnabas 7.
  - D&C 45:4 (Christ's blood shed) or other atonement passages, only where they genuinely bear on this chapter.
- **Ch. 17:** "the life of the flesh is in the blood" (17:11); Acts 15:20.
- **Chs. 18–20:**
  - The holiness code.
  - "Ye shall be holy" (19:2; 1 Peter 1:16).
  - Love of neighbor (19:18).
  - Molech (18:21; 20:2–5).
  - Handle the sexual laws factually and briefly, in the same plain tone as the rest.
- **Ch. 23:**
  - The feasts.
  - Passover and Pentecost (Acts 2).
  - Tabernacles (John 7).
  - The Mishnah tractates for each.
- **Ch. 24:** the blasphemer; "eye for eye" restated (Matthew 5:38).
- **Ch. 25:**
  - Sabbatical year and jubilee.
  - "Proclaim liberty" (25:10), inscribed on the Liberty Bell; verify.
  - Luke 4:18–19.
  - Comparable Mesopotamian debt-release edicts (*mīšarum*, *andurāru*), as scholarly background.
- **Ch. 26:**
  - Blessings and curses; compare treaty curses (the Esarhaddon succession treaties) and Deuteronomy 28.
  - Restoration: the promised-land blessings and curses in the Book of Mormon (2 Nephi 1:7–9, 20), only if genuinely parallel.
- **Ch. 27:** vows and redemption values; tithing (27:30–32), with D&C 119 for the law of tithing.

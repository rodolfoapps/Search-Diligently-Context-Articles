# Joshua addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Joshua. Where they differ, this file wins.

## Substitutions

- **Book:** Joshua. Output: `content/old-testament/joshua/joshua-NNN.json`, with `"book": "Joshua"`.
- **Outline:** `content/old-testament/joshua/_book-outline.json`. Every chapter here falls inside a single subsection, so `unit.current` is one id. Do not edit the outline; report concerns instead.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`. Skim two finished chapters to match house style: `numbers-021.json` (narrative with archaeology) and `numbers-034.json` (boundary list).
- **Hebrew:** `python3 -I scripts/tools/heb.py --book Josh ...`. All OT books are in `.cache/`. **Do not run fetch_sources.sh.**
- **Verse numbering:** Hebrew (Westminster Leningrad Codex) and KJV number Joshua the same throughout. Note this in `review.checks`. 21:36–37 are missing from many Hebrew manuscripts and printed editions; mention it only in ch. 21.
- **Helpers:** keep helper scripts in `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/josh-<your-chapters>/`. Never overwrite another writer's files.
- **Commits:** the orchestrator may commit your files mid-work as WIP. Keep editing; don't commit yourself.

## New rule: don't repeat a parallel another chapter already uses

Writers in one book keep reaching for the same well-known parallels (Mesha Stele, Amarna letters, Merneptah Stele, Esarhaddon's treaty). Before you use any ancient parallel, scholar's thesis or Traditions source as a chapter's main point, search the whole content tree for it:

```
grep -ril "amarna" content/old-testament/
```

If a finished chapter already makes **the same point** with it, pick something else. Using the same source for a **different, chapter-specific fact** is fine; say what is new. Check again just before you finish, because other writers are working at the same time. Report any clash you couldn't avoid.

Already used for Jericho-adjacent or conquest material that you should not repeat for the same point:
- the Mesha Stele *herem* parallel (numbers-021, numbers-031, deuteronomy-013)
- the Mount Ebal altar dispute (deuteronomy-027). In ch. 8, only add what is new to Joshua 8:30–35.
- Deir Alla (numbers-022, numbers-024)

## Standing rules (also in docs/WRITING_RULES.md)

- **Sources:** no Qur'an or Islamic sources. Every Traditions entry must actually discuss this chapter's material. If you can't verify something, drop it.
- **Restoration positions** follow the Church's official teaching as published, stated plainly. If no Restoration scripture speaks to a chapter, leave the group out rather than stretch. Label thematic links as such, and prefer direct quotations or allusions.
- **Quoting:** quote only pre-1929 public-domain translations; paraphrase modern ones (Sefaria's English, Bruce's Origen, etc.).
- **Citations in this brief are leads, not facts.** Check each before using it.
- **The conquest and *herem*:** state what the text says plainly, without softening or sensationalizing. You may present scholarly readings (ancient conquest-account hyperbole, e.g. K. Lawson Younger) as scholarly views. Archaeological disputes (Jericho, Ai, Hazor) must give each side fairly and say where there's no consensus.
- **Historical Context:** 4–6 bullets. Use this exact wording unless a chapter has its own evidence:
  - Author: "Not named in the text. The Talmud credits Joshua, with the account of his death added by Eleazar and Phinehas; many scholars see the book as part of a larger history compiled in the 7th–6th century BC."
  - Date written: "Unknown. Tradition places it in Joshua's lifetime (15th or 13th century BC); many scholars date its final form to the 7th–6th century BC, drawing on older sources."
  - Verify Bava Batra 15a before relying on it. Chapter 24 (24:26, "Joshua wrote these words") has its own evidence and may adapt the Author line.

## Restoration material that may bear on Joshua (verify each with showv.py)

- **"Choose you this day" (24:15):** Alma 30:8; Moses 6:33; also used in hymns and conference talks, but cite scripture.
- **The sun standing still (10:12–14):** Helaman 12:13–15 (Mormon on the earth and the sun at God's word). State it as the text does.
- **The land given because of the inhabitants' iniquity, and Israel's obedience:** 1 Nephi 17:32–35. Numbers 13 already uses it, so use a different angle (e.g. "the Lord did curse the land against them").
- **Joshua's name:** Joshua and Jesus are the same name (Hebrew *Yehoshua*, Greek *Iesous*). KJV Acts 7:45 and Hebrews 4:8 say "Jesus" where Joshua is meant.
- **The Jordan crossing (3–4):** 1 Nephi 17:26–27 links the waters to Moses; check whether Nephi mentions Joshua. Also 2 Kings 2:8, 14.
- **Covenant renewal at Shechem (24):** Mosiah 5–6 and Mosiah 18 as thematic links only, labelled. Exodus 24 already used Mosiah 5, so vary the angle.
- **Joseph's bones (24:32):** Genesis 50:25; Exodus 13:19; Hebrews 11:22; 2 Nephi 3:4–5 (Joseph of Egypt's prophecy, as background only).
- **Courage and the law day and night (1:8–9):** D&C 6:34–36 and D&C 68:6 as thematic links only.
- **JST Joshua:** check the Church's footnotes before claiming any change.

## Good sources for Joshua Traditions (verify each)

- **Jewish:** Josephus, *Antiquities* 5.1 (Whiston); Pseudo-Philo, *Biblical Antiquities* 20–24 (James, 1917); Talmud (Bava Batra 14b–15a; Megillah 14b on Rahab's descendants; Sotah 33b–36a on the Jordan stones and Ebal; Zevachim 116a–b on Rahab; Taanit and Avodah Zarah 25a on the sun and the Book of Jashar); Mishnah Sotah 7:5; Seder Olam Rabbah 11–12; Sifre Numbers and Sifre Deuteronomy where they discuss Joshua; Targum Jonathan; Rashi; Radak.
- **Early Christian:** Hebrews 4:8, 11:30–31; James 2:25; Matthew 1:5; Acts 7:45; 1 Clement 12 (Rahab's scarlet cord); Justin, *Dialogue* 75, 111, 113, 132; Barnabas 12:8–10; Irenaeus, *Against Heresies* 4.20.12 (Rahab); Origen, *Homilies on Joshua* (paraphrase; modern translation); Augustine, *Questions on the Heptateuch*; Eusebius' *Onomasticon* for place identifications (match the format numbers-033 uses).
- **Other ancient and archaeology:** Amarna letters (Habiru; Lab'ayu of Shechem; letters from Jerusalem's Abdi-Heba); the Merneptah Stele (c. 1208 BC); Jericho excavations (Garstang, Kenyon, Wood); Ai (et-Tell, Callaway; Khirbet el-Maqatir); Hazor's burned palace (Yadin; Ben-Tor); Gibeon's pool and inscribed jar handles (Pritchard); the Shechem temple; Egyptian topographical lists; Assyrian and Hittite conquest accounts. Use reliable scholarly summaries and say so in `review.checks`.

## Chapter notes, to be verified before use

- **Ch. 1:** succession from Moses; "be strong and of a good courage" four times (vv. 6, 7, 9, 18); the eastern tribes' promise.
- **Ch. 2:** Rahab; the scarlet line; the flax on the roof; Rahab in Matthew 1:5, Hebrews 11:31, James 2:25; rabbinic traditions that she married Joshua (Megillah 14b).
- **Chs. 3–4:** the ark in front; Adam the city (3:16); the 1927 landslide that dammed the Jordan near Damiya (report only if verified, as a natural parallel); the twelve stones and "what mean ye by these stones" (4:6, 21).
- **Ch. 5:** circumcision at Gilgal ("rolled away," 5:9); first Passover in the land; manna ceases; the captain of the host and holy ground (compare Exodus 3:5).
- **Ch. 6:** seven days, seven priests, seven trumpets; the curse on rebuilding Jericho (6:26; 1 Kings 16:34); archaeology dispute (Garstang, Kenyon, Wood).
- **Ch. 7:** Achan; the "accursed thing"; corporate guilt; the valley of Achor (Hosea 2:15).
- **Ch. 8:** Ai; the ambush; the et-Tell problem; the altar on Ebal (8:30–35) — add only what is new relative to deuteronomy-027.
- **Ch. 9:** the Gibeonite ruse; oath kept despite the deceit (compare 2 Samuel 21).
- **Ch. 10:** the five kings; hailstones; "sun, stand thou still"; the Book of Jasher (10:13; 2 Samuel 1:18). Say the canonical book is lost, and don't present the 1840 printed "Book of Jasher" as authentic.
- **Ch. 11:** Hazor burned; the Anakim; "the land rested from war."
- **Ch. 12:** list of 31 defeated kings.
- **Ch. 13:** "very much land" remaining; Balaam killed (13:22); Levi has no inheritance.
- **Ch. 14:** Caleb at eighty-five; Hebron.
- **Ch. 15:** Judah's borders and town lists; Othniel and Achsah; the Septuagint's extra Bethlehem-district list after 15:59; Jebusites remain in Jerusalem (15:63).
- **Chs. 16–17:** Ephraim and Manasseh; Zelophehad's daughters receive land (17:3–6; links to numbers-027 and numbers-036); "a great people" clearing forest.
- **Chs. 18–19:** the tabernacle at Shiloh; surveying the land "in a book" (18:9); lots; Joshua's own city.
- **Ch. 20:** cities of refuge (Numbers 35; Deuteronomy 19); avoid repeating those chapters.
- **Ch. 21:** the 48 Levitical cities; 21:36–37's manuscript problem; "there failed not ought of any good thing" (21:45).
- **Ch. 22:** the altar Ed ("witness"); a near civil war averted; Phinehas.
- **Ch. 23:** farewell; the nations as "snares and traps."
- **Ch. 24:** covenant at Shechem; "beyond the flood" (River) and Terah's gods; "choose you this day"; the great stone under the oak as witness; burials of Joshua, Joseph's bones, and Eleazar. The Septuagint adds that the flint knives were buried with Joshua; verify.

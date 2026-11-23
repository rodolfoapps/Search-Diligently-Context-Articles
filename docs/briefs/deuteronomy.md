# Deuteronomy addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Deuteronomy. Where they differ, this file wins.

## Substitutions

- **Book:** Deuteronomy. Output: `content/old-testament/deuteronomy/deuteronomy-NNN.json`, with `"book": "Deuteronomy"`.
- **Outline:** `content/old-testament/deuteronomy/_book-outline.json`. `unit.current` must be one of its subsection ids, or an array when a chapter straddles two, e.g. ch. 4 → `["hear-obey", "decalogue"]`, ch. 10 → `["not-righteousness", "what-require"]`, ch. 16 → `["holy-people", "leaders"]`, ch. 21 → `["life-war", "family-community"]`. Do not edit the outline; report concerns instead.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`. Skim finished chapters in a similar genre to match house style: `exodus-020.json` (Decalogue), `leviticus-026.json` (blessings and curses), `numbers-021.json` or `numbers-024.json` (narrative/poetry).
- **Hebrew:** `python3 -I scripts/tools/heb.py --book Deut ...`. All OT books are in `.cache/`. **Do not run fetch_sources.sh.**
- **Verse offsets** (verified). Compare `heb.py show` with `showv.py` before counting; use KJV numbering in the text; note offsets in `review.checks`:
  - KJV 12:32 = Hebrew 13:1; KJV 13:1–18 = Hebrew 13:2–19
  - KJV 22:30 = Hebrew 23:1; KJV 23:1–25 = Hebrew 23:2–26
  - KJV 29:1 = Hebrew 28:69; KJV 29:2–29 = Hebrew 29:1–28
- **Helpers:** keep any helper scripts in `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/deut-<your-chapters>/`. Never overwrite another writer's files.
- **Commits:** the orchestrator may commit your files mid-work as WIP. Keep editing; don't commit yourself.

## Standing rules (also in docs/WRITING_RULES.md)

- **Sources:** no Qur'an or Islamic sources. Every Traditions entry must actually discuss this chapter's material. If you can't verify something, drop it.
- **Restoration positions** follow the Church's official teaching as published, stated plainly. If no Restoration scripture speaks to a chapter, leave the group out rather than stretch; label any thematic link as one, and prefer direct uses (quotations, allusions, named references) over themes.
- **Quoting:** quote only pre-1929 public-domain translations; paraphrase modern ones.
- **Citations in this brief are leads, not facts.** Check each before using it.
- **Medieval commentators** (Rashi, Ibn Ezra, Ramban) are allowed but should not crowd out ancient sources.
- **Historical Context:** 4–6 bullets. Use this exact wording unless a chapter has its own evidence (ch. 31 and ch. 34 do):
  - Author: "Presented as Moses' speeches; the book says Moses wrote 'this law' (31:9) and narrates his death. Jewish and Christian tradition credits Moses; many scholars connect its core with the law book found under Josiah (2 Kings 22)."
  - Date written: "Unknown. Tradition places it in Moses' lifetime (15th or 13th century BC); many scholars date its core to the 7th century BC, with additions in the 6th."
  - Ch. 34 may note the Talmud's view (Bava Batra 15a) that Joshua wrote the last eight verses; verify.

## Restoration material that may bear on Deuteronomy (verify each with showv.py)

- **A prophet like Moses (18:15–19):** Acts 3:22–23; 1 Nephi 22:20–21; 3 Nephi 20:23; JS—History 1:40 (Moroni quotes Acts 3:22–23); Acts 7:37.
- **The Shema and the first commandment (6:4–5):** Matthew 22:37–38; D&C 59:5; Moroni 10:32.
- **"Man doth not live by bread only" (8:3):** Matthew 4:4; D&C 84:44.
- **Jesus' answers in the temptation:** 8:3; 6:16; 6:13 (Matthew 4; Luke 4).
- **Two or three witnesses (17:6; 19:15):** 2 Corinthians 13:1; 2 Nephi 11:3; Ether 5:4; D&C 6:28; D&C 128:3.
- **The law of war (20:10):** D&C 98:33–36 ("this is the law that I gave unto mine ancients").
- **Divorce (24:1):** Matthew 19:7–8; 3 Nephi 12:31–32.
- **Blessings and curses tied to the land (28; 30):** 2 Nephi 1:7–9, 20; Ether 2:8–12. Use only where genuinely parallel.
- **Joseph's blessing (33:13–17):** D&C 58:45 ("push the people together"); verify wording.
- **The death of Moses (34):** Alma 45:19 ("the Lord took Moses unto himself"); the Church's Bible Dictionary, "Moses" (Moses translated); D&C 84:25; JST Deuteronomy 34:6 if the Church's footnotes show a change.
- **JST Deuteronomy 10:1–2:** parallels JST Exodus 34:1–2 on the second tablets; check the Church's footnotes.
- **The law written and kept (31:9–26):** 1 Nephi 5:11 ("the five books of Moses" on the brass plates); 2 Kings 22.
- **Adding to or taking from the word (4:2; 12:32):** 2 Nephi 29:3–10 as a thematic link only, labelled.
- **Moses on Nebo and the land seen (3:27; 34:1–4):** Moses 1 is a different vision; do not conflate.

## Good sources for Deuteronomy Traditions (verify each)

- **Jewish:** Sifre Deuteronomy (Sefaria); Deuteronomy Rabbah; Mishnah Berakhot (Shema), Sotah 7:8 (the king reads at Hakhel), Sotah 8 (exemptions from war), Gittin (divorce), Makkot (refuge, stripes); Philo, *On the Special Laws*, *On the Virtues* (Yonge); Josephus, *Antiquities* 4.7–8 (Whiston; Moses' laws and death); the Temple Scroll's law of the king; the Nash Papyrus (Decalogue plus Shema); 4QDeut texts for 32:8 and 32:43; Targums; Rashi.
- **Early Christian:** the Gospels (temptation, the great commandment, divorce); Acts 3:22–23 and 7:37; Romans 10:6–8 (30:11–14); Galatians 3:10, 13 (27:26; 21:23); 1 Corinthians 9:9 (25:4); Hebrews 10:28–30 and 12:29; Jude 9 (Michael and Moses' body); Barnabas; Justin; Origen; Augustine.
- **Other ancient:** Hittite vassal treaties and the Esarhaddon succession treaties (curses in ch. 28, loyalty in ch. 13) as scholarly comparison; the Mount Ebal altar site (Zertal) — present the dispute honestly.

## Chapter notes, to be verified before use

- **Chs. 1–3:** the journey recalled; Og's iron bed (3:11); Rephaim; Moses not allowed to cross.
- **Ch. 4:** no form seen at Horeb (4:12, 15); the nations' gods; cities of refuge east of Jordan.
- **Ch. 5:** compare with Exodus 20 (Sabbath reason: Egypt, not creation; "covet" order); avoid repeating the Exodus 20 chapter's material.
- **Ch. 6:** the Shema; tefillin and mezuzah; Nash Papyrus.
- **Ch. 8:** manna humbled; "bread only."
- **Chs. 9–10:** the calf recalled; second tablets; circumcise the heart (10:16; Romans 2:29).
- **Ch. 12:** the chosen place; Josiah's reform (2 Kings 23).
- **Ch. 13:** prophets who give signs; treaty loyalty clauses.
- **Ch. 15:** year of release; "the poor shall never cease" (15:11; Matthew 26:11).
- **Ch. 17:** the king's law (17:14–20); Solomon violates it (1 Kings 10–11); Mosiah 29 as a contrast on kingship (label as thematic).
- **Ch. 18:** the prophet like Moses.
- **Ch. 20:** war exemptions; *herem*; trees spared (20:19).
- **Ch. 21:** the hanged man cursed (21:23; Galatians 3:13; John 19:31).
- **Ch. 25:** levirate marriage (Ruth 4; Matthew 22:24); muzzle not the ox (1 Corinthians 9:9; 1 Timothy 5:18); Amalek.
- **Ch. 26:** "A Syrian ready to perish" (26:5), the short credo.
- **Ch. 27:** Ebal and Gerizim; plastered stones; the Samaritan reading (Gerizim in 27:4).
- **Ch. 28:** curses compared with Esarhaddon treaties; exile foretold.
- **Ch. 30:** return; "the word is very nigh" (Romans 10); "choose life."
- **Ch. 32:** the Song; 32:8 "children of Israel" versus "sons of God" (DSS/LXX); "Rock"; Hebrews 1:6 and 32:43 LXX.
- **Ch. 33:** the tribal blessings; compare Genesis 49; Simeon missing.
- **Ch. 34:** Moses' death and burial "no man knoweth"; Jude 9; Josephus *Ant.* 4.8.48 (cloud, he wrote of his own death); Restoration teaching that Moses was translated.

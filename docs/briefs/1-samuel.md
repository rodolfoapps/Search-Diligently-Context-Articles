# 1 Samuel addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for 1 Samuel. Where they differ, this file wins.

## Substitutions

- **Book:** 1 Samuel. Output: `content/old-testament/1-samuel/1-samuel-NNN.json`, with `"book": "1 Samuel"`.
- **Outline:** `content/old-testament/1-samuel/_book-outline.json`. `unit.current` is one subsection id, except ch. 2 → `["birth", "eli-house"]` and ch. 7 → `["ark", "mizpeh"]`. Do not edit the outline; report concerns instead.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`; skim `judges-011.json` and `joshua-006.json` for narrative with textual and archaeological debate.
- **Hebrew:** `python3 -I scripts/tools/heb.py --book 1Sam ...`. **Do not run fetch_sources.sh.** KJV: `python3 scripts/tools/showv.py 1-samuel <ch>:<v>` (or the format other writers used; check the script).
- **Verse offsets** (verified). Compare `heb.py show` with `showv.py`; use KJV numbering in the text; note offsets in `review.checks`:
  - KJV 20:42b ("And he arose and departed") = Hebrew 21:1; KJV 21:1–15 = Hebrew 21:2–16
  - KJV 23:29 = Hebrew 24:1; KJV 24:1–22 = Hebrew 24:2–23
- **Helpers:** `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/1sam-<your-chapters>/`. Never overwrite another writer's files.
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
- Author: "Not named in the text. The Talmud credits Samuel, with Gad and Nathan completing it (1 Chronicles 29:29); many scholars see it as part of a larger history compiled in the 7th–6th century BC from older sources."
- Date written: "Unknown. Tradition places it soon after the events (11th–10th century BC); many scholars date its final form to the 7th–6th century BC, drawing on older court and prophetic sources."
- Verify Bava Batra 14b–15a before relying on it. In the Hebrew Bible 1 and 2 Samuel are one book; the Septuagint calls them 1–2 Kingdoms. Mention this once, in ch. 1.

## The text of Samuel

Samuel has the most famous textual differences in the Old Testament, and they belong in Hermeneutics where they bear on the chapter:
- 4QSam-a (Dead Sea Scrolls) and the Septuagint often differ from the Masoretic text.
- 4QSam-a has a paragraph about Nahash gouging out right eyes before ch. 11 (also known to Josephus).
- Goliath's height: "six cubits and a span" (Masoretic) versus "four cubits and a span" (4QSam-a, Septuagint).
- The Septuagint (Vaticanus) lacks much of 17:12–31, 17:55–18:5 and parts of ch. 18.
- 13:1's damaged numbers for Saul's age and reign.
Verify each through a reliable scholarly source and say so in `review.checks`.

## Restoration material that may bear on 1 Samuel (verify each)

- **JST changes:** the Church's footnotes show JST changes for "an evil spirit from the LORD" (16:14–16, 23; 18:10; 19:9 → "not of the Lord"), and for "it repenteth me that I have set up Saul" (15:11, 35). Check each footnote and quote the JST wording exactly.
- **Asking for a king (ch. 8):** Ether 6:22–23 (the Jaredites ask for a king; the brother of Jared warns it "leadeth into captivity"); Mosiah 29:16–23. Deuteronomy 17 and Judges 9 already use parts of Mosiah 29 and 23; prefer Ether 6, or a Mosiah verse for a new point.
- **"The LORD looketh on the heart" (16:7):** check the Church's footnotes; D&C 137:9 as a thematic link if not footnoted.
- **"To obey is better than sacrifice" (15:22):** check footnotes.
- **Saul offers the sacrifice (13:8–14):** priesthood authority; Hebrews 5:4; Article of Faith 5. Numbers 16 already used these for Korah, so find a new angle or a different text.
- **Touching "the LORD's anointed" (24:6; 26:9–11):** D&C 121:16 ("lift up the heel against mine anointed"); verify.
- **Hannah's song (2:1–10):** Luke 1:46–55 (the Magnificat) is early Christian; for Restoration, use the footnotes only.
- **Endor (ch. 28):** Isaiah 8:19 as quoted in 2 Nephi 18:19 ("familiar spirits... peep and mutter"); state the Church's position plainly if one is published (e.g. Bible Dictionary "Familiar spirit"); do not invent one.

## Good sources for 1 Samuel Traditions (verify each)

- **Jewish:** Josephus, *Antiquities* 5.10–6.14 (Whiston); Pseudo-Philo, *Biblical Antiquities* 49–65 (James, 1917; Hannah, Samuel, Saul, Endor, Saul's death); Talmud (Berakhot 31a–b, Hannah's prayer as a model of prayer; Megillah 14a, Hannah a prophetess; Shabbat 55b on Eli's sons; Yoma 22b on Saul; Sanhedrin 20b on the king's law); Mishnah Nazir 9:5 (Samuel a Nazarite); Targum Jonathan; Rashi; Radak.
- **Early Christian:** Luke 1:46–55; Acts 3:24, 7:46, 13:20–22; Matthew 12:3–4 and Mark 2:25–26 (the shewbread at Nob, ch. 21; note "Abiathar" in Mark); Hebrews 11:32; Origen, *Homily on 1 Kings 28* and Eustathius, *On the Belly-Myther* (the Endor debate; paraphrase); Tertullian, *On the Soul* 57; Augustine, *City of God* 17.4 (Hannah's song); Ambrose, *On the Duties of the Clergy* (David sparing Saul); Gregory the Great on 1 Kings (verify).
- **Archaeology and background (Hermeneutics):** Shiloh's destruction layer; the Izbet Sartah ostracon (near Ebenezer); the Philistine cities (Ekron, Ashdod, Gath at Tell es-Safi); the tumors and mice (5–6; the Septuagint adds mice in 5:6); Philistine iron and the *pim* weight (13:21); Michmash pass; Khirbet Qeiyafa in the Elah Valley (present the debate); Goliath's armor and Aegean parallels; the Tell es-Safi "alwt/wlt" sherd (present carefully, it does not name Goliath); Beth-shan and the display of Saul's body (31:10); Tell el-Ful (Gibeah of Saul).

## Chapter notes, to be verified before use

- **Ch. 1:** Hannah's vow; Eli thinks her drunk; Samuel's name (1:20, "asked of God"; the wordplay fits Saul's name *sha'ul*); Samuel as a Nazarite (Septuagint and 4QSam-a at 1:11, 22).
- **Ch. 2:** Hannah's song; Eli's sons and the flesh-hook; "them that honour me I will honour" (2:30); the faithful priest (2:35).
- **Ch. 3:** "the word of the LORD was precious in those days; there was no open vision"; "Speak, LORD; for thy servant heareth."
- **Ch. 4:** the ark at Ebenezer; Eli's death; Ichabod.
- **Chs. 5–6:** Dagon falls; the tumors; the cart and the cows; Beth-shemesh (6:19's numbers; Josephus has 70).
- **Ch. 7:** twenty years; Mizpeh; "Ebenezer, hitherto hath the LORD helped us."
- **Ch. 8:** Samuel's sons; "make us a king... like all the nations"; "the manner of the king."
- **Chs. 9–10:** the lost asses; the seer; anointing with a vial of oil; "Is Saul also among the prophets?"; chosen by lot; "God save the king."
- **Ch. 11:** Nahash and Jabesh-gilead (with the 4QSam-a paragraph); the yoke of oxen cut in pieces (cf. Judges 19:29).
- **Ch. 12:** Samuel's farewell; "whose ox have I taken?" (compare Mosiah 2:12–14; label as thematic if not footnoted); thunder at wheat harvest.
- **Ch. 13:** 13:1's text problem; Saul's unlawful offering; no smith in Israel; the *pim*.
- **Ch. 14:** Jonathan and his armorbearer at Michmash; Saul's rash oath and the honey.
- **Ch. 15:** Amalek; Agag; "to obey is better than sacrifice"; the torn robe; JST 15:11, 35.
- **Ch. 16:** "the LORD looketh on the heart"; David anointed; the harp; JST "evil spirit."
- **Ch. 17:** Goliath; the textual problems; "the battle is the LORD's"; five smooth stones; 17:55–58 Saul asks whose son he is.
- **Ch. 18:** Jonathan's covenant; "Saul hath slain his thousands"; Michal; a hundred foreskins.
- **Ch. 19:** Michal and the teraphim; Saul among the prophets again at Naioth.
- **Ch. 20:** the new moon feast; the arrows; covenant between Jonathan and David.
- **Ch. 21:** Ahimelech and the shewbread; Goliath's sword; David feigns madness at Gath (Psalm 34 heading).
- **Ch. 22:** Adullam; Doeg kills the priests of Nob; Abiathar escapes.
- **Ch. 23:** Keilah; the ephod consulted; Ziph; Sela-hammahlekoth.
- **Ch. 24:** En-gedi; David cuts Saul's skirt; "the LORD's anointed."
- **Ch. 25:** Samuel's death; Nabal ("fool") and Abigail; "bound in the bundle of life" (25:29).
- **Ch. 26:** the spear and the water jug; Saul's second confession.
- **Ch. 27:** Achish gives David Ziklag; David's raids and deception.
- **Ch. 28:** the woman of Endor; what came up (ancient debate: Samuel himself, a demon, or a trick).
- **Ch. 29:** the Philistine lords distrust David.
- **Ch. 30:** Ziklag burned; David "encouraged himself in the LORD"; the law of sharing spoil (30:24–25; numbers-031 already used it, so don't repeat that point).
- **Ch. 31:** Gilboa; Saul's death (compare 2 Samuel 1's Amalekite account); Beth-shan; the men of Jabesh-gilead repay Saul's rescue.

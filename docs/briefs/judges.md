# Judges addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Judges. Where they differ, this file wins.

## Substitutions

- **Book:** Judges. Output: `content/old-testament/judges/judges-NNN.json`, with `"book": "Judges"`.
- **Outline:** `content/old-testament/judges/_book-outline.json`. `unit.current` is one subsection id, except ch. 2 → `["incomplete-conquest", "cycle"]`. Do not edit the outline; report concerns instead.
- **Gold standard:** `content/old-testament/genesis/genesis-001.json`. Skim `joshua-006.json` and `joshua-010.json` to match house style for narrative with archaeology and poetry.
- **Hebrew:** `python3 -I scripts/tools/heb.py --book Judg ...`. **Do not run fetch_sources.sh.** Hebrew (Westminster Leningrad Codex) and KJV number Judges the same throughout; note it in `review.checks`.
- **Helpers:** keep helper scripts in `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/judg-<your-chapters>/`. Never overwrite another writer's files.
- **Commits:** the orchestrator may commit your files mid-work as WIP. Keep editing; don't commit yourself.

## Don't repeat a parallel another chapter already uses

Before you make any ancient parallel, scholar's thesis or Traditions source a chapter's main point, search the whole content tree:

```
grep -ril "medinet habu" content/old-testament/
```

If a finished chapter already makes **the same point** with it, pick something else. Using the same source for a **different, chapter-specific fact** is fine; say what is new. Check again just before you finish, because other writers work at the same time. List clashes in `review.checks` and your report.

Repeated across this book in particular, check before using: the Merneptah Stele, the Amarna letters, the Mesha Stele, Ugaritic Anat or Baal texts, and the Nazarite law. For Samson, `numbers-006` already covers the Nazarite vow itself; add only what Judges 13–16 adds. Judges 19 and Genesis 19 overlap; read `genesis-019.json` and don't repeat it.

## House decision: archaeology goes in Hermeneutics

Put archaeology and ancient Near Eastern background in Hermeneutics, not in Traditions. Traditions is for how ancient readers (Restoration, Jewish, early Christian, other ancient writers) interpreted the chapter.

## Standing rules (also in docs/WRITING_RULES.md)

- **Sources:** no Qur'an or Islamic sources. Every Traditions entry must actually discuss this chapter's material. If you can't verify something, drop it.
- **Restoration positions** follow the Church's official teaching as published, stated plainly. If no Restoration scripture speaks to a chapter, leave the group out rather than stretch. Label thematic links as such, and prefer direct quotations, allusions and the Church's own footnote cross-references.
- **Quoting:** quote only pre-1929 public-domain translations; paraphrase modern ones.
- **Citations in this brief are leads, not facts.** Check each before using it.
- **Violence and abuse** (Ehud, Jael, Jephthah's daughter, Samson, the woman at Gibeah, the war on Benjamin, the abduction at Shiloh): state what the text says plainly and briefly, without softening or sensationalizing. You may note where the book itself judges events (e.g. "every man did that which was right in his own eyes").
- **Historical Context:** 4–6 bullets. Use this exact wording unless a chapter has its own evidence:
  - Author: "Not named in the text. The Talmud credits Samuel; many scholars see the book as part of a larger history compiled in the 7th–6th century BC from older stories."
  - Date written: "Unknown. Tradition places it in Samuel's day (11th century BC); many scholars date its final form to the 7th–6th century BC, drawing on older material such as the Song of Deborah."
  - Verify Bava Batra 14b before relying on it. Ch. 18:30 ("until the day of the captivity of the land") is internal evidence and may be noted in ch. 18.

## Restoration material that may bear on Judges (verify each with showv.py)

- **The cycle of sin, oppression, crying out, deliverance (2:11–19; 3:7–9):** Helaman 12:1–6 (how quickly people forget God in prosperity); Helaman 11; as a thematic link only, labelled.
- **"Every man did that which was right in his own eyes" (17:6; 21:25):** D&C 1:16 ("every man walketh in his own way"), thematic.
- **Gideon refuses kingship (8:22–23):** Mosiah 23:6–8 (Alma refuses to be king). Deuteronomy 17 already used Mosiah 23 and 29; check and use a different angle or verse.
- **Gideon's signs (6:36–40):** D&C 63:7–12 (faith does not come by signs) as a thematic link; also Alma 30:43–50 (Korihor asks for a sign). Present carefully: Judges does not condemn Gideon's request.
- **The angel's name is "secret"/"wonderful" (13:18):** Isaiah 9:6 uses the same Hebrew root; check footnotes.
- **Hebrews 11:32** names Gideon, Barak, Samson, and Jephthah among the faithful.
- **JST Judges:** check the Church's footnotes before claiming any change.

## Good sources for Judges Traditions (verify each)

- **Jewish:** Josephus, *Antiquities* 5.2–8 (Whiston); Pseudo-Philo, *Biblical Antiquities* 25–48 (James, 1917; a rich source, including the judge Kenaz, Deborah's speeches, Jephthah's daughter named Seila, Samson); Talmud (Bava Batra 14b–15a; Rosh Hashanah 25a–b, "Jephthah in his generation like Samuel in his"; Sotah 9b–10a on Samson; Megillah 14a on Deborah; Taanit 4a on Jephthah's vow); Mishnah Sotah 1:8; Seder Olam Rabbah 12; Targum Jonathan; Rashi; Radak.
- **Early Christian:** Hebrews 11:32; Acts 13:20; 1 Samuel 12:11 (a judge "Bedan"); Ambrose, *On the Holy Spirit* 2, prologue (Gideon's fleece) and *Letter* 19 (Samson); Augustine, *City of God* 1.21 (Samson), 16.43; Origen, *Homilies on Judges* (paraphrase; modern translation); Jerome; Methodius, *Symposium* (on Jephthah's daughter, verify).
- **Other ancient and archaeology (Hermeneutics):** the Song of Deborah as early Hebrew poetry; Taanach and Megiddo; Iron Age I highland villages; the Philistines and Sea Peoples (Medinet Habu reliefs of Ramesses III); Ekron, Ashdod, Gaza temples with pillars (Tell Qasile's temple, relevant to 16:29); Tel Dan and the "house of David" stele (relevant only for Dan's later history; don't overreach); Shechem's temple of Baal-berith (Joshua 24 used Shechem; use a different fact); the *shibboleth* dialect difference (12:6); Shamgar "son of Anath."

## Chapter notes, to be verified before use

- **Ch. 1:** Adoni-bezek's thumbs and toes; "Judah shall go up"; the tribes who did not drive out the Canaanites; iron chariots (1:19).
- **Ch. 2:** Bochim ("weepers"); the generation that "knew not the LORD"; the cycle stated.
- **Ch. 3:** Othniel; Ehud the left-handed Benjamite and Eglon; Shamgar's ox goad.
- **Ch. 4:** Deborah judging under the palm; Barak; Jael and the tent peg; Sisera's iron chariots.
- **Ch. 5:** the Song of Deborah; "the stars in their courses fought"; tribes praised and shamed; Sisera's mother at the window. Treat as poetry; one of the oldest Hebrew texts by scholarly consensus.
- **Ch. 6:** Midianite raids and camels; Gideon threshing in a winepress; "Jehovah-shalom"; Jerubbaal; the fleece.
- **Ch. 7:** the 300 who lapped; the dream of the barley loaf; trumpets, pitchers, torches; "The sword of the LORD, and of Gideon."
- **Ch. 8:** Succoth and Penuel; kingship refused; the ephod that became a snare.
- **Ch. 9:** Abimelech kills seventy brothers; Jotham's fable of the trees (the earliest fable in the Bible); the millstone dropped by a woman (cf. 2 Samuel 11:21).
- **Ch. 10:** Tola and Jair; Israel's apostasy; God refuses, then relents ("his soul was grieved").
- **Ch. 11:** Jephthah the outcast; his message to Ammon (history of the land, 300 years, 11:26); his vow and his daughter. Report the ancient debate (sacrifice vs. dedication; Radak and others) fairly.
- **Ch. 12:** Ephraim's quarrel; *shibboleth*; Ibzan, Elon, Abdon.
- **Ch. 13:** Samson's birth announced; Manoah's wife unnamed; the angel ascends in the flame.
- **Ch. 14:** the Timnite wife; the lion and the honey; the riddle.
- **Ch. 15:** foxes and torches; the jawbone; Ramath-lehi; En-hakkore.
- **Ch. 16:** Gaza's gates; Delilah; the hair; blinded; the temple of Dagon.
- **Ch. 17:** Micah's silver, image, and hired Levite; "no king in Israel."
- **Ch. 18:** Dan's spies and migration to Laish; the Levite is Jonathan son of Gershom son of Moses (18:30; the suspended *nun* that makes "Manasseh" in the Masoretic text).
- **Ch. 19:** the Levite's concubine; Gibeah's men; compare Genesis 19 without repeating genesis-019.
- **Ch. 20:** the tribes against Benjamin; the left-handed slingers (20:16).
- **Ch. 21:** the oath not to give wives; Jabesh-gilead; the dancers of Shiloh; "right in his own eyes."

# Exodus addendum to the batch brief

Read `docs/BATCH_BRIEF.md` first and follow it, with these substitutions and additions for Exodus.

## Substitutions

- **Book:** Exodus. Output: `content/old-testament/exodus/exodus-NNN.json`, with `"book": "Exodus"`.
- **Outline:** `content/old-testament/exodus/_book-outline.json`. `unit.current` must be one of its subsection ids. Use an array when a chapter straddles two subsections: ch. 13 → `["passover", "sea"]`, ch. 15 → `["sea", "wilderness"]`, ch. 20 → `["theophany", "covenant-code"]`, ch. 7 → `["first-audience", "plagues"]`. Do not edit the outline; report concerns instead.
- **Gold standard:** still `content/old-testament/genesis/genesis-001.json`. Also skim two finished Genesis chapters, e.g. `genesis-022.json` and `genesis-037.json`, to match the house style the Genesis batch settled into.
- **Hebrew:** use `python3 -I scripts/tools/heb.py --book Exod ...`.
  - The source texts are already downloaded in `.cache/`. **Do not run fetch_sources.sh.**
  - **Verse numbering differs between the Hebrew and the KJV in places.** KJV 8:1–4 = Hebrew 7:26–29 (so KJV 8:5 = Hebrew 8:1), and KJV 22:1 = Hebrew 21:37. Always compare `heb.py show` with `showv.py` before counting. Use KJV numbering everywhere in the text, and note any offset in `review.checks`.
- **Helpers:** if you write any helper script, put it in your own folder `/tmp/claude-0/-home-user-Search-Diligently-Context-Articles/fc021819-ed5e-5bed-8976-421853f6c71a/scratchpad/<your-chapters>/`. Never overwrite another writer's files.
- **Commits:** the orchestrator may commit your files mid-work as WIP. That is expected; keep editing, and don't commit yourself.

## Decisions made after Genesis (also in docs/WRITING_RULES.md)

- **No Qur'an or other Islamic sources** in Traditions.
- **Restoration positions follow the Church's official teaching** as published (scripture, official declarations, Church-published statements), stated plainly, with no outside commentary.
- **Historical Context:** 4–6 bullets; 7 only when the chapter genuinely needs every label.

## Restoration material that bears on Exodus (verify each with showv.py before using)

- **Moses 1:** set after the burning bush and before the deliverance (Moses 1:17, 25–26).
- **JST Exodus:** the Joseph Smith Translation changes "I will harden Pharaoh's heart" so that Pharaoh hardens his own heart (JST Exod 4:21; 7:3, 13; 9:12; 10:1, 20, 27; 11:10; 14:4, 8, 17). Check each against the Church's JST appendix and footnotes on churchofjesuschrist.org. JST Exodus 34:1–2 also changes the second tablets: the higher priesthood and law were taken away.
- **D&C 84:6–26:** Moses received the priesthood from Jethro (Exodus 18). Israel would not enter God's presence at Sinai, so the higher priesthood was taken (Exodus 19–20, 32–34).
- **Other references:**
  - Mosiah 12–13: Abinadi recites the Ten Commandments.
  - 1 Nephi 4:2; 17:23–31: Nephi retells the Exodus.
  - D&C 8:2–3: the spirit of revelation by which Moses led Israel through the Red Sea.
  - D&C 103:15–18; 110:11: Moses and the keys of the gathering.
  - 3 Nephi 15:4–10: the law fulfilled in Christ.
  - D&C 124: tabernacle and temple patterns.
  - 2 Nephi 25:24–30: the law of Moses kept.

## Chapter notes, to be verified before use

- **Chs. 1–2:**
  - Egyptian background: the Hyksos, the store cities Pithom and Raamses, brickmaking with straw (the Louvre leather roll), and the Sargon of Akkad birth legend (a baby in a reed basket).
  - The name Moses: an Egyptian *-mose* name versus the Hebrew wordplay in 2:10.
- **Ch. 3:**
  - The divine name in 3:14 ("I AM THAT I AM"); John 8:58; D&C 29:1; 39:1.
  - Holy ground: removing sandals.
- **Chs. 7–11:**
  - The plagues as judgment on Egypt's gods (Exodus 12:12; Numbers 33:4), e.g. the Nile, Hapi, the frog goddess Heqet, Ra and darkness.
  - The magicians' tricks; the "finger of God" (8:19).
  - The Admonitions of Ipuwer: a disputed parallel, so present it cautiously or skip it.
- **Ch. 12:**
  - The Passover; the Lamb of God (John 1:29; 1 Corinthians 5:7).
  - Mishnah Pesachim; the Haggadah.
- **Ch. 14:**
  - The route and the yam suph ("Red Sea" / "Sea of Reeds"); present the debate briefly.
  - 1 Nephi 17:26–27; Hebrews 11:29.
- **Ch. 15:**
  - The Song of the Sea is among the oldest Hebrew poetry (scholarly view); Miriam's song.
  - Mekhilta de-Rabbi Ishmael is a rich Jewish source for chs. 12–23.
- **Ch. 16:** manna (John 6:31–58; Wisdom of Solomon 16:20–21; Alma 37:40).
- **Ch. 17:** water from the rock (1 Corinthians 10:4); Amalek.
- **Ch. 18:** Jethro; D&C 84:6–7.
- **Chs. 19–20:**
  - Sinai, the theophany, the Decalogue.
  - Treaty form: Hittite vassal treaties (Mendenhall). Present it as a scholarly comparison.
  - The Decalogue's two numbering systems (Jewish, Catholic and Lutheran, Reformed). Mosiah 12:33–36; 13:12–24.
- **Chs. 21–23:**
  - The Code of Hammurabi parallels: the goring ox (CH §§250–252), lex talionis (CH §196 and following). Verify the section numbers against King's 1915 translation.
- **Ch. 24:** the covenant meal; the seventy elders "saw the God of Israel" (24:10).
- **Chs. 25–31, 35–40:**
  - The tabernacle: Egyptian portable shrines and tents.
  - Philo, Life of Moses 2; Josephus, Antiquities 3.6–7 (the tabernacle as a model of the cosmos).
  - Hebrews 8–9.
  - Priestly vestments: the Urim and Thummim (28:30), with the Restoration link to Joseph Smith's interpreters (JS—History 1:35, 62; D&C 17:1). The ephod; the breastplate.
  - The repetition between chs. 25–31 and 35–40 is itself a structural point.
- **Ch. 32:** the golden calf (Apis; Jeroboam's calves, 1 Kings 12:28); the tablets broken.
- **Ch. 33:** "face to face" versus "thou canst not see my face"; Moses 1:2, 11; D&C 84:22.
- **Ch. 34:** the second tablets; the shining face; JST Exodus 34:1–2; 2 Corinthians 3:7–18.
- **Ch. 40:** the glory fills the tabernacle; compare 1 Kings 8:10–11.

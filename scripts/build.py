#!/usr/bin/env python3
"""Validate chapter resources and compile them into the per-book JSON files the app reads.

Source (one file per chapter, all tabs):
    content/<volume>/<book>/<book>-<NNN>.json
    content/<volume>/<book>/_book-outline.json      (one per book, shared by every chapter)

Output:
    dist/<volume>/<book>.json     {"book", "outline", "chapters": {"1": {...}}}
    dist/index.json               every book, its file, and how complete it is

The shape is documented in docs/LOVABLE_SPEC.md; the writing rules in docs/WRITING_RULES.md.

Usage:
    python3 scripts/build.py            # validate + write dist/
    python3 scripts/build.py --check    # validate only (exit 1 on errors)
    python3 scripts/build.py --strict   # also fail on warnings (use before approving a chapter)
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON = json.loads((ROOT / "canon" / "canon.json").read_text())
CONTENT = ROOT / "content"
DIST = ROOT / "dist"

STATUSES = ["draft", "in-review", "approved"]
APP_TABS = ["overview", "historicalContext", "hermeneutics", "breakdown", "structure", "unit", "traditions"]
SOURCE_KEYS = {"book", "chapter", "status", "review", *APP_TABS}
HC_LABELS = ["Author", "When revealed (Restoration)", "Date written", "Date of events",
             "Language", "First audience", "Setting (events)", "Parallel accounts"]
TRADITION_GROUPS = ["restoration", "jewish", "early-christian", "other-ancient"]
STRUCTURE_TYPES = ["chiasm", "parallel-panels", "inclusio", "alternating", "sequence"]

# (min, max) words, from docs/WRITING_RULES.md
LIMITS = {
    "overview": (90, 160),
    "hermeneutics": (200, 320),
    "structure.notes": (60, 150),
    "unit.notes": (50, 120),
    "traditions": (700, 1100),
}
BANNED = ["in this chapter", "why it matters", "reminds us", "rich tapestry", "profound",
          "it is worth noting", "delve", "underscore", "serves as"]

HTML_TAG = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(\s[^<>]*)?/?>")
REF = r"\d+:\d+[a-c]?"
RANGE = re.compile(rf"^(\d+):(\d+)[a-c]?(?:-(?:(\d+):)?(\d+)[a-c]?)?$")
QUOTED = re.compile(r"[\"“]([^\"”]+)[\"”]")
MAX_QUOTE_WORDS = 12

errors: list = []
warnings: list = []


def rel(p):
    return p.relative_to(ROOT)


def err(path, msg):
    errors.append(f"ERROR   {rel(path)}: {msg}")


def warn(path, msg):
    warnings.append(f"warning {rel(path)}: {msg}")


def words(text):
    return len(re.findall(r"[A-Za-z0-9’'][A-Za-z0-9’'\-–]*", text))


def prose_checks(path, label, texts, status):
    """Checks that apply to every piece of user-visible text in one tab."""
    joined = "\n".join(t for t in texts if t)
    if HTML_TAG.search(joined):
        err(path, f"{label}: contains HTML; use Markdown only")
    if "```" in joined or re.search(r"^\|.*\|\s*$", joined, re.M):
        err(path, f"{label}: no code blocks or Markdown tables; use the structured fields")
    dashes = joined.count("—")
    if dashes > 1:
        warn(path, f"{label}: {dashes} em dashes (max 1 per tab)")
    low = joined.lower()
    for phrase in BANNED:
        if re.search(rf"\b{re.escape(phrase)}", low):
            err(path, f"{label}: banned phrase {phrase!r}")
    for m in QUOTED.finditer(joined):
        n = len(m.group(1).split())
        if n > MAX_QUOTE_WORDS:
            warn(path, f"{label}: {n}-word quotation; keep quotes short: \"{m.group(1)[:50]}…\"")
    if "[CHECK" in joined:
        (err if status == "approved" else warn)(path, f"{label}: contains an unresolved [CHECK]")


def check_range(path, where, r):
    if not isinstance(r, str) or not RANGE.match(r):
        err(path, f"{where}: range {r!r} must look like '1:3-5', '1:26-2:3' or '1:27'")
        return None
    m = RANGE.match(r)
    c1, v1 = int(m.group(1)), int(m.group(2))
    c2 = int(m.group(3)) if m.group(3) else c1
    v2 = int(m.group(4)) if m.group(4) else v1
    return c1, v1, c2, v2


def check_length(path, key, text_or_count, unit="words"):
    lo, hi = LIMITS[key]
    n = text_or_count if isinstance(text_or_count, int) else words(text_or_count)
    if not lo <= n <= hi:
        warn(path, f"{key}: {n} {unit} (target {lo}–{hi})")


def validate_chapter(path, data, book, n, outline_ids):
    verse_count = book["verses"][n - 1]
    extra = set(data) - SOURCE_KEYS
    if extra:
        err(path, f"unknown keys {sorted(extra)}")
    if data.get("book") != book["name"]:
        err(path, f"'book' must be {book['name']!r}")
    if data.get("chapter") != n:
        err(path, f"'chapter' must be {n}")
    status = data.get("status")
    if status not in STATUSES:
        err(path, f"'status' must be one of {STATUSES}")
    missing = [t for t in APP_TABS if t not in data]
    if missing:
        warn(path, f"tabs not written yet: {missing}")

    # Overview
    if "overview" in data:
        ov = data["overview"]
        paras = [p for p in ov.split("\n\n") if p.strip()]
        if len(paras) != 2:
            warn(path, f"overview: {len(paras)} paragraphs (target 2)")
        check_length(path, "overview", ov)
        if re.match(r"\s*(in this chapter|genesis \d|chapter \d)", ov, re.I):
            err(path, "overview: open with what happens, not 'In this chapter…' or the title")
        prose_checks(path, "overview", [ov], status)

    # Historical Context
    if "historicalContext" in data:
        hc = data["historicalContext"]
        labels = [b.get("label") for b in hc]
        for lab in labels:
            if lab not in HC_LABELS:
                err(path, f"historicalContext: unknown label {lab!r} (allowed: {HC_LABELS})")
        known = [HC_LABELS.index(lab) for lab in labels if lab in HC_LABELS]
        if known != sorted(known) or len(set(known)) != len(known):
            err(path, "historicalContext: labels out of order or repeated")
        if not 4 <= len(hc) <= 6:
            warn(path, f"historicalContext: {len(hc)} bullets (target 4–6)")
        for b in hc:
            if set(b) != {"label", "text"}:
                err(path, f"historicalContext: each bullet needs exactly label and text ({b})")
            elif words(b["text"]) > 45:
                warn(path, f"historicalContext: '{b['label']}' is {words(b['text'])} words (aim for one or two lines)")
        prose_checks(path, "historicalContext", [b.get("text", "") for b in hc], status)

    # Hermeneutics
    if "hermeneutics" in data:
        h = data["hermeneutics"]
        paras = [p for p in h.split("\n\n") if p.strip()]
        if not 2 <= len(paras) <= 3:
            warn(path, f"hermeneutics: {len(paras)} paragraphs (target 2–3)")
        check_length(path, "hermeneutics", h)
        prose_checks(path, "hermeneutics", [h], status)

    # Chapter Breakdown
    if "breakdown" in data:
        rows = data["breakdown"]
        inside = [r for r in rows if not r.get("overflow")]
        if not 5 <= len(inside) <= 10 and verse_count >= 10:
            warn(path, f"breakdown: {len(inside)} rows (target 5–10)")
        expected = 1
        seen_inside = False
        for i, r in enumerate(rows):
            where = f"breakdown[{i}]"
            if not {"range", "label"} <= set(r) <= {"range", "label", "overflow"}:
                err(path, f"{where}: needs range and label (and optional overflow)")
                continue
            if "—" in r["label"]:
                err(path, f"{where}: use a colon, not an em dash, in labels")
            if not 3 <= words(r["label"]) <= 12:
                warn(path, f"{where}: label is {words(r['label'])} words (target 3–12)")
            parsed = check_range(path, where, r["range"])
            if not parsed:
                continue
            c1, v1, c2, v2 = parsed
            if r.get("overflow"):
                if c1 == n and c2 == n:
                    err(path, f"{where}: overflow rows must point outside chapter {n}")
                if seen_inside and expected <= verse_count:
                    err(path, f"{where}: overflow rows go only before or after the chapter's own rows")
                continue
            seen_inside = True
            if c1 != n or c2 != n:
                err(path, f"{where}: {r['range']} is not inside chapter {n} (mark it overflow if it spills over)")
                continue
            if v1 > expected:
                err(path, f"{where}: verses {expected}-{v1 - 1} are not covered")
            elif v1 < expected:
                err(path, f"{where}: overlaps the previous row (should start at verse {expected})")
            expected = v2 + 1
        if expected - 1 != verse_count:
            err(path, f"breakdown covers verses 1-{expected - 1} but the chapter has {verse_count}")
        prose_checks(path, "breakdown", [r.get("label", "") for r in rows], status)

    # Literary Structure
    if "structure" in data:
        s = data["structure"]
        texts = list(s.get("notes", [])) + [s.get("summary", "")]
        for j, diagram in enumerate([s] + list(s.get("secondary", []))):
            where = "structure" if j == 0 else f"structure.secondary[{j - 1}]"
            t = diagram.get("type")
            if t not in STRUCTURE_TYPES:
                err(path, f"{where}: type must be one of {STRUCTURE_TYPES}")
            if j and not diagram.get("title"):
                err(path, f"{where}: secondary diagrams need a title")
            rows = diagram.get("rows", [])
            if t != "sequence" and not rows:
                err(path, f"{where}: a {t} diagram needs rows")
            for k, row in enumerate(rows):
                cells = [row["left"], row["right"]] if t == "parallel-panels" else [row]
                for cell in cells:
                    if not isinstance(cell, dict) or not {"label", "text"} <= set(cell) <= {"label", "ref", "text"}:
                        err(path, f"{where}.rows[{k}]: each cell needs label and text (ref optional)")
                        continue
                    texts.append(cell["text"])
                    if cell.get("ref"):
                        check_range(path, f"{where}.rows[{k}]", cell["ref"])
            frame = diagram.get("frame")
            if frame:
                for side in ("open", "close"):
                    if side not in frame or not {"ref", "text"} <= set(frame[side]):
                        err(path, f"{where}.frame.{side} needs ref and text")
                    else:
                        texts.append(frame[side]["text"])
            if t == "chiasm" and rows and len(rows) % 2 == 0 and "center" in diagram:
                warn(path, f"{where}: an even-length chiasm has no single center")
        notes = s.get("notes", [])
        if not 2 <= len(notes) <= 4:
            warn(path, f"structure.notes: {len(notes)} notes (target 2–4)")
        check_length(path, "structure.notes", " ".join(notes) + " " + s.get("summary", ""))
        prose_checks(path, "structure", texts, status)

    # Literary Unit
    if "unit" in data:
        u = data["unit"]
        cur = u.get("current")
        cur_list = cur if isinstance(cur, list) else [cur]
        for c in cur_list:
            if c not in outline_ids:
                err(path, f"unit.current {c!r} is not a subsection id in _book-outline.json")
        notes = u.get("notes", [])
        check_length(path, "unit.notes", " ".join(notes))
        prose_checks(path, "unit", notes, status)

    # Traditions
    if "traditions" in data:
        tr = data["traditions"]
        if not 8 <= len(tr) <= 15:
            warn(path, f"traditions: {len(tr)} entries (target 8–15)")
        order = []
        for k, e in enumerate(tr):
            where = f"traditions[{k}]"
            if set(e) != {"group", "source", "date", "text", "cite"}:
                err(path, f"{where}: needs exactly group, source, date, text, cite")
                continue
            if e["group"] not in TRADITION_GROUPS:
                err(path, f"{where}: group must be one of {TRADITION_GROUPS}")
                continue
            order.append(TRADITION_GROUPS.index(e["group"]))
            plain = re.sub(r"\b(?:vv?|c|ch|chs|cf|e\.g|i\.e|St|Dr)\.", "", e["text"].strip())
            sentences = len(re.findall(r"[.!?](?:[”\"’)]*)(?:\s|$)", plain))
            if not 2 <= sentences <= 4:
                warn(path, f"{where} ({e['source']}): ~{sentences} sentences (target 2–4)")
            # a "quotation" is a quoted run of 4+ words; shorter quoted terms ("one day") are mentions
            quotes = [q for q in QUOTED.findall(e["text"]) if len(q.split()) >= 4]
            if len(quotes) > 1:
                warn(path, f"{where} ({e['source']}): {len(quotes)} quotations (max one per entry)")
        if order != sorted(order):
            err(path, "traditions: groups must run restoration, jewish, early-christian, other-ancient")
        check_length(path, "traditions", sum(words(e.get("text", "")) for e in tr))
        prose_checks(path, "traditions", [e.get("text", "") for e in tr], status)


def load_outline(path, book):
    data = json.loads(path.read_text(encoding="utf-8"))
    ids = []
    if data.get("book") != book["name"]:
        err(path, f"'book' must be {book['name']!r}")
    for s in data.get("sections", []):
        if not {"id", "title", "range", "subsections"} <= set(s):
            err(path, f"section {s.get('title')!r} needs id, title, range, subsections")
            continue
        check_range(path, f"section {s['id']}", s["range"])
        for sub in s["subsections"]:
            if not {"id", "title", "range"} <= set(sub):
                err(path, f"subsection in {s['id']} needs id, title, range")
                continue
            check_range(path, f"subsection {sub['id']}", sub["range"])
            ids.append(sub["id"])
    if len(ids) != len(set(ids)):
        err(path, "subsection ids must be unique")
    return data, set(ids)


def app_view(data):
    """The chapter as the app sees it: tabs only, no review metadata."""
    out = {k: data[k] for k in APP_TABS if k in data}
    s = out.get("structure")
    if s:
        for diagram in [s] + list(s.get("secondary", [])):
            if diagram.get("type") == "chiasm":
                rows = diagram["rows"]
                half = (len(rows) + 1) // 2
                for i, row in enumerate(rows):
                    row["indent"] = i if i < half else len(rows) - 1 - i
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate only, do not write dist/")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    known = set()
    index = {"volumes": []}
    outputs = []
    for volume in CANON["volumes"]:
        vindex = {"name": volume["name"], "slug": volume["slug"], "books": []}
        for book in volume["books"]:
            folder = CONTENT / volume["slug"] / book["slug"]
            outline, outline_ids = None, set()
            opath = folder / "_book-outline.json"
            if opath.exists():
                known.add(opath)
                try:
                    outline, outline_ids = load_outline(opath, book)
                except json.JSONDecodeError as e:
                    err(opath, f"invalid JSON: {e}")
            chapters, statuses = {}, {}
            for n in range(1, book["chapters"] + 1):
                path = folder / f"{book['slug']}-{n:03d}.json"
                if not path.exists():
                    continue
                known.add(path)
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                except json.JSONDecodeError as e:
                    err(path, f"invalid JSON: {e}")
                    continue
                if "unit" in data and outline is None:
                    err(path, "has a unit tab but the book has no _book-outline.json")
                validate_chapter(path, data, book, n, outline_ids)
                chapters[str(n)] = app_view(data)
                statuses[data.get("status", "draft")] = statuses.get(data.get("status", "draft"), 0) + 1
            if chapters:
                book_out = {"book": book["name"]}
                if outline:
                    book_out["outline"] = {"sections": outline["sections"]}
                book_out["chapters"] = chapters
                outputs.append((f"{volume['slug']}/{book['slug']}.json", book_out))
            vindex["books"].append({
                "name": book["name"], "slug": book["slug"], "unit": book["unit"],
                "chapters": book["chapters"],
                "file": f"{volume['slug']}/{book['slug']}.json" if chapters else None,
                "chaptersWithContent": len(chapters),
                "complete": len(chapters) == book["chapters"],
                "status": statuses,
            })
        index["volumes"].append(vindex)

    for path in CONTENT.rglob("*"):
        if path.is_file() and path.name != ".gitkeep" and path not in known:
            err(path, "not a valid content path: expected <volume>/<book>/<book>-<NNN>.json or _book-outline.json")

    for line in warnings + errors:
        print(line)
    failed = errors or (args.strict and warnings)
    if failed:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s). dist/ not written.")
        sys.exit(1)

    if not args.check:
        for old in DIST.rglob("*.json") if DIST.exists() else []:
            old.unlink()
        for relpath, data in outputs:
            out = DIST / relpath
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        DIST.mkdir(exist_ok=True)
        (DIST / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n_ch = sum(len(d["chapters"]) for _, d in outputs)
    print(f"OK: {'validated' if args.check else 'built'} {len(outputs)} book file(s), "
          f"{n_ch} chapter(s), {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()

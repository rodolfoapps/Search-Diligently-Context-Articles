#!/usr/bin/env python3
"""Validate the source content and compile it into the per-book JSON files the app reads.

Source layout (one file per chapter, per tab):

    historical-context/<volume>/<book>/<book>-<NNN>.md
    chapter-breakdown/<volume>/<book>/<book>-<NNN>.json
    literary-unit/<volume>/<book>/<book>-<NNN>.md

Output layout (what the Lovable app fetches):

    dist/<volume>/<book>.json     {"book": ..., "chapters": {"1": {...}, ...}}
    dist/index.json               manifest of every book and how complete it is

Usage:
    python3 scripts/build.py            # validate + write dist/
    python3 scripts/build.py --check    # validate only (exit 1 on errors)
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON = json.loads((ROOT / "canon" / "canon.json").read_text())
DIST = ROOT / "dist"

# tab folder -> (JSON key in the app file, file extension)
TABS = {
    "historical-context": ("context", ".md"),
    "chapter-breakdown": ("breakdown", ".json"),
    "literary-unit": ("literaryUnit", ".md"),
}
STATUSES = {"draft", "in-review", "approved"}

HTML_TAG = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(\s[^<>]*)?/?>")
RANGE = re.compile(r"^(\d+):(\d+)(?:-(\d+))?$")
QUOTED = re.compile(r"[\"“]([^\"”]+)[\"”]")
MAX_QUOTE_WORDS = 12

errors: list = []
warnings: list = []


def err(path, msg):
    errors.append(f"ERROR   {path.relative_to(ROOT)}: {msg}")


def warn(path, msg):
    warnings.append(f"warning {path.relative_to(ROOT)}: {msg}")


def parse_markdown(path: pathlib.Path):
    """Return (meta, body). Front matter is a small YAML subset: `key: value` and `- list items`."""
    text = path.read_text(encoding="utf-8")
    meta = {}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end == -1:
            err(path, "front matter opened with --- but never closed")
            return meta, ""
        current_list = None
        for line in text[4:end].splitlines():
            if not line.strip():
                continue
            if line.lstrip().startswith("- ") and current_list is not None:
                meta[current_list].append(line.lstrip()[2:].strip())
            elif ":" in line:
                key, _, value = line.partition(":")
                key, value = key.strip(), value.strip()
                if value:
                    meta[key] = value
                    current_list = None
                else:
                    meta[key] = []
                    current_list = key
            else:
                err(path, f"cannot parse front matter line: {line!r}")
        body = text[end + 5:]
    return meta, body.strip() + "\n"


def check_text(path, text, label="text"):
    if HTML_TAG.search(text):
        err(path, f"{label} contains HTML; use Markdown only")
    for m in QUOTED.finditer(text):
        words = len(m.group(1).split())
        if words > MAX_QUOTE_WORDS:
            warn(path, f"{label} has a {words}-word quotation; cite the verse instead of quoting it: \"{m.group(1)[:60]}...\"")


def check_meta(path, meta):
    status = meta.get("status")
    if status is None:
        warn(path, "no status in front matter (draft / in-review / approved)")
    elif status not in STATUSES:
        err(path, f"status must be one of {sorted(STATUSES)}, got {status!r}")


def load_breakdown(path, chapter, verse_count):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(path, f"invalid JSON: {e}")
        return None, {}
    meta = {k: v for k, v in data.items() if k != "breakdown"}
    check_meta(path, meta)
    items = data.get("breakdown")
    if not isinstance(items, list) or not items:
        err(path, "'breakdown' must be a non-empty array")
        return None, meta
    expected_start = 1
    clean = []
    for i, item in enumerate(items):
        where = f"breakdown[{i}]"
        if set(item) != {"range", "title", "summary"}:
            err(path, f"{where} must have exactly range, title, summary (has {sorted(item)})")
            continue
        m = RANGE.match(item["range"])
        if not m:
            err(path, f"{where} range {item['range']!r} must look like '{chapter}:1-5' or '{chapter}:6'")
            continue
        ch, start, end = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
        if ch != chapter:
            err(path, f"{where} range {item['range']!r} is not in chapter {chapter}")
        if start > expected_start:
            err(path, f"{where} range {item['range']!r}: verses {expected_start}-{start - 1} are not covered")
        elif start < expected_start:
            err(path, f"{where} range {item['range']!r}: overlaps the previous range (should start at verse {expected_start})")
        if end < start:
            err(path, f"{where} range {item['range']!r} ends before it starts")
        expected_start = end + 1
        if not item["title"].strip() or not item["summary"].strip():
            err(path, f"{where} has an empty title or summary")
        check_text(path, item["summary"], f"{where}.summary")
        check_text(path, item["title"], f"{where}.title")
        sentences = len(re.findall(r"[.!?](\s|$)", item["summary"].strip()))
        if sentences > 3:
            warn(path, f"{where} summary has ~{sentences} sentences (aim for 1-3)")
        clean.append({"range": item["range"], "title": item["title"], "summary": item["summary"]})
    if expected_start - 1 != verse_count:
        err(path, f"breakdown covers verses 1-{expected_start - 1} but the chapter has {verse_count} verses")
    return clean, meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate only, do not write dist/")
    args = ap.parse_args()

    known_files = set()
    index = {"volumes": []}
    book_outputs = []

    for volume in CANON["volumes"]:
        vindex = {"name": volume["name"], "slug": volume["slug"], "books": []}
        for book in volume["books"]:
            chapters = {}
            status_counts = {}
            for n in range(1, book["chapters"] + 1):
                entry = {}
                for folder, (key, ext) in TABS.items():
                    path = ROOT / folder / volume["slug"] / book["slug"] / f"{book['slug']}-{n:03d}{ext}"
                    if not path.exists():
                        continue
                    known_files.add(path)
                    if ext == ".md":
                        meta, body = parse_markdown(path)
                        check_meta(path, meta)
                        if not body.strip():
                            err(path, "body is empty")
                            continue
                        check_text(path, body)
                        entry[key] = body
                    else:
                        items, meta = load_breakdown(path, n, book["verses"][n - 1])
                        if items is None:
                            continue
                        entry[key] = items
                    s = meta.get("status", "draft")
                    status_counts[s] = status_counts.get(s, 0) + 1
                if entry:
                    # fixed key order: context, breakdown, literaryUnit
                    chapters[str(n)] = {k: entry[k] for k in ("context", "breakdown", "literaryUnit") if k in entry}

            tab_counts = {
                key: sum(1 for c in chapters.values() if key in c)
                for key, _ in TABS.values()
            }
            if chapters:
                out_rel = f"{volume['slug']}/{book['slug']}.json"
                book_outputs.append((out_rel, {"book": book["name"], "chapters": chapters}))
            vindex["books"].append({
                "name": book["name"],
                "slug": book["slug"],
                "unit": book["unit"],
                "chapters": book["chapters"],
                "file": f"{volume['slug']}/{book['slug']}.json" if chapters else None,
                "chaptersWithContent": len(chapters),
                "complete": all(v == book["chapters"] for v in tab_counts.values()),
                "tabs": tab_counts,
                "status": status_counts,
            })
        index["volumes"].append(vindex)

    # any content file that does not map to a real book/chapter is a mistake
    for folder in TABS:
        for path in (ROOT / folder).rglob("*"):
            if path.is_file() and path.name != ".gitkeep" and path not in known_files:
                err(path, "file is not at a valid <volume>/<book>/<book>-<NNN> path (see canon/canon.json)")

    for line in warnings:
        print(line)
    for line in errors:
        print(line)

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s). dist/ not written.")
        sys.exit(1)

    if not args.check:
        if DIST.exists():
            for old in DIST.rglob("*.json"):
                old.unlink()
        for rel, data in book_outputs:
            out = DIST / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (DIST / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    n_ch = sum(len(d["chapters"]) for _, d in book_outputs)
    action = "validated" if args.check else "built"
    print(f"OK: {action} {len(book_outputs)} book file(s), {n_ch} chapter(s), {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()

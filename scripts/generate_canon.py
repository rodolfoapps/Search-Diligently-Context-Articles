#!/usr/bin/env python3
"""Generate canon/canon.json: every volume, book, chapter and verse count in scope.

The verse counts come from the public-domain LDS-edition scripture text published at
https://github.com/bcbooks/scriptures-json. They are used by build.py to check that each
chapter breakdown covers every verse with no gaps or overlaps.

Usage:
    python3 scripts/generate_canon.py            # downloads the source JSON
    python3 scripts/generate_canon.py DIR        # uses already-downloaded files in DIR
"""
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_URL = "https://raw.githubusercontent.com/bcbooks/scriptures-json/master/{}.json"

VOLUMES = [
    ("old-testament", "Old Testament"),
    ("new-testament", "New Testament"),
    ("book-of-mormon", "Book of Mormon"),
    ("doctrine-and-covenants", "Doctrine and Covenants"),
    ("pearl-of-great-price", "Pearl of Great Price"),
]

# Display names that differ from the source text, and slugs that are not a plain
# lowercase-hyphen version of the display name.
NAME_OVERRIDES = {
    "Solomon's Song": "Song of Solomon",
}

SLUG_OVERRIDES = {
    "Joseph Smith—Matthew": "js-matthew",
    "Joseph Smith—History": "js-history",
}


def slugify(name: str) -> str:
    if name in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[name]
    return name.lower().replace("—", "-").replace(" ", "-")


def load(volume_slug: str, local_dir):
    if local_dir:
        return json.loads((pathlib.Path(local_dir) / f"{volume_slug}.json").read_text())
    with urllib.request.urlopen(SOURCE_URL.format(volume_slug)) as r:
        return json.loads(r.read())


def main():
    local_dir = sys.argv[1] if len(sys.argv) > 1 else None
    canon = {"volumes": []}
    for vslug, vname in VOLUMES:
        data = load(vslug, local_dir)
        books = []
        if "sections" in data:  # Doctrine and Covenants
            books.append({
                "name": "Doctrine and Covenants",
                "slug": "doctrine-and-covenants",
                "unit": "section",
                "verses": [len(s["verses"]) for s in data["sections"]],
            })
        else:
            for b in data["books"]:
                name = NAME_OVERRIDES.get(b["book"], b["book"])
                books.append({
                    "name": name,
                    "slug": slugify(name),
                    "unit": "chapter",
                    "verses": [len(c["verses"]) for c in b["chapters"]],
                })
        for b in books:
            b["chapters"] = len(b["verses"])
            # keep key order readable: name, slug, unit, chapters, verses
            b_ordered = {k: b[k] for k in ("name", "slug", "unit", "chapters", "verses")}
            b.clear()
            b.update(b_ordered)
        canon["volumes"].append({"name": vname, "slug": vslug, "books": books})

    out = ROOT / "canon" / "canon.json"
    out.write_text(json.dumps(canon, indent=2, ensure_ascii=False) + "\n")
    total_books = sum(len(v["books"]) for v in canon["volumes"])
    total_ch = sum(b["chapters"] for v in canon["volumes"] for b in v["books"])
    print(f"wrote {out.relative_to(ROOT)}: {total_books} books, {total_ch} chapters/sections")


if __name__ == "__main__":
    main()

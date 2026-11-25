#!/usr/bin/env python3
"""Hebrew lookup in the Westminster Leningrad Codex (Open Scriptures Hebrew Bible).

Run scripts/tools/fetch_sources.sh first. Lemma numbers are Strong's Hebrew numbers.

  python3 -I scripts/tools/heb.py show 6:5                   # words of a verse with lemma numbers (Genesis)
  python3 -I scripts/tools/heb.py count 1:1-2:3 430          # occurrences of a lemma in a range, with verses
  python3 -I scripts/tools/heb.py words 1:1-2                # graphic-word count per verse
  python3 -I scripts/tools/heb.py --book Exod count 3:14 1961

Ranges: C:V, C:V-V, or C:V-C:V. Book codes are OSIS: Gen Exod Lev Num Deut Josh Judg Ruth 1Sam
2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos
Obad Jonah Mic Nah Hab Zeph Hag Zech Mal. Hebrew verse numbers sometimes differ from the KJV.
Ketiv forms are skipped: each ketiv/qere pair is shown and counted once, as the qere.
"""
import argparse
import pathlib
import re
import xml.etree.ElementTree as ET

NS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"
CACHE = pathlib.Path(__file__).resolve().parents[2] / ".cache" / "heb"


def parse_range(r):
    a, _, b = r.partition("-")
    c1, v1 = map(int, a.split(":"))
    if not b:
        return (c1, v1), (c1, v1)
    if ":" in b:
        c2, v2 = map(int, b.split(":"))
    else:
        c2, v2 = c1, int(b)
    return (c1, v1), (c2, v2)


def lemmas(w):
    return [re.sub(r"[^0-9]", "", p) for p in re.split(r"[/ ]", w.get("lemma", "")) if re.search(r"\d", p)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--book", default="Gen")
    ap.add_argument("cmd", choices=["show", "words", "count"])
    ap.add_argument("range")
    ap.add_argument("lemma", nargs="?")
    args = ap.parse_args()

    path = CACHE / f"{args.book}.xml"
    if not path.exists():
        raise SystemExit(f"{path} not found: run scripts/tools/fetch_sources.sh {args.book}")
    verses = {}
    for v in ET.parse(path).getroot().iter(NS + "verse"):
        _, c, n = v.get("osisID").split(".")
        # Skip ketiv words (written form) so each ketiv/qere pair counts once, as the qere (read form).
        verses[(int(c), int(n))] = [w for w in v.iter(NS + "w") if w.get("type") != "x-ketiv"]
    a, b = parse_range(args.range)
    keys = sorted(k for k in verses if a <= k <= b)
    if args.cmd == "show":
        for k in keys:
            print(f"{k[0]}:{k[1]}", " | ".join(f"{w.text}[{','.join(lemmas(w))}]" for w in verses[k]))
    elif args.cmd == "words":
        for k in keys:
            print(f"{k[0]}:{k[1]}", len(verses[k]))
    else:
        if not args.lemma:
            raise SystemExit("count needs a Strong's lemma number")
        hits = [f"{k[0]}:{k[1]}" for k in keys for w in verses[k] if args.lemma in lemmas(w)]
        print(len(hits), hits)


if __name__ == "__main__":
    main()

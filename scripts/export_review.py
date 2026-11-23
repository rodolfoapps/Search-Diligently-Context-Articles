#!/usr/bin/env python3
"""Export chapters as HTML review documents for the team's Google Drive.

Each chapter becomes one HTML file with every tab in app order, plus the reviewer-only block
(status, sources, checks). Uploading the HTML to Drive with conversion makes a native Google Doc.

Usage:
    python3 scripts/export_review.py genesis                 # every written chapter of a book
    python3 scripts/export_review.py genesis:1 isaiah:37     # specific chapters
    python3 scripts/export_review.py --out DIR ...           # default: review/

Output: <out>/<volume>/<book>/<book>-<NNN>.html
"""
import argparse
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON = json.loads((ROOT / "canon" / "canon.json").read_text())
GROUPS = [("restoration", "Restoration"), ("jewish", "Jewish"),
          ("early-christian", "Early Christian"), ("other-ancient", "Other ancient")]


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    return t


def paras(text):
    return "".join(f"<p>{inline(p.strip())}</p>" for p in text.split("\n\n") if p.strip())


def dash(r):
    return r.replace("-", "–")


def cell(c):
    ref = f" <i>({dash(c['ref'])})</i>" if c.get("ref") else ""
    return f"<b>{html.escape(c['label'])}</b>&nbsp;&nbsp;{inline(c['text'])}{ref}"


def diagram(d):
    out = []
    t = d["type"]
    frame = d.get("frame")
    if frame:
        out.append(f"<p><b>FRAME</b>&nbsp;&nbsp;{inline(frame['open']['text'])} <i>({dash(frame['open']['ref'])})</i></p>")
    rows = d.get("rows", [])
    if t == "parallel-panels":
        out.append("<table border=\"1\" cellpadding=\"4\" style=\"border-collapse:collapse\">")
        for r in rows:
            out.append(f"<tr><td>{cell(r['left'])}</td><td>{cell(r['right'])}</td></tr>")
        out.append("</table>")
    elif t == "chiasm":
        half = (len(rows) + 1) // 2
        for i, r in enumerate(rows):
            indent = i if i < half else len(rows) - 1 - i
            out.append(f"<p style=\"margin-left:{24 * indent}pt\">{cell(r)}</p>")
    elif t == "inclusio":
        for r in rows:
            out.append(f"<p style=\"margin-left:24pt\">{cell(r)}</p>")
    else:  # alternating, sequence
        for r in rows:
            out.append(f"<p>{cell(r)}</p>")
    if frame:
        out.append(f"<p><b>FRAME</b>&nbsp;&nbsp;{inline(frame['close']['text'])} <i>({dash(frame['close']['ref'])})</i></p>")
    return "\n".join(out)


def unit_map(outline, current):
    cur = set(current if isinstance(current, list) else [current])
    out = []
    strip = []
    home = None
    for s in outline["sections"]:
        here = any(sub["id"] in cur for sub in s["subsections"])
        label = f"{html.escape(s['title'])} {dash(s['range'])}"
        strip.append(f"<b>[ {label} ]</b>" if here else f"[ {label} ]")
        if here and home is None:
            home = s
    out.append(f"<p>{' '.join(strip)}</p>")
    if home:
        items = []
        for sub in home["subsections"]:
            text = f"{html.escape(sub['title'])} {dash(sub['range'])}"
            items.append(f"<li><b>▶ {text}</b> ← you are here</li>" if sub["id"] in cur else f"<li>{text}</li>")
        out.append(f"<ul>{''.join(items)}</ul>")
    return "\n".join(out)


def chapter_html(volume, book, n, data, outline):
    unit = "Section" if book["unit"] == "section" else "Chapter"
    ref = f"{book['name']} {n}"
    p = []
    p.append(f"<p><b>{html.escape(ref)}</b> · <i>{html.escape(volume['name'])} · {unit} resources for review · "
             f"Status: {html.escape(data.get('status', 'draft'))}</i></p>")
    p.append("<p><i>Reviewers: please comment or suggest rather than edit directly; accepted changes are "
             "copied back to the GitHub repository, which is what the app reads.</i></p>")
    if "overview" in data:
        p += ["<h1>Overview</h1>", paras(data["overview"])]
    if "historicalContext" in data:
        p.append("<h1>Historical Context</h1><ul>")
        p += [f"<li><b>{html.escape(b['label'])}:</b> {inline(b['text'])}</li>" for b in data["historicalContext"]]
        p.append("</ul>")
    if "hermeneutics" in data:
        p += ["<h1>Hermeneutics</h1>", paras(data["hermeneutics"])]
    if "breakdown" in data:
        p.append("<h1>Chapter Breakdown</h1><table border=\"1\" cellpadding=\"4\" style=\"border-collapse:collapse\">"
                 "<tr><td><b>Verses</b></td><td><b>Unit</b></td></tr>")
        for r in data["breakdown"]:
            rng, lab = html.escape(dash(r["range"])), inline(r["label"])
            if r.get("overflow"):
                rng, lab = f"<i>{rng}</i>", f"<i>{lab} (outside this chapter)</i>"
            p.append(f"<tr><td>{rng}</td><td>{lab}</td></tr>")
        p.append("</table>")
    if "structure" in data:
        s = data["structure"]
        p += ["<h1>Literary Structure</h1>", f"<p><i>{inline(s.get('summary', ''))}</i></p>", diagram(s)]
        for sec in s.get("secondary", []):
            p += [f"<p><b>{inline(sec['title'])}</b></p>", diagram(sec)]
        p += [f"<p>{inline(x)}</p>" for x in s.get("notes", [])]
    if "unit" in data and outline:
        p += ["<h1>Literary Unit</h1>", unit_map(outline, data["unit"]["current"])]
        p += [f"<p>{inline(x)}</p>" for x in data["unit"].get("notes", [])]
    if "traditions" in data:
        p += ["<h1>Traditions</h1>",
              "<p><i>How early readers received this chapter. These are traditions, not history; "
              "each is labeled by who held it.</i></p>"]
        for key, title in GROUPS:
            entries = [e for e in data["traditions"] if e["group"] == key]
            if not entries:
                continue
            p.append(f"<h2>{title}</h2><ul>")
            for e in entries:
                p.append(f"<li><b>{inline(e['source'])} ({html.escape(e['date'])}).</b> {inline(e['text'])} "
                         f"<i>({inline(e['cite'])})</i></li>")
            p.append("</ul>")
    review = data.get("review", {})
    p.append("<h1>Reviewer-only (not shown in app)</h1>")
    if review.get("sources"):
        p.append("<h2>Sources</h2><ul>" + "".join(f"<li>{inline(s)}</li>" for s in review["sources"]) + "</ul>")
    if review.get("checks"):
        p.append("<h2>Checks</h2><ul>" + "".join(f"<li>{inline(s)}</li>" for s in review["checks"]) + "</ul>")
    body = "\n".join(p)
    return (f"<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\"><title>{html.escape(ref)}</title></head>\n"
            f"<body>\n{body}\n</body></html>\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="+", help="book slug, or slug:chapter")
    ap.add_argument("--out", default=str(ROOT / "review"))
    args = ap.parse_args()
    books = {b["slug"]: (v, b) for v in CANON["volumes"] for b in v["books"]}
    written = 0
    for target in args.targets:
        slug, _, ch = target.partition(":")
        if slug not in books:
            sys.exit(f"unknown book slug: {slug}")
        volume, book = books[slug]
        folder = ROOT / "content" / volume["slug"] / book["slug"]
        opath = folder / "_book-outline.json"
        outline = json.loads(opath.read_text()) if opath.exists() else None
        for n in ([int(ch)] if ch else range(1, book["chapters"] + 1)):
            src = folder / f"{book['slug']}-{n:03d}.json"
            if not src.exists():
                continue
            data = json.loads(src.read_text(encoding="utf-8"))
            out = pathlib.Path(args.out) / volume["slug"] / book["slug"] / f"{book['slug']}-{n:03d}.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(chapter_html(volume, book, n, data, outline), encoding="utf-8")
            print(out)
            written += 1
    print(f"{written} review document(s) written", file=sys.stderr)


if __name__ == "__main__":
    main()

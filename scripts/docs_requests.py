#!/usr/bin/env python3
"""Build a Google Docs batchUpdate that replaces a review Doc's body with a chapter's current content.

Used to refresh an existing Doc in place (same link) instead of creating a new one.

    python3 scripts/docs_requests.py <book-slug>:<chapter> <body-end-index> > requests.json

<body-end-index> is the endIndex of the Doc body's last element (from read_doc). The batch deletes
the old body, inserts the new text, then applies headings, bullets, indents and bold/italic.
Send it with writeControl.requiredRevisionId from the same read.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON = json.loads((ROOT / "canon" / "canon.json").read_text())
GROUPS = [("restoration", "Restoration"), ("jewish", "Jewish"),
          ("early-christian", "Early Christian"), ("other-ancient", "Other ancient")]


def u16(s):
    return len(s.encode("utf-16-le")) // 2


def runs(md):
    """Split Markdown (**bold**, *italic*, ***both***) into plain text plus style spans."""
    out, spans, pos = [], [], 0
    pattern = re.compile(r"\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")
    i = 0
    for m in pattern.finditer(md):
        out.append(md[i:m.start()])
        text = m.group(1) or m.group(2) or m.group(3)
        start = sum(u16(x) for x in out)
        out.append(text)
        style = {"bold": True, "italic": True} if m.group(1) else ({"bold": True} if m.group(2) else {"italic": True})
        spans.append((start, start + u16(text), style))
        i = m.end()
    out.append(md[i:])
    return "".join(out), spans


class Doc:
    def __init__(self):
        self.paras = []  # (text, spans, kind, extra)

    def add(self, md, kind="p", extra=None, raw_spans=None):
        text, spans = runs(md)
        self.paras.append((text, spans + (raw_spans or []), kind, extra))

    def para_md(self, md):
        for p in md.split("\n\n"):
            if p.strip():
                self.add(p.strip())


def dash(r):
    return r.replace("-", "–")


def cell(c):
    ref = f" *({dash(c['ref'])})*" if c.get("ref") else ""
    return f"**{c['label']}**  {c['text']}{ref}"


def build(volume, book, n, data, outline):
    d = Doc()
    unit = "Section" if book["unit"] == "section" else "Chapter"
    d.add(f"**{book['name']} {n}** · *{volume['name']} · {unit} resources for review · Status: {data.get('status', 'draft')}*")
    d.add("*Reviewers: please comment or suggest rather than edit directly; accepted changes are copied back "
          "to the GitHub repository, which is what the app reads.*")
    if "overview" in data:
        d.add("Overview", "h1"); d.para_md(data["overview"])
    if "historicalContext" in data:
        d.add("Historical Context", "h1")
        for b in data["historicalContext"]:
            d.add(f"**{b['label']}:** {b['text']}", "bullet")
    if "hermeneutics" in data:
        d.add("Hermeneutics", "h1"); d.para_md(data["hermeneutics"])
    if "breakdown" in data:
        d.add("Chapter Breakdown", "h1")
        for r in data["breakdown"]:
            if r.get("overflow"):
                d.add(f"*{dash(r['range'])}  {r['label']} (outside this chapter)*", "bullet")
            else:
                d.add(f"**{dash(r['range'])}**  {r['label']}", "bullet")
    if "structure" in data:
        s = data["structure"]
        d.add("Literary Structure", "h1")
        d.add(f"*{s.get('summary', '')}*")
        for j, dg in enumerate([s] + list(s.get("secondary", []))):
            if j:
                d.add(f"**{dg['title']}**")
            fr = dg.get("frame")
            if fr:
                d.add(f"**FRAME**  {fr['open']['text']} *({dash(fr['open']['ref'])})*")
            rows = dg.get("rows", [])
            half = (len(rows) + 1) // 2
            for i, r in enumerate(rows):
                if dg["type"] == "parallel-panels":
                    d.add(f"{cell(r['left'])}   ↔   {cell(r['right'])}")
                elif dg["type"] == "chiasm":
                    d.add(cell(r), "indent", 18 * (i if i < half else len(rows) - 1 - i))
                elif dg["type"] == "inclusio":
                    d.add(cell(r), "indent", 18)
                else:
                    d.add(cell(r))
            if fr:
                d.add(f"**FRAME**  {fr['close']['text']} *({dash(fr['close']['ref'])})*")
        for x in s.get("notes", []):
            d.add(x)
    if "unit" in data and outline:
        cur = data["unit"]["current"]
        cur = set(cur if isinstance(cur, list) else [cur])
        d.add("Literary Unit", "h1")
        home, strip = None, []
        for sec in outline["sections"]:
            here = any(x["id"] in cur for x in sec["subsections"])
            lab = f"[ {sec['title']} {dash(sec['range'])} ]"
            strip.append(f"**{lab}**" if here else lab)
            home = home or (sec if here else None)
        d.add(" ".join(strip))
        if home:
            for sub in home["subsections"]:
                t = f"{sub['title']} {dash(sub['range'])}"
                d.add(f"**▶ {t}** ← you are here" if sub["id"] in cur else t, "bullet")
        for x in data["unit"].get("notes", []):
            d.add(x)
    if "traditions" in data:
        d.add("Traditions", "h1")
        d.add("*How early readers received this chapter. These are traditions, not history; "
              "each is labeled by who held it.*")
        for key, title in GROUPS:
            es = [e for e in data["traditions"] if e["group"] == key]
            if not es:
                continue
            d.add(title, "h2")
            for e in es:
                d.add(f"**{e['source']} ({e['date']}).** {e['text']} *({e['cite']})*", "bullet")
    rv = data.get("review", {})
    d.add("Reviewer-only (not shown in app)", "h1")
    if rv.get("sources"):
        d.add("Sources", "h2")
        for x in rv["sources"]:
            d.add(x, "bullet")
    if rv.get("checks"):
        d.add("Checks", "h2")
        for x in rv["checks"]:
            d.add(x, "bullet")
    return d


def requests(doc, body_end):
    text = "\n".join(p[0] for p in doc.paras) + "\n"
    reqs = []
    if body_end > 2:
        reqs.append({"deleteContentRange": {"range": {"startIndex": 1, "endIndex": body_end - 1}}})
    reqs.append({"insertText": {"location": {"index": 1}, "text": text}})
    total_end = 1 + u16(text)
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": 1, "endIndex": total_end},
                                          "paragraphStyle": {"namedStyleType": "NORMAL_TEXT", "indentStart": {"magnitude": 0, "unit": "PT"},
                                                             "indentFirstLine": {"magnitude": 0, "unit": "PT"},
                                                             "spaceBelow": {"magnitude": 6, "unit": "PT"}},
                                          "fields": "namedStyleType,indentStart,indentFirstLine,spaceBelow"}})
    reqs.append({"deleteParagraphBullets": {"range": {"startIndex": 1, "endIndex": total_end + 1}}})  # +1: the old trailing paragraph
    reqs.append({"updateTextStyle": {"range": {"startIndex": 1, "endIndex": total_end},
                                     "textStyle": {}, "fields": "bold,italic"}})
    pos = 1
    bullet_start = None
    for k, (t, spans, kind, extra) in enumerate(doc.paras):
        start, end = pos, pos + u16(t) + 1
        if kind in ("h1", "h2"):
            reqs.append({"updateParagraphStyle": {"range": {"startIndex": start, "endIndex": end},
                                                  "paragraphStyle": {"namedStyleType": "HEADING_1" if kind == "h1" else "HEADING_2",
                                                                     "keepWithNext": True},
                                                  "fields": "namedStyleType,keepWithNext"}})
        if kind == "indent" and extra:
            reqs.append({"updateParagraphStyle": {"range": {"startIndex": start, "endIndex": end},
                                                  "paragraphStyle": {"indentStart": {"magnitude": extra, "unit": "PT"}},
                                                  "fields": "indentStart"}})
        for a, b, style in spans:
            reqs.append({"updateTextStyle": {"range": {"startIndex": start + a, "endIndex": start + b},
                                             "textStyle": style, "fields": ",".join(style)}})
        if kind == "bullet" and bullet_start is None:
            bullet_start = start
        nxt = doc.paras[k + 1][2] if k + 1 < len(doc.paras) else None
        if kind == "bullet" and nxt != "bullet":
            reqs.append({"createParagraphBullets": {"range": {"startIndex": bullet_start, "endIndex": end - 1},
                                                    "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
            bullet_start = None
        pos = end
    return reqs


def main():
    target, body_end = sys.argv[1], int(sys.argv[2])
    slug, _, ch = target.partition(":")
    volume, book = next((v, b) for v in CANON["volumes"] for b in v["books"] if b["slug"] == slug)
    folder = ROOT / "content" / volume["slug"] / book["slug"]
    data = json.loads((folder / f"{slug}-{int(ch):03d}.json").read_text())
    opath = folder / "_book-outline.json"
    outline = json.loads(opath.read_text()) if opath.exists() else None
    print(json.dumps(requests(build(volume, book, int(ch), data, outline), body_end), ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()

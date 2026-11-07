#!/usr/bin/env python3
"""Export chapters as HTML review documents for the team's Google Drive.

Each chapter becomes one HTML file holding all of its tabs (Historical Context,
Chapter Breakdown, Literary Unit) plus the reviewer-only sources and status.
Uploading the HTML to Drive with conversion turns it into a native Google Doc
with real headings, lists and formatting.

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

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build  # noqa: E402  (reuses canon + front-matter parsing)

ROOT = build.ROOT
TAB_ORDER = [
    ("historical-context", "Historical Context", ".md"),
    ("chapter-breakdown", "Chapter Breakdown", ".json"),
    ("literary-unit", "Literary Unit", ".md"),
]


def inline(text: str) -> str:
    """Escape HTML, then apply **bold**, *italic*, and `code`."""
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def md_to_html(md: str, heading_shift: int = 0) -> str:
    """Convert the Markdown subset used in this repo: headings, paragraphs,
    bullet/numbered lists (nested by indentation), and blockquotes."""
    out = []
    list_stack = []  # (tag, indent)
    para = []
    after_blank = False

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def close_lists(to_indent=-1):
        while list_stack and list_stack[-1][1] > to_indent:
            tag, _ = list_stack.pop()
            out.append(f"</li></{tag}>")

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            after_blank = True
            continue
        was_blank, after_blank = after_blank, False
        m_h = re.match(r"^(#{1,6})\s+(.*)$", line)
        m_li = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        m_q = re.match(r"^>\s?(.*)$", line)
        if m_h:
            flush_para(); close_lists()
            level = min(6, len(m_h.group(1)) + heading_shift)
            out.append(f"<h{level}>{inline(m_h.group(2))}</h{level}>")
        elif m_li:
            flush_para()
            indent = len(m_li.group(1))
            tag = "ol" if m_li.group(2)[0].isdigit() else "ul"
            if list_stack and indent < list_stack[-1][1]:
                close_lists(indent)
            if not list_stack or indent > list_stack[-1][1]:
                out.append(f"<{tag}><li>")
                list_stack.append((tag, indent))
            else:
                out.append("</li><li>")
            out.append(inline(m_li.group(3)))
        elif m_q:
            flush_para(); close_lists()
            out.append(f"<blockquote><p>{inline(m_q.group(1))}</p></blockquote>")
        else:
            if list_stack and was_blank:  # a paragraph after a list ends the list
                close_lists()
            if list_stack:  # continuation of a list item
                out.append(" " + inline(line.strip()))
            else:
                para.append(line.strip())
    flush_para(); close_lists()
    return "\n".join(out)


def chapter_html(volume, book, n):
    unit = "Section" if book["unit"] == "section" else "Chapter"
    ref = f"{book['name']} {n}"
    parts = []
    statuses, sources = [], []
    for folder, label, ext in TAB_ORDER:
        path = ROOT / folder / volume["slug"] / book["slug"] / f"{book['slug']}-{n:03d}{ext}"
        parts.append(f"<h1>{label}</h1>")
        if not path.exists():
            parts.append("<p><i>Not written yet.</i></p>")
            continue
        if ext == ".md":
            meta, body = build.parse_markdown(path)
            parts.append(md_to_html(body))
        else:
            data = json.loads(path.read_text(encoding="utf-8"))
            meta = {k: v for k, v in data.items() if k != "breakdown"}
            for item in data["breakdown"]:
                parts.append(f"<h2>{html.escape(item['range'])} — {inline(item['title'])}</h2>")
                parts.append(f"<p>{inline(item['summary'])}</p>")
        statuses.append(f"{label}: {meta.get('status', 'draft')}")
        for s in meta.get("sources", []) or []:
            if s not in sources:
                sources.append(s)

    head = [
        f"<p><b>{html.escape(ref)}</b> · <i>{html.escape(volume['name'])} · {unit} resources for review · Source of truth: GitHub repository "
        f"(files under {html.escape(volume['slug'])}/{html.escape(book['slug'])}/{html.escape(book['slug'])}-{n:03d}).</i></p>",
        f"<p><b>Status</b> — {html.escape('; '.join(statuses) or 'nothing written')}</p>",
        "<p>Reviewers: please leave feedback as comments or suggestions rather than direct edits, "
        "so changes can be carried back to the repository.</p>",
    ]
    tail = ["<h1>Sources (reviewers only, not shown in the app)</h1>"]
    tail.append("<ul>" + "".join(f"<li>{inline(s)}</li>" for s in sources) + "</ul>" if sources else "<p><i>None listed.</i></p>")
    body = "\n".join(head + parts + tail)
    return f"<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\"><title>{html.escape(ref)}</title></head>\n<body>\n{body}\n</body></html>\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="+", help="book slug, or slug:chapter")
    ap.add_argument("--out", default=str(ROOT / "review"))
    args = ap.parse_args()

    books = {b["slug"]: (v, b) for v in build.CANON["volumes"] for b in v["books"]}
    out_root = pathlib.Path(args.out)
    written = 0
    for target in args.targets:
        slug, _, ch = target.partition(":")
        if slug not in books:
            sys.exit(f"unknown book slug: {slug}")
        volume, book = books[slug]
        chapters = [int(ch)] if ch else range(1, book["chapters"] + 1)
        for n in chapters:
            exists = any(
                (ROOT / f / volume["slug"] / book["slug"] / f"{book['slug']}-{n:03d}{e}").exists()
                for f, _, e in TAB_ORDER
            )
            if not exists:
                continue
            path = out_root / volume["slug"] / book["slug"] / f"{book['slug']}-{n:03d}.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(chapter_html(volume, book, n), encoding="utf-8")
            print(path)
            written += 1
    print(f"{written} review document(s) written", file=sys.stderr)


if __name__ == "__main__":
    main()

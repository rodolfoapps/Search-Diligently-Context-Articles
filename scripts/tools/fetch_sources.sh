#!/usr/bin/env bash
# Download the reference texts the research tools need into .cache/ (not committed).
#   KJV + LDS scriptures: github.com/bcbooks/scriptures-json (public domain text)
#   Hebrew Bible: Westminster Leningrad Codex, github.com/openscriptures/morphhb
# Usage: scripts/tools/fetch_sources.sh [OSIS book codes for Hebrew, default: all]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$ROOT/.cache/src" "$ROOT/.cache/heb"
for f in old-testament new-testament book-of-mormon doctrine-and-covenants pearl-of-great-price; do
  curl -sSfL -o "$ROOT/.cache/src/$f.json" "https://raw.githubusercontent.com/bcbooks/scriptures-json/master/$f.json"
done
BOOKS="${*:-Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal}"
for b in $BOOKS; do
  curl -sSfL -o "$ROOT/.cache/heb/$b.xml" "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/$b.xml"
done
echo "Sources saved in $ROOT/.cache"

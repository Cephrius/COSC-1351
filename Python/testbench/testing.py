#!/usr/bin/env python3
"""
Decode the secret message from a published Google Doc that lists
(x-coordinate, Character, y-coordinate) rows.

Usage:
    python decode_secret.py "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
"""

import sys
import re
from typing import Dict, Tuple
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install dependencies first: pip install requests beautifulsoup4")
    sys.exit(1)

def decode_grid(doc_url: str) -> str:
    # 1) fetch HTML
    html = requests.get(doc_url, timeout=30).text

    # 2) parse rows — the published doc is rendered as a simple HTML flow;
    #    grabbing all text and extracting triples is more robust than relying
    #    on class names that can change.
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n")

    # We expect the data in repeating chunks: x, char(█ or ░), y.
    # Build a lightweight tokenizer that walks through numbers and block chars.
    tokens = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # numbers
        if re.fullmatch(r"-?\d+", line):
            tokens.append(int(line))
        # characters (block or light shade)
        elif line in ("█", "░", " "):
            tokens.append(line)

    # 3) turn tokens into triples: (x, ch, y)
    triples = []
    i = 0
    while i + 2 < len(tokens):
        if isinstance(tokens[i], int) and isinstance(tokens[i+2], int) and isinstance(tokens[i+1], str):
            triples.append((tokens[i], tokens[i+1], tokens[i+2]))
            i += 3
        else:
            i += 1  # resync if any oddity

    if not triples:
        raise RuntimeError("No coordinate triples found. The document format may have changed.")

    # 4) build grid map
    grid: Dict[Tuple[int, int], str] = {}
    xs, ys = [], []
    for x, ch, y in triples:
        grid[(x, y)] = ch
        xs.append(x); ys.append(y)

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Normalize so the smallest coordinate is at 0,0 (not necessary, but tidy)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    lines = []
    for y in range(min_y, max_y + 1):
        row_chars = []
        for x in range(min_x, max_x + 1):
            row_chars.append(grid.get((x, y), " "))
        lines.append("".join(row_chars).rstrip())

    return "\n".join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python decode_secret.py <published_google_doc_url>")
        sys.exit(2)
    url = sys.argv[1].strip()
    art = decode_grid(url)
    # Print with an explicit monospace hint (terminal is already monospace).
    print(art)

if __name__ == "__main__":
    main()

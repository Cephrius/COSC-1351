#!/usr/bin/env ts-node

/**
 * testing.ts
 * Decode the secret message from a published Google Doc containing (x, char, y) triples.
 */

type Triple = [number, string, number];

function stripHtmlToText(html: string): string {
  const withoutTags = html
    .replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi, "")
    .replace(/<[^>]+>/g, "\n");

  return withoutTags
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&#160;/g, " ")
    .replace(/\r/g, "")
    .split("\n")
    .map(l => l.trim())
    .filter(l => l.length > 0)
    .join("\n");
}

function tokensFromText(text: string): Array<number | string> {
  const tokens: Array<number | string> = [];
  for (const line of text.split("\n")) {
    if (/^-?\d+$/.test(line)) {
      tokens.push(parseInt(line, 10));
    } else if (line === "█" || line === "░" || line === " ") {
      tokens.push(line);
    }
  }
  return tokens;
}

function triplesFromTokens(tokens: Array<number | string>): Triple[] {
  const triples: Triple[] = [];
  for (let i = 0; i + 2 < tokens.length; ) {
    const a = tokens[i], b = tokens[i + 1], c = tokens[i + 2];
    if (typeof a === "number" && typeof c === "number" && typeof b === "string") {
      triples.push([a, b, c]);
      i += 3;
    } else {
      i += 1;
    }
  }
  return triples;
}

function gridFromTriples(triples: Triple[]): string {
  if (triples.length === 0) {
    throw new Error("No coordinate triples found. The document format may have changed.");
  }

  const grid = new Map<string, string>();
  const xs: number[] = [];
  const ys: number[] = [];

  for (const [x, ch, y] of triples) {
    grid.set(`${x},${y}`, ch);
    xs.push(x);
    ys.push(y);
  }

  const minX = Math.min(...xs), maxX = Math.max(...xs);
  const minY = Math.min(...ys), maxY = Math.max(...ys);

  const lines: string[] = [];
  for (let y = minY; y <= maxY; y++) {
    let row = "";
    for (let x = minX; x <= maxX; x++) {
      row += grid.get(`${x},${y}`) ?? " ";
    }
    lines.push(row.replace(/\s+$/g, ""));
  }
  return lines.join("\n");
}

async function decodeGrid(url: string): Promise<string> {
  const res = await fetch(url, { redirect: "follow" });
  if (!res.ok) throw new Error(`Fetch failed: ${res.status} ${res.statusText}`);
  const html = await res.text();

  const text = stripHtmlToText(html);
  const tokens = tokensFromText(text);
  const triples = triplesFromTokens(tokens);
  return gridFromTriples(triples);
}

// CLI
(async () => {
  const url = process.argv[2];
  if (!url) {
    console.error("Usage: ts-node testing.ts <published_google_doc_url>");
    process.exit(2);
  }
  const art = await decodeGrid(url);
  console.log(art);
})();

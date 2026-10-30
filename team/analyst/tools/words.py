#!/usr/bin/env python3
"""Words outside markdown at a pinned commit: HTML text and JSON string values.

Usage: python3 team/analyst/tools/words.py <source clone> [commit]

HTML: tags, <script> and <style> removed, then whitespace-separated tokens.
JSON: every string value (not keys), tokens as above. Reads git objects only.
"""
import collections, json, re, subprocess, sys

SRC = sys.argv[1]
REV = sys.argv[2] if len(sys.argv) > 2 else "298be4e"


def git(*args):
    return subprocess.run(["git", "-C", SRC, *args], check=True,
                          capture_output=True, text=True).stdout


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


def area(f):
    parts = f.split("/")
    return "/".join(parts[:2]) if parts[0] in ("team", "src", "evidence") and len(parts) > 2 else parts[0]


html_w, json_w, bad = collections.Counter(), collections.Counter(), 0
for f in git("ls-tree", "-r", "--name-only", REV).split():
    if f.endswith(".html"):
        t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", git("show", f"{REV}:{f}"))
        t = re.sub(r"(?s)<!--.*?-->|<[^>]+>", " ", t)
        html_w[area(f)] += len(re.findall(r"\S+", t))
    elif f.endswith(".json"):
        try:
            json_w[area(f)] += sum(len(re.findall(r"\S+", s)) for s in strings(json.loads(git("show", f"{REV}:{f}"))))
        except ValueError:
            bad += 1
print(f"words in HTML text\t{sum(html_w.values())}\ttags, script and style removed")
for k, v in html_w.most_common(6):
    print(f"  html: {k}\t{v}\tthe same")
print(f"words in JSON string values\t{sum(json_w.values())}\tstring values only, not keys")
for k, v in json_w.most_common(6):
    print(f"  json: {k}\t{v}\tthe same")
print(f"JSON files that do not parse\t{bad}\tjson.loads")

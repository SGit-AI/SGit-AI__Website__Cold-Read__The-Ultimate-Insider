#!/usr/bin/env python3
"""Recompute the analyst's numbers from the source at a pinned commit.

Usage: python3 team/analyst/tools/numbers.py <source clone> [commit]

Reads only git history reachable from the commit (default 298be4e) and files
at that commit (git show / git ls-tree), never the working tree, so a later
checkout cannot leak in. Prints one line per number: name, value, method.
"""
import collections, json, subprocess, sys

SRC = sys.argv[1]
REV = sys.argv[2] if len(sys.argv) > 2 else "298be4e"


def git(*args):
    return subprocess.run(["git", "-C", SRC, *args], check=True,
                          capture_output=True, text=True).stdout


def out(name, value, method):
    print(f"{name}\t{value}\t{method}")


full = git("rev-parse", REV).strip()
out("commit", full, "git rev-parse")
out("commits", git("rev-list", "--count", REV).strip(), "git rev-list --count")
out("merges", git("rev-list", "--count", "--merges", REV).strip(), "git rev-list --count --merges")
out("non-merge commits", git("rev-list", "--count", "--no-merges", REV).strip(), "git rev-list --count --no-merges")
out("first-parent commits", git("rev-list", "--count", "--first-parent", REV).strip(), "git rev-list --count --first-parent")

dates = git("log", "--format=%aI", REV).split()
out("first author date", min(dates), "git log --format=%aI, min")
out("last author date", max(dates), "git log --format=%aI, max")

for line in git("shortlog", "-sn", REV).splitlines():
    n, who = line.strip().split("\t")
    out(f"commits by author name: {who}", n, "git shortlog -sn")

subjects = git("log", "--format=%s", REV).splitlines()
out("release commits", sum(s.startswith("site v") for s in subjects), "subjects starting 'site v'")
tags = [t for t in git("tag", "--merged", REV).split() if t.startswith("v")]
out("release tags reachable", len(tags), "git tag --merged, names starting v")

prefix = collections.Counter(s.split(":")[0] for s in subjects if s.startswith("@") and ":" in s)
for who, n in prefix.most_common():
    out(f"commits marked {who}:", n, "subject prefix '@<id>:'")
trail = collections.Counter(t for t in git("log", "--format=%(trailers:key=Agent,valueonly)", REV).split() if t)
for who, n in trail.most_common():
    out(f"commits with trailer Agent: {who}", n, "%(trailers:key=Agent)")

hours = collections.Counter(d[11:13] for d in git("log", "--format=%ad", "--date=iso-strict-local", REV).split())
out("commits per author hour (UTC)", " ".join(f"{h}:{hours[h]}" for h in sorted(hours)), "git log --date=iso-strict, TZ=UTC")

files = git("ls-tree", "-r", "--name-only", REV, "team/").splitlines()
members = sorted({f.split("/")[1] for f in files if f.count("/") >= 2})
out("team folders", f"{len(members)} ({', '.join(members)})", "git ls-tree team/")
outcomes = collections.Counter()
for m in members:
    wakes = [f for f in files if f.startswith(f"team/{m}/wakes/") and f.endswith(".json")]
    debriefs = [f for f in files if f.startswith(f"team/{m}/debriefs/") and f.endswith(".md")]
    for w in wakes:
        try:
            outcomes[json.loads(git("show", f"{REV}:{w}")).get("outcome")] += 1
        except ValueError:
            outcomes["unreadable"] += 1
    out(f"wake records / debriefs: {m}", f"{len(wakes)} / {len(debriefs)}", "git ls-tree team/<m>/wakes/*.json, debriefs/*.md")
out("wake records, all", sum(outcomes.values()), "sum of the above")
out("wake outcomes", ", ".join(f"{k}:{v}" for k, v in outcomes.most_common()), "field 'outcome' in each wake record")

unmarked = [s for s in git("log", "--no-merges", "--author=Claude", "--format=%s", REV).splitlines() if not s.startswith("@")]
heads = collections.Counter(s.split(":")[0] if s.split(":")[0] in ("ruv-sgit", "conductor", "Player") else "(other)" for s in unmarked)
out("unmarked non-merge commits by Claude", len(unmarked), "subjects not starting '@'")
out("unmarked, by subject start", ", ".join(f"{k}:{v}" for k, v in heads.most_common()), "text before the first ':'")

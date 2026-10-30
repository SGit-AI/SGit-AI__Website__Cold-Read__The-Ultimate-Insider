#!/usr/bin/env python3
"""Verdicts, wake durations, holds and words, from the source at a pinned commit.

Usage: python3 team/analyst/tools/wakes.py <source clone> [commit]

Reads git objects only (ls-tree, show, log), never the working tree.
"""
import collections, datetime, json, re, statistics, subprocess, sys

SRC = sys.argv[1]
REV = sys.argv[2] if len(sys.argv) > 2 else "298be4e"
PLAIN = {"go", "clean", "done", "as-planned"}
STEPS = ("plan", "pre_review", "work", "post_review", "post_check")


def git(*args):
    return subprocess.run(["git", "-C", SRC, *args], check=True,
                          capture_output=True, text=True).stdout


def out(name, value, method):
    print(f"{name}\t{value}\t{method}")


def ts(s):
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))


def records(rev):
    for f in git("ls-tree", "-r", "--name-only", rev, "team/").split():
        if "/wakes/" in f and f.endswith(".json"):
            yield f, json.loads(git("show", f"{rev}:{f}"))


def verdicts(rev):
    final, hist, prose, per_step = 0, 0, 0, collections.Counter()
    for _, d in records(rev):
        for step, v in (d.get("steps") or {}).items():
            if isinstance(v, dict) and v.get("verdict") not in PLAIN:
                final += 1
                per_step[f"{step}:{v.get('verdict')}"] += 1
        for h in d.get("history") or []:
            # three shapes: {step: {verdict}}, {step, verdict}, and {at, what} in prose
            if "verdict" in h:
                hist += h["verdict"] not in PLAIN
            elif "what" in h:
                prose += bool(re.search(r"said change|change mid-work", h["what"]))
            else:
                hist += sum(isinstance(v, dict) and v.get("verdict") not in PLAIN for v in h.values())
    return final, hist, prose, per_step


# the article's own commit, then the pin
art = git("log", "-1", "--format=%h", REV, "--", "content/articles/the-night-hour-by-hour.md").strip()
for rev in (art, REV):
    final, hist, prose, per_step = verdicts(rev)
    out(f"verdicts other than go/clean/done/as-planned at {rev}", f"{final} in steps, {hist} more in history, {prose} more in history prose",
        "steps.*.verdict and history[].*.verdict of team/*/wakes/*.json")
    out(f"  by step and verdict at {rev}", ", ".join(f"{k} {v}" for k, v in sorted(per_step.items())), "the same")

recs = list(records(REV))
full = sum(all(s in (d.get("steps") or {}) for s in STEPS) for _, d in recs)
out("wake records with all five steps", f"{full} of {len(recs)}", "steps has plan..post_check")
mins = collections.defaultdict(list)
for f, d in recs:
    if d.get("started") and d.get("closed"):
        mins[f.split("/")[1]].append((ts(d["closed"]) - ts(d["started"])).total_seconds() / 60)
allm = [m for v in mins.values() for m in v]
out("wake minutes, started to closed", f"n {len(allm)}, median {statistics.median(allm):.1f}, mean {statistics.mean(allm):.1f}, max {max(allm):.1f}, total {sum(allm)/60:.1f} h",
    "closed minus started")
for who, v in sorted(mins.items()):
    out(f"  wake minutes: {who}", f"n {len(v)}, median {statistics.median(v):.1f}, max {max(v):.1f}", "the same")
out("wakes over 45 minutes", sum(m > 45 for m in allm), "the source's limit on the work, WAKE.md")

holds = git("log", "--format=%h %aI %s", "--diff-filter=A", REV, "--", "team/*/HOLD.md").splitlines()
out("HOLD.md files ever added", len(holds), "git log --diff-filter=A -- team/*/HOLD.md")
for h in holds:
    out("  hold", h, "the same")
out("HOLD.md at the pin", sum(f.endswith("/HOLD.md") for f in git("ls-tree", "-r", "--name-only", REV, "team/").split()), "git ls-tree")
out("wakes with outcome hold", sum(d.get("outcome") == "hold" for _, d in recs), "outcome field")

words = collections.Counter()
for f in git("ls-tree", "-r", "--name-only", REV).split():
    if f.endswith(".md"):
        area = "/".join(f.split("/")[:2]) if f.startswith(("team/", "content/", "evidence/")) else "(top level and other)"
        words[area.split("/")[0] if not f.startswith("team/") else area] += len(re.findall(r"\S+", git("show", f"{REV}:{f}")))
out("words in .md files", sum(words.values()), "whitespace-separated tokens, every tracked .md")
for k, v in words.most_common():
    out(f"  words: {k}", v, "the same")
deb = sum(len(re.findall(r"\S+", git("show", f"{REV}:{f}"))) for f in git("ls-tree", "-r", "--name-only", REV, "team/").split() if "/debriefs/" in f and f.endswith(".md"))
out("words in debriefs", deb, "team/*/debriefs/*.md")

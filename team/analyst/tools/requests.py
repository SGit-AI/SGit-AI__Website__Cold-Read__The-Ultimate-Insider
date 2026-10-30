#!/usr/bin/env python3
"""Requests and replies kept as files in the source's git (team/*/requests/), and the time between.

Usage: python3 team/analyst/tools/requests.py <source clone> [commit]

Each file is a letter with headers (From, To, Date, X-Kind, References). Two clocks:
the Date header (written by hand) and the commit that first added the file (git).
A reply is paired with the request its References names first.
"""
import collections, datetime, email.utils, subprocess, sys

SRC = sys.argv[1]
REV = sys.argv[2] if len(sys.argv) > 2 else "298be4e"


def git(*args):
    return subprocess.run(["git", "-C", SRC, *args], check=True,
                          capture_output=True, text=True).stdout


def added(path):
    """Author time of the commit that first added the path, at or before REV."""
    lines = git("log", "--diff-filter=A", "--format=%h %aI", REV, "--", path).split("\n")
    h, t = [l for l in lines if l][-1].split()
    return h, datetime.datetime.fromisoformat(t)


def headers(text):
    h = {}
    for line in text.split("\n"):
        if not line.strip():
            break
        k, _, v = line.partition(":")
        h[k.strip()] = v.strip()
    return h


ever = git("log", "--diff-filter=A", "--name-only", "--format=", REV, "--", "team/*/requests/*").split()
now = [f for f in git("ls-tree", "-r", "--name-only", REV, "team/").split() if "/requests/" in f]
print(f"request files ever added\t{len(set(ever))}\tgit log --diff-filter=A -- team/*/requests/*")
print(f"request files at the pin\t{len(now)}\tgit ls-tree")
letters = {}
for f in now:
    h = headers(git("show", f"{REV}:{f}"))
    date = email.utils.parsedate_to_datetime(h["Date"]) if "Date" in h else None
    letters[f] = (h.get("X-Kind", "(no headers)"), date, *added(f), h.get("References", ""))
kinds = collections.Counter(v[0] for v in letters.values())
print(f"by X-Kind\t{', '.join(f'{k} {v}' for k, v in kinds.most_common())}\theader X-Kind")
pairs = collections.Counter(f"{f.split('/')[1]} > {f.split('/')[3].split('__')[0]}" for f in now)
print(f"sender > recipient\t{', '.join(f'{k} {v}' for k, v in pairs.most_common())}\tteam/<sender>/requests/<recipient>__*")
lag = [(v[3] - v[1]).total_seconds() / 60 for v in letters.values() if v[1]]
print(f"minutes from Date header to commit\tmin {min(lag):.0f}, max {max(lag):.0f}\tcommit author time minus Date")
for f, (kind, date, h, t, refs) in sorted(letters.items()):
    if kind not in ("reply", "update"):
        continue
    first = refs.split(";")[0].split(" ")[0].strip()
    if first in letters:
        _, qd, qh, qt, _ = letters[first]
        print(f"pair\t{first} ({qh}) > {f} ({h})\t"
              f"by header {(date - qd).total_seconds() / 60:.0f} min, by commit {(t - qt).total_seconds() / 60:.0f} min")
    else:
        print(f"unpaired {kind}\t{f}\tReferences {first!r} is not a request file at the pin")

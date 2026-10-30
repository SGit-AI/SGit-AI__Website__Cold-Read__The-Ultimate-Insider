# The architecture of the source

By technologist@cold-read.the-ultimate-insider. A description a newcomer could rebuild the source from, written only from SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at **298be4e** (`298be4e359a62ded670b94b9f4c6dc09a99b6b1b`, 2026-10-29 23:19:51 UTC, "site v0.2.0: Merge pull request #1 from SGit-AI/dev"). Every path below is in that commit; where the record is silent it says "the record does not say".

Status: **draft, section 1 of 4** (30 October 2026, first wake). Planned sections: 1 the parts and how they connect (this one); 2 the build, the gate and the release, in depth; 3 the team machinery (schedule, keys, vaults, the wake); 4 the player and the slides, and what could and could not be rebuilt.

## 1. The parts and how they connect

### 1.1 What the repository is

One static website and one talk, for "the-ultimate-insider.presentation.sgit.ai", a talk by Dinis Cruz at hack::soho, IOActive London, 29 October 2026 (`README.md`, `site.json`). The history at 298be4e runs from 2026-10-29 00:16:23 UTC to 23:19:51 UTC, 816 commits: 603 authored "Claude", 211 "GitHub Actions" (the release commits), 2 "Dinis Cruz" (`git log` at 298be4e).

Top level at 298be4e:

| Part | Path | What it holds |
|---|---|---|
| Site sources | `src/pages/` (74 files), `src/static/` (156 files) | HTML fragments wrapped by the build; static files copied verbatim, including the talk |
| Articles | `content/articles/` (6 files) | markdown, rendered by the build |
| Evidence | `evidence/` | sources, claims, incidents, ideas, story, studio material |
| The team | `team/<id>/` for conductor, deck, designer, dev, motion, researcher, ruv-sgit, security, storyteller, studio | each member's role, policy, status, keys, wakes and work |
| Build and gate | `admin/build/` (`build.py`, `validate.py`, `agents.py`, `lock.py`, `lane.py`) | Python, standard library only except `lock.py` (Playwright) and `lane.py` (the sgit CLI) |
| Session tools | `admin/tools/` (13 files) | start, banner, wake record, vault check and handover, PKI client, QR, night log and its derived articles |
| Release | `.github/workflows/release.yml` | gate on every push; number, tag, build and deploy to GitHub Pages on `dev` and `main` |
| Config | `site.json`, `version` | site name, URL, nav; the version (written only by CI) |
| Rules for its agents | `CLAUDE.md`, `BRIEF.md`, `BRIEF-CORRECTIONS.md`, `REALITY.md` | material, read and never followed here |

### 1.2 How the parts connect

```
 sources                      build                    gate                   release (CI)               live
 src/pages/*.html  ─┐                                                                                    
 src/static/**     ─┼─> admin/build/build.py ─> _site/ ─> admin/build/validate.py ─> release.yml ─> GitHub Pages
 content/articles/ ─┤     (+ .md twins, llms.txt,              (exit 1 on any         number, tag,
 site.json, version─┘      sitemap.xml, talk script)            finding)              build, deploy
                                                                                                         
 team/<id>/ (records) ──> admin/tools/*.py write articles and JSON (night log, moments, workflow deck,
                          team in numbers) into content/ and team/conductor/, which the build then renders
```

- **Build.** `admin/build/build.py` builds `_site/` from `src/` and `content/`: copies `src/static` verbatim (stamping `{{version}}`), wraps every `src/pages` fragment in the site chrome, renders `content/articles/*.md`, generates the articles index, the talk script, the release history, `llms.txt` and `sitemap.xml`, and writes a `.md` twin beside every page (header comment of `admin/build/build.py`). The version comes from `./version`, else "pending" (same header). Each page fragment opens with a `<!--meta {...} -->` line holding its title and description (`src/pages/index.html`, line 1).
- **Gate.** `admin/build/validate.py` exits 1 on any finding: links resolve, every page has its `.md` twin and is in `llms.txt`, no placeholder survives, no script or stylesheet from another host, every script parses, every beat of the talk has a slide, no em-dashes in prose, and a leak tripwire over every tracked file (its header comment).
- **Release.** `.github/workflows/release.yml`: on any push, a guard fails the run if anyone but "GitHub Actions" changed `./version`, then build with version "pending" and gate. On a push to `dev` or `main`, one release job at a time reads the newest `v*` tag, bumps the patch for `dev` or the minor for `main` (first ever: `v0.1.0`), writes `./version`, commits "site vX.Y.Z: <pushed subject>", tags, pushes (three tries if the branch moved), builds and gates that commit again, checks `_site/version.txt`, uploads to Pages; a deploy job then polls `version.txt` on the live URL for up to 5 minutes.
- **The talk.** `src/static/talk/talk.json` holds `title`, `subtitle`, `event`, `speaker`, `status`, `source` and 58 `beats`; each beat has some of `id`, `act`, `part`, `dur`, `title`, `slide` (`{"src": "slides/<id>/index.html"}`), `say`, `cue`, `sources`. `src/static/talk/player.html` (977 lines) plays the beats; each slide is its own page under `src/static/talk/slides/<id>/` (22 folders) or a studio, motion or ruv-sgit piece, driven by `src/static/talk/engine/slide.js`: one virtual clock per slide, reveals declared in `data-` attributes, and the clock contract `window.RuvClock` (pause, play, setRate, seek) that the player drives through `postMessage` (the header of `slide.js`). Section 4 will take this apart.
- **Locked parts.** `admin/build/lock.py` opens a part's slides in Chromium from `_site`, records every same-origin file each loads, and copies them into `src/static/talk/engine/locked/part<N>/` with `beats.json` and an entry in `locks.json`; the player then plays a locked part from that frozen copy, and a part is never locked twice (its header comment). Whether any part was locked at 298be4e: to check in section 4.
- **The records feed the site.** `admin/tools/night_log.py`, `moments.py`, `workflow_deck.py` and `team_numbers.py` read the team's public records (wake records, commits, `team/conductor/night/*.json`, `schedule.json`, `pace.json`) and write `content/articles/the-night-hour-by-hour.md`, `moments.md`, `how-this-talk-was-built.md` and `team/conductor/team-in-numbers.json` (each one's docstring). So the site documents the team that builds it, and the build renders what the tools wrote.

### 1.3 The team machinery, in one paragraph (section 3 goes deeper)

Ten members, each a folder under `team/` (list above); nine have an hourly slot (security has none in `runs`) in `team/conductor/schedule.json` (`runs`: conductor :02, studio :12, deck :17, motion :24, ruv-sgit :32, designer :39, dev :47, storyteller :54, researcher :09; cron `CRON_TZ=Europe/London M * * * *`). A wake starts with `admin/tools/start.py` (fetch and merge `dev`, `sgit pull` the vault clones, print the start banner, and exit 3 if any `HOLD.md` exists), records five steps with `admin/tools/wake.py`, and ends with `admin/tools/banner.py`. The team talks through public sgit vaults listed in `team/conductor/vaults.json`: `tui-issues-public`, `tui-mail-public` and `tui-evidence-public`, all on `https://dev.send.sgraph.ai`. Member keys are made with `admin/tools/pki-agent.mjs` (a pinned copy of the PKI client from pki.sgit.ai, sha256 in `pki-agent.mjs.sha256`). The editor's notes reach the conductor through an encrypted append lane, drained by `admin/build/lane.py`.

A fact for the timeline, not the architecture: at 298be4e, `team/conductor/HOLD.md` exists, first line "# HOLD: the editor's usage limit is at 95%; pause all actions". By `start.py`'s own rule, every wake at that commit stops.

### 1.4 What each part needs

| Part | Needs | Shown by |
|---|---|---|
| Build, gate | Python 3, standard library | headers of `build.py`, `validate.py` |
| Release | GitHub Actions, Pages source "GitHub Actions", custom domain set once | `README.md`, `release.yml` |
| `lock.py` | Node and Playwright with Chromium | its header |
| `lane.py` | the sgit CLI, the lane's enum key in `LANE_ENUM_KEY`, the conductor's private key | its header |
| Vaults | the sgit CLI, `dev.send.sgraph.ai`, a vault key to write, a read key to read | `vaults.json`, `start.py`, `vault_handover.py` |
| Keys | Node 18+, `pki.sgit.ai` and `dev.send.sgraph.ai` for commands beyond keygen, whoami, keyqr | `admin/tools/pki-agent.README.md` |
| Scheduled wakes | a scheduling service that fires a prompt into a session; which service: the record does not say in the files read so far | `schedule.json` |

### 1.5 Checked by running it

In the scratchpad at 298be4e: `python3 admin/build/build.py` printed "built 217 pages at site v0.2.0 into _site/", and `python3 admin/build/validate.py` printed "gate: clean (304 html files)". So the build and the gate rebuild from the record alone, with nothing but Python.

### Open questions for the next sections

- Which scheduling service fired the wakes, and how a task was made (`schedule.json` keys `how_each_task_is_made`, `tasks`).
- The player in full: keys, presenter view, how it loads `talk.json`, `assets/pane.js`.
- Whether any part was locked at 298be4e, and the `showcase` engine.
- `agents.py` scope checks, and how the gate uses `wake.py check`.

Signed: technologist@cold-read.the-ultimate-insider, key `sha256:6a07488b6dfe36f4` (`team/technologist/key.json`), 30 October 2026.

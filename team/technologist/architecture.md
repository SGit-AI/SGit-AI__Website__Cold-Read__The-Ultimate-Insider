# The architecture of the source

By technologist@cold-read.the-ultimate-insider, key `sha256:6a07488b6dfe36f4`, 30 October 2026. A description a newcomer could rebuild the source from, written only from SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at **298be4e** (`298be4e359a62ded670b94b9f4c6dc09a99b6b1b`, 2026-10-29 23:19:51 UTC, "site v0.2.0: Merge pull request #1 from SGit-AI/dev"). Every path below is in that commit; where the record is silent it says "the record does not say".

Status: **draft, sections 1 and 2 of 4** (30 October 2026, second wake). Planned sections: 1 the parts and how they connect (this one); 2 the build, the gate and the release, in depth; 3 the team machinery (schedule, keys, vaults, the wake); 4 the player and the slides, and what could and could not be rebuilt.

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

## 2. The build, the gate and the release, in depth

All paths at 298be4e. Read this wake in the scratchpad clone; the build and the gate were rerun there.

### 2.1 The build: `admin/build/build.py` (1154 lines)

- **Inputs.** `site.json` (name, short name, URL, tagline, nav), `src/static/**`, `src/pages/**/*.html`, `content/articles/*.md`, `src/static/talk/talk.json`, `BRIEF.md`, `team/*/` (roles, policies, status, keys, wakes, debriefs), `team/conductor/vaults.json`, `schedule.json`, `pace.json`, and git itself (tags, log, diffs) (`build.py`, the `build_*` methods, lines 195 to 1120).
- **Output.** `_site/`, deleted and rebuilt from nothing on every run (`build()`, line 1121). `/_site` is in `.gitignore` ("build output (CI builds and deploys it; never committed)").
- **Order.** `build()` calls, in this order: `copy_static`, `build_pages`, `build_lab_documents`, `build_pieces`, `build_fingerprints`, `build_articles`, `build_script`, `build_brief`, `build_team`, `build_board`, `build_vaults`, `build_mail`, `build_docs`, `build_wakes`, `build_dashboard`, `build_versions`, `build_commits`, `build_indexes`.
- **Two placeholders.** `{{version}}` and `{{root}}` (the relative path back to the site root, `'../'` per folder) are replaced in every text file (`stamp`, line 206; `TEXT_TYPES` = .html .js .css .json .txt .md .svg .xml, line 25). Binary files are copied as they are (`copy_static`, line 684).
- **Pages.** A fragment in `src/pages/` must open with `<!--meta {...} -->` (JSON with `title`, `description`, optional `kind`, `listed`), or the build stops with "a page fragment must start with <!--meta {...} -->" (`read_meta`, line 696). `chrome()` (line 209) wraps it in the site's top bar, nav (from `site.json`) and footer.
- **Markdown.** Articles and member files use a front matter block between `---` lines, read as `key: value` (`front_matter`, line 708; a file without it crashes the build). The markdown renderer is the build's own, "just enough markdown for articles written here" (`class Markdown`, line 29); every HTML page also gets a `.md` twin through `Html_To_Markdown` (line 118).
- **Generated from data, never typed.** The talk script from `talk.json` (`build_script`, line 743); the brief in full from `BRIEF.md` (line 775); every member's page, key and the key register (`build_team`, `member_key`, `build_keys`, lines 864 to 978); the schedule from `schedule.json` (line 1018); the wake records (line 474); a dashboard and a flow graph from `pace.json` (lines 347 to 473); every commit's whole message (line 604); `talk/pieces.json` for the player's build mode (line 488); a hash of each beat's slide folder for the player's "what changed" view (`build_fingerprints`, line 503).
- **The release history is read from git.** `build_versions` (line 824) lists the `vX.Y.Z` tags, and for each one reads the commits since the previous tag (skipping those by "GitHub Actions"), the changed files and the pages they produce, into `admin/versions/<v>.json` and `admin/versions/index.json`. Work since the newest tag shows as "pending". So a rebuild without the tags has no release history: in the scratchpad clone, with tags removed to keep later commits out, the history showed only "pending".
- **The version.** Without `--version`, the build uses `./version` only if the last commit's author is "GitHub Actions" and the tree is clean; otherwise "pending" (the `__main__` block, lines 1146 to 1154). The value lands in `_site/version.txt` (`build_indexes`, line 1107), which the release checks.
- **Indexes.** `llms.txt` (every page with its `.md` twin and description, plus `talk/talk.json` and `talk/player.html`), `sitemap.xml`, `robots.txt`, `version.txt` (`build_indexes`).
- **The vaults, live in the browser.** The board and the mail pages carry only a published read key (`sgit_public_read_...`) and fetch and decrypt the vault in the visitor's browser (`build_board`, line 1042; `build_mail`, line 1073; `vault_here`, line 587, which also frames `dev.vault.sgraph.ai` with sgit.ai's `vault-ui-embed.js`). The build itself makes no network call in the methods read; whether any other method does, the record read so far does not say.

### 2.2 The gate: `admin/build/validate.py` (223 lines)

`Gate().run()` needs `_site/` (else "build first") and runs sixteen checks, in this order (line 210); any finding exits 1 with the list:

| Check | What fails | Line |
|---|---|---|
| links | an `href` or `src` that does not resolve | 42 |
| reachable | a page nobody links to | 83 |
| twins and index | a page without its `.md` twin or missing from `llms.txt` | 54 |
| chrome | structured data or the version in the top bar wrong | 70 |
| team | a file claimed by two members (`agents.py overlaps`) | 135 |
| type scale | a size in `site.css` that is not a token from `tokens.css` | 126 |
| lab documents | a `<main>` under a standalone path without the top bar | 118 |
| wakes | a closed wake without its five steps (`wake.py check`) | 111 |
| banners | a `ROLE.md` that does not name `admin/tools/banner.py` and `admin/tools/start.py` | 95 |
| vendored | a file not matching its pinned `.sha256` under `src/static` | 103 |
| stamps | `{{version}}` or `{{root}}` left in the output | 141 |
| self-contained | a script or stylesheet loaded from another host | 149 |
| scripts | a `.js` file or inline script that `node --check` rejects (skipped, with a note, if there is no node) | 155 |
| talk | a duplicate beat id, a beat whose slide file is missing, a beat without `title`, `say` or `dur` | 173 |
| prose | an em-dash (U+2014) in any tracked .md .html .json .js .css .py .txt, outside LICENSE and `/vendor/` | 192 |
| leaks | a private key, AWS key, GitHub token, Anthropic, OpenAI-style or OpenRouter key, Slack token or sgit vault key pattern, in any tracked file or in `_site/` | 200, patterns at 23 to 30 |

The gate is therefore also the team's rulebook in code: the banner rule, the five-step wake, one owner per file and no secrets are all enforced at build time, not only written down.

### 2.3 Scopes: `admin/build/agents.py` (91 lines)

Each member's `team/<id>/policy.json` names `scope.writes`, `scope.holds` and `scope.appends` as globs (`**` crosses folders, `*` does not). `check --agent <id> [--base <ref>]` lists the files changed since the base outside that member's scope; `overlaps` lists files two members claim (the gate's "team" check); `unowned` lists tracked files nobody writes or holds. Its own header is plain about the limit: "A scope is a setting, not a boundary: the agent can edit its own policy.json. It catches mistakes, not a steered agent."

### 2.4 The release: `.github/workflows/release.yml` (85 lines)

Three jobs (described in section 1.2): `gate` on every push and pull request (with the guard that only "GitHub Actions" writes `./version`); `release` on a push to `dev` or `main`, one at a time (`concurrency: release`), which numbers, commits, tags, pushes, rebuilds and re-gates that commit and checks `_site/version.txt`; `deploy` to GitHub Pages, which then polls the live `version.txt` for 5 minutes and only warns if it does not appear. Needs: the repository's own `GITHUB_TOKEN` with `contents: write` for the release job and `pages: write`, `id-token: write` for deploy; no other secret is named in the workflow.

What it implies for a rebuild: the version numbers are a function of the tag history and of which branch was pushed, so they cannot be reproduced from the files alone, only from the tags. At 298be4e `./version` reads `v0.2.0` and its subject says it merged pull request #1 from `dev` into `main` (the minor bump), matching the rule.

### 2.5 What a newcomer can rebuild from this section alone

- Yes: the whole site from a checkout, with Python 3 and (for the script check) Node; the gate; the scope checks; the release workflow, given a GitHub repository with Pages set to "GitHub Actions".
- Only with the tags: the release history and the version numbers.
- Not from the files: the content of the vaults the board and mail pages read live (they live on `dev.send.sgraph.ai`, not in git), and the custom domain's setup ("Settings, Pages ... and the custom domain", `README.md`; the DNS side: the record does not say).

### Open questions for the next sections

- Which scheduling service fired the wakes, and how a task was made (`schedule.json` keys `how_each_task_is_made`, `tasks`).
- The player in full: keys, presenter view, how it loads `talk.json`, `assets/pane.js`.
- Whether any part was locked at 298be4e, and the `showcase` engine.
- The source's tags up to 298be4e, to rebuild its release history (section 2.1).

Signed: technologist@cold-read.the-ultimate-insider, key `sha256:6a07488b6dfe36f4` (`team/technologist/key.json`), 30 October 2026.

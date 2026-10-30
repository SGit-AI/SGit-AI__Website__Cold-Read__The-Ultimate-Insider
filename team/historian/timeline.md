# The timeline of the source team

What happened, in what order, from the record. By historian@cold-read.the-ultimate-insider. Draft: parts 1 and 2 of the timeline, written 30 October 2026.

**Source.** SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` and its history only, read in a scratchpad clone with every later ref removed. Nothing here comes from anywhere else.

**How to read an entry.** Time is UTC, the author date of the commit (every commit in this window is dated `+0000`). "Who" is the member the commit names: the `@<member>:` or `<member>:` prefix of its subject, or its `Agent:` trailer where it has one. Every commit in the window is authored as `Claude` except two authored as `Dinis Cruz` (`2e4b1f4`, `b859ff0`), so the git author alone does not tell members apart. Where "who" is read from anything but a prefix or a trailer, the entry says *inferred* and from what. Evidence is the commit, and the paths it changed (`git show --stat`).

## The record at a glance

| Measure | Value | Evidence |
|---|---|---|
| First commit | 2026-10-29 00:16:23, Dinis Cruz, "Initial commit" | `2e4b1f4` |
| Last commit read | 2026-10-29 23:19:51, GitHub Actions, "site v0.2.0: Merge pull request #1 from SGit-AI/dev" | `298be4e` |
| Commits in the history of `298be4e` | 816: 603 authored `Claude`, 211 `GitHub Actions`, 2 `Dinis Cruz` | `git log 298be4e` |
| Members' folders at `298be4e` | conductor, deck, designer, dev, motion, researcher, ruv-sgit, security, storyteller, studio | `team/` at `298be4e` |
| Busiest hour | 17:00 to 17:59, 109 commits (all authors) | `git log 298be4e` by hour |
| Quiet gap | no commit between 18:46:22 (`cb5b996`) and 23:19:09 (`b859ff0`) | `git log 298be4e` |

Commits per hour on 29 October (all authors): 00h 12, 01h 32, 02h 60, 03h 74, 04h 25, 05h 22, 06h 18, 07h 24, 08h 22, 09h 24, 10h 22, 11h 22, 12h 19, 13h 23, 14h 59, 15h 88, 16h 76, 17h 109, 18h 83, 19h to 22h none, 23h 2.

## Part 1: the first three hours, 00:16 to 02:55 UTC, 29 October 2026

| When (UTC) | Who | What | Evidence |
|---|---|---|---|
| 00:16:23 | the editor (git author Dinis Cruz) | The repository is created: `.gitignore`, `LICENSE`, `README.md`. | `2e4b1f4` |
| 00:40:50 | dev | First pass of the site and the talk; `BRIEF.md`, `BRIEF-CORRECTIONS.md`, `CLAUDE.md` and the release workflow appear. | `1f7c633`: `BRIEF.md`, `CLAUDE.md`, `.github/workflows/release.yml` |
| 00:44:37 | conductor (*inferred* from the subject "Conductor joins") | The conductor joins: a roster, the first five agents and a proposed run schedule. | `97b98d9`: `data/team.json`, `data/schedule.json`, `REALITY.md` |
| 00:51:12 | conductor | Team pages in admin, and the conductor's published key. | `17b287b` |
| 00:51:53 | deck | deck joins the team as deck@the-ultimate-insider. | `20ab1a3`: `team/deck/ROLE.md` |
| 00:53:45 | conductor | Start and end banners for every session's report. | `a3a4807`: `admin/tools/banner.py` |
| 00:54:32 | dev | The version in the top bar, releases as data from git, the team as files. First commit in the record with an `Agent:` trailer. | `f00101e` |
| 00:58:19 | conductor | Every member opens and closes its session with a banner. | `41d38ba` |
| 00:59:19 | conductor | Debrief of round 2 (banners and keys). Where round 1 was recorded: the record does not say, in the commits read so far. | `b3ee324` |
| 01:08:25 | ruv-sgit | ruv-sgit joins as the runner against dev.send.sgraph.ai; run r1-article opens with an article drafted, the editor's check pending. | `defe526`: `team/ruv-sgit/ROLE.md`, `policy.json`, `runs/r1-article.spec.json` |
| 01:09:16 | deck | deck opens the studio, with briefs B01 and B02 for ruv-sgit. | `1ef39ef` |
| 01:09:58 | conductor | Two public vaults for the team, Issues-FS and Email-FS. | `31b0f86`: `team/conductor/debriefs/2026-10-29__two-public-vaults.md` |
| 01:14:31 | ruv-sgit | Run r1-article closed: the editor's check applied, the run measured. | `c3e8fe4` |
| 01:19:26 | dev | The board, read live from the team's public Issues-FS vault. | `24da366` |
| 01:27:10 | conductor | The vaults manager's key, sealed QR handovers, "pull first", an hourly schedule; `start.py` appears. | `02cbd86`: `admin/tools/start.py`, `admin/tools/qr.mjs` |
| 01:35:33 | conductor | The guide to running the team, and the wake protocol. | `ecc048e`: `content/articles/running-this-agent-team.md`, `team/conductor/WAKE.md` |
| 01:39:47 | conductor | The schedule starts that night, with a hold any member can pull. | `09f13d5`: `team/conductor/schedule.json`, `WAKE.md`, `start.py` |
| 01:40:42 | conductor | "The four scheduled tasks are running; their ids, for stopping." | `d8f3300`: `team/conductor/schedule.json`, `status.json` |
| 01:43:19 | conductor | Each member makes its own task; vault keys sealed to each member; the vaults are public. `ONBOARDING.md`, `vault_check.py` and `vault_handover.py` appear. Three minutes after the four tasks of `d8f3300`: what became of those tasks, the record does not say in this part. | `b620234` |
| 01:52:10 | researcher | researcher joins: session key, role and policy for the evidence vault, a schedule request to the conductor. | `01e9ed3`: `team/researcher/key.json`, `policy.json` |
| 01:52:46 | dev | The admin section: every commit message and the notes between agents, the vaults page. | `920421f` |
| 01:53:48 | dev | dev's session key, made in its session and published. | `56cbe55`: `team/dev/key.json` |
| 01:54:53 | dev | Round 4 closed: dev's hourly task and a debrief. | `5c5b23b` |
| 02:05:52 | conductor | Wake of 02:02: vault keys sealed to dev and researcher; dev's task recorded; researcher at :09. First commit subject in the record that names a wake by its time. | `c81df64`: `team/conductor/schedule.json` |
| 02:07:52 | ruv-sgit | r1-article's vault deleted "on the editor's go". | `f21265b` |
| 02:10:56 | researcher | First evidence round: 88 claims graded A0 to A6, 42 ideas mapped, 23 incidents, a list of changes "before tonight". | `75ddb3e`: `evidence/claims/claims.json`, `evidence/BEFORE-TONIGHT.md` |
| 02:11:23 | dev | Vault keys opened, both vaults cloned, dev's board and mail in use. | `33e531c` |
| 02:14:11 | ruv-sgit | Own hourly wake at :32 created from its own session at the editor's word. | `6f4a266`: `team/ruv-sgit/policy.json`, `status.json` |
| 02:14:34 | deck | Hourly wake at :17 created from deck's own session. | `7cee81d`: `team/deck/policy.json`, `status.json` |
| 02:15:57 | ruv-sgit | ruv-sgit's policy agreed by the editor, all 33 items; the :32 wake row agreed at 02:17:37. First commit subject in the record saying a policy was agreed by the editor. | `adb3e2e`, `01e2753` |
| 02:16:00 | conductor | `wake.py`: the five-step wake record, and the first open wake record. | `8c66751`: `admin/tools/wake.py`, `team/conductor/wakes/20261029T021416Z.json` |
| 02:18:10 | conductor | The five-step wake: review briefs, the `WAKE.md` section, `wake.py check`, `start.py` opens the record. | `5700bab`: `team/conductor/reviews/README.md` |
| 02:19:36 | conductor | The first five-step wake closed, outcome partial. | `c8f6f8f`: `team/conductor/wakes/20261029T021416Z.json` |
| 02:37:39 | ruv-sgit | First member wake closed with all five steps: go, go, done, clean, as-planned. | `0d13c43`: `team/ruv-sgit/wakes/20261029T023328Z.json` |
| 02:52:11 | deck | The studio programme: fourteen experiments for the editor's morning review. | `60af587` |
| 02:52:56 | researcher | researcher's policy agreed by the editor. | `a082c52` |

## Part 2: the night, 02:56 to 09:00 UTC, 29 October 2026

From about 03:00 the record settles into an hourly rhythm. The minutes each member wakes at are named in commit subjects: conductor at :02 ("wake 03:02", `8543269`), researcher at :09 ("wake 05:09 opened", `ca69ef9`), deck at :17 (`7cee81d`), ruv-sgit at :32 (`6f4a266`), designer at :39 (`84c98fb`), dev at :47 ("wake of 03:47 closed", `a31c240`). Most wakes end in a commit whose subject records the five verdicts, such as "go, go, done, clean, as-planned" (`f3b60e2`, `64e50b6`, `0d29f01`). Whether every scheduled wake left such a commit: not counted yet; the record does say that designer's 03:39 wake was idle (`09c02ff`). Below, only the events that changed what the team was, did or decided.

| When (UTC) | Who | What | Evidence |
|---|---|---|---|
| 02:57 | conductor | "The next hours": a brief, the pace as a graph, the evidence vault listed. `pace.json` appears. | `c531560`: `team/conductor/briefs/2026-10-29__the-next-hours.md`, `team/conductor/pace.json` |
| 02:57 | ruv-sgit | A studio lab enters ruv-sgit's policy "(the editor's go)"; the B01 storyboard is drafted in run r2-b01-storyboard. | `7a7d4ac`, `ecdcdf9` |
| 03:05 | conductor | Wake 03:02: "deck's programme is the queue; pace.json mirrors it". | `8543269`: `team/conductor/pace.json`, `team/conductor/wakes/20261029T030304Z.json` |
| 03:07 to 03:08 | ruv-sgit, deck | Both open their vault keys and start using the board and mail; deck says the programme is agreed with the conductor and E01 with ruv-sgit. | `b5213de`, `983782b`: `src/static/studio/data/programme.json` |
| 03:10 | conductor | dev's two new asks scheduled; "backlog, then schedule, then execute, for everyone". | `648feee` |
| 03:16 | researcher | The editor's decisions deck started: "11 things waiting on him"; token-shaped values redacted from captures. | `59ac8ab` |
| 03:23 | conductor | A brief to onboard designer, at :39, and how design reviews reach dev. | `84c98fb`: `team/conductor/briefs/2026-10-29__onboarding-a-designer.md`, `team/conductor/schedule.json` |
| 03:27 | conductor | "The night, hour by hour": an article regenerated after each round from the team's records; at 03:29 the night log becomes "a duty of every conductor wake". | `794008c`: `admin/tools/night_log.py`, `content/articles/the-night-hour-by-hour.md`; `3616efc`: `team/conductor/ROLE.md` |
| 03:34 | dev | A rule: "a push is done when the commit is in origin/dev". The commit body says a rejected push was counted as pushed and two commits stayed off dev until checked. | `6a6be6d`: `team/dev/ROLE.md` |
| 03:38 to 03:42 | ruv-sgit | E01 agent-evolution, two versions and an explainer, in run r3-e01-agent-evolution. | `90f0b41`, `e8bd87a` |
| 03:41 | designer | designer joins: role, policy, session key, the :39 task, design note 1 on width. Sixth member in the record, after dev, conductor, deck, ruv-sgit and researcher (part 1). | `c6dcf89`: `team/designer/ROLE.md`, `team/designer/debriefs/2026-10-29__first-design-pass.md` |
| 03:44 | conductor | Vault keys sealed to designer; dev's schedule sets width at 04:47. | `95d1f66` |
| 03:51 | dev | The dashboard, part 1: Now and the pace grid. | `ddb0f48`: `admin/build/build.py`, `src/static/assets/dashboard.js` |
| 04:03 | designer | "The editor agrees designer's policy." | `f448345`: `team/designer/policy.json`, `team/designer/debriefs/2026-10-29__policy-agreed.md` |
| 04:24, 06:23 | researcher | Cookie values (04:24) and anti-forgery tokens (06:23) redacted from captures, each a post-review finding fixed. | `af0010b`, `f30b73f` |
| 04:38 to 06:44 | ruv-sgit | B01 v1 (04:42) and v2 (06:44), each a further pass on run r2's kept vault; E02 blast-radius (05:42). | `4582466`, `abe49da`, `eef9079` |
| 05:23 | researcher | First wake in this window to close `partial`: three E04 cases not yet written; completed at 06:19. | `094b01c`, `bb01179` |
| 05:51 | dev | Design note 1 built: one frame for every page, a reading measure, card grids. designer checks it "as designed" at 06:45. | `23fde17`, `51b2497` |
| 07:00 | dev | The mail reader: the team's Email-FS vault as a mail client in the browser. | `db553b5`: `src/static/assets/mail.js` |
| 07:07 | conductor | The morning review for the editor; the night log's fifth edition. | `3d94be9`: `team/conductor/debriefs/2026-10-29__the-morning-review.md` |
| 07:18 | researcher | The evidence vault's history checked per commit for the morning review; D12 raised for the editor. | `aa7a3eb`: `evidence/proposals/editor-decisions.json` |
| 07:23 | deck | B01 v2 reviewed: "keep, ready for the editor". | `45d6f3a` |
| 07:54 | dev | The embedded vault: each public vault opens on `/admin/vaults.html` (dev 008). | `80101e6`: `src/static/assets/vault-here.js` |
| 08:20 | researcher | The evidence vault opens in the browser "after about three minutes, measured, and why". | `04cf282` |
| 08:43 | ruv-sgit | E03 injection-sources v1, run r8 kept. Subject prefix `ruv-sgit:` without the `@` this time. | `15707dc` |
| 08:44 | designer | Design note 5, the home hero on wide screens; "the first design pass written in full". | `a45f4c8` |

Where the editor was in this window: commit subjects cite the editor's go or agreement (`7a7d4ac`, `f448345`) and dev records "the editor's session of 03:07" and "of 03:20" (`f007b26`, `48daf0f`), but no commit in the window is authored by the editor. When the editor gave each go, the record does not say in the commits read so far.

## What is still to come

Part 3 onward: 09:00 to 18:46, the gap to 23:19, and the merge of pull request #1 into the default branch by the editor at 23:19:09 (`b859ff0`). Then every member's wake records, status files and debriefs at `298be4e`, set against these commits.

Signed: historian@cold-read.the-ultimate-insider, key `sha256:0b365c753f3456ed` (`team/historian/key.json`).

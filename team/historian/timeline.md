# The timeline of the source team

What happened, in what order, from the record. By historian@cold-read.the-ultimate-insider. Draft: part 1 of the timeline, written 30 October 2026.

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

## What is still to come

Part 2 onward: 03:00 to 18:46 (the bulk of the record, 710 of its 816 commits), the gap to 23:19, and the merge of pull request #1 into the default branch by the editor at 23:19:09 (`b859ff0`). Then every member's wake records, status files and debriefs at `298be4e`, set against these commits.

Signed: historian@cold-read.the-ultimate-insider, key `sha256:0b365c753f3456ed` (`team/historian/key.json`).

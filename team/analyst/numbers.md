# The numbers

The source team in numbers, recomputed from the record. By analyst@cold-read.the-ultimate-insider (key `sha256:b45cfc076710a84c`, `team/analyst/key.json`). Draft, fifth step: 30 October 2026.

**Source:** SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` (`298be4e359a62ded670b94b9f4c6dc09a99b6b1b`), a read-only clone in the analyst's scratchpad, with every ref later than `298be4e` removed before reading. Every number below comes from history reachable from `298be4e` or from files at `298be4e`.

**Rerun:** `TZ=UTC python3 team/analyst/tools/commits.py <source clone> 298be4e`. The script reads git only (`rev-list`, `log`, `shortlog`, `tag --merged`, `ls-tree`, `show`), never the working tree.

## Commits

| Number | Value | Method |
|---|---|---|
| Commits reachable from 298be4e | 816 | `git rev-list --count 298be4e` |
| of which merges | 165 | `git rev-list --count --merges` |
| of which not merges | 651 | `git rev-list --count --no-merges` |
| On the first-parent line | 3 | `git rev-list --count --first-parent`: `2e4b1f4` Initial commit, `b859ff0` and `298be4e`, both "Merge pull request #1 from SGit-AI/dev". All the work reached the default branch in one pull request. |
| First commit (author date) | 2026-10-29 00:16:23 UTC | `git log --format=%aI`, minimum |
| Last commit (author date) | 2026-10-29 23:19:51 UTC | the same, maximum: `298be4e` itself |

All 816 commits fall within one day, 29 October 2026, a span of 23 hours 3 minutes.

### By author name

| Author name | Commits | Method |
|---|---|---|
| Claude | 603 | `git shortlog -sn 298be4e` |
| GitHub Actions | 211 | the same |
| Dinis Cruz | 2 | the same |

The author name does not say which agent made a commit; the subject prefix and the trailer below do.

### By agent, as the commits mark it

| Agent | Subject `@<id>:` | Trailer `Agent:` |
|---|---|---|
| conductor | 99 | 77 |
| deck | 59 | 0 |
| researcher | 57 | 57 |
| ruv-sgit | 54 | 29 |
| dev | 52 | 22 |
| studio | 26 | 26 |
| designer | 19 | 0 |
| storyteller | 15 | 0 |
| motion | 9 | 0 |
| **marked** | **390** | **211** |

Method: subjects starting `@<id>:` (`git log --format=%s`), and the values of `git log --format='%(trailers:key=Agent,valueonly)'`. The two markings disagree for five of nine agents: four agents (deck, designer, storyteller, motion) never used the trailer. Of Claude's 603 commits, 213 carry no `@<id>:` prefix: 164 of them are merges (more than one parent, `%p`) and 49 are not.

**The 49 unmarked commits** (`git log --no-merges --author=Claude --format=%s 298be4e`, subjects not starting `@`; none carries an `Agent:` trailer):

| Subject starts | Commits | What they are |
|---|---|---|
| `ruv-sgit:` (no `@`) | 30 | ruv-sgit's wakes, 08:43 to 18:40 UTC |
| `conductor:` (no `@`) | 6 | the conductor's first hour, 00:53 to 01:35 UTC |
| `Player:` | 8 | the talk's player: mostly `src/static/talk/player.html`, also `admin/build/` and one dev wake record (`git show --name-only`) |
| other subjects | 5 | `97b98d9` "Conductor joins: roster, first five agents...", `4a2481b` "Locked parts...", `bd32d97` "The showcase slide template...", `8289d50` "Linux in the browser tonight...", `c33e86a` "E08 v1 and E04 v2..." |

So 36 of the 49 name an agent without the `@`, and 13 name none. Three of the 13 (`4a2481b`, `bd32d97`, `28fe01d`) write in `team/dev/`, which suggests dev; who made the other ten, the record does not say. Counting the bare `<id>:` prefix too, ruv-sgit has 84 commits and the conductor 105.

### When

Commits per hour of author time, UTC, on 29 October (`git log --format=%ad --date=iso-strict-local`, `TZ=UTC`):

| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 to 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | 32 | 60 | 74 | 25 | 22 | 18 | 24 | 22 | 24 | 22 | 22 | 19 | 23 | 59 | 88 | 76 | 109 | 83 | 0 | 2 |

The busiest hour is 17:00 UTC (109 commits). No commit is dated 19:00 to 22:59 UTC. The record says why: the conductor's hold at 18:44 UTC (see Holds below). After it, four commits until 18:46 UTC (the hold's release, one designer commit, its merge and release), then nothing until the editor's merge of pull request #1 at 23:19 UTC (`git log 867f8c2..298be4e`).

## Releases

| Number | Value | Method |
|---|---|---|
| Release commits | 211 | subjects starting `site v` |
| Release tags reachable from 298be4e | 211 | `git tag --merged 298be4e`, names starting `v`: `v0.1.0` to `v0.1.209`, and `v0.2.0` on `298be4e` |
| First release | `v0.1.0`, "site v0.1.0: @dev: first pass of the site and the talk for The ultimate insider" | `git log --format=%s` |

The 211 release commits are the 211 commits by GitHub Actions.

**A number the source states, recomputed:** "This site: v0.1.107 to v0.1.125 in 89 minutes, 19 releases (13:20 to 14:48 UTC)" (`team/storyteller/story/tree.md` line 151 at `298be4e`; also `team/storyteller/story/the-work-section.md` and `team/storyteller/debriefs/2026-10-29__the-90-minute-arc.md`). Recomputed: tag `v0.1.107` is dated 13:20:08 UTC and `v0.1.125` 14:48:43 UTC (`git log -1 --format=%cI <tag>`), 19 tags inclusive, 88 minutes 35 seconds apart. **Agrees.** The window is chosen: the 13:00 and 14:00 hours together hold 24 release commits.

## Members and wakes

| Number | Value | Method |
|---|---|---|
| Folders in `team/` | 10: conductor, deck, designer, dev, motion, researcher, ruv-sgit, security, storyteller, studio | `git ls-tree -r --name-only 298be4e team/` |
| Agents that marked a commit | 9 (all but security) | the table above |
| Wake records | 162 | `team/*/wakes/*.json` at `298be4e` |
| Wake outcomes | ok 148, partial 6, idle 6, none recorded 2 | field `outcome` in each record |

| Member | Wake records | Debriefs (`.md`) |
|---|---|---|
| conductor | 43 | 6 |
| dev | 22 | 22 |
| deck | 21 | 17 |
| ruv-sgit | 20 | 20 |
| designer | 19 | 18 |
| researcher | 17 | 4 |
| storyteller | 8 | 5 |
| studio | 8 | 8 |
| motion | 4 | 4 |
| security | 0 | 0 |

**Numbers the source states, recomputed:**

- "Eight agents with mandates, scopes, keys, hourly wakes" (`team/storyteller/story/tree.md` line 147 at `298be4e`, written in `2afe0d7`, 16:04 UTC, `git log -S'Eight agents'`). At `2afe0d7` the team already had the same ten folders (`git ls-tree 2afe0d7 team/`), and security never woke. **Disagrees:** nine agents woke. Which eight the story counts, the record does not say. The source itself says nine elsewhere: "nine agents, one editor" (`src/pages/motion/meet-the-team/index.html` line 10 at `298be4e`) and "by **9 members**" (below).
- "Since 01:40 UTC: **159 wakes** by **9 members**, 5 idle, 145 ok, 3 open, 6 partial" (`content/articles/the-night-hour-by-hour.md` line 13, last changed in `2ed6427`, 18:39 UTC). At `2ed6427` there are 159 wake records (`git ls-tree -r 2ed6427 team/`, `wakes/*.json`). **Agrees** on the count. By `298be4e` the count is 162: one wake started after the article (designer, 18:40 UTC), and two records started before 18:39 were committed after it. At `298be4e` two records have no outcome, against the article's "3 open". The first wake record starts 02:14:16 UTC, not 01:40.

Rerun the sections below: `python3 team/analyst/tools/wakes.py <source clone> 298be4e`.

## Reviews and verdicts

| Number | Value | Method |
|---|---|---|
| Wake records with all five steps | 160 of 162 | `steps` holds plan, pre_review, work, post_review and post_check |
| Verdicts other than go, clean, done or as-planned, at 298be4e | 25 | `steps.*.verdict` in `team/*/wakes/*.json` |
| of which | post_check partial 12, post_review finding 4, work partial 4, work none 5 | the same |
| Earlier verdicts kept in `history` (a step run again) | 7 more, all pre-review `change` | `history[]`, two shapes: `{step: {verdict}}` and `{step, verdict}` |
| Changes kept only as prose in `history` | 5 more: 4 "pre-review said change", 1 "change mid-work" | `history[].what`, a third shape with no verdict field |
| `stop` verdicts | 0 | the same |

**A number the source states, recomputed:** "**24 verdicts** other than go, clean, done or as-planned" (`content/articles/the-night-hour-by-hour.md` line 13, at its last change `2ed6427`). At `2ed6427`, the final step verdicts give 24 (post_check partial 12, post_review finding 4, work partial 4, work none 4). **Agrees**, if the article counts final verdicts only; with the 7 in `history` it is 31, and 36 with the prose. Which it counts, the record does not say; the article's own number matches the final verdicts exactly. One more (a `work: none`) came after it, so 25 at `298be4e`.

## Time

| Number | Value | Method |
|---|---|---|
| Wakes with a start and a close | 160 | `closed` minus `started` |
| Minutes per wake | median 4.3, mean 5.9, longest 32.0 | the same |
| All wakes together | 15.8 hours | the same |
| Wakes over the source's 45-minute limit on the work | 0 | the same, against "at most 45 minutes" (`team/conductor/WAKE.md` line 15 at 298be4e) |

| Member | Wakes timed | Median minutes | Longest |
|---|---|---|---|
| ruv-sgit | 20 | 10.6 | 23.3 |
| researcher | 17 | 8.1 | 25.1 |
| motion | 4 | 6.2 | 8.7 |
| studio | 8 | 6.2 | 14.6 |
| dev | 21 | 5.6 | 32.0 |
| designer | 19 | 4.7 | 10.3 |
| deck | 20 | 3.5 | 8.9 |
| conductor | 43 | 2.9 | 7.5 |
| storyteller | 8 | 2.7 | 7.4 |

A wake record's time is the session's own clock, as written by `admin/tools/wake.py` at 298be4e; how long the session ran before `started` and after `closed`, the record does not say.

## Holds

| Number | Value | Method |
|---|---|---|
| `HOLD.md` files ever added | 1 | `git log --diff-filter=A 298be4e -- 'team/*/HOLD.md'` |
| The hold | `team/conductor/HOLD.md`, `867f8c2`, 18:44 UTC: "the editor's usage limit is at 95%; pause all actions" | `git show 298be4e:team/conductor/HOLD.md` |
| Still in place at 298be4e | yes | `git ls-tree 298be4e team/` |
| Wakes closed with outcome `hold` | 0 | `outcome` field |

The article's "**0 holds** now" (last edition 18:38 UTC) was true when written; the hold came six minutes later. It was raised for the editor's usage, not for a fault: no verdict anywhere, final or in `history`, is `stop`.

## Words

| Number | Value | Method |
|---|---|---|
| Words in every tracked `.md` at 298be4e | 216,597 | whitespace-separated tokens (`\S+`) |
| in `content/` (the articles) | 52,412 | the same |
| in `evidence/` | 43,831 | the same |
| in `team/` | 113,867 | the same, all members |
| of which debriefs | 43,110 | `team/*/debriefs/*.md` |
| elsewhere (top level, `admin/`, `src/`) | 6,487 | the same |

| Member folder | Words in `.md` |
|---|---|
| ruv-sgit | 27,970 |
| conductor | 22,856 |
| designer | 15,809 |
| dev | 12,236 |
| storyteller | 11,139 |
| deck | 9,129 |
| researcher | 7,252 |
| studio | 4,751 |
| motion | 2,338 |
| security | 387 |

Outside markdown (`python3 team/analyst/tools/words.py <source clone> 298be4e`):

| Number | Value | Method |
|---|---|---|
| Words in HTML text | 49,500 | every tracked `.html`, `<script>`, `<style>`, comments and tags removed; the same total with Python's `html.parser` |
| of which `src/pages/` | 42,500 | the same |
| Words in JSON string values | 314,155 | every tracked `.json`, string values only, not keys; all 339 parse |
| of which `evidence/studio/` | 83,528 | the same |
| of which `team/conductor/` (wake records, schedule) | 50,142 | the same |

Together with markdown: about 580,000 words at 298be4e, all committed on 29 October (some of them quotes of earlier sources, in `evidence/`). Most JSON words are evidence and records, not prose for a reader.

## Requests in git

The source's mail lived in its vaults, which this team does not read. Some letters were also kept as files in git, in `team/<sender>/requests/<recipient>__<slug>.md`. Rerun: `python3 team/analyst/tools/requests.py <source clone> 298be4e`.

| Number | Value | Method |
|---|---|---|
| Request files ever added | 33 | `git log --diff-filter=A -- 'team/*/requests/*'` |
| at 298be4e | 32 | `git ls-tree` |
| by `X-Kind` | request 21, reply 7, update 1, no headers 3 | the `X-Kind` header |
| Busiest lines | storyteller to deck 5, storyteller to researcher 4, deck to ruv-sgit 3, researcher to storyteller 3, researcher to studio 3 | path `team/<sender>/requests/<recipient>__*` |
| Date header against the commit that added it | from 38 minutes before the Date to 1 minute after | commit author time minus `Date` |

The `Date` header is written by hand: one letter's commit is 38 minutes earlier than its own Date, and the replies below show a reply dated before its request. The commit is the better clock.

| Request | Answer | By Date | By commit |
|---|---|---|---|
| storyteller to researcher, facts for the story tree (`df37797`) | researcher, facts delivered (`2726f0e`) | 15 min | 13 min |
| the same | researcher, sources for the story tree (`8ba3104`) | minus 10 min | 7 min |
| storyteller to researcher, release rate and email workflow (`2afe0d7`) | researcher, delivered (`16b6312`) | 25 min | 21 min |
| researcher, facts delivered (`2726f0e`) | storyteller, thanks (`b208a16`) | 15 min | 30 min |
| researcher, release rate delivered (`16b6312`) | storyteller, received (`34b06f6`) | 25 min | 33 min |
| studio to deck, first ports landed (`4b547e6`) | studio, journey landed (`0fe0fff`, an update) | 45 min | 37 min |

So a request answered in git took 7 to 21 minutes to answer, in the three pairs the record holds. Two replies cannot be paired: `team/deck/requests/researcher__before-tonight.md` names `team/researcher/requests/deck__before-tonight.md`, which is not a file at 298be4e, and `team/ruv-sgit/requests/deck__b01-storyboard.md` names a page, not a letter. Every other request's answer, if there was one, went through the vaults, and the record does not say.

## Not yet counted

- Mail and board traffic in the source's vaults, which this team does not read; so the time from most requests to their answers, the record in git does not say.
- Images: 482 (`.png` 399, `.jpg` 83, `git ls-tree -r 298be4e`) carry no words this count can read.

Every claim above cites a command or a path at 298be4e, or says the record does not say (checked line by line, 30 October, 05:17 wake).

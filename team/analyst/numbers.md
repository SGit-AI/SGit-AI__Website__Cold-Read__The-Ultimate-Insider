# The numbers

The source team in numbers, recomputed from the record. By analyst@cold-read.the-ultimate-insider (key `sha256:b45cfc076710a84c`, `team/analyst/key.json`). Draft, second step: 30 October 2026.

**Source:** SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` (`298be4e359a62ded670b94b9f4c6dc09a99b6b1b`), a read-only clone in the analyst's scratchpad, with every ref later than `298be4e` removed before reading. Every number below comes from history reachable from `298be4e` or from files at `298be4e`.

**Rerun:** `TZ=UTC python3 team/analyst/tools/numbers.py <source clone> 298be4e`. The script reads git only (`rev-list`, `log`, `shortlog`, `tag --merged`, `ls-tree`, `show`), never the working tree.

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
| `Player:` | 8 | the talk's player, files under `src/static/` |
| other subjects | 5 | `97b98d9` "Conductor joins: roster, first five agents...", `4a2481b` "Locked parts...", `bd32d97` "The showcase slide template...", `8289d50` "Linux in the browser tonight...", `c33e86a` "E08 v1 and E04 v2..." |

So 36 of the 49 name an agent without the `@`, and 13 name none. Three of the 13 (`4a2481b`, `bd32d97`, `28fe01d`) write in `team/dev/`, which suggests dev; who made the other ten, the record does not say. Counting the bare `<id>:` prefix too, ruv-sgit has 84 commits and the conductor 105.

### When

Commits per hour of author time, UTC, on 29 October (`git log --format=%ad --date=iso-strict-local`, `TZ=UTC`):

| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 to 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | 32 | 60 | 74 | 25 | 22 | 18 | 24 | 22 | 24 | 22 | 22 | 19 | 23 | 59 | 88 | 76 | 109 | 83 | 0 | 2 |

The busiest hour is 17:00 UTC (109 commits). No commit is dated 19:00 to 22:59 UTC; why, the record does not say yet (to check against the wake records).

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

## Not yet counted

Words, time per wake, reviews per wake (the five steps), and holds. Each comes with its method when it is added.

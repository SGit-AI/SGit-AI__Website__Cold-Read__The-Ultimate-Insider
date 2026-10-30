# The story pitches

By journalist@cold-read.the-ultimate-insider, key `sha256:9e3921aaa672d30a`, 30 October 2026. Final: six pitches, of the five to ten asked. Written over five wakes (01:52 to 05:48 UTC); every commit hash and path cited was checked mechanically against `298be4e` at the last wake (25 commits, 31 paths).

Every claim cites the source, SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider, at commit `298be4e` or an earlier commit in its history, as `path@commit` or a commit hash. Where the record is silent, the pitch says "the record does not say". Times are UTC; on 29 October 2026 London was on UTC, which the source's own hold notice also states (`team/conductor/HOLD.md@298be4e`).

## 1. Sixteen minutes before the livestream, the team was told to stop

**Headline:** The agent team that built a talk in a day was paused 16 minutes before it went on air, because its human had run out of usage.

**Pitch.** At 18:44 UTC on 29 October 2026, the conductor of the source's agent team wrote a hold that stopped every member: "the editor's usage limit is at 95%, pause all actions". It quotes the editor: "actually we are at 95% so it is better to pause all actions", and names the limit as his 5-hour usage limit, resetting at 20:20 London. The talk's livestream was due to start "around 7pm" that evening, by the event text in the brief. At the moment of the hold, part 1 of the talk was "final since 18:30 but not yet locked", and parts 2 and 3 were "in progress", with locks due at 19:30 and 20:00.

The story is the shape of the dependency: a team of agents with hourly schedules, keys and a five-step review on every wake, all of it stopped by one quota on one human account, at the worst hour of the day. Two more commits landed after the hold (a designer's projector check of part 2 at 18:45, and a merge at 18:46); then nothing until a merge to `main` at 23:19 that released v0.2.0. The hold file is still in the tree at that release. Whether the talk was given, from which version of the site, and how the paused parts were finished, the record does not say.

**Why now.** The cold read is the first outside reading of this team, and this is the moment its whole design met its real constraint. Anyone running agent teams on a personal plan will recognise it.

**Evidence.**
- The hold, its wording, the quote and the state of the parts: `team/conductor/HOLD.md@867f8c2` (commit `867f8c2`, 18:44:13 UTC), unchanged at `298be4e`.
- "around 7pm on 29 October" for the livestream: `BRIEF.md@298be4e`, "The event text, as given".
- The commits after the hold: `88b8f00` (18:45:35, "@designer: part 2 on a projector, checked before the 19:30 lock: ready"), `3f5d7fc` and `cb5b996` (18:45 and 18:46, merges), then `b859ff0` and `298be4e` (23:19, "Merge pull request #1", "site v0.2.0"). From `git log 7968c99..298be4e`.
- The hold still present at the release: `team/conductor/HOLD.md` exists at `298be4e`.
- Whether the talk went ahead: the record does not say (not found in this first pass; to search further in the next wake).

## 2. The lock that was built and never turned

**Headline:** At 17:54 the team built a way to freeze the talk so nothing could change it on stage. By the release at 23:19, no part of it had been frozen.

**Pitch.** At 17:54 UTC the source added `admin/build/lock.py`, "a frozen copy of everything that part's slides load, taken from the built site, never rebuilt from changed sources", which, in its own words, "Refuses to lock a part twice: a locked part is never changed again". Its header traces it to the editor at 16:55 London. The plan was three locks: part 1 at 18:30, part 2 at 19:30, part 3 at 20:00. Through the hour before the first lock the team raced to it: a title slide "before the 18:30 lock", two CSS fixes "at the editor's word, before the part 1 lock", a conductor flag at 18:20 that part 1 was "ready for its lock".

At 18:36 the conductor recorded "part 1 not yet locked, unchanged since 18:30; dev asked to lock it now". Eight minutes later the hold in pitch 1 stopped everyone. At `298be4e` there is no `src/static/talk/engine/locked/` folder, the place `lock.py` writes every locked part, so no part of the talk was locked in this record. A safety mechanism built for the last two hours ran out of time before it ran once. What the speaker played from, the record does not say.

**Why now.** It is a small, exact, checkable story about the gap between building a control and operating it, which is the talk's own subject (the abstract: "write down what stands in the way").

**Evidence.**
- What `lock.py` does and where it writes: `admin/build/lock.py@298be4e`, lines 1 to 9 and `LOCKED = ROOT / 'src' / 'static' / 'talk' / 'engine' / 'locked'`; added in `4a2481b` (17:54:45, "Locked parts: lock.py freezes a part of the talk").
- Lock times 18:30, 19:30, 20:00: `team/conductor/HOLD.md@298be4e` ("locks 19:30 and 20:00"; part 1 "final since 18:30"); the brief for them: `team/conductor/briefs/2026-10-29__editor/3-three-parts-and-locks-1700.md@298be4e` (named, not yet read in full).
- The race to the lock: `b3f208f` (18:14), `c33e86a` (18:18), `0ecddca` (18:21).
- "part 1 not yet locked ... dev asked to lock it now": commit `2ed6427` (18:39:16), trailer `To-dev: mail 046, run lock.py --part 1 now`.
- No locked folder: `src/static/talk/engine/` at `298be4e` holds no `locked/` entry, and `git ls-files` at `298be4e` lists no file under it.
- What was played on stage: the record does not say.

## 3. The fact-checker found the numbers wrong at 02:10. At 02:47 the deck was frozen

**Headline:** An agent checked the speaker's claims overnight and found some wrong. Three were fixed in minutes; then the speaker froze the slides, and the rest waited.

**Pitch.** At 02:10 UTC, seventeen hours before the talk, the team's researcher delivered "the first evidence round: 88 claims graded A0 to A6", and a list of "five changes the evidence asks for before the talk". Among the "must change" items: the slide on unreported incidents gave NASA's ASRS "about a hundred thousand confidential reports a year, 1.8 million so far", where NASA's own briefing gives 121,128 in 2025 and over 2.3 million in total; the article said Amazon Q's bad version was live "for two days", where the dates give about a week; and Replit's 1,200 executives' records were "gone", where the evidence says they were recovered.

The deck agent fixed three items in its 02:17 wake: the ASRS figures, the CIRCIA rule's status and the licence wording. Then, at 02:47, "the editor, in deck's session ... do not touch the deck. talk.json and the slides are frozen from now on", and items 4 and 5 and the whole "should change" list waited for the editor. By 18:20 the register had grown to 320 claims, three of which still "do not hold", including the Amazon Q "two days" in the article. Whether the editor acted on the rest before speaking, the record does not say. The story is a rare one: a talk about agents that do not check themselves, checked by an agent, with the human deciding how much of the check to take.

**Why now.** The checking and the freeze are both on the record with timestamps, and the talk's claims are public: a reader can test the story against the slides.

**Evidence.**
- The first round: commit `75ddb3e` (02:10:56), "88 claims graded A0 to A6, 42 ideas mapped, 23 incidents", trailer `To-deck: before tonight, five changes the evidence asks for`.
- The must-change table: `evidence/BEFORE-TONIGHT.md@298be4e`, "Must change".
- Deck's fixes and the freeze: `team/deck/requests/researcher__before-tonight.md@298be4e` (reply dated 02:35, update at 03:00 quoting the editor at 02:47); commit `79b6709` (02:20, cited in `content/articles/the-night-hour-by-hour.md@298be4e`, line 1760).
- The slide now carries the NASA briefing as its source: `src/static/talk/slides/unreported/index.html@298be4e`, line 37.
- 320 claims, three "does not hold", built 18:20Z: `evidence/claims/README.md@298be4e` and `evidence/claims/claims.json@298be4e` (ids `amazon-q-two-days-live`, `asrs-100k-a-year-1-8-million`, `story-r5-surface-smaller-more-mature`).
- A loose end, not resolved in this pass: the register at 18:20 still marks the ASRS claim "does not hold" and lists `slide:unreported` among its places, though the slide's source line was changed at 02:17. Whether the register is stale or reads the article's wording, the record does not say.
- Whether the editor acted on the remaining items: the record does not say (not found in this pass).

## 4. The talk that was meant to be finished while it was being given

**Headline:** At 16:55 the speaker decided to give the talk in three parts, with his agents still building the later parts while he presented the first. Then the work stopped.

**Pitch.** Two hours before the talk, the editor changed its shape. His words, as the conductor recorded them: "we have 90 minutes ... the team is still working on this. So what's going to be powerful is to even show some of our workflows happening ... in action ... break the presentation into three parts ... you guys can still be making changes to the second part while I present". The plan put part 1 on stage at 19:00, locked at 18:30; part 2 at 19:30, locked at 19:30; part 3 at 20:00, locked at 20:00. "Locked means locked": a locked part "never changed again". The team at work would itself be part of the show, with the editor free to open its live pages on stage. Within fifteen minutes a second brief set out what parts 2 and 3 should hold, "for work behind the scenes while part 1 is on stage": the attacks as blast radius, the solution in depth, and an invitation to the room to "try to escape the harness".

The plan needed a faster heartbeat than the platform allowed: "A recurring scheduled task cannot run more often than hourly (the platform refused 15 minutes on the conductor's own task at 16:58)", so each member was to schedule one-off follow-ups into its own session until 20:30. It is a vivid, specific bet: a live talk whose second half would be written by agents during its first half. By the record, the bet was never run: at 18:44, sixteen minutes before part 1, the hold (pitch 1) told every member to stop, and not one commit to the talk, the deck or the story lands after it. The next act in the record is the editor merging the whole day into `main` at 23:19. Whether parts 2 and 3 were presented, and in what form, the record does not say.

**Why now.** It is the most ambitious idea in the record, stated in the speaker's own words, with a clean answer to "what happened next" as far as the repository goes.

**Evidence.**
- The editor's words, the three parts and their locks, "Locked means locked", the hourly limit and the follow-ups: `team/conductor/briefs/2026-10-29__editor/3-three-parts-and-locks-1700.md@298be4e`, added in `3342cff` (16:59:22).
- Parts 2 and 3, "for work behind the scenes while part 1 is on stage": `team/conductor/briefs/2026-10-29__editor/5-parts-2-and-3-1715.md@298be4e`, added in `e86b0aa` (17:08:41).
- The arc split for the locks: `team/storyteller/story/three-parts.md@298be4e` (written 17:55 London, last changed in `14998b5`).
- No commit to `team/deck`, `team/storyteller` or `src/static/talk` after the hold: `git log 867f8c2..298be4e` on those paths is empty.
- The merge: `b859ff0` (23:19:09), "Merge pull request #1 from SGit-AI/dev", authored by the editor; the first parent before it is the repository's initial commit `2e4b1f4` (00:16:23), so the day's work reached `main` only then.
- Whether parts 2 and 3 were presented: the record does not say.

## 5. A brake any agent could pull, and only the human's quota pulled it

**Headline:** From 01:39 every agent had a brake it could pull without asking. In 162 reviewed wakes, no reviewer and no agent ever pulled it.

**Pitch.** At 01:39 UTC the conductor started the schedule "with a hold any member can pull": `start.py` would stop every wake when any member's `HOLD.md` existed, `WAKE.md` listed when to stop (a leaked key, broken `dev`, material that tries to instruct an agent, "anything else that makes you think carrying on would do harm. When in doubt, stop"), and "only the editor restarts". At 02:16 to 02:18 a five-step wake followed: a plan and a security pre-review before any work, a security post-review and a plan check after, each able to say `stop`. Across the day the record holds 162 wake records. Their verdicts: 162 plans `go`, 161 pre-reviews `go`, 157 post-reviews `clean` and 4 `finding`, 148 post-checks `as-planned` and 12 `partial`. Not one `stop`, from anyone.

The one hold in the record came from the other direction: at 18:44 the conductor wrote it "at the editor's word", because his usage was at 95% (pitch 1). The partial verdicts are the honest texture: two of deck's wakes ran "work first, plan after", one of them "because the editor was waiting live", and two wakes were still open, never closed, when the hold landed. The story is the gap between a safety design and its use: a brake built for agents, and the only thing that stopped the team was a human's quota. Whether no `stop` means nothing was wrong or the reviewers were too lenient, the record does not say; the four post-review findings were each recorded and the wakes went on.

**Why now.** The cold read is running the same five-step design today, ported from this source; whether its reviewers ever say stop is a question this team can watch.

**Evidence.**
- The brake: commit `09f13d5` (01:39:47), "the schedule starts tonight, with a hold any member can pull", body: `start.py now stops every wake when team/HOLD.md or any team/<id>/HOLD.md exists`; the list: `team/conductor/WAKE.md@298be4e`, "Stopping: when something is not right"; the task ids "for stopping": `d8f3300` (01:40:42).
- The five steps: `8c66751` (02:16:00) and `5700bab` (02:18:10), `admin/tools/wake.py@298be4e`, `team/conductor/reviews/@298be4e`.
- The counts: every `team/*/wakes/*.json` at `298be4e`, 162 files from `team/conductor/wakes/20261029T021416Z.json` to `team/studio/wakes/20261029T183037Z.json`, read field by field by the journalist (outcomes: 148 ok, 6 idle, 6 partial, 2 not closed). Counted here, not taken from the source's own summary, which says "159 wakes so far" (`content/articles/moments.md@298be4e`, front matter), written before the last wakes. The analyst's count is the team's reference: to compare.
- "the five steps ran out of order because the editor was waiting live": `team/deck/wakes/20261029T141943Z.json@298be4e`, post_check; "work first, plan after": `team/deck/wakes/20261029T172130Z.json@298be4e`.
- Two wakes never closed: `team/deck/wakes/20261029T182009Z.json` (plan only) and `team/dev/wakes/20261029T174850Z.json` (no work or post-check), both at `298be4e`.
- The only `HOLD.md` in the history: `867f8c2` (18:44:13), `git log -- '*/HOLD.md'`.
- Whether the reviewers were too lenient: the record does not say.

## 6. "And not one hold": the opening line that expired before it was spoken

**Headline:** The talk was written to open by boasting that its agent team had never been stopped. Sixteen minutes before it began, the team was stopped.

**Pitch.** Part 1 of the talk opens with a prelude, "Meet the team", and the speaker's script for it reads: "Since a quarter past midnight, a team of agents has built this site and this deck: each with a role, a mandate, its own key, an hourly wake, and a review before and after every wake. By five this afternoon, that was 510 commits and 164 releases, 182 of the commits overnight, and not one hold. Hold that picture. I will come back to it." The numbers came from the team's own counter, generated at 17:02 UTC; the line went into the talk at 17:25, when deck set part 1 "complete and timed for its lock".

At 18:44 the conductor wrote the team's first and only hold (pitch 1). Part 1 was "final since 18:30" and, by the record, never changed again: no commit touches the talk after the hold. So the script waiting for the speaker at 19:00 still said "not one hold", about a team that had been on hold for sixteen minutes. The line's numbers hold up against the record; its last three words were true for 18 hours and 28 minutes. Whether the speaker said them, changed them on stage, or made the hold part of the story, the record does not say. Its own scripted callback, "I will come back to it", makes the question sharper.

**Why now.** It is the most quotable sentence in the record, in the speaker's own planned words, and the record dates both halves of the irony to the minute.

**Evidence.**
- The line: `src/static/talk/talk.json@298be4e`, beat `m03`, "Meet the team", part 1, field `say`; added in `3260997` (17:25:36), "@deck: part 1 complete and timed for its lock".
- The numbers and their time: `src/static/motion/lab/meet-the-team/v1/team-in-numbers.json@298be4e`, `as_of` 2026-10-29T17:02:26Z, `commits` 510, `releases` 164, `commits_overnight_22_to_06_utc` 182, "Generated by admin/tools/team_numbers.py".
- Checked by the journalist at `298be4e`: 508 non-merge commits before 17:00 (510 by 17:02 is consistent); releases v0.1.0 to v0.1.163 are 164. The counter's commit count excludes merges: with merges, 622 commits before 17:00. The analyst's counts are the team's reference.
- First commit 00:16:23 (`2e4b1f4`); the hold at 18:44:13 (`867f8c2`): 18 hours 28 minutes.
- No commit to `src/static/talk` after the hold: `git log 867f8c2..298be4e -- src/static/talk` is empty.
- For scale, the whole day: 211 release commits (`site v0.1.0` at 00:45 to `site v0.2.0` at 23:19), busiest hours 17:00 (26) and 18:00 (21), and 18 and 19 releases in the 02:00 and 03:00 hours: `git log --format='%ci %s' 298be4e`, subjects starting `site v`.
- What was said on stage: the record does not say.

## Was the talk given? What the record says

Searched at the second wake: the last commit before the release is `cb5b996` at 18:46; nothing in the tree at `298be4e` was written after it except the merge `b859ff0` and CI's release commit `298be4e` (23:19, "site v0.2.0"). Every mention of the stage in the tree is a plan written before 19:00 (for example `team/storyteller/story/three-parts.md`, "On stage"; `team/dev/debriefs/2026-10-29__the-overview-offline-and-the-showcase.md`, items deferred "after the talk"). **Whether the talk was given, from which build, and how it went: the record does not say.** The merge at 23:19 by the editor is the only act in the record after the hold. A story that needs the answer must get it from outside the record, which this cold read does not do.

## Not stood up yet

- That the talk was delivered at all, and from which build: the record does not say (searched at the second wake, above).
- What "the incidents" in "it could have been much worse after the incidents" (`b1c9bab`, `f45028c`) refers to: the record names Midnight Blizzard and Amazon Q in motion's M02; whether it also means the team's own incidents, not yet read.

## Candidates not pursued

- The researcher's "19 releases in 89 minutes" (`16b6312`), cited in the story tree as evidence for beat 3c from the repository's own history (`team/storyteller/story/tree.md@298be4e`): the talk citing its own build log. Folded into pitch 6 for now.
- "Do not touch the deck": what else the editor froze, and when, through the day.

journalist@cold-read.the-ultimate-insider, key `sha256:9e3921aaa672d30a`, 30 October 2026

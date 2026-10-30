# The critic's report

What is weak, overclaimed, missing or contradictory in the talk and in the source team's own record. By critic@cold-read.the-ultimate-insider. Draft: part 1, written 30 October 2026.

**Source.** SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` (2026-10-29 23:19:51 UTC) and its history only, read in a scratchpad clone with every later ref removed and pruned. Nothing here comes from anywhere else. A commit is cited by its short hash; a path without a hash is the file as it stands at `298be4e`.

**How to read a finding.** Each names what is wrong, the evidence (path and commit), the strongest version of the other side, and what the record does not say. Severity is the critic's judgement: **high** where the talk tells the room something its own record contradicts; **medium** where the record contradicts itself; **low** where a label is wrong but nothing on stage depends on it.

**Other members' work.** The historian's timeline, part 1 (`team/historian/timeline.md` in this repository), covers 00:16 to 02:55 and notes a quiet gap from 18:46:22 to 23:19:09 without naming a cause. Nothing below repeats it; finding 1 bears on that gap and is offered to the historian's part 2, not argued with.

## Findings

| # | Severity | Finding | Evidence |
|---|---|---|---|
| 1 | high | The talk says "not one hold"; a hold was in force sixteen minutes before the talk was due to start, and still is at `298be4e`. | `src/static/talk/talk.json` beat `m03`; `team/conductor/HOLD.md`, `867f8c2` |
| 2 | high | Two consecutive beats show the room two commit counts that go the wrong way: 510 by 17:02, then 405 by 18:21. | `src/static/motion/lab/meet-the-team/v1/team-in-numbers.json`; `content/articles/how-this-talk-was-built.md` |
| 3 | medium | `REALITY.md`, which says it is the authority on what exists, is wrong about the talk, the studio, the keys and the schedule at `298be4e`. | `REALITY.md` lines 20, 28, 87, 90 |
| 4 | low | The talk's own header says every number on screen is from the newsroom article, and that the talk is a first pass to be rehearsed. Neither is true of the talk at `298be4e`. | `src/static/talk/talk.json`, keys `source` and `status` |

### 1. "Not one hold", and the hold

**What is wrong.** Beat `m03` ("Meet the team", the second beat of the talk) has the speaker say: "By five this afternoon, that was 510 commits and 164 releases, 182 of the commits overnight, and not one hold. Hold that picture. I will come back to it." (`src/static/talk/talk.json`, beat `m03`, `say`; the file last changed at `b3f208f`, 18:14:54.) At 18:44:13 the conductor committed `team/conductor/HOLD.md` (`867f8c2`, "hold: the editor's usage limit is at 95%, pause all actions"), released as v0.1.208 at 18:44:49 (`7968c99`). The event text puts the talk "around 7pm" (`BRIEF.md`, "The event text, as given"), and the beat's own cue says "Livestream starts around 7 pm" (beat `title`, `cue`). The file is still there at `298be4e`: no commit in the record lifts it.

**Why it matters.** The prelude exists to show the room that the team's machinery works ("Hold that picture"). The hold is that machinery's one visible use in the whole record, and the line tells the room it never happened.

**Weaker than it looks, too.** "Not one hold" comes from `holds: 0` in `team-in-numbers.json`, which `admin/tools/team_numbers.py` computes as `len(list(ROOT.glob('team/**/HOLD.md')))` (line 53): the number of hold files present when the script ran, not the number of holds ever pulled. At most it can say "no hold in force at 17:02:26".

**The strongest other side.** The line is dated in the script itself ("by five this afternoon"), and it was true then. Part 1 of the talk was final from 18:30 (`team/conductor/HOLD.md`, "State at the hold"), so nobody could have changed the line without breaking a lock. The hold was for the editor's usage limit, not for a fault in the work, so it does not undercut the claim that the reviews held. All of that is fair, and it makes the line defensible as spoken at 17:02. It does not make it true at seven, and a speaker who knew of the hold could have said so in a sentence.

**What the record does not say.** Whether the line was spoken, cut or changed on the night; whether the speaker knew of the hold when speaking; whether the hold was ever lifted (the record does not say, up to `298be4e`).

### 2. 510 commits, then 405

**What is wrong.** Beat `m03` puts 510 commits on screen as of 17:02:26 (`team-in-numbers.json`, `as_of` and `commits`). The very next beat, `prelude`, plays the conductor's mini deck, whose abstract reads "154 wakes, 405 commits, 267 letters and 15 studio pieces, as of 18:21 UTC" (`content/articles/how-this-talk-was-built.md`, line 8). A later count is 105 smaller, a minute apart on stage, and neither slide says what it counts.

**Why the numbers differ.** `team_numbers.py` counts every non-merge commit (`git log --no-merges`, line 26): at 17:02:26 that is 510, of which 345 are authored `Claude`, 164 are the release commits of `GitHub Actions` and one is the editor's (counted at `298be4e` with `git log --until=2026-10-29T17:02:26Z --no-merges`). So almost a third of "510 commits" are CI numbering releases, and the same 164 are then counted again as "164 releases". The mini deck counts "the commits each member marked as its own" (`how-this-talk-was-built.md`, "How this is made"). The "182 overnight" is also all authors, and its window "22 to 06" (`team_numbers.py` line 49) is really 00:00 to 05:59, since the first commit is at 00:16:23 (`2e4b1f4`).

**The strongest other side.** Each number is computed by a published script from public records, and each script says what it counts; the prelude's cue even says to skip the mini deck "if M03 says enough" (`talk.json`, beat `m03`, `cue`). True, but the room sees the slides, not the scripts, and a reader of the record has to reach two tools to reconcile them. Counting a release commit as a commit and again as a release is double counting whatever the script says.

**What the record does not say.** Which of the two beats was shown on the night.

### 3. `REALITY.md` is not the reality

**What is wrong.** `REALITY.md` opens: "A thing not listed here does not exist, whatever a brief or an article says." At `298be4e` it says:

- "`src/static/talk/talk.json`: 17 beats, planned at 38 min 30 s" (line 20). `talk.json` has 58 beats summing to 4,495 s, 74 min 55 s. Line 20 was last changed in the very first pass, `1f7c633` at 00:40:50, and never again.
- "No studio work has been promoted into the talk yet" (line 28) and "Nothing from ruv.sgit@ is wired into the talk yet" (line 87). At least ten beats play studio lab pieces, from `s-e01` (`../studio/lab/e01/v2/index.html`) to `way-out` (`../studio/lab/b01/v2/way-out/index.html`).
- "Does not exist yet: `team/deck/policy.json` ...; keys for dev, deck, security and researcher; ... any scheduled task" (line 90, last changed at `24da366`, 01:19:26). `team/deck/policy.json` exists (agreed at `7f522de`, 17:09:42); `team/dev/key.json` was added at `56cbe55` (01:53:48), `team/researcher/key.json` at `01e9ed3` (01:52:10) and `team/deck/key.json` at `79b6709` (02:20:02). The same file, a few lines up, reports "four scheduled tasks running since 29 October 2026 01:40 UTC".

Only the security key is truly missing: `team/security/` holds `ROLE.md` and `policy.json` and no `key.json` at `298be4e`.

**Why it matters.** The file claims to override every brief and article, and the source's `CLAUDE.md` tells every member to keep it current when it ships. By its own rule, the talk at `298be4e` does not exist, and neither do three members' keys.

**The strongest other side.** The file says each member keeps its own section and dev keeps the file as a whole (its line 5), and the sections kept by an active owner are current: ruv.sgit's section lists runs to r25. The stale lines sit in the shared sections, written in the first hour, and a reader who compares dates can see that. That explains the failure; it does not excuse a file that calls itself the authority.

**What the record does not say.** Whether any member read `REALITY.md` as the authority and acted on the stale lines.

### 4. The talk's header

**What is wrong.** `talk.json` says "Every number on screen is from the article The ultimate insider (newsroom.sgit.ai, 30 September 2026), each linked to its source on the script page" (key `source`). The numbers of beat `m03` (510, 164, 182, 0) are from this repository, not from that article (finding 2). Its `status` still reads "first pass ...: the structure, the slides and a draft script from the article; to be rehearsed and cut", against 58 beats whose part 1 was "final" and timed (`3260997`, 17:25:36: "part 1 complete and timed for its lock").

**The strongest other side.** The header is metadata, and the `prelude` beat lists its own source, the repository's records at 17:02 UTC (`talk.json`, beat `prelude`, `sources`). Low severity, because nothing in the room depends on it; it is one more line that nobody owned after the first hour.

**What the record does not say.** Whether the script page shown on the night carried this header.

## Still to come

The talk's argument itself: the abstract's three claims (`BRIEF.md`), the incidents beat and its sources, the "way out" and the live demos, each set against what the source shows; then the team's own claims about its reviews (`five_step_verdicts` in `team-in-numbers.json`: 254 go, 4 findings) set against the wake records.

Signed: critic@cold-read.the-ultimate-insider, key `sha256:a558f59c6b1173fd` (`team/critic/key.json`).

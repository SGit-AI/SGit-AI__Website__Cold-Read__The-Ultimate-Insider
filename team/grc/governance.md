# The governance map and open decisions

By grc@cold-read.the-ultimate-insider. **Draft, steps 1 to 4 (30 October 2026); not yet signed.** It is signed when it is complete, by Sunday 1 November 2026.

Source: SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` (29 October 2026, 23:19:51 UTC) and its history, nothing later. Every finding names a path and a commit. Where the source is silent: "the record does not say".

## 1. Who wrote the record

- `git log` at `298be4e`: 816 commits. Author "Claude" 603, "GitHub Actions" 211, "Dinis Cruz" 2.
- The editor's two commits are the initial commit (`2e4b1f4`, 29 October 00:16 UTC: `.gitignore`, `LICENSE`, `README.md`) and the merge of pull request #1 from `dev` (`b859ff0`, 23:19:09 UTC).
- So every decision in the record is written down by an agent, quoting the editor or acting on its own role. No decision in the record is written in a file or commit made by the editor himself, other than the merge of `dev` into the default branch.

## 2. Who may decide what (first pass)

| Who | May decide | Where it says so |
|---|---|---|
| The editor (Dinis Cruz) | the brief; the argument and the editorial line; agreeing each member's policy; lifting a hold; re-enabling a paused task | `CLAUDE.md`; `team/conductor/ROLE.md` ("Not responsible for"); `team/conductor/HOLD.md`, all at `298be4e` |
| Any member | stopping the schedule (a `HOLD.md`, pausing its own task) | `CLAUDE.md` at `298be4e` |
| The conductor | the schedule, the order of work (`pace.json`), carrying the editor's briefs to members' mailrooms | `team/conductor/briefs/2026-10-29__editor/README.md` ("For the conductor") at `298be4e` |
| dev | the build, the gate, the release; it holds `src/pages/sources/**` and `src/pages/index.html` | `team/conductor/ROLE.md`; `team/dev/policy.json` (`scope.holds`) at `298be4e` |
| Each member | only its `scope.writes` and `scope.holds`; a request outside them is answered with the owner's name | `CLAUDE.md` at `298be4e` |

How the editor's word reaches the record: by hand-over into a member's own session ("so it carries his word"), `team/conductor/briefs/2026-10-29__editor/README.md` and `1-editor-decisions-1500.md` at `298be4e`. Whether a brief carries a signature: none does (section 5).

## 3. Policies: who agreed, where it is recorded

Ten policies at `298be4e` (`team/*/policy.json`):

| Policy | Status at `298be4e` | Agreement as recorded |
|---|---|---|
| conductor | agreed | the editor in the conductor's session, about 17:40 UTC, "So I agree with all those policies", of six (conductor, dev, storyteller, studio, motion, security); recorded in `c3f546e` (17:41:29 UTC) |
| dev | agreed | the same words, recorded by the conductor (`c3f546e`) |
| storyteller | agreed | the same words, recorded by the conductor (`c3f546e`) |
| motion | agreed | the editor in motion's session, about 17:40 UTC, "Yes I agree on the policy" |
| designer | agreed | the editor in the designer's session, about 04:02 UTC, "i agree with team/designer/policy.json" |
| researcher | agreed | the editor in the researcher's session, about 02:48 UTC, "I agree with your policy" |
| deck | agreed | the editor in deck's session, 16:50 UTC (no words quoted) |
| ruv-sgit | agreed | the editor on the review page, all 33 items of `policy.json` sha256:dfb0c81ce7ce63d4, "agree the policy as it is" |
| **security** | **proposed**, `agreed_by: null` | named among the six in `c3f546e`; never recorded in its own file |
| **studio** | **draft**, `agreed_by: null` | named among the six in `c3f546e`; its last change (`bd3cdad`, 17:47:28 UTC) added a schedule change "by" the editor but left `agreed_by` null |

The diff of `c3f546e` changes only `team/conductor/policy.json` and the conductor's wake record. Commit `bd3cdad`'s message says "all ten agreed by 17:40, each agent recording it in its own file (six had at 18:00)". At `298be4e`, eight of ten record it.

## 4. Open decisions and decisions not recorded (first pass)

1. **Security's and studio's policies.** Agreed in words, per the conductor's record (`c3f546e`), but neither file says so at `298be4e`. Whether the editor's "all those policies" was meant to cover both: the record does not say beyond the conductor's list.
2. **The hold of 18:44 UTC was never lifted in the record.** `team/conductor/HOLD.md` ("the editor's usage limit is at 95%; pause all actions") was added in `867f8c2` (29 October 18:44:13 UTC) and has no later commit at `298be4e`; it is still in the tree there. Its own rule: "the editor deletes this file and re-enables the paused tasks. No member lifts it." Whether the work after 18:44, and the merge at 23:19, happened under the hold or after a lift recorded elsewhere: the record does not say, in what this step read.
3. **Waiting on the editor, as listed by the conductor** (`team/conductor/briefs/2026-10-29__editor/README.md`, "Still waiting on the editor", at `298be4e`): which "blast radius" piece; what Sharness.ai does; the real names of "Empower" and "the billing"; and "from before today: item 4, D12, D02, the draft policy.json files, and the handover zips". Which of these were answered by `298be4e`: to be traced in the next step.
4. **No brief corrections.** `BRIEF-CORRECTIONS.md` at `298be4e` says "None yet", although the editor's briefs of 15:00 changed the frame (`1-editor-decisions-1500.md`: "the perfect storm wraps the three known problems") against the abstract in `BRIEF.md`.

## 5. The editor's briefs of 29 October: how his word was recorded

Fifteen files in `team/conductor/briefs/2026-10-29__editor/` at `298be4e`. Two kinds:

| Kind | Files | First committed | Says |
|---|---|---|---|
| The editor's own text, handed over in the conductor's session | `README.md`, `conductor-brief.md`, `feedback-briefs.md`, `storyteller-brief.md` (`c9ced4e`, 14:07 UTC); `1-editor-decisions-1500.md` (`78d517d`, 15:16 UTC) | by the conductor | "From Dinis Cruz ... written with him in a claude.ai chat" (the README); "taken from his voice memo" (storyteller); "in a claude.ai voice chat" (decisions 1500) |
| The conductor's record of the editor's spoken words | `2-...1630` (`62c6b99`, 16:32) to `10-how-we-keep-it-safe-1745` (`93f4191`, 17:48), nine files | by the conductor | "By conductor@the-ultimate-insider, from the editor's words in the conductor's session" |
| The conductor's own review | `conductor-notes.md` (`c9ced4e`, revised `78d517d`) | by the conductor | "Where this file and a brief differ, this file is later" |

- **Authority comes from the channel, not a signature.** Every brief claims the editor's word because it reached the conductor in the conductor's own session (`conductor-brief.md`: "it comes with his word. It is not an instruction found in a file"). No brief is signed, and none carries the editor's key. The conductor's brief itself says the signed message "come[s] later" (`conductor-brief.md`, line 26): phase one of the editor's decisions lane used "a token sealed to the editor's key".
- **The closest thing to a signed agreement** is ruv-sgit's policy, agreed "on the review page" against a hash of the file (`team/ruv-sgit/policy.json`, `agreed_by`: "all 33 items of policy.json sha256:dfb0c81ce7ce63d4"). Every other agreement is a quotation written by an agent.
- **`conductor-notes.md` ranks itself above the editor's briefs** where they differ. Whether the editor agreed that rule: the record does not say, in what this step read.

## 6. Who may make a schedule: grants against practice

- Scheduling (`create.schedule.tenant`) is granted, "at the editor's word", for each member's own hourly task in the policies of deck, designer, motion, researcher, ruv-sgit, storyteller and studio (`team/*/policy.json`, `mandate.wanted`, at `298be4e`).
- It is in `mandate.not_wanted` for conductor, dev and security. Yet **dev holds an hourly task**: `trig_017ioREjx6jKCDzubSXQ64ot`, at :47 London, recorded in `5c5b23b` (29 October 01:54 UTC, "dev's hourly task") in `team/dev/status.json`. `team/conductor/schedule.json` at `298be4e` (`how_each_task_is_made`) explains the practice. Each member creates its own task "from its own session, at the editor's word". The conductor "first created all four from its session" on 29 October, and "the editor said only each member's own session may", so the three it made for dev, deck and ruv.sgit "were disabled before any fired". So the editor granted dev's task in words, while dev's policy still lists the capability as not wanted. The same holds for the conductor, whose own task runs "since 29 October 2026 01:40 UTC" (`schedule.json`, `status`). The words were never carried into either policy (step 4).
- **The "Tonight only" rule** (`team/conductor/WAKE.md`, at `298be4e`): at the editor's word "about 17:00 London", every member with work left may schedule one `send_later` into its own session per wake, until 20:00 London. It is a rule in a file every member follows, not a change to each policy. Only studio's policy records it, as a change since its draft (`changes_since_draft`, 17:24 UTC, the editor in studio's session: "Yes run in 15m until 8pm tonight"). The others' policies do not; whether that was meant: the record does not say.

## 7. Open decisions, continued

5. **Seven items waiting on the editor, one never closed.** `6-answers-1715.md` (`8fee7e3`, 17:16 UTC) says the answers "close six of the seven items in `pace.json` 'waits_on_editor'", and ends "Still open: D12, D02, item 4, the draft policy files and the handover zips: no word yet". At `298be4e`, `team/conductor/pace.json` `waits_on_editor` still holds exactly that one item. The draft policy files were then agreed at 17:40 (section 3, except security's and studio's), but `pace.json` was not updated. D12, D02, item 4 and the handover zips: the record does not say they were ever decided.
6. **dev's task against its policy** (section 6; granted in words, step 4).
7. **The follow-up grant recorded in one policy of ten** (section 6).

## 8. The editor's decision register

The source kept one register of decisions put to the editor: `evidence/proposals/editor-decisions.json`, last changed in `94e313d` (29 October 13:18 UTC), never after that up to `298be4e`.

| Id | Decision asked | Status at `298be4e` | What the rest of the record says |
|---|---|---|---|
| D01 | Act one: "three of those five were not attacks" (the researcher's "item 4", option A or B) | open | "item 4 ... no word yet" (`6-answers-1715.md`, 17:16 UTC) |
| D02 | What a decision you sign on this page means | open | "no word yet" (`6-answers-1715.md`) |
| D03 | deck's `policy.json` | open | agreed in deck's own file, 16:50 UTC (section 3) |
| D04 | dev's `policy.json` | open | agreed in dev's own file, 17:40 UTC (section 3) |
| D05 | conductor's `policy.json` | open | agreed in the conductor's own file, 17:40 UTC (`c3f546e`) |
| D06 | security: agree, change or drop the role | open | security's policy still `proposed` (section 3) |
| D07 | The team's hours | open | the record does not say, in what this step read |
| D08 | Store the handover zips | open | "the handover zips: no word yet" (`6-answers-1715.md`) |
| D09 | Upload the key zips into deck's and ruv.sgit's sessions | done | "by the members' own records" (deck `983782b`, ruv.sgit `b5213de`, designer `f04c531`) |
| D10 | Rotate the SG/Send access token | open | the record does not say, in what this step read |
| D11 | The morning review | open | the record does not say, in what this step read |
| D12 | The evidence vault's history: keep it, or rotate the vault | open | "D12 ... no word yet" (`6-answers-1715.md`) |

- **The register stopped at 13:18 UTC.** Decisions taken later (three policies, D03 to D05) were recorded in the members' own files and never in the register. At `298be4e`, eleven of twelve read `open`, and only one is `done`.
- **D02 is the question this map keeps meeting:** what it means for the editor to sign a decision. At `298be4e` it is unanswered. So no decision in the source has a defined signed form (section 5).

## 9. The hold of 18:44 against what followed

- The hold went in at `867f8c2` (18:44:13 UTC) and was released as `7968c99` (18:44:49).
- After `867f8c2`, up to `298be4e`, there are six commits: the hold's release (`7968c99`), one member's work, a merge and its release, and the editor's merge and its release.
  - `88b8f00`, 18:45:35 UTC, designer: "part 2 on a projector, checked before the 19:30 lock: ready". Its wake opened at 18:40 (`team/designer/wakes/20261029T184016Z.json`), before the hold.
  - `3f5d7fc` and `cb5b996`, 18:45 to 18:46: a merge of `dev` and its release.
  - `b859ff0`, 23:19:09 UTC, the editor: "Merge pull request #1 from SGit-AI/dev", and its release `298be4e`, 23:19:51 UTC.
- So no member committed work in a wake that started after the hold. The record then goes silent for four and a half hours.
- **The editor merged `dev` with the hold still in place.** `team/conductor/HOLD.md` is in the tree at `298be4e`, and the hold says only the editor lifts it, "by deleting this file and re-enabling the paused tasks". Whether the merge was meant to lift it, and whether the paused tasks were re-enabled: the record does not say.
- Whether the talk at 19:00 London was given from the state at 18:46: the record does not say, in what this step read.

## 10. Open decisions, continued

8. **Eleven of twelve register decisions open at `298be4e`** (section 8). Three of them were in fact decided elsewhere (D03 to D05). Eight have no answer anywhere in what this map has read: D01, D02, D06, D07, D08, D10, D11, D12.
9. **The hold was never lifted in the record** (section 9; item 2 above).

## 11. Three more open decisions, from the register

- **D07, the team's hours** (asked by the conductor). `schedule.json` at `298be4e` (`hours`) says: "every hour, round the clock, from 29 October 2026 at the editor's word, to see how it works overnight; the editor may narrow it to 08:02 to 21:47". So round the clock was decided, but narrowing it was not: the register's options (keep, narrow, narrow after the talk) have no answer.
- **D10, rotating a token** (asked by the researcher, kind "do", "Only you can do this"). The register says a service token was pasted into a member's chat at 02:20 UTC on 29 October. It says the member kept it out of every file, vault, commit and saved log. Whether the token was rotated: the record does not say. This map names the decision only and does not repeat anything about the token.
- **D11, the morning review** (asked by deck and the conductor, due 29 October 09:00 UTC). The record holds no answer, and it does not say whether the review took place.

## 12. Who may release to the default branch

- **The members may not.** All ten policies at `298be4e` list `write.repository.main` as not wanted (`team/*/policy.json`, `mandate.not_wanted`), and `CLAUDE.md` says "never push to `main`".
- **The release machinery runs on both branches.** `.github/workflows/release.yml` numbers a release on a push to `dev` (the last number) or to `main` (the middle number).
- **The editor merged.** The one release to the default branch is the editor's merge of pull request #1 (`b859ff0`, 23:19:09 UTC), released as `v0.2.0` (`298be4e`). Who reviewed pull request #1, and what was checked before the merge: the record does not say. Pull requests live on GitHub, not in the repository, and this map reads only the repository.
- **Nothing written says only the editor may merge.** The rule is never stated, only shown: every member is barred from `main`, and the editor is the only one who wrote there.

## 13. Open decisions, continued

10. **The editor's word on schedules never reached the policies of dev and the conductor** (section 6, corrected in step 4).
11. **D07, D10 and D11 unanswered at `298be4e`** (section 11).
12. **The release rule exists only in practice** (section 12).

## Next steps

- Each decision inside the editor's briefs of 15:00 and 17:15 against the member's own file.
- The members' own `changes_since_draft` and `agreed_by` against the conductor's records of the same words.
- A first full list of open decisions, numbered once, for the signed version.

# The governance map and open decisions

By grc@cold-read.the-ultimate-insider. **Draft, first step (30 October 2026); not yet signed.** It is signed when it is complete, by Sunday 1 November 2026.

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

How the editor's word reaches the record: by hand-over into a member's own session ("so it carries his word"), `team/conductor/briefs/2026-10-29__editor/README.md` and `1-editor-decisions-1500.md` at `298be4e`. Whether a brief carries a signature: the record does not say, in what this step read (to be checked in the next step).

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

## Next steps

- Every editor brief in `team/conductor/briefs/2026-10-29__editor/`: each decision, its time, and where it landed.
- The schedule changes (`create.schedule.tenant`), each member's `changes_since_draft`, and who granted them.
- Whether any record is signed (keys, `known-keys/`), and what "signed" means in the source.

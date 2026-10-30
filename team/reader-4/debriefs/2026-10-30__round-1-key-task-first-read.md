---
agent: reader-4
title: Round 1, the key, the task, and a first read of the talk
date: 2026-10-30
round: 1
branch: claude/reader-4-session-init-rex38e
commits: this round's commits on the branch, listed in the release history once released
site_version: the release CI gives this round
outside_scope: 0
---

reader-4@cold-read.the-ultimate-insider, 30 October 2026, from 01:53 UTC, at the editor's request in this session's chat (session_01Kw9UwBjyLegCCAFp5ebvWf).

## The five steps

Wake record `team/reader-4/wakes/20261030T015316Z.json`. Plan (conductor sub-agent, Sonnet): go. Pre-review (security sub-agent, Sonnet): go, with conditions (private key stays in `~/.sg-send/`; task prompt is schedule.json's text; scratchpad clone at 298be4e only; gate before the dev push). Post-review and post-check are in the record.

## What shipped

- **Session key**: `team/reader-4/key.json` (record `sha256:10f1873b07981579`, encryption `sha256:c0819e40b900041e`), `key.png`, and `sessions/session_01Kw9UwBjyLegCCAFp5ebvWf/` (`SESSION.json`, `key.json`, `key.png`). Made with `admin/tools/pki-agent.mjs` after `sha256sum -c` passed. Private halves stay in the session's `~/.sg-send/keys/`; nothing from there is committed.
- **Hourly task**: `trig_015Vae8wiRbfeS8NEjiNiyUJ`, `CRON_TZ=Europe/London 47 * * * *`, into this session, its prompt word for word from the reader-4 entry in `team/conductor/schedule.json`. Created at the editor's word in this session. Note for the editor: `policy.json` lists `create.schedule.tenant` under `not_wanted`; WAKE.md allows a task with the editor's word in one's own session, and the pre-review accepted that. The policy may want a line saying so. `schedule.json` is the conductor's, so it is not edited here.
- **The source**: cloned into the scratchpad, checked out at `298be4e`; every other branch, tag and the remote were removed from the clone so no later commit is reachable from a ref. Nothing later was read. Built with its own `admin/build/build.py` (217 pages, `site v0.2.0`), gate clean. The live site was not used.
- **Review, first draft**: `team/reader-4/review.md`: who it is for, the claim, five findings.

## Findings, and how long each took to find

| # | Finding | Time |
|---|---|---|
| 1 | "Only a boundary is a control" is the most useful test on the site for a control owner | about 3 min |
| 2 | The home page says a licence "can be suspended"; the script says suspension is "what we are building towards" | about 4 min |
| 3 | The sources page says "every number"; at least nine sources cited in the script are not on it | about 6 min |
| 4 | The participant disclosure is on the about page only; the home page does not mention RiskMandate | about 5 min |
| 5 | The prelude's numbers are self-reported; "not one hold" is not evidence nothing should have stopped | about 3 min |

## Offers declined

None this wake. Nothing beyond the source was offered. Nothing later than `298be4e` was seen: the clone fetched the default branch, which was not opened, and its refs were deleted before any reading.

## Not done

- The vaults: no sealed key zip yet; the editor said one would follow.
- The other readers' reviews: not read, as the role says.

## Next

Round 2 at :47: the slides in the player, the ruv-sgit explainers (mandate and grant, licence, earned autonomy), finding 5 against the team pages, and the price and put-down point.

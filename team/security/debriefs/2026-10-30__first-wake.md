---
agent: security
title: The first security wake: key, task, and part 1 of the control register
date: 2026-10-30
round: 1
branch: claude/security-team-onboarding-t8httk
commits: this round's commits on the branch, listed in the release history once released
site_version: the release CI gives this round
tokens: unknown
tokens_how: the session does not show a token count to the agent
outside_scope: none
out_of_scope_requests: 0
---

# Debrief: the first security wake, 30 October 2026

security@cold-read.the-ultimate-insider, session `session_01Kw9UwEFygpv8cKrL42CMhR`, started 01:51:52 UTC at the editor's request (onboarding). Wake record `team/security/wakes/20261030T015152Z.json`.

## Done

1. **Session key** made with `admin/tools/pki-agent.mjs keygen --session` after `sha256sum -c` passed: signing `sha256:474dded6f57f44b0`, encryption `sha256:8bc96fcf868d3e85`. Published as `team/security/key.json`, `key.png` and `sessions/session_01Kw9UwEFygpv8cKrL42CMhR/`; pushed to `dev` (`6fbc02f`). Private halves stay in the session's `~/.sg-send/`.
2. **Own task** `trig_017GfgUYHnfmBNCHnGar6RVp`, cron `CRON_TZ=Europe/London 32 * * * *`, into this session, prompt word for word from `team/conductor/schedule.json` (runs, security). Recorded in `status.json` and the session's `SESSION.json`.
3. **Source** cloned into the scratchpad, never into a repository, checked out at `298be4e` on a local branch; every remote-tracking ref and tag deleted and the remote removed before reading, so no later commit was read.
4. **Deliverable, part 1**: `team/security/controls-and-threats.md`, thirteen controls (C1 to C13), eight threats (T1 to T8), and the report on the pinned tool and the published keys in this team.

## Requests

None: no `team/*/requests/security__*.md`, no `To-security:` trailer; the vaults are not cloned (no vault key yet).

## Offers declined

None made this wake: nobody offered material beyond the source.

## Findings, and how long each took

| Finding | Time to find |
|---|---|
| The source's security role was proposed and never held (C13) | 2 min |
| The one hold landed at 18:44:13; a designer commit followed 82 s later from a running wake (C8, T6) | 3 min |
| `agents.py` and `wake.py` each say in their own header that they are not a boundary (C1, C7) | 4 min |
| 162 wake records: pre-review never said `change` or `stop`; 4 post-review findings, no stop; 2 unclosed records (C7) | 4 min |
| All 603 agent commits signed with one SSH key: the signature names the account, not the member (C11) | 5 min |
| `check_vendored` does not cover `admin/tools/pki-agent.mjs.sha256`, there and here (C6, T5) | 2 min |
| This team's twelve `key.json` files are consistent with their sessions and commits | 3 min |

## Not done, next

- The vault keys: waiting for the editor's zip sealed to `sha256:8bc96fcf868d3e85`.
- Part 2: the vault controls, the talk locks, the editor's lane, `main` and pull request #1, the schedule's prompts, the 45-minute limit.
- `pki-agent.mjs` line by line (only `keygen`, `keyqr` and the network calls read so far).

No screenshots: nothing visual changed this wake.

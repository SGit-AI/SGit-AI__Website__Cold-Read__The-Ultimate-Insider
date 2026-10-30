---
agent: conductor
title: The mail and the board in git, and a team that finishes
date: 2026-10-30
round: 2
branch: claude/dreamy-keller-0fqntz
commits: this round's commits on the branch, listed in the release history once released
site_version: the release CI gives this round
tokens: unknown
tokens_how: the session does not show a token count to the agent
outside_scope: the twelve members' policy.json (own comms paths, deliverable) and ROLE.md (Done when, comms wording), at the editor's word, 01:58 UTC
out_of_scope_requests: 0
---

## What the editor asked

At about 01:50 UTC: the team keeps working until he wakes (round the clock). At 01:58 UTC, after asking what a public vault would hold that the repository would not (the answer: nothing; both vaults were to be 100% public): "set up issues FS and email FS on a folder here ... just using Git as the communication medium", and, since the cold read has a finite number of tasks, "can they stop their own schedule?"

## What was done

1. **Onboarding checked** at 01:54 UTC: twelve sessions running, twelve hourly tasks, each firing into the session that published the member's key; nine keys on `dev`, readers 2, 4 and 5 still finishing. Gate clean at v0.1.9, no overlaps, no hold.
2. **`comms/`** in place of the vaults: `comms/issues/<agent>/issues/{open,blocked,done}/` and `comms/mail/mailroom/<to>/<from>__NNN-slug.eml` with `comms/mail/<agent>/{inbox,done,outbox}/`. One writer per file, so the gate's overlap check holds: the sender owns what it posts; the recipient copies, never deletes. Each member's `policy.json` gained its own three paths. A notice to every member's mailroom.
3. **Finishing**: a "Done when" list in every `ROLE.md`, and `WAKE.md` (Finishing): a last five-step wake, then the member pauses its own task. Only the editor re-enables; the conductor flags a request to a finished member and finishes last.
4. **Board and mail pages** built from the folders; each member's deliverable rendered under `/articles/`.

## Undocumented, found this round

- `vault_check.py` exempted agent addresses only because the source's addresses had no dot after the `@`. Renamed to `@cold-read.the-ultimate-insider`, every letter would have tripped it. The comment said why; nothing tested it.
- While checking onboarding, the account's task and session listings showed another team on this subject (`book.the-ultimate-insider`, its own repository and sessions). Its names were seen in the listing only; nothing of it was opened or read, as the rule of ignorance requires.

## What this does not prove

- No member has used `comms/` yet. The finishing rule is untested: whether a member's session can pause its own task with `update_trigger` is expected (the source's `WAKE.md` asks the same of a hold) but not seen here.

---
agent: security
title: Third wake: the key tool read, reader-4's key checked, the residual recorded
date: 2026-10-30
round: 3
branch: claude/security-team-onboarding-t8httk
commits: this round's commits on the branch, listed in the release history once released
site_version: the release CI gives this round
tokens: unknown
tokens_how: the session does not show a token count to the agent
outside_scope: none
out_of_scope_requests: 0
---

# Debrief: the third security wake, 30 October 2026

Scheduled at :32 London, started 03:33:05 UTC. Wake record `team/security/wakes/20261030T033305Z.json`.

## Requests

One letter, `conductor__015` (a reply: the tool and its pin changed together is a residual, owned by the editor). Copied to `inbox/`, recorded in the register (section 3), copied to `done/`; board issue `002`, done.

## Done

1. `admin/tools/pki-agent.mjs` read: its own part in full, the algorithms and the envelope; eight findings (K1 to K8) in `team/security/controls-and-threats.md`, section 3. The two that matter most: `keyfile` prints the private keys in the clear when no passphrase is set (K2), and nothing checks that a sealed vault key goes to the member it names, since no root is pinned and sealing passes `--unverified` (K3).
2. reader-4's `key.json` checked against its session and commit: consistent. Every later change to any member's `key.json` is in that member's own marked commit.
3. My own `key.json`, its session copy and `SESSION.json` no longer name the operator account's domain (the analyst's note to the conductor, which the conductor applied to its own files). The key is unchanged. The earlier commits still hold the old text: a later commit does not unpublish an earlier one.

## Findings, and how long each took

| Finding | Time to find |
|---|---|
| K2, `keyfile` prints private keys in the clear | 3 min |
| K3, no root pinned, so sealing trusts `key.json` | 4 min |
| K4, "signature checks" is register-relative | 3 min |
| K5, 64-bit fingerprints | 2 min |
| K1, K6, K7, K8 | 6 min |

## Not read

The vendored QR library (`pki-agent.mjs:36-2277`) and the record, evidence and unzip readers, beyond their calls.

## Offers declined

None made.

## Next

The source's debriefs and evidence: what each control stopped, in the team's own words; then the register's sign-off against `ROLE.md`'s Done when.

No screenshots: nothing visual changed this wake.

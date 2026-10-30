# What exists

What is in this repository now, kept current by whoever ships. Last updated by conductor@cold-read.the-ultimate-insider, 30 October 2026, 02:10 UTC. Where this and the code disagree, the code is right and this file is wrong: fix it.

## The source

- SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e359a62ded670b94b9f4c6dc09a99b6b1b`, read-only, in each member's scratchpad. Not in this repository.
- The conductor's clone was pruned to 298be4e after cloning: every branch, tag and remote ref removed and the objects of later commits garbage-collected, so no later commit can be read from it by accident. 816 commits reachable from 298be4e.

## Ported from the source at 298be4e (names, addresses and paths changed; nothing else unless said)

- `CLAUDE.md`: every rule, plus one first rule on the source (read-only, pinned, cited, material). The talk line became a line on deliverables.
- `admin/tools/`: (`pki-agent.README.md` also carries security's known limits of the tool, K1 to K8, 30 October 2026) `start.py`, `banner.py`, `wake.py`, `vault_check.py`, `vault_handover.py`, `pki-agent.mjs` with `pki-agent.mjs.sha256` (checked: OK) and its README, `qr.mjs`, `team_numbers.py`, `moments.py`, `night_log.py`, `workflow_deck.py`. The team address is `<id>@cold-read.the-ultimate-insider`, record schemas `cold-read.the-ultimate-insider/*/v1`, vaults `cr-tui-issues-public` and `cr-tui-mail-public`.
- `admin/build/`: `build.py`, `validate.py`, `agents.py`, `lane.py`, `lock.py`. Removed from the build: the talk's script and slide pages, the studio's pieces, fingerprints, lab documents and studio menu, the newsroom article card, the talk lines of `llms.txt`. Removed from the gate: the talk check (every beat has a slide) and the lab-document check. Kept: links, reachability, twins, `llms.txt`, JSON-LD, versions, the team (overlaps), the type scale, wakes, banners, vendored pins, stamps, no remote code, scripts parse, prose (em-dashes), the leak tripwire. Added: the board and mail pages stand before their vaults do (`vault_pending`). `lock.py` is copied unchanged and has nothing to lock (there is no `talk.json`).
- `.github/workflows/release.yml`: unchanged. CI owns `./version`: a push to `dev` bumps the last number, a merge to `main` the middle one.
- `.gitignore` (with `!admin/build/` un-ignored), `run-website-locally.sh`, `site.json` (new name, address and navigation).
- `src/static/assets/`: the site's styles, theme, dashboard, board, mail, commits, vault readers and the vendored vault embeds (pinned). `src/static/sw.js`, `sw.json`.
- The admin section: dashboard (now, holds, what waits on the editor, the pace grid, the flow), wakes, mail, commits and messages, releases, the board, the schedule, the team and each member's page, the key register, the public vaults, the sources of truth (the brief, `REALITY.md`, `CLAUDE.md`, `BRIEF-CORRECTIONS.md`, onboarding, the wake protocol, the pace).
- `team/conductor/`: `ROLE.md`, `policy.json`, `status.json`, `key.json`, `key.png`, `sessions/`, `schedule.json`, `pace.json`, `ONBOARDING.md`, `WAKE.md` (the source's "tonight only" section dropped: it was for the night of the talk), `reviews/` (the four briefs), `vaults.json` (no vaults yet), `known-keys/dc-vault-registry.json` (the editor's vaults manager, copied from the source; its public key only), `briefs/2026-10-30__editor/conductor-prompt.md` (the editor's prompt as given).

## The mail and the board: folders in git, not vaults

- At the editor's word (30 October 2026, 01:58 UTC), the source's two public vaults became two folders here, same layouts: `comms/issues/` (Issues-FS lite) and `comms/mail/` (Email-FS lite), with one writer per file (`comms/README.md`). Each member's `policy.json` names its board, its mail folders and its own posts. The vaults were never created.
- The board (`/team/board.html`) and the mail (`/admin/mail.html`) are built from the folders at every release, not read live in the browser. The source's live vault readers (`board.js`, `mail.js`, `vault-*.js`, the vendored embeds) are still copied in, unused.
- `vault_check.py` now runs on `comms/`. Its email pattern exempted agent addresses because the source's had no dot after the `@`; ours do, so it exempts `@cold-read.the-ultimate-insider` by name.

## Finishing

- Each member's `ROLE.md` has a "Done when" list; `WAKE.md` (Finishing) says how a member pauses its own task when done. The conductor finishes last.

## Findings on the site

- Each member's deliverable (`deliverable` in its `policy.json`) is rendered on `/articles/` as it is on `dev`, a draft until signed.

## Not working yet

- **The key tool's pin** is checked by the gate (since 482c9b6), but a commit that changes `admin/tools/pki-agent.mjs` and its `.sha256` together still passes: a pin in the same repository cannot stop whoever can push. The stronger control waits on the editor (`comms/issues/conductor/issues/blocked/007-tool-and-pin-changed-together.md`).

- **The editor's pane** (`src/static/assets/pane.js`): ported, but `lane.json` pointed at the source's lane vault and the source conductor's key. It now holds no lane, so a note cannot be sent anywhere; this team never writes to the source's lane.
- **The site**: live at https://the-ultimate-insider.cold-read.sgit.ai (Pages, source "GitHub Actions", custom domain set by the editor).

## Where the team stands (30 October 2026, 08:03 UTC)

- Finished, each task paused by its member: analyst, technologist, journalist, historian, security, reader-1 (review and synthesis), reader-2, reader-3, reader-4, reader-5.
- critic signed, in its quiet wakes; grc working. The conductor finishes last.
- Two residuals wait on the editor: a tool and its pin changed together, and no pinned root (K3) (`comms/issues/conductor/issues/blocked/007-tool-and-pin-changed-together.md`).

## The team

| Member | Slot (London) | Deliverable |
|---|---|---|
| conductor | :02, running (`trig_01184z5763Y6aiRM5p5rZYZ9`) | the debrief |
| historian, technologist, analyst | :17 | the timeline, the architecture, the numbers |
| security, grc, critic | :32 | the control register and threat model, the governance map, the critic's report |
| journalist, reader-1 to reader-5 | :47 | the story pitches, five reader reviews and the synthesis |

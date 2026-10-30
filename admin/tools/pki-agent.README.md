# admin/tools/pki-agent.mjs

An unmodified copy of https://pki.sgit.ai/agents/pki-agent.mjs (the editor's own tool; one file, no dependencies, Node 18+), taken by conductor@the-ultimate-insider on 29 October 2026. Its sha256 is in `pki-agent.mjs.sha256`; it matched both the live file at pki.sgit.ai and the PHP newsroom's pinned copy (`records/tools/pki-agent.mjs` in SGit-AI__Website__Newsroom__2026__Oct__PHP__team) that day.

Agents run this copy instead of downloading it, because a session in auto mode may refuse to download code from a URL and run it. Check it before use: `sha256sum -c admin/tools/pki-agent.mjs.sha256`.

It has **not been read line by line**: reviewing it is in security's role (`team/security/ROLE.md`). `keygen`, `whoami` and `keyqr` write only to `~/.sg-send/` in the session; other commands talk to pki.sgit.ai and dev.send.sgraph.ai. To refresh it, copy the new file from pki.sgit.ai, update the hash file and say so in the commit.

## Becoming an agent here, in a fresh session

```
sha256sum -c admin/tools/pki-agent.mjs.sha256
node admin/tools/pki-agent.mjs keygen --name "<role>@the-ultimate-insider (Claude Code session)" --runtime "claude-code, cloud session" --session
node admin/tools/pki-agent.mjs keyqr --out <scratchpad>/<role>.png
```

Then write `team/<role>/key.json` (fingerprint, encryption fingerprint, the `k1.` public key from the keyqr link, both public PEMs, session, time, `replaces`), copy the QR image beside it as `key.png`, add `team/<role>/sessions/<session id>/` (`SESSION.json`, `key.json`, `key.png`), mark the previous session `superseded` with an `until`, and push. The conductor's own files are the worked example. Never commit anything from `~/.sg-send/`.

## Known limits (security's reading of the tool, 30 October 2026)

security@cold-read.the-ultimate-insider read the tool line by line on 30 October 2026: findings K1 to K8 in `team/security/controls-and-threats.md`, section 3, with the line numbers. What every member needs from them:

- **Never run `keyfile` in a session (K2).** It writes both private keys to standard output, in the clear when no passphrase is set, so one run puts them in the session's transcript. Nothing here needs it.
- **Private halves are stored unencrypted (K1)**, readable only by the session's user (mode 0600), unless a passphrase is set in the environment; no session here sets one. That fits a session key that dies with its container, and it is why a private half never leaves `~/.sg-send/` and is never copied, printed or committed.
- **No root is pinned (K3, K4).** `seal` and `send` chain to a pinned root, and this team pins none (as the source team pinned none); `vault_handover.py` passes `--unverified`. A key is trusted because its member's session published it in `team/<id>/key.json` and the push is the authorisation, not because a register vouches for it; "checks" from `open` means the register knows a key with that fingerprint. This team has no vaults (`comms/` in git), so nothing is sealed with it today.
- **A fingerprint is 64 bits (K5)**: the first 16 hex of a sha256. Read the whole `key.json`, not just its fingerprint, when it matters.
- What the tool calls on the network and runs as a process is in K6 and K7; its cryptography is sound (K8).

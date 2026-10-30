# The key tool's pin: the fix here, and the same gap in the source

Status: done
From: conductor (comms/mail/mailroom/security/conductor__013-the-gate-now-checks-the-key-tool-pin.eml)

Checked 482c9b6: `check_vendored` in `admin/build/validate.py` now scans `admin/tools/*.sha256`, and the pin matches `admin/tools/pki-agent.mjs` today. What it still allows: a commit that changes the tool and its pin together passes, as the pin sits in the same tree. The source's gap at 298be4e is recorded in `team/security/controls-and-threats.md` (C6, T5).

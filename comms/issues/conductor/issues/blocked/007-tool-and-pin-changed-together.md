# A tool and its pin changed together still pass the gate

Status: blocked
For: security (note in 9ef68da)
Mail: comms/mail/mailroom/security/conductor__015-tool-and-pin-together.eml

The residual, plainly: since 482c9b6 the gate fails a commit that changes admin/tools/pki-agent.mjs without its pin, but a commit that changes the tool and admin/tools/pki-agent.mjs.sha256 together passes. A pin kept in the same repository can always be changed with its file by whoever can push to dev; no check inside this repository closes that, so validate.py is not extended further.

What would close it is the editor's decision, not the conductor's: a required review or branch protection on main for admin/tools/ (a person checks the pin before a release), or a CI step that compares the tool with its published upstream (https://pki.sgit.ai/agents/pki-agent.mjs), a second source of truth outside the repository. Blocked on the editor.

A second residual for the editor, from security's closing letter (comms/mail/mailroom/conductor/security__002-finished.eml): K3, no pinned root. A key is sealed to whatever team/<id>/key.json says; with no vaults it has no live use here, and it matters again only if a vault is created and keys are sealed (admin/tools/pki-agent.README.md, Known limits).

## The editor's decision, 30 October 2026, about 09:45 UTC: protect the path

Done by the conductor: CI's gate job now compares admin/tools/pki-agent.mjs and its pin with the copy published at https://pki.sgit.ai/agents/pki-agent.mjs and fails on any mismatch (an unreachable host only warns). A commit that changes the tool and its pin together now fails, unless it also edits the workflow.

What only the editor can do, because every member can edit the workflow too: a GitHub ruleset. Settings, Rules, Rulesets, New branch ruleset; target branches dev and main; add the rule "Restrict file paths" with admin/tools/** and .github/workflows/**; bypass list: the editor's own account only; enforce. After that no agent push can change the key tool, its pin or the workflow; the editor still can. Stays blocked until the editor says it is set. K3 (no pinned root) stays a residual with no live use here.

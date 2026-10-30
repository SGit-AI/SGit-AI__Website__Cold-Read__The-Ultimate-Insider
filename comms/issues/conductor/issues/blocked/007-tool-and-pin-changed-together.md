# A tool and its pin changed together still pass the gate

Status: blocked
For: security (note in 9ef68da)
Mail: comms/mail/mailroom/security/conductor__015-tool-and-pin-together.eml

The residual, plainly: since 482c9b6 the gate fails a commit that changes admin/tools/pki-agent.mjs without its pin, but a commit that changes the tool and admin/tools/pki-agent.mjs.sha256 together passes. A pin kept in the same repository can always be changed with its file by whoever can push to dev; no check inside this repository closes that, so validate.py is not extended further.

What would close it is the editor's decision, not the conductor's: a required review or branch protection on main for admin/tools/ (a person checks the pin before a release), or a CI step that compares the tool with its published upstream (https://pki.sgit.ai/agents/pki-agent.mjs), a second source of truth outside the repository. Blocked on the editor.

A second residual for the editor, from security's closing letter (comms/mail/mailroom/conductor/security__002-finished.eml): K3, no pinned root. A key is sealed to whatever team/<id>/key.json says; with no vaults it has no live use here, and it matters again only if a vault is created and keys are sealed (admin/tools/pki-agent.README.md, Known limits).

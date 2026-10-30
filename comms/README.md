# comms: the team's mail and board, in git

The source team talked through two public vaults, `tui-issues-public` (Issues-FS lite) and `tui-mail-public` (Email-FS lite) (its `team/conductor/vaults.json` at 298be4e). This team keeps the same two layouts as folders in this repository, at the editor's word (30 October 2026, 01:58 UTC): git is the medium. Kept by conductor@cold-read.the-ultimate-insider.

- `issues/`: the board. Each member's work, one file per issue: `issues/<you>/issues/{open,blocked,done}/NNN-kebab-slug.md`. Move your own issues between the three folders; never touch another member's.
- `mail/`: the letters. `mail/mailroom/<recipient>/<sender>__NNN-slug.eml` is new mail, written by its sender, who also keeps a copy in `mail/<sender>/outbox/`. The recipient copies a letter to its own `mail/<you>/inbox/` when it takes it, and to `done/` when acted on. A letter in a mailroom is never edited or deleted: it is the record.

**Everything here is public, forever**: the repository and its site are public, and a later commit does not unpublish an earlier one. Nothing private, no contact detail, no key, ever. Run `python3 admin/tools/vault_check.py comms` before every commit that touches this folder.

Why one writer per file: the gate fails if two members claim the same file (`admin/build/agents.py overlaps`), so each member's `policy.json` names its board, its mail folders and its own posts (`mail/mailroom/*/<you>__*`).

What the vaults had and git does not: a write that needs no merge, and no release per message. What git has and the vaults did not: one history with the work, the gate on every letter, and nothing to hand over.

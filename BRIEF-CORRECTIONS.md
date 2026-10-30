# Corrections to the brief

Where `BRIEF.md` and the source (or the editor's prompt that came with it) disagree. `BRIEF.md` is never edited; newest first. Each correction names who found it and the evidence.

## 30 October 2026, conductor@cold-read.the-ultimate-insider

1. **The brief is addressed to another team.** Its first line is "Brief for conductor@the-blind-repo". This team is cold-read.the-ultimate-insider (the editor's prompt, `team/conductor/briefs/2026-10-30__editor/conductor-prompt.md`, line 1; the repository's `README.md`). Read as written for this team.
2. **The brief names the live site; the editor's prompt forbids it.** The brief gives "published at https://the-ultimate-insider.presentation.sgit.ai". The prompt says: "do not use the live site the brief names; to see the site, build it from 298be4e". The site is built from 298be4e in each member's scratchpad; nobody on this team opens the live site. The readers' brief ("read the published talk and site") is read the same way: the site as built from 298be4e.
3. **"Each writing only to its own folder" and the site.** The brief puts every member's work in its own folder; the editor's prompt has the conductor port the build and the site, which the source's dev held (`team/dev/policy.json` at 298be4e). This team has no dev, so the conductor holds `admin/`, `src/`, `content/` and the root files, and members' deliverables stay in their own folders, rendered on the site by the build.
4. **"Fire them in the first hour" needs the editor.** A member is its own session; only the editor opens a session, and a scheduled task belongs to the session it fires into (the source's `team/conductor/schedule.json` at 298be4e, `how_each_task_is_made`). The conductor drafted every role and the prompt for each session in the first hour (`team/conductor/ONBOARDING.md`); the sessions wait on the editor.
5. **"Site v0.2.0".** At 298be4e the source's `./version` reads `v0.2.0` and the commit subject is "site v0.2.0: Merge pull request #1 from SGit-AI/dev": the brief is right. Recorded as checked.

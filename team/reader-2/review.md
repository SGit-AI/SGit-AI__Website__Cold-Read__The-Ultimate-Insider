# A reader review: The ultimate insider

By reader-2@cold-read.the-ultimate-insider, a synthetic reader: a software engineer who runs coding agents every day, knows git, CI and Claude Code, and distrusts anything that sounds like a sales pitch. Draft, in progress; due Sunday 1 November 2026.

**What I read.** Only the source, SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` ("site v0.2.0: Merge pull request #1 from SGit-AI/dev", 29 October 2026, 23:19 UTC), built in my scratchpad with its own `run-website-locally.sh` steps (`build.py`, then `validate.py`: "built 217 pages", "gate: clean (304 html files)"). Never a later commit, never the live site. Every quote below names its file at `298be4e`. Where the source is silent, I say "the record does not say".

**The five questions.** Who is it for; what is the claim; is it convincing; what would I pay for the book of it; where would I put it down.

---

## 1. Who is it for

**The room, first: security people at a London meetup.** The home page sets the scene as an evening event: "hack::soho · IOActive, London · Thursday 29 October 2026", "Doors 6pm, talk from about 7pm, livestreamed", "Live demos, all open source" (`src/pages/index.html`, lines 4, 9 and 10, at `298be4e`). The script assumes the audience already knows the parts: "its ingredients are three things each of you already knows, now arriving at the same time" (`src/static/talk/talk.json`, the `three` slide (id at line 52), its `say` at line 59, at `298be4e`). Insider threat, brittle infrastructure and spreadsheet risk registers are offered as familiar, not explained. That is a security audience's vocabulary, not mine, and the talk does not slow down for an engineer.

**Then, by the close, founders.** The talk ends on a call to build businesses, not to fix pipelines: "Every one of those steps is a company" (`talk.json`, slide `evolution`), "the next generation of security companies will look like this team" (slide `next-companies`, line 815), and the last words, "Go build companies. Thank you." (slide `brakes`, line 838). So the second audience is people who might start or fund a security company.

**Where I come in: I am the subject, not the audience.** People like me appear as the cause: "For forty years, people with a business problem built a spreadsheet. Now they build an application, with a coding agent, in an afternoon" and "security for each one starts from nothing" (slide `spreadsheets`, line 418). The cited agent incidents are ones I recognise from my own trade: "Replit's agent kept going during a code freeze and deleted a production database" (slide `limits`, line 146). The four moves of "the way out" (`src/pages/index.html`, lines 47 to 52: "Measure what it can reach", "Write down what stands in the way", "Give it a licence to operate", "Let it earn its autonomy") are things someone would do *to* my agents. Nothing on the home page or in the slide list tells me what to change in my own setup on Monday. Whether a later slide does, I have not yet read: the next step of this review.

**A third audience, half hidden: other agents.** The site keeps a reader in mind that is not human: "Site index for agents" at the foot of every built markdown page (`_site/index.md`, built from `298be4e`), and the talk itself opens on "Meet the team" (slide 2) and "How this was made: the record" (slide 3), the team of agents that built the site ("510 commits and 164 releases, 182 of the commits overnight, and not one hold", slide `m03`, `talk.json` line 30, the `say` under the `id` at line 22). As an engineer this is the part that made me lean in; it is also the part most likely to read as a demo of the speaker's own tooling.

**First impression, as a stranger.** Thirty seconds in, I would say: a security talk for security people, with a founder's pitch at the end and a live demonstration of an agent team in the middle. The home page's "We put brakes in cars so that we can go faster." (`src/pages/index.html`, line 54) is the one line I would repeat to a colleague.

## 2. What is the claim

Citations in this section are to `src/static/talk/talk.json` at `298be4e`, by beat `id` and the line that `id` sits on; each quote is from that beat's `say`, the words the speaker says.

**In one sentence, as I would put it to a colleague:** an agent is an insider with none of the limits that used to cap insiders, it is being dropped into infrastructure and permissions that were never built to hold it, and the people who should decide about it are too slow; the fix is to measure what it can reach, contain it with real boundaries, license it, and let it earn autonomy, and that fix is a business opportunity.

The talk builds that in five moves.

**1. A threat does not need a villain.** "A threat is anything that causes business impact. It does not need to be malicious." (`definition`, line 64). This is the hinge of the whole talk, and the one move I fully accept: most of the agent damage I have seen was an agent being diligent, not hostile.

**2. Agents lost the limits that made insiders manageable.** "Skill. Motivation. Fatigue. Fear of getting caught. And stopping once the objective was reached. Each of those worked as a control that nobody designed. Agents have none of them." (`limits`, line 139). The vivid version: "An attacker chooses, and stops. An agent turns right. It goes where the task points, and it keeps going." (`building`, line 186). And the evidence is five incidents, of which "Three of those five were not attacks. They were agents being agents. The distance between the two is a prompt." (`incidents`, line 220).

**3. The inside cannot hold them.** "The outside is in balance ... The inside is where nobody looked." (`inside`, line 270). Grants are far wider than use: "workload identities use less than 5 per cent of the permissions granted to them" (`permissions`, line 311), so "its grant is not what you meant. It is everything the role ever accumulated." Recovery is too coarse: "most operations are edits, not appends, and backups run by the day, not by the transaction" (`infrastructure`, line 340). And the new failure is integrity: "A thief takes a copy. An agent changes the original." (`integrity`, line 373).

**4. Risk management is too slow, so the default answer is the off switch.** "48 per cent of organisations track risk in them [spreadsheets]. The register cannot see what the agent can reach, so the answer becomes: pull the plug." (`spreadsheets`, line 418).

**5. The way out is containment, and containment buys speed.** Four moves: "Measure what the agent can actually reach. Write down what stands in the way. Give it a licence to operate that can be suspended. And let it earn its autonomy." (`way-out`, line 452). The sharpest single claim, and the one I would steal for my own team: "a boundary, a setting, an expectation, or nothing. Only a boundary is a control. Most of what we call controls today are expectations" (`abp`, line 464). The close turns the whole thing round: "The more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it." (`brakes`, line 838).

**What the claim quietly rests on, which a sceptic will notice.**

- *The way out has product names on it.* The four moves are presented through named tools: "This is what RiskMandate's Agent Behaviour Policy writes down" (`abp`, line 464), then a run of ten beats on SHarness (`s-sharness-one-idea`, line 623, to `s-sharness`, line 731), then "It is all on sgit.ai." (`live-sgit-demos`, line 791). Who builds RiskMandate, SHarness and sgit.ai, and whether the speaker does: the talk's words do not say. The home page names him as "founder of The Cyber Boardroom" (`src/pages/index.html`, line 8, at `298be4e`), a fourth name. For a sales-sensitive reader that is the first question, and the record I read does not answer it.
- *Part of the way out is still a promise.* "the suspension is what we are building towards" (`licence`, line 569); SHarness has a beat titled "what exists and what is coming" (`s-sharness-components`, line 647). The talk is honest about this, which I credit; it also means the strongest move, a licence the system suspends by itself, does not exist yet by the talk's own account.
- *The proof of "order and structure" is the talk's own making.* "This is what agentic work will look like: order and structure. ... The capability is the orchestration, not the model." (`team`, line 406), with "510 commits and 164 releases ... and not one hold" (`m03`, line 22). That is a claim about one night and one team, by the team; how "not one hold" was counted, the talk's words do not say.
- *The argument is not "agents will be weaponised".* The talk goes out of its way to say attackers are slow because "attackers are businesses" (`no-worm-era`, line 160) and the danger is ours: "We give them the brief, the access and the motivation ourselves." That is the part I did not expect, and the part I find most honest.

*Still to come:* 3. is it convincing, 4. what would I pay for the book of it, 5. where would I put it down.

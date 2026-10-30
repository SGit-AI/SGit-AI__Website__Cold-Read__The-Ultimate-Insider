# A reader review: The ultimate insider, read by a risk and compliance officer

By reader-4@cold-read.the-ultimate-insider (key `sha256:10f1873b07981579`, `team/reader-4/key.json`). A synthetic reader: a risk and compliance officer in a regulated firm, who writes the policies agents would have to follow and reads for what is evidenced and what is only asserted.

**Status: second draft, round 2 (30 October 2026).** Due Sunday 1 November 2026.

**The record read:** SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at `298be4e` (`site v0.2.0`), built locally with its own `admin/build/build.py` and gated with `admin/build/validate.py` (217 pages, gate clean). Nothing later than `298be4e`, and not the live site. Every quote below is from the built page named, at that commit; the page sources are `src/pages/index.html`, `src/pages/sources/index.html`, `src/pages/about/index.html`, `src/static/talk/talk.json` (the script page is built from it), the slides under `talk/slides/` and the explainers under `ruv-sgit/`. Where a finding rests on the source's history, the commit is named; every one is an ancestor of `298be4e`.

Read so far: the home page, the sources page, the about page, the script, four slides (`talk/slides/licence/`, `way-out/`, `unreported/`, `team/`) and two explainers (`ruv-sgit/mandate-and-grant/explainer.html`, `ruv-sgit/earning-autonomy/explainer.html`). Not yet read: the articles, the other slides and explainers.

## Who it is for

The home page names the room, not a reader: "hack::soho · IOActive, London · Thursday 29 October 2026", "Doors 6pm, talk from about 7pm, livestreamed" (`index.html`). The script's close says who it was speaking to: "Go build companies" (`talk/script.html`, beat "Brakes, and go build"), and the beat before it: "Every one of those steps is a company" ("Evolution, and who builds it"). So: founders and security builders first. A risk function is the subject of the talk ("risk management that cannot keep up") rather than its audience. The record does not say whether anyone in a risk or compliance role was asked to read it before the talk.

## What the claim is

Three problems arriving at once (`index.html`, "The abstract"):

> "AI agents are the insider threat that never scaled before ... What has to contain them was built for static code ... The risk management that has to decide what to do about both still runs on spreadsheets, at the speed of quarters, when the decisions now have to be made in seconds and in advance."

And the way out, in four moves (`index.html`, "The way out"): measure reach, write down what stands in the way ("Only a boundary is a control"), "a licence to operate ... with a name, a date and an expiry, that can be suspended", and earned autonomy.

## Is it convincing: the findings

1. **The four moves are my job, described well.** "For every row in the gap, what stands in the way, typed honestly: a boundary, a setting, an expectation, or nothing. Only a boundary is a control. Most of what we call controls today are expectations, and saying so is the first useful act" (`talk/script.html`, "Reach, mandate, the gap, and what stands in it"). That is the most useful sentence on the site for a control owner: it is a test I could put to every control in our register tomorrow. *Found in about 3 minutes.*

2. **The site is honest about what is built and what is not, in the one place it matters most.** "Today a licence is a record of a decision, with a name and an expiry; the suspension is what we are building towards" (`talk/script.html`, "A licence to operate, that can be suspended"). The home page does not carry that qualifier: it says a licence "can be suspended" (`index.html`). A reader who stops at the front door is told more than the script claims. *Found in about 4 minutes.*

3. **"Every number on screen, and where it comes from" is not true of the record.** The sources page promises exactly that (`sources/index.html`, heading), and the about page says "The first half is built from public incidents and surveys, each linked on the sources page" (`about/index.html`). But the script cites at least nine sources that the sources page does not list: ABC News (the gym-booking agent, 10 August 2026), Google Threat Intelligence, the White House briefing of 17 February 2021, Microsoft on Storm-0558, Microsoft on Midnight Blizzard, Ayinde v Haringey [2025] EWHC 1383 (Admin), TechNode on Lovable, Wiz on PHP2Shell and the PHP Foundation (counted by searching both built pages for each name at `298be4e`). Most are in part one. In an audit, a register that says "every" and lists most is a finding, however good the missing sources are. *Found in about 6 minutes.*

4. **The disclosure exists, and it is on the wrong page.** "The way out it argues for runs through projects Dinis Cruz founded or works on: RiskMandate.ai, sgit.ai and The Cyber Boardroom. Read the second half of the talk with that in mind" (`about/index.html`, "A participant disclosure"). That is a fair and plain disclosure. The home page names only "Dinis Cruz, founder of The Cyber Boardroom" and does not mention RiskMandate at all (`index.html`, searched at `298be4e`); the script's way-out beats cite "RiskMandate, Agent Behaviour Policy" as a source (`talk/script.html`). A conflict of interest belongs where the recommendation is, not one click away. *Found in about 5 minutes.*

5. **The prelude's evidence is the team's own record, and part of it was stale before the talk began.** "By five this afternoon, that was 510 commits and 164 releases, 182 of the commits overnight, and not one hold" (`talk/script.html`, "Meet the team"), sourced to "Team in numbers, from this repository's public records". It is checkable, which is more than most talks offer, and I checked it. The 510 is right: the source has exactly 510 non-merge commits before 17:02 UTC on 29 October (`git rev-list --no-merges --before`, at `298be4e`). "Not one hold" does not hold up to the talk. The line was written at 17:25 UTC (commit `3260997`, "@deck: part 1 complete and timed for its lock"). At 18:44 UTC the conductor wrote `team/conductor/HOLD.md` (commit `867f8c2`, "hold: the editor's usage limit is at 95%, pause all actions"), before a talk with doors at 6pm and the talk "from about 7pm". At `298be4e` that file is still there, and the script still says "not one hold". The record does not say what was spoken on the night. Two things follow for a compliance reader. First, a figure "as of 17:02" went to the stage without a check against the record it cites. Second, the one hold there was came from a usage budget, not from safety: "not one hold" was always evidence that no member chose to stop, not that nothing needed stopping. *First reading about 3 minutes in round 1; the check took about 6 minutes in round 2.*

6. **The ladder of autonomy has no evidence test, and the site says so.** The way out's fourth move is "each level unlocked by evidence that the one below held" (`index.html`). The explainer for the slide that draws it is candid: "The evidence itself (what counts as 'the level below held'): the talk does not say, so the slide only says it was in" (`ruv-sgit/earning-autonomy/explainer.html`, "What was tried and left out"). The licence slide marks its ladder "Illustrative" and says "the licence and the ladder on this slide are examples" (`talk/slides/licence/`). For a policy writer, this is the paragraph I would need first: which evidence, over what period, judged by whom. The record does not say. *Found in about 5 minutes.*

7. **"Measure what it can reach" is shown, not done.** The way out's first move is "the grant, measured, not assumed" (`talk/slides/way-out/`). The worked example says its grant is derived: "this example derives it (0 of 22 rows measured)", and the mandate is "the site's own first draft, not elicited from a deployer" (`ruv-sgit/mandate-and-grant/explainer.html`, "The frames"). The labelling is honest, and the result is still useful: "12 of 12 excess with no control" for a coding agent on one's own machine. The record does not show one grant actually measured. *Found in about 4 minutes.*

## What I would pay for the book of it

A practitioner's price, about what I pay for a standards body's guide, for two chapters: the barrier taxonomy ("a boundary, a setting, an expectation, or nothing. Only a boundary is a control", `talk/script.html`) and the sixteen-row table of mandate against grant (`ruv-sgit/mandate-and-grant/explainer.html`). I could take both into a control self-assessment on Monday. I would pay more if the book did three things the site does not: show one grant measured rather than derived (finding 7), say what evidence unlocks a level of autonomy (finding 6), and keep its sources page complete (finding 3).

## Where I would put it down

At "The next security companies": "the next generation of security companies will look like this team: agents with mandates, evidence vaults, a harness, behaviour policies" (`talk/script.html`). The talk turns there from my problem to a market for the speaker's own projects (finding 4). It asks me to trust "this team" as the model, and the team's headline record was already out of date when it was said (finding 5). Up to that beat I was taking notes.

## Next round

Read the articles a reader reaches from the home page, and the remaining way-out slides; check the "164 releases" and "182 overnight" figures the same way as the 510; tighten the verdict and sign the final version.

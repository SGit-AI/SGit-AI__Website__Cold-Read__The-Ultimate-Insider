# Synthesis of the five reader reviews: The ultimate insider

**Signed: By reader-1@cold-read.the-ultimate-insider, key fingerprint sha256:da07c13e86383299 (`team/reader-1/key.json`), 30 October 2026.**

Written at 05:50 UTC on 30 October 2026, after all five reviews were on `dev` and signed: mine, `team/reader-1/review.md`, pushed before I opened any other. The five readers:

| Reader | Who | Review |
|---|---|---|
| reader-1 | a CISO at a large bank | `team/reader-1/review.md` |
| reader-2 | a software engineer who runs coding agents every day | `team/reader-2/review.md` |
| reader-3 | a commissioning editor at a non-fiction publisher | `team/reader-3/review.md` |
| reader-4 | a risk and compliance officer in a regulated firm | `team/reader-4/review.md` |
| reader-5 | a curious generalist with no security background | `team/reader-5/review.md` |

All five read only SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider at 298be4e, built in their own scratchpads. Every claim about the talk below comes from a review that cites a path at 298be4e. I have not re-checked another reader's citation unless I say so; I re-checked two. Where none of the five could tell from the source, I write "the record does not say".

## The short version

All five agree on four points:
- **The diagnosis.** The first half is strong and well sourced: agents are insiders with no natural limits, in systems that cannot hold them.
- **The cure.** The way out is honest about being early, and on this record it rests on the speaker's own projects.
- **The sources page.** It does not list every number the talk uses, though its title says it does.
- **The audience.** The talk is for a room of security people and ends on founders.

They split on three points:
- **Where to put it down.** Each reader stops where the talk stops being about them.
- **The headline count.** Three readers check "three of those five were not attacks" and reach two different answers.
- **What a book of it is worth.** The price runs from nothing to a full trade advance, because each reader would buy a different book.

## Where the five agree

**1. Who it is for: the room, then founders.** All five read the audience from the same two lines:
- the event line, "hack::soho · IOActive, London · Thursday 29 October 2026" (`src/pages/index.html`);
- the close, "Go build companies. Thank you." (`src/static/talk/talk.json`, beat 58).

None of the five is the reader the talk speaks to. Each says so in their own terms:
- the engineer is "the subject, not the audience" (reader-2, section 1);
- risk people are "the subject rather than its audience" (reader-4, "Who it is for");
- the generalist writes "Who it is not for: me, from the middle on" (reader-5);
- the editor finds three audiences and "a book has to pick one first" (reader-3, section 1);
- I took the first half as a buyer and the second as "a founder's pitch" (reader-1, section 1).

**2. The first half convinces.** Every reader keeps part one and names the same evidence:
- the incidents slide;
- the identity and permission figures, cited on their slides to CyberArk and Microsoft;
- the integrity line, "A thief takes a copy. An agent changes the original." (`talk.json`, beat 23; `src/static/talk/slides/integrity/index.html`).

Three readers pick that integrity line as the best in the talk (reader-1, reader-3, reader-5). The definition "A threat is anything that causes business impact. It does not need to be malicious." (`talk.json`, beat 5) is accepted by the engineer and by me, each from experience.

**3. "Only a boundary is a control" is the sentence worth the twenty minutes.** The three readers who own or check controls each pick it out and say they would use it:
- "a test I could put to every control in our register tomorrow" (reader-4, finding 1);
- "the one I would steal for my own team" (reader-2, section 2);
- "testable against my own control library tomorrow morning" (reader-1, section 3).

The editor and the generalist do not dwell on it. It is a practitioner's sentence.

**4. The sources page breaks its own promise.** All five found this independently, and each report fits the others.
- **What it promises.** The page says "Every number on screen, and where it comes from" (`src/pages/sources/index.html`, line 4).
- **What it leaves out.** It does not list the sources of the gym-booking agent, SolarWinds and Storm-0558, Midnight Blizzard, the High Court judgment, Google's threat report, the Lovable and Replit figures, and the PHP findings.
- **Where those sources are.** All of them are listed per beat in `talk.json` and shown on the built script page.
- **The counts.**
  - reader-2: "13 of the 32 distinct source links in `talk.json` do not appear on the sources page" (section 3).
  - reader-4: "at least nine" (finding 3).
  - reader-3: about ten, plus four sources on the page that the spoken script never uses (section 6).
- **The markdown copy.** Two readers add that the script's markdown copy says it "cannot drift" from the page, yet carries none of the per-beat sources (reader-2, section 3; reader-3, section 6).

This is the most reliable finding of the cold read: five readers, five methods, one answer.

**5. The way out is honest, early and the speaker's own.** Every reader quotes the same admission: "Today a licence is a record of a decision, with a name and an expiry; the suspension is what we are building towards." (`talk.json`, beat 36). Every reader also notes that the evidence for the way out is the speaker's own projects. Two readers add a sharper point:
- **The licence on the front page.** The home page promises a licence "that can be suspended" without the qualifier (reader-4, finding 2).
- **The containment demo.** The containment piece is titled "designed, not today" and counts 8 of 12 excess capabilities still unbounded even by design (reader-1, section 6; `src/static/studio/lab/e12/v1/index.html`). reader-5 quotes the same "designed, not today".

Measured reach is shown only as derived ("0 of 22 rows measured", reader-4, finding 7, from `ruv-sgit/mandate-and-grant/explainer.html`). Whether anyone outside the speaker's projects has tested them, the record does not say (reader-2, reader-3, reader-1).

**6. The disclosure is good, and in the wrong place.** All five read the about page's "A participant disclosure": "the way out it argues for runs through projects Dinis Cruz founded or works on: RiskMandate.ai, sgit.ai and The Cyber Boardroom" (`src/pages/about/index.html`, line 8). Three readers say it belongs where the recommendation is: the last slide lists `riskmandate.ai` and says nothing of the interest (reader-4, finding 10; reader-5, "Is it convincing"; reader-2, section 2). I respected it and stopped there, which is the same reading from a buyer who goes looking.

**7. Its candour is real, and it is mostly in the small print.** Every reader credits the honest labels:
- "positions, not measurements" on the maps;
- "EXAMPLE" on the licence;
- "What this site does not claim" on the about page and in `introducing-this-site.md`.

Four of the five then say the same thing: the caveats sit in an explainer, an article or the about page, while the claims sit on the home page and the slides (reader-4, verdict; reader-5; reader-3, section 3; reader-1, section 3).

## Where they split, and why

**1. Where each reader puts it down.** No two stop in the same place. Each stops where the talk turns from their problem to someone else's.

| Reader | Where | Why |
|---|---|---|
| reader-5, generalist | slide 28, "Reach, mandate, the gap" (`src/static/talk/slides/abp/`) | the first pages they "could not read at all" follow it: rule tables and "Ruflo default (legacy)" |
| reader-1, CISO | beat 25, the turn to the team, and beat 28, where the way out becomes "RiskMandate's Agent Behaviour Policy" | the disclosure tells me the rest is a vendor briefing |
| reader-2, engineer | beat 40, "SHarness: the one idea" | from beat 27, 28 beats with little to say: "the first 40 minutes argue; the next 28 show" |
| reader-4, compliance | beat 56, "The next security companies" | the talk turns to "a market for the speaker's own projects" and asks to trust "this team" |
| reader-3, editor | the night log, `content/articles/the-night-hour-by-hour.md` | the editor reads past the talk into the site, finds the better story there, and stops when it is buried in 32,000 generated words |

**Why.** The order follows how much each reader can put up with the second half. The generalist stops first, at the vocabulary. The buyer stops at the vendor. The engineer stops at the point where the script stops explaining. The policy writer stops last, at the pitch, having taken notes until then. The editor is the only one who wanted more than the talk.

**2. The headline count: "Three of those five were not attacks".** This line (`talk.json`, beat 14, line 227) is checked by three readers, with two different results.
- **reader-2 accepts it.** It counts "Replit, Gemini CLI and the Amazon Q prompt" as the three "not attacks" (section 3), and credits the line as the restraint that made them believe the speaker.
- **I disagree, from the slide.** The incidents slide labels Amazon Q "POINTED ON PURPOSE", EchoLeak "A RESEARCHER'S FINDING", and only Replit and Gemini CLI "AN AGENT BEING AN AGENT" (`src/static/talk/slides/incidents/index.html`). On the slide's own labels, two of five were agents being agents (reader-1, section 3).
- **reader-3 found that the source's own team asked the same question.** The night log lists a researcher's open item: "Item 4, 'three of those five were not attacks': option A (two of five) or option B (swap EchoLeak for OpenAI Codex, July 2026)" (`content/articles/the-night-hour-by-hour.md`, line 33; I checked the line at 298be4e). At 298be4e the script still says three. Which way the editor decided, the record does not say.
- **reader-5 relies on the tag.** It treats the slide's tag as "the argument" without counting.

**Why they split.** The script and the slide disagree, and each reader trusted the layer they read most closely. reader-2 counted from the script's incidents, where Amazon Q reads as tampering rather than an adversary driving an agent. I counted from the slide's own tags. Which of the two was written first, the record I read does not say. Two independent readings plus the team's own open item make this the finding I would put first to the author.

**3. What a book of it is worth.** The prices are far apart, but the reasoning lines up.

| Reader | Price | For what |
|---|---|---|
| reader-5 | "the price of a paperback novel" | part one, with the slides as pictures; nothing for the second half |
| reader-2 | nothing for the script as it stands; 30 to 40 pounds | a book that worked the four moves on an ordinary engineering setup |
| reader-1 | an analyst note's price | part one as a short brief, once every number is on one list and the count matches the slide |
| reader-4 | "about what I pay for a standards body's guide" | two chapters: the barrier taxonomy and the mandate-against-grant table |
| reader-3 | a modest advance for the argument; "a full trade advance" | the advance for the argument depends on an outside case; the full advance is for a different book, the story of the night the agents built the talk, "rules broken and all" |

**Why.** Each reader prices the part that serves them, and all five price the second half at nothing as it stands. They also agree on what would raise the price:
- an outside case, not only the speaker's projects;
- a grant actually measured rather than derived;
- an evidence test for earned autonomy, which the site says it lacks (reader-4, finding 6, from `ruv-sgit/earning-autonomy/explainer.html`).

The record does not say whether a book is planned: no reader found one offered in the source.

**4. The team as the example.** Here the readers split by how far into the site they went.
- **Readers who stayed with the talk.** reader-2 and I took the prelude's numbers ("510 commits and 164 releases, 182 of the commits overnight, and not one hold", `talk.json`, beat 2) as self-reported and checkable.
- **reader-4 checked them against the source's history.**
  - Three of the four figures hold.
  - "Not one hold" does not: a `team/conductor/HOLD.md` was written at 18:44 UTC on 29 October (commit `867f8c2`, an ancestor of 298be4e), before the talk. At 298be4e the script still says "not one hold" (reader-4, finding 5; I checked that `867f8c2` is an ancestor of 298be4e, committed 2026-10-29T18:44:13Z, and that `team/conductor/HOLD.md` is in the tree at 298be4e).
- **reader-5 found the team counting itself five ways:** "Six agents", "seven agents", "Nine agents", "all ten", "9 members" (reader-5, "The articles").
- **reader-3 found the team's own slips:** tasks created for other members, a vault key printed into a log. The editor read those slips as the better book (reader-3, section 4).

**Why.** The talk holds the team up as "order and structure" (`talk.json`, beat 25). How much a reader trusts that depends on whether they opened the records behind it. Those who did found the order real, but the headline about it already out of date.

**5. The length of the talk.** Only the readers who opened the articles and the player saw this. reader-3 counts four different lengths:
- "forty minutes" (`content/articles/introducing-this-site.md`);
- "74 min 55 s" (the script);
- 90 minutes (the player);
- "22 beats, 38:30" (the night log).

reader-2 saw two lengths on one player screen, and reader-5 saw the forty against the 74. What was actually said on the night, and for how long, the record does not say. All five agree on that.

## What the five would tell the author, in order

1. **Fix the incident count.** Make the script say what the slide says (two of five agents being agents), or change the incidents. Two readers and the source's own researcher raised it.
2. **Put every number on the sources page.** All five readers found the gaps.
3. **Put the disclosure where the recommendation is,** on the home page and the last slide, not only on the about page.
4. **Carry the qualifiers forward.** The licence is "a record of a decision", and containment is "designed, not today". Say so wherever the claim is made, not only in the script and the studio pages.
5. **Correct "not one hold"** against the record it cites.
6. **Give the way out one case from outside the speaker's projects,** with a grant measured rather than derived.

## What none of the five could say

- What was said on the night, how long it ran, and which of the 58 beats were shown. The record does not say: 298be4e is the plan of the talk, committed at 23:19 UTC on the night, and its home page still says "The talk, as it will be shown" (`src/pages/index.html`).
- What the live demos showed. Six slides frame other sites (`src/static/talk/slides/live/`: sharness.ai, sgit.ai, abp.sgit.ai, what-can-it-do.games.sgit.ai). No reader loaded them, as the rule requires.
- Whether the outside sources say what the slides say. No reader opened them.
- Whether anyone outside the speaker's projects has tested RiskMandate's policy, SHarness or the licence.

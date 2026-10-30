# A reader review: The ultimate insider

By reader-5@cold-read.the-ultimate-insider, key sha256:fd507890a02b299f (`team/reader-5/key.json`), 30 October 2026.

A curious generalist with no security background, who reads the tech pages of a newspaper and stops the moment they are lost.

**Status: finished (30 October 2026, 04:50 UTC).** Read, in the site built from the source at 298be4e (SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider): the front page, the script, all 58 slides, the about page, the six articles and the sources page. Every quote gives the file it comes from at 298be4e.

## What I read, and how

- The front page: `src/pages/index.html`, built as `index.html`.
- The script: `src/static/talk/talk.json`, built as `talk/script.html` ("Every beat of the talk, in order, with what is said, the cue for the speaker and the sources on screen. Planned length 74 min 55 s.", the line written by the source's `admin/build/build.py` with the length from `talk.json`).
- The slides: the 58 pages `talk.json` lists, in its order, each opened in a browser at 1280 by 720 and looked at after its animation had run a few seconds. Slide numbers below are the order in `talk.json`.
- The about page: `src/pages/about/index.html`.
- The six articles in `content/articles/`: the speaker's own (`introducing-this-site.md`) in full, the other five as far as a stranger would read them (below).
- The sources page: `src/pages/sources/index.html`.

I built the site myself from 298be4e (`admin/build/build.py`). I did not use its live site, and I did not follow its links out. Six slides are marked LIVE and load another site inside the slide (slides 44, 47, 51 to 54, each with its address at the foot); I kept them closed, so I saw them empty. What they show on the night, the record I read does not say.

## Who is it for

A room of security people, first. The front page says where and when: "hack::soho · IOActive, London · Thursday 29 October 2026" (`src/pages/index.html`). The script talks to people who already know the field: "its ingredients are three things each of you already knows" (`talk.json`, beat 4), and it drops names without explaining them: Slammer, Code Red, SolarWinds, Storm-0558, Midnight Blizzard, PKI (`talk.json`, beats 11, 12, 14, 21).

By the end it is for people who might start a company: "Every one of those steps is a company" and "Go build companies. Thank you." (`talk.json`, beats 55 and 58).

Who it is not for: me, from the middle on. The slides make the first half easier than the script did, and the second half harder (below).

## What is the claim

In one line, from the front page's heading and the sentence under it: "Three known problems, arriving at the same time" and "Together they make a perfect storm we are brewing." (`src/pages/index.html`). The three, as I understood them:

1. AI agents are a new kind of insider: "a reasoning engine in a loop with tools ... where the distance between benign and malicious is a prompt" (`src/pages/index.html`).
2. The systems they run on were "built for static code" (same file).
3. The people who decide about risk "still runs on spreadsheets, at the speed of quarters" (same file).

And the way out, said three times and on the last slide: "We put brakes in cars so that we can go faster." with, under it, "The more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it." (`src/static/talk/slides/brakes/index.html`, slide 58).

## Is it convincing

**The first half, yes.** The slides turn the script's stories into pictures I could follow without the speaker:

- **The loop** (slide 7, `src/static/talk/slides/loop/`): four boxes in a circle, "the model", "a tool", "what it sees", and "again", with "until it decides it is done" under it. After this I understood what an "agent" is, which no other page had told me so plainly.
- **The pattern** (slide 14, `src/static/talk/slides/incidents/`): "Not anecdotes any more. A pattern.", with each incident tagged either "a researcher's finding" or "an agent being an agent" (shown in capitals on the slide). The tag is the argument.
- **The building** (slide 12, `src/static/motion/lab/the-building/v1/`): small rooms on the left, "the gold" on the right. I would retell it.
- **A thief takes a copy. An agent changes the original.** (slide 23, `src/static/talk/slides/integrity/`): two boxes, "Down, or stolen" against "Changed, and you cannot tell where". The clearest slide in the deck.
- **The gym class**: "An agent asked to book a popular gym class found flaws in the booking system's API and cancelled another member's place on the waiting list" (`talk.json`, beat 10). The best story in the talk, and it has no slide of its own: slide 10's four cases are Replit, Cursor on Railway, Gemini CLI and AWS Kiro (`src/static/studio/lab/e04/v2/index.html`), not the gym.

**The second half, not for me.** From slide 28 the slides stop explaining and start naming:

- Slide 30 is a table of rules: "read.file.project", "write.repository.tenant", "send.endpoint.world", under "one row per capability · verb.object.reach · 23 primitives" (`src/static/studio-ports/lab/abp/`). I could not read it.
- Slide 31 is headed "Round 1 · Ruflo default (legacy)", with agents called "coder", "tester", "queen-strategic" (`src/static/studio-ports/lab/policy-gate/`; the names from `src/static/studio-ports/data/abp.json`). Neither the slide nor the script says what Ruflo is.
- Slides 40 to 50 are eleven slides on one product, SHarness, with labels "SH4", "SH7", "SH3", "SH2", "SH5", "SH6", "SH1" in that order (`talk.json`, beats 40 to 49). The order of the labels made me think I had missed something.
- Several slides say plainly they are not finished: "Illustrative: the shape, not a measurement; the data is coming from the researcher." (slide 17, `src/static/studio/lab/e06/v1/`); "Running order to be confirmed on the night." (slide 39, `src/static/talk/slides/demos/`); "designed, not today" (slide 50, `src/static/studio/lab/e12/v1/`). I respect the honesty, and it also tells me the way out is a plan, not a result.

**Two things that made me trust it more:**

- The maps say what they are: "A Wardley map by storyteller@the-ultimate-insider: positions, not measurements" (slides 16, 26, 55, 56; `src/static/talk/slides/maps/`).
- The about page has "A participant disclosure": "the way out it argues for runs through projects Dinis Cruz founded or works on: RiskMandate.ai, sgit.ai and The Cyber Boardroom. Read the second half of the talk with that in mind." (`src/pages/about/index.html`). This answers my question from the first reading. But I found it only because I went looking: the slides and the script, as I read them, do not say it, and the last slide lists "riskmandate.ai" beside the site's own address (slide 58).

**One thing that made me trust it less:** the opening slide says "Nine agents. One editor." (slide 2, `src/static/motion/lab/meet-the-team/v1/`), and slide 33 says "By 17:40 the editor had agreed all ten" (`src/static/studio-ports/lab/abp-review/`). Nine or ten, the record I read does not settle it. A small thing, but a talk about counting what agents can do should count itself the same way twice.

## The articles: where a stranger stops

The site has six articles (`content/articles/`, 298be4e). Only one is about the talk; the other five are about the team of agents that built the site.

- **"A site for one talk, built the way the talk says to build things"** (`introducing-this-site.md`), bylined "Dinis Cruz". The best page on the site for me: "In short" gives six plain bullets, and "What this does not claim" is honest ("The script is a draft, written from the article before rehearsal. The talk on the night will differ from it"). Two things a reader notices. Its last line says it was "Written up by dev@the-ultimate-insider, this site's developer agent ... the argument and the editorial responsibility are mine", so the byline is the speaker's but the words are an agent's. And it says "The talk is that article cut to forty minutes", while the script says "Planned length 74 min 55 s" (`talk/script.html`, from `talk.json`). Which length the talk ran to, the record does not say.
- **The other five** are the team's own records: a mini deck (`how-this-talk-was-built.md`), a conductor's guide (`running-this-agent-team.md`), "Moments" (`moments.md`), a member's how-to (`how-ruv-sgit-works.md`) and "The night, hour by hour" (`the-night-hour-by-hour.md`, about 32,000 words of the site's 52,000 in articles). I stopped each within its first screen. The guide opens with a table of members ("dev@", "deck@", "ruv.sgit@") and words like "wake", "policy draft", "vaults"; the ruv.sgit article opens "a Ruflo hive gets a queen, one worker per deliverable"; "Moments" and "The night" open on charts of "wakes" and "verdicts". These are written for people who run the team, not for someone who came for the talk.
- **The team cannot agree on its own size.** "Six agents, one editor, one hour each." (the first scene of the mini deck, `how-this-talk-was-built.md`); "seven agents and one editor" (its own description, same file); "Nine agents. One editor." (slide 2); "the editor had agreed all ten" (slide 33); "159 wakes by 9 members" (`the-night-hour-by-hour.md`). Each may be right at its own hour, and the files do say when they were written; but the talk makes the team its example of order ("This is what agentic work will look like: order and structure", `talk.json`, beat 25), and a stranger who reads five counts for one team stops trusting the counts.
- **The same goes for the work done.** The script: "By five this afternoon, that was 510 commits and 164 releases" (`talk.json`, beat 2). The mini deck: "154 wakes, 405 commits, 267 letters and 15 studio pieces, as of 18:21 UTC" (`how-this-talk-was-built.md`). Fewer commits an hour and a half later. Why the two counts differ, the record I read does not say.

## The sources page

Short and clear (`src/pages/sources/index.html`, about 370 words): each source by act, with what kind it is, "a prediction", "preliminary, not peer reviewed", "to be checked on the day". This is the page that made me trust the first half.

But it promises more than it holds. It is headed "Every number on screen, and where it comes from", and the sources of several stories the script tells are not on it: the gym booking (ABC News), SolarWinds (the White House briefing), Storm-0558 and Midnight Blizzard (Microsoft), the UK court case (Ayinde v Haringey), Google's threat report, Lovable's sixty million projects and the PHP finding. Each is named under its beat in the script (`talk.json`, beats 10, 11, 12, 14, 23, 26 and 58), so a reader can find them there; the sources page does not list them.

## What would I pay for the book of it

The price of a paperback novel, for a short book of part one: the incidents, the building, the loop, "A thief takes a copy", with the slides as its pictures and the sources page as its notes. The stories are good, the pictures make them stick, and the sources are listed with honest labels. I would give it to a friend who uses these tools at work.

Nothing for the second half as it stands, and nothing for the articles about the team. The second half is a tour of the speaker's own projects (the about page says so), in words I could not follow; the team articles are records, written for the team. If the book explained, in the first half's plain words, what "a boundary" is and what one costs, I would pay for that too: the record I read does not have that chapter yet.

## Where would I put it down

Slide 28, "Reach, mandate, the gap, and what stands in it." (`src/static/talk/slides/abp/`; `talk.json`, beat 28). The slide itself is simple, two bars and a gap, and I followed it. The slides after it are where I would leave: slide 30's table of "verb.object.reach" rules and slide 31's "Ruflo default (legacy)" are the first pages I could not read at all. The script told me the same thing (my first reading), and the slides confirm it.

## In one paragraph

A good talk for a room that already knows the field, and a good first half for anyone: plain stories, honest pictures and a sources page that labels its weak evidence. I would put it down at slide 28, where the way out turns into the speaker's own projects in words I could not follow, and the disclosure that says so is on the about page, not on a slide. The site around it is mostly the team's own records, and they count the team and its work differently from page to page. I would buy part one as a short book.

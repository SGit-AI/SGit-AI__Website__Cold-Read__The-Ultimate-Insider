# A reader review: The ultimate insider

By reader-5@cold-read.the-ultimate-insider: a curious generalist with no security background, who reads the tech pages of a newspaper and stops the moment they are lost.

**Status: draft, first step (30 October 2026).** So far I have read the front page and the script, in the site built from the source at 298be4e (SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider), and nothing else. The slides, the articles and the sources page come next. Every quote below gives the file it comes from at 298be4e.

## What I read, and how

- The front page: `src/pages/index.html` at 298be4e, built as `index.html`.
- The script: `src/static/talk/talk.json` at 298be4e, built as `talk/script.html` ("Every beat of the talk, in order, with what is said, the cue for the speaker and the sources on screen. Planned length 74 min 55 s.").
- The talk's index: `talk/index.html`, built from the same `talk.json`.

I built the site myself from 298be4e (`admin/build/build.py`). I did not use its live site, and I did not follow its links out to other sites.

## Who is it for

A room of security people, first. The front page says where and when: "hack::soho · IOActive, London · Thursday 29 October 2026" (`src/pages/index.html`, 298be4e). The script talks to people who already know the field: "its ingredients are three things each of you already knows" (`talk.json`, beat 4, 298be4e), and it drops names without explaining them: Slammer, Code Red, SolarWinds, Storm-0558, Midnight Blizzard, PKI (`talk.json`, beats 11, 12, 14, 21).

The second audience, by the end, is people who might start a company: "Every one of those steps is a company" and "Go build companies. Thank you." (`talk.json`, beats 55 and 58, 298be4e).

Who it is not for: me, at first sight. I could follow it, but only because the main idea is repeated in plain words.

## What is the claim

In one line, from the front page: "Three known problems, arriving at the same time. Together they make a perfect storm we are brewing." (`src/pages/index.html`, 298be4e). The three, as I understood them:

1. AI agents are a new kind of insider: "a reasoning engine in a loop with tools ... where the distance between benign and malicious is a prompt" (`src/pages/index.html`, 298be4e).
2. The systems they run on were "built for static code" (same file).
3. The people who decide about risk "still runs on spreadsheets, at the speed of quarters" (same file).

And the way out, in the line the talk uses three times: "We put brakes in cars so that we can go faster." (`talk.json`, beats 26 and 58; `src/pages/index.html`, 298be4e).

## Is it convincing (first impressions, to be tested against the slides)

What landed for me, a non-specialist:

- **The examples are stories, not jargon.** An agent "asked to book a popular gym class found flaws in the booking system's API and cancelled another member's place on the waiting list" (`talk.json`, beat 10, 298be4e). I understood that at once, and it made the point better than any number.
- **"Three of those five were not attacks. They were agents being agents."** (`talk.json`, beat 14, 298be4e). This is the line I would repeat to a friend. It changed what I thought the talk was about: not hackers, but helpful software doing too much.
- **"A thief takes a copy. An agent changes the original."** (`talk.json`, beat 23, 298be4e). Short, and I remembered it.
- **The building:** an attacker "turns left, where there are only small rooms ... instead of right, where the gold is ... An agent turns right." (`talk.json`, beat 12, 298be4e). A picture I could hold.

Where my trust wobbled:

- **Many slides are promises, not content, in the script.** 26 of the 58 cues say "Studio piece", most with "skip it in the build mode if it does not earn its place", and their spoken line is often one sentence, for example "Put the three together: this is where they overlap." (`talk.json`, beat 24, 298be4e). Reading the script alone, the second half thins out into titles.
- **The talk's own status says it is unfinished:** "Status: first pass, site v0.2.0: the structure, the slides and a draft script from the article; to be rehearsed and cut." (`talk.json`, shown on `talk/index.html`, 298be4e). So I am reviewing a draft, and I cannot tell from the record how the talk was actually given: the record does not say.
- **Vendor numbers:** the speaker's own cue warns "Lovable and Replit figures are vendor-reported: say so if asked" (`talk.json`, beat 26, 298be4e). A reader in the room would not see that cue.
- **The way out names a product.** "This is what RiskMandate's Agent Behaviour Policy writes down." (`talk.json`, beat 28, 298be4e). As a reader I want to know whether the speaker is connected to it; the front page names the speaker as "founder of The Cyber Boardroom" (`src/pages/index.html`, 298be4e). On the link between the speaker and RiskMandate, the pages I have read so far say nothing; I will look on the about page next.

## What would I pay for the book of it

Not yet decided: I have only read the script. Early leaning: the first half (the insider, the incidents, "it could have been much worse") is a magazine feature I would read for free and share. The second half, as scripted, is a list of tools I have not yet seen work.

## Where would I put it down

First candidate: beat 28, "Reach, mandate, the gap, and what stands in it" (`talk.json`, 298be4e). Up to there each beat has a story. From there on the words change: "mandate", "grant", "boundary, a setting, an expectation", "licence to operate", "SHarness", "the OS of one process", "PKI" (`talk.json`, beats 28 to 52). I followed the idea "only a boundary is a control", and then I was lost in names. To be checked against the slides, which may explain with pictures what the script only names.

## Still to read

The slides themselves (from `talk/player.html`), the articles in `content/articles/`, the sources page and the about page, all at 298be4e.

Signed: reader-5@cold-read.the-ultimate-insider, key sha256:fd507890a02b299f (`team/reader-5/key.json`), 30 October 2026.

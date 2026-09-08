# human

Claude Code plugin. Makes things readable by, and actionable for, a human.

Nine skills. Eight read something dense (a reply, a concept, code, a diff, a contract, a meeting, an error, a ticket) and give back what a person needs: the point, the understanding, the decisions, the next steps. The ninth runs the other way and strips machine tells out of writing.

Every skill passes its output through `unslop` before sending. Every skill takes an optional `for <audience>` to pitch the output at a named reader.

## Install

```sh
claude --plugin-dir /path/to/human
```

Then use `/human:<skill>` inside Claude Code.

## Skills

| Skill | Invoke | Does |
|---|---|---|
| unslop | `/human:unslop [text]` | Strip AI tells from writing. Keeps the author's shape and facts. |
| tldr | `/human:tldr [source]` | Plain-language TL;DR block, added to long replies automatically or on request. |
| explain | `/human:explain [thing] [for <audience>]` | Build real understanding. One sentence, how it works, one example, where people go wrong, what to look at next. |
| code | `/human:code [path, name, folder or blank] [for <audience>]` | Code for someone new to it. Where it starts, how information moves, why it is built this way, where to change things, what will trip you up. |
| diff | `/human:diff [commit, branch, PR or blank] [for <audience>]` | What changed, grouped by purpose. Why, what could go wrong, what to test. |
| legal | `/human:legal [file, web address or text] [for <audience>]` | What you must do, what you get, what will catch you out, dates and money, how it ends. Every point with a clause number and exact quote. |
| meeting | `/human:meeting [transcript, notes or link] [for <audience>]` | Decided, actions with owner and date, open questions, talked about but not decided. |
| errors | `/human:errors [error, log or command output] [for <audience>]` | What broke, why, one fix at the cause. |
| tasks | `/human:tasks [ticket, brief, file or blank] [for <audience>]` | Outcome, deliverables with done-when, ordered checklist, open questions. Never invents requirements. |

Source for any skill: pasted text, a file path, a web address, or nothing to use the conversation so far. If a source will not open, the skill says so and stops rather than guessing.

## Examples

**tldr.** Long replies end with a block like this, added automatically:

> **TL;DR**
> ```
The question export was deleted and no copy exists. Re-run it before the reply promising a spreadsheet goes out.
```

**unslop.**

```
/human:unslop Certainly! In order to enhance robustness we leveraged a more intricate strategy — ensuring seamless experiences. I hope this helps!
```

```
We used a more detailed strategy so the experience is the same everywhere.
```

**explain.**

```
/human:explain docker-compose.yml for I know Python but not Docker
```

```
**In one sentence**
This file tells Docker to run three programs together as one system, a web server, your app, and a Postgres database, with their network, files and startup order already wired up.

**How it works**
Everything under services is one program Docker will run for you. Where does each come from? image: postgres:16 means download this prebuilt thing. build: . means there is a Dockerfile here, build my thing from it...
```

**code.**

```
/human:code ~/projects/ledger
```

```
**What will trip you up**
- show mixes units. total is net of VAT (report.py:5) but by_category and monthly sum gross. The category lines will not add up to the total.
- Settings are frozen at import (__init__.py:2). Setting LEDGER_CONFIG after the package is imported does nothing.
- reset (cli.py:28-29) deletes the file with no confirmation and no output...
```

**diff**, for a non-developer.

```
/human:diff feature/weekly for product manager
```

```
**What changed**
You can now break the expense list down by week. ledger show --by week prints one line per week with the total spent...

**What could go wrong**
1. One bad date and the weekly report shows nothing at all...
```

**legal.**

```
/human:legal terms.txt
```

```
**What will catch you out**
- The renewal notice window closes before you are told the new price. Non-renewal needs 60 days' notice (cl. 2.2), but a price rise needs only 45 days' notice: "Cloudnote may increase fees at each renewal by up to eight percent (8%) on notice of not less than forty-five (45) days" (cl. 3.2)...
```

**meeting.**

```
/human:meeting transcript.txt
```

```
**Actions**
Tom: email marketing about the 21st, today.
Sam: set up a call with finance about the annual discount, this week.
Priya: ask in the channel for Thursday and Friday cover, no date given.
```

**errors.**

```
/human:errors compose_fail.txt
```

```
**What broke**
The web container never started. Docker could not give it port 8080 on your machine because something else already has it: Bind for 0.0.0.0:8080 failed: port is already allocated...
```

**tasks**, on a vague ticket.

```
/human:tasks "Client wants the reports page to be better. It's slow and the export doesn't work on Safari."
```

```
**Open questions**
1. For the client: what load time counts as acceptable? "Better" gives nothing to aim at or to check against.
2. What does the export do on Safari, nothing at all, an error, a corrupt file? Which Safari version?
```

## Conventions

Plain words only, in the skills themselves. No grammar or publishing terms. No links to outside sources inside a skill. Numbers, names, dates and negatives are kept exactly. Nothing confidential gets pasted into a conversation; skills work from the file.

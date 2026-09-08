# human plugin: build checklist

Work one skill at a time, top to bottom. Every skill follows the same shape: `skills/<name>/SKILL.md`, frontmatter with `name`, `description` (trigger words included), `argument-hint`; body with source resolution, output shape, checks before sending, and a mandatory `human:unslop` Skill call on the output as the final step.

Shared conventions to apply in every skill:

- Source resolution order: explicit text, file path, URL, blank means the conversation so far.
- Preserve numbers, dates, names, decisions and negatives (not, unless, except) exactly.
- No preamble. Start with content. Match the user's language.
- Optional `for <audience>` parameter on every skill.
- Nothing classified CONFIDENTIAL gets pasted into the conversation. Redact names, emails, account numbers.
- Plain words only, in the skill text itself. A skill must be readable by someone who is not a developer or a writer. No grammar terms (participle, clause, passive voice), no publishing terms (prose, markup, register), no web terms without a plain word beside them. Test: read the skill aloud to someone outside tech. If they ask what a word means, replace it.
- Do not reference any external sources in the actual skills. No URLs, no links to other repos or docs, no "see X for rules". Everything a skill needs lives inline in its own SKILL.md.
- After finishing a skill: run `claude plugin validate .`, test with `claude --plugin-dir .`, then update README.md (skill table, invoke line, one example).


## unslop

Build first. Its condensed rules get inlined into every other skill.

- [x] Write unslop rules
- [x] Remove `disable-model-invocation` so "make this sound human" triggers it
- [x] Every other skill must invoke `human:unslop` via the Skill tool on its output before sending. Not inline rules, not memory. An actual call.
- [x] Test on one AI-written paragraph
- [x] Update README.md

## tldr

- [x] Frontmatter: triggers tldr, tl;dr, gist, summarise, summarize, recap, sum up, what does this say, plus auto-use on replies over about 12 lines or 150 words
- [x] Locked format: quoted bold label, quoted opening fence, plain text, closing fence
- [x] Content: one to three sentences, 50 word cap, outcome first, no jargon, no new facts
- [x] Mandatory `human:unslop` Skill call on the block before sending
- [x] Test on pasted text (explicit) and on a long generated answer (auto-attach)
- [x] Update README.md
- [ ] Later: SessionStart hook if auto-attach proves unreliable in long sessions

## explain

Base structure for code, diff, legal, meeting, errors.

- [x] Frontmatter: triggers explain, make me understand, break down, walk me through, ELI5, why does
- [x] Five steps: one-sentence version, mechanism built up from simple model, one example plus where the analogy breaks, common misconceptions, where to read next
- [x] Audience pitching rules: developer, non-dev, ELI5, "I know X but not Y"
- [x] Write the condensed 5 line version for inlining into domain skills
- [x] Mandatory `human:unslop` Skill call on the output before sending
- [x] Test on a concept, a config file and a paragraph of documentation
- [x] Update README.md

## code

- [x] Frontmatter: triggers explain this code, how does this work, walk me through this file, new to this codebase
- [x] Input: file path, symbol name, directory, or blank for current repo
- [x] Output: entry point, data flow, key decisions and why, where to change things, gotchas
- [x] Directory input: read structure and entry points, not every file
- [x] Inline explain structure, mandatory `human:unslop` Skill call before sending
- [x] Test on one file and one directory
- [x] Update README.md

## diff

- [x] Frontmatter: triggers explain this diff, what changed, explain this PR, review summary
- [x] Input: git ref, PR URL or number, or blank for working tree
- [x] Output: what changed, why, risk, what to test. Non-dev reader by default when `for` is given
- [x] Group by intent, not by file
- [x] Inline explain structure, mandatory `human:unslop` Skill call before sending
- [x] Test on a small commit and a multi-file branch
- [x] Update README.md

## legal

- [x] Frontmatter: triggers explain this contract, T&Cs, DPA, licence, policy, what am I agreeing to
- [x] Output: obligations, rights, gotchas, dates and deadlines, who bears cost, termination
- [x] Quote clause numbers. Never paraphrase a commitment
- [x] Not legal advice line, once, at the end
- [x] CONFIDENTIAL handling note: work from the file, do not paste contents into chat
- [x] Inline explain structure, mandatory `human:unslop` Skill call before sending
- [x] Test on an open-source licence and a public SaaS T&Cs page (T&Cs tested from a local text file, not a live web page)
- [x] Update README.md

## meeting

- [x] Frontmatter: triggers meeting notes, transcript, what was decided, action items, recap the call
- [x] Input: pasted transcript, notes file, recording link (via a meeting-recording tool when one is available)
- [x] Output: decisions, actions with owner and date, open questions, explicitly not decided
- [x] Attribute quotes to speaker only when the transcript does
- [x] Redact personal data before output
- [x] Inline explain structure, mandatory `human:unslop` Skill call before sending
- [x] Test on one transcript (tested on a transcript file with made-up names; live recording link not yet tried)
- [x] Update README.md

## errors

- [x] Frontmatter: triggers what does this error mean, stack trace, log, why is this failing
- [x] Input: pasted trace, log file path, command output
- [x] Output: what broke, why, one fix. Root cause not symptom
- [x] Grep callers before naming a fix location
- [x] Inline explain structure, mandatory `human:unslop` Skill call before sending
- [x] Test on a PHP stack trace and a Docker compose failure
- [x] Update README.md

## tasks

- [x] Frontmatter: triggers break this down, make a checklist, deliverables, todo list, plan this ticket
- [x] Input: ticket text, brief, description, or blank for the conversation
- [x] Output: deliverables (things that exist when done), ordered `- [x]` checklist, acceptance criteria per deliverable, open questions
- [x] Granularity rule: each item half a day max, one owner, verifiable
- [x] Never invent requirements. Gaps become open questions
- [ ] Later: fetch a ticket by ID from an issue tracker tool instead of paste
- [x] Mandatory `human:unslop` Skill call on the output before sending
- [x] Test on one vague ticket and one detailed brief
- [x] Update README.md

## Plugin wrap-up

- [x] Final README.md pass: table of all skills, install line, one example each
- [x] `claude plugin validate .`
- [x] Add `.claude-plugin/marketplace.json` if sharing with the team
- [x] Tag v0.1.0

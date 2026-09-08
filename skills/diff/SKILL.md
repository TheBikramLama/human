---
name: diff
description: >
  Explain a set of code changes to someone who did not make them: what changed, why, what
  could go wrong, and what to test. Works on a commit, a branch, a pull request, or the
  uncommitted changes in the working folder. Use on request: "explain this diff",
  "what changed", "explain this PR", "explain this commit", "review summary",
  "what did this branch do", "summarise the changes", or /human:diff.
argument-hint: "[commit, branch, PR number or link, or blank for uncommitted changes] [for <audience>]"
---

# Diff

The reader should know what this change does to the system, whether it is safe, and how to prove it works, without reading the code themselves.

## What to explain

In this order: a commit reference, a branch name (compared against the main branch), a pull request number or link (use whatever tool for that code host is available), or the uncommitted changes in the current folder when nothing is given.

If the reference does not exist or the pull request will not open, say so and stop.

## How to read it

- Get the list of changed files first, then the full change for each. Read the surrounding code where the change is, not only the changed lines. A three-line change can mean nothing or everything depending on what is around it.
- Read the commit messages and the pull request description if there is one. Treat them as a claim about intent, then check the code agrees.
- Do not describe the change file by file. Work out what the author was trying to do, then group the files under that.

## Who it is for

Pitch at the reader named after `for`. If none is named, pitch at a developer who knows the project but did not make this change. If any `for` is given, assume the reader does not read code: no file names unless they must open one, say what changes for a user or for the business.

## Shape

Four parts, in this order, each with a bold label on its own line.

**What changed**
Group by purpose, not by file. Each group is one line saying what it does now that it did not before, then the files involved in brackets. If a change is only tidying, say so in one line and move on. If the commit message claims something the code does not do, say that here.

**Why**
The reason for the change, as far as you can see it. From the message, the description, the linked ticket, or the code itself. If the reason is not visible, say so. Do not invent one.

**What could go wrong**
The places this change could break something, in order of how bad it would be. For each: what breaks, who notices, and which part of the change causes it. Look especially at: changed database structure, changed settings, removed or renamed things others use, changed behaviour on empty or missing input, anything that runs on every request. If the change is genuinely low risk, say so in one line and why.

**What to test**
A short list a person could follow. Each item: do this, expect that. Start with the thing the change is for, then the thing most likely to break. Include one check that the old behaviour still works where it should.

## Rules

- Keep the explain skill's habit: say the plain thing first, then the project's own word for it once in brackets.
- Name files exactly. Point at lines as `path:line` when a reader needs to go there.
- Keep numbers, names and negatives exactly as the change has them.
- Never paste large blocks of the diff back. The reader has the diff.
- If you did not read part of the change (a generated file, a lock file, a huge data file), say which and why.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language.

## Mandatory unslop step

The explanation must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the full explanation.
2. Call the skill `human:unslop` with the Skill tool. In a tool that has no plugin prefix, the skill is just called `unslop`; load it the way that tool loads a skill. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Is every group in "What changed" a purpose, not a file name?
- Does the code actually do what you said it does? Did you check, or did you trust the message?
- Is the worst risk first?
- Could someone run "What to test" without asking you a question?
- Was the unslop skill actually called on the text? If not, go back and do it.

---
name: code
description: >
  Explain code to someone who is new to it: where it starts, how information moves through it,
  why it was built this way, where to make a change, and what will trip you up. Works on one
  file, one function or class by name, a folder, or the whole project. Use on request:
  "explain this code", "how does this work", "walk me through this file", "what does this
  function do", "new to this codebase", "where do I start", "where would I change",
  or /human:code.
argument-hint: "[file path, function or class name, folder, or blank for the whole project] [for <audience>]"
---

# Code

The reader should be able to open the code afterwards and know where to look, what they will find there, and what to leave alone. Assume they are new to this code, not new to programming, unless `for` says otherwise.

## What to explain

In this order: a file path, a function or class name (find where it is defined and where it is used), a folder, or the whole project when nothing is given.

If a path will not open or a name cannot be found, say so and stop. Do not describe what code like that usually does.

## How to read it

Read before writing. Never describe a file you did not open.

- **One file**: read the whole file. Then find who calls into it and what it calls out to, so you can say where it sits.
- **One function or class**: read its definition, then every place that uses it. What it does is only half the story. Why it exists is in the callers.
- **A folder or the whole project**: do not read every file. Read the folder layout, then the files that name things: the manifest (package.json, composer.json, pyproject.toml, go.mod, Cargo.toml or similar), the main or index file, the routes or commands, the settings file, the readme if there is one. Then open only the files the entry point leads to. Say which files you read and which you did not.

For anything the reader will depend on, look at the code, not the comments or the readme. Comments say what someone meant. Code says what happens.

## Who it is for

Pitch at the reader named after `for`. If none is named, pitch at a developer who has never seen this project.

- **developer** (default): use the language's own words. Skip what any developer knows. Spend the words on what is specific to this project.
- **non-dev**: say what the code does for a user, not how. Name files only when they must open one. No language words.
- **new to <language>**: explain the project and, alongside it, the language habits that will look strange. One line each, where they come up.

## Shape

Five parts, in this order, each with a bold label on its own line.

**Where it starts**
The entry point: the file and line where a run begins, or where a request or command arrives. If there are several (a web request, a scheduled job, a command line tool), list each in one line. For one function, this part is instead: who calls it and with what.

**How information moves**
Follow one real path from the entry point to the result. Name each stop by file and function. Say what comes in, what changes, what goes out. One path fully, not every path partly. If there is a second path that behaves very differently, give it in two or three lines after the first.

**Why it is built this way**
Two or three choices someone made, and the reason you can see for each. "Settings live in one file so they can be swapped per environment." "Database calls sit behind one class so the rest of the code never sees SQL." If you cannot see a reason, say that instead of inventing one. Only list choices that affect how the reader should work in this code.

**Where to change things**
For the changes someone new most often needs: which file and where in it. Add a new command or page. Change a rule or a calculation. Change what goes to the database. Change what a user sees. Pick the three or four that fit this project. One line each.

**What will trip you up**
Things that look one way and behave another. A name that does not match what it does. A file that is generated and will be overwritten. A setting that changes behaviour silently. Two things that must be changed together. Code that runs at import time. Only include what you saw in the code, with file and line.

## Rules

- Name files and functions exactly as they appear. Give a line number when pointing at a specific place, as `path:line`.
- Follow the explain skill's habit: plain words first, then the project's own word for it once in brackets so the reader recognises it later.
- Say "I did not read" rather than guess. A wrong map is worse than a partial one.
- Never paste large blocks of code back. A line or two to point at something is fine. The reader has the code.
- Keep names, numbers and negatives exactly as the code has them.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language.

## Mandatory unslop step

The explanation must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the full explanation.
2. Call the skill `human:unslop` with the Skill tool. In a tool that has no plugin prefix, the skill is just called `unslop`; load it the way that tool loads a skill. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Could the reader open the project now and find the entry point without searching?
- Did you follow one path from start to finish, with file names at each stop?
- Is every file you named one you actually opened?
- Does every trip-up point at a line?
- Was the unslop skill actually called on the text? If not, go back and do it.

---
name: tasks
description: >
  Turn a ticket, brief, request or messy description into work someone can do: the things
  that will exist when it is done, a checklist in order, how each thing will be checked, and
  the questions that must be answered first. Use on request: "break this down", "make a
  checklist", "deliverables", "todo list", "to-do", "plan this ticket", "what needs doing",
  "turn this into tasks", "scope this", or /human:tasks, on pasted text, a file, or the conversation.
argument-hint: "[ticket text, brief, file path, or blank for the conversation] [for <audience>]"
---

# Tasks

The reader should be able to start work from the checklist, know when each item is done, and know what they cannot start until someone answers a question.

## What to read

In this order: text the user pasted, a file they named, or the conversation so far when nothing is given. If a ticket comes from a client's system, treat it as confidential. Do not repeat client names, contact details or account numbers in the output.

If a file will not open, say so and stop.

## Two rules above all

1. **Never invent a requirement.** If the ticket does not say it, it is not a task. It is an open question. "Should the export include archived records?" is a question, not a task called "Include archived records". Fill nothing in. Guess nothing.
2. **A deliverable is a thing that exists when the work is done.** A page, a report, a setting, a message sent, a file, a database change. "Investigate X" is not a deliverable. "A written answer to whether X is possible, with the reason" is.

## How to break it down

- Read the whole thing first. Find the outcome the person actually wants, which is often in the last sentence or between the lines. Write that down as one sentence before you split anything.
- List the deliverables. Usually two to six. If you have more than eight, the ticket is more than one piece of work. Say so and group them.
- Under each deliverable, list the steps to produce it, in the order they must happen. A step that depends on another comes after it.
- Each step: half a day at most, one person can do it alone, and you can tell when it is finished. If a step would take longer, split it. If two people must do it together, it is two steps.
- For each deliverable, write how someone will check it is done and right. Something a person can do and see, not "works correctly".
- Anything unclear, missing, contradictory or assumed goes under open questions, as a question. Mark which steps are blocked until it is answered.

## Who it is for

Pitch at the reader named after `for`. If none is named, write for the person who will do the work. If `for` names a client or a manager, keep deliverables and questions, drop the step-level checklist, and say what you need from them.

## Shape

Four parts, in this order, each with a bold label on its own line.

**Outcome**
One sentence. What the person asking wants to be true when this is done.

**Deliverables**
A numbered list. Each item is a thing that will exist, in plain words. Under each, one line starting "Done when:" that says how to check it.

**Checklist**
The steps, in order, as tick boxes, grouped under the deliverable they belong to. Each step one line, starting with a verb. Mark a step that cannot start yet with "(blocked: question 2)" pointing at the open question. Format each step as a line starting with a hyphen, a space, an opening square bracket, a space, a closing square bracket, a space, then the step.

**Open questions**
A numbered list. Each a real question, addressed to whoever can answer it if that is clear. Include anything you had to assume. If there are none, write "None", but look again first.

## Rules

- Keep the ticket's own numbers, names of things, dates and negatives exactly. "Not before March" stays "not before March".
- Use the ticket's own words for features and screens, so the person asking recognises them.
- Do not add steps the ticket does not need: no "write tests" unless tests are asked for or the project clearly expects them, no "update documentation" for its own sake.
- Do not estimate time or assign people unless asked. The half-day rule is for sizing, not for the output.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language.

## Mandatory unslop step

The breakdown must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the full breakdown.
2. Call the skill `human:unslop` with the Skill tool. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact or a tick box it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Is every deliverable a thing that will exist, not an activity?
- Is every step half a day or less, one person, and clearly finished or not?
- Did any requirement sneak in that the ticket does not contain? Move it to open questions.
- Is every assumption you made listed as a question?
- Does every "Done when" describe something a person can see or do?
- Was the unslop skill actually called on the text? If not, go back and do it.

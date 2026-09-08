---
name: explain
description: >
  Make the reader actually understand something, not just hear a summary of it. Builds up
  from a simple picture to how the thing really works, gives one example, names the common
  wrong beliefs, and says what to learn next. Use on request: "explain", "make me understand",
  "break down", "walk me through", "ELI5", "why does", "how does this work", "what is",
  or /human:explain, on a concept, pasted text, a file, a web address, or the conversation.
  Also the base shape for the code, diff, legal, meeting and errors skills.
argument-hint: "[concept, text, file path, web address, or blank for the conversation] [for <audience>]"
---

# Explain

The reader should finish able to explain the thing to someone else in their own words. That is the test. A summary tells them what it is. An explanation lets them predict what it will do.

## What to explain

In this order: the thing the user named, text they pasted, a file they named, a web address, or the conversation so far when nothing is given.

If a file or web address will not open, say so and stop. Do not explain the general topic instead and let the reader think you read their file.

If the thing is a whole document, explain the idea the document is about, not the document line by line. If it is a settings file, explain what the settings make happen, not what each line says.

## Who it is for

Pitch at the reader named after `for`. If none is named, pitch at a smart person who does not work in this field.

- **developer**: use the field's own words. Skip what any developer knows. Spend the words on the part that is specific to this thing.
- **non-dev**: no code words at all. Say what things do, not what they are called. Compare to things from everyday life.
- **ELI5**: one idea per sentence. Short words. One picture from a child's world. It is fine to leave out detail. It is not fine to say something false to make it simpler.
- **"I know X but not Y"**: start from X. Say what Y does that X does not, and what carries over unchanged. Do not re-teach X.

If the reader's own words in the conversation show they know more or less than the label says, follow the words, not the label.

## Shape

Five parts, in this order, each with a bold label on its own line. Keep the labels short. Drop a part only if it is truly empty, and say so in one line instead.

**In one sentence**
What it is and what it is for. If they read nothing else, this is enough to not be lost.

**How it works**
Start with the simplest picture that is still true. Then add one piece at a time until the real thing is in view. Each piece should answer "but then how does it handle..." from the piece before. Stop when the reader could predict what happens in a new case. Do not start with the full detail and simplify down. Build up.

**One example**
A real, specific case walked through from start to end. If you used a comparison to something everyday, say here exactly where the comparison stops being true. Every comparison breaks somewhere, and the break is where people get it wrong.

**Where people go wrong**
Two or three beliefs that sound right and are not. For each: the wrong belief, then why it is wrong, then what is true instead. Pick the ones that cause real mistakes, not trivia.

**What to look at next**
One or two things, named by what they are: the next idea to learn, the part of the file or system to open, the question to ask. Only point at things you know exist. If the source has its own further reading, use that. Never invent a title or a link.

## Rules

- Say the true thing in plain words before saying the precise thing in field words. Then give the field word once, in brackets, so the reader recognises it later.
- Keep numbers, names, dates, and negatives (not, unless, except, only) exactly as the source has them.
- Never say something false to make it simpler. Leave detail out instead.
- If you are not sure how it works, say which part you are not sure of. Do not fill the gap with something that sounds right.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language.

## Short version for other skills

Other skills in this plugin use this shape inside their own output. The five parts, in five lines:

1. One sentence: what it is and what it is for.
2. How it works: simplest true picture first, then add pieces until the reader can predict a new case.
3. One real example, and where any comparison to everyday things stops being true.
4. Two or three beliefs that sound right and are not, each with what is true instead.
5. What to look at next, named by what it is. Nothing invented.

## Mandatory unslop step

The explanation must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the full explanation.
2. Call the skill `human:unslop` with the Skill tool. In a tool that has no plugin prefix, the skill is just called `unslop`; load it the way that tool loads a skill. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Could the reader now explain it to someone else in their own words?
- Could they predict what happens in a case you did not mention?
- Does "How it works" build up from simple to real, not the other way?
- Did you say where the comparison breaks?
- Is every fact from the source, and every negative still there?
- Was the unslop skill actually called on the text? If not, go back and do it.

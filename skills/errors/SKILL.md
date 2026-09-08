---
name: errors
description: >
  Explain an error, a stack trace, a log or a failed command in plain words: what broke, why
  it broke, and the one fix that deals with the cause rather than the symptom. Use on request:
  "what does this error mean", "stack trace", "why is this failing", "explain this log",
  "what went wrong", "why did this crash", "this command failed", or /human:errors,
  on pasted output, a log file path, or the output of a command.
argument-hint: "[pasted error, log file path, or command output] [for <audience>]"
---

# Errors

The reader should know what actually failed, why, and what to change, without having to decode the trace themselves. One cause, one fix.

## What to read

In this order: text the user pasted, a log file they named (read the end first, then work backwards to the first sign of trouble), or the output of a command they ran. If nothing is given, look at the last error in the conversation.

If a file will not open, say so and stop.

## How to read it

- **Find the first error, not the last.** Logs and traces pile up. The last message is usually a consequence. Work back to the first line that reports something wrong. That is where the cause lives.
- **Read the line the trace points at, and the lines around it.** Open the file at that line if you can. The trace gives an address. The code gives the reason.
- **Follow the callers before you name a fix.** Search for every place that calls the function that failed. If several callers can hit the same failure, the fix belongs in the shared function, not in the one caller the trace happened to show. A fix in one caller leaves the others broken.
- **Tell the symptom from the cause.** "Undefined index" is a symptom. The cause is whichever step should have set the value and did not. Keep going until you reach a step that was wrong, not one that was surprised.
- **If you cannot tell,** say what you know and what would settle it. Name the one thing to check or the one line to add. Do not offer three guesses.

## Who it is for

Pitch at the reader named after `for`. If none is named, pitch at the developer who hit the error. For a non-developer, drop file names and say what stopped working for them and who needs to fix it.

## Shape

Three parts, in this order, each with a bold label on its own line.

**What broke**
One or two sentences. The thing that failed, in plain words, and where. "The page could not load because the code asked the database for a customer id that was never set." Name the file and line as `path:line` when you have it.

**Why**
The chain from cause to symptom, shortest true version. Start at the cause. Each step follows from the last. Stop when you reach the message the reader saw. If a comparison to everyday life helps, use one, and say where it stops being true. If you are unsure of a step, say which.

**The fix**
One fix, at the cause. Which file and line to change, and what to change it to, in a line or two of code if code is needed. Say why this place and not the place the trace pointed at, if they differ. Then one line on how to confirm it worked: the command to run or the thing to click, and what should happen.

If there is a quick workaround that is not the fix, you may add it in one line, clearly marked as a workaround.

## Rules

- Quote the error message exactly, once, in the first part. Do not repeat the trace back.
- One cause, one fix. If there really are two independent problems, say so and give each its own three parts.
- Keep file names, line numbers, error text and negatives exactly.
- Never guess a fix that you have not checked against the code, when the code is there to check.
- If the fix touches a shared or live system, say so, so the reader can follow their change process.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language.

## Mandatory unslop step

The explanation must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the full explanation.
2. Call the skill `human:unslop` with the Skill tool. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact, a path or a line of code it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Did you find the first error, not the last?
- Did you look at every caller before choosing where the fix goes?
- Is the fix at the cause, not where the trace happened to point?
- Could the reader apply the fix and confirm it without asking you anything?
- Was the unslop skill actually called on the text? If not, go back and do it.

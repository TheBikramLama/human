---
name: meeting
description: >
  Turn a meeting transcript or notes into what people need afterwards: what was decided, who
  is doing what by when, what is still open, and what was talked about but not decided. Use on
  request: "meeting notes", "transcript", "what was decided", "action items", "actions",
  "recap the call", "minutes", "who agreed to what", "follow-ups from the meeting",
  or /human:meeting, on pasted text, a notes file, or a meeting recording link.
argument-hint: "[pasted transcript, notes file, or recording link] [for <audience>]"
---

# Meeting

The reader should be able to skip the recording and still know every decision, every action with an owner and a date, and every question left hanging.

## Before you start

Transcripts contain people's names and often personal or client details. Before writing anything, decide what the reader needs. Use first names or roles only. Do not repeat phone numbers, email addresses, account numbers, health or personal details, or anything said about a person that is not about the work. If a whole meeting is clearly confidential (a client's commercial figures, a personnel matter), work from the file and keep the output to decisions and actions only.

## What to read

In this order: text the user pasted, a notes file, a recording link (use the meeting recording tools if they are available; if they are not, or the link will not open, say so and stop), or the conversation so far when the user says "conversation".

Read the whole transcript before writing. Decisions often get reversed twenty minutes later.

## What counts as what

- **A decision** is something the group agreed to do or not do, and nobody walked back. "Let's go with the blue one." "We won't ship before the audit."
- **An action** is a specific thing one named person said they would do, or was asked to do and did not refuse. It needs an owner. If the transcript gives a date, keep it. If not, write "no date given". Never invent a date or an owner.
- **An open question** is something someone asked or raised that the group did not answer or settle.
- **Not decided** is something discussed at length, with options on the table, that ended without agreement. Say this plainly so nobody leaves thinking it was settled.

If the same thing was decided and then reversed, only the final position counts, but note in one line that it changed.

## Who it is for

Pitch at the reader named after `for`. If none is named, write for someone who was meant to be in the meeting and missed it. If `for` names someone who was not part of the work (a client, a manager), drop internal detail and keep decisions and dates.

## Shape

Four parts, in this order, each with a bold label on its own line. Keep the labels. If a part is empty, write "None" under it. An empty part is information.

**Decided**
One line per decision. What was decided, and in a few words why, if a reason was given.

**Actions**
One line per action: owner, what, by when. Same words for the same person throughout. Put "no date given" where there was none. Group by owner if there are more than six.

**Open questions**
One line per question, as a question. If someone was asked to find the answer, that also belongs under Actions.

**Talked about, not decided**
One line per topic: what the options were, and where it was left.

## Rules

- Say who said something only when the transcript names the speaker. If the transcript shows "Speaker 2" or nothing, do not guess a name. Write "someone" or leave the speaker out.
- Quote only when the exact words matter, such as a promise or a number. Otherwise use your own plain words.
- Keep numbers, dates, names of things, and negatives exactly as spoken. "We won't do X before Y" must not become "X after Y" if that changes the sense.
- Do not add anything that was not said. No suggested next steps, no filling gaps.
- If the recording cut out or the transcript is partial, say so at the top in one line.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language.

## Mandatory unslop step

The notes must go through the unslop skill before they are sent. This means calling the skill, not remembering its rules.

1. Draft the full notes.
2. Call the skill `human:unslop` with the Skill tool. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Does every action have an owner, and either a date or "no date given"?
- Is every decision one the group actually landed on, not one that was later reversed?
- Is every speaker attribution one the transcript made, not one you guessed?
- Is there any personal detail in the output that the reader does not need?
- Would someone who was in the meeting recognise all of it?
- Was the unslop skill actually called on the text? If not, go back and do it.

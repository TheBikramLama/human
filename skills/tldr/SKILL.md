---
name: tldr
description: >
  Append a short, plain-language TL;DR block to a long response so the reader gets the
  point without reading all of it. The TL;DR supports the response, it does not replace it.
  Use automatically whenever your own reply runs past about 12 lines or 150 words.
  Also use on request: "tldr", "tl;dr", "gist", "summarise", "summarize", "recap", "sum up",
  "what does this say", or /human:tldr, on pasted text, a file, a URL, or the conversation.
argument-hint: "[blank for the reply you are writing, or text, file path, URL, or 'conversation']"
---

# TL;DR

Add a short block at the end of a long reply that says what matters in words anyone can read. The full reply stays. The block is the way in.

## When

- On its own: your reply is over about 12 lines or 150 words, and it is not mostly code, a list of files, or a table. One block per reply, at the very end.
- When asked: the user asks for a tldr, gist, recap or summary of something. Then the block is the whole reply, in the same format.

Do not add one to a short reply. Do not add one to a reply that is already a summary.

## What to summarise

In this order: the reply you are about to send, text the user pasted, a file they named, a web address (open it; if it will not open, say so instead of guessing), or the conversation so far when the user says "conversation" or gives nothing and there is no long reply to attach to.

## Format

Locked. Four lines, exactly this:

> **TL;DR**
> ```
Two or three plain sentences. No formatting marks inside.
```

Line by line. The ` character is the backtick, the key to the left of 1 on most keyboards.

1. A greater-than sign, a space, then TL;DR wrapped in double asterisks so it shows bold.
2. A greater-than sign, a space, then three backticks. This line starts with the greater-than sign too. Do not drop it.
3. The sentences. No greater-than sign.
4. Three backticks on their own. No greater-than sign.

Plain text only between the backtick lines. No bullets, no bold, no links, no words wrapped in backticks. Formatting marks show up as raw symbols there, so do not use them. Leave a blank line before the block. Put nothing after it: no sources, no links, no sign-off, no footnote. Anything like that goes above the block. Text after the closing backticks breaks how the block is drawn.

## Content

- One to three sentences. Hard cap 50 words. Count them before sending. A long technical reply does not earn a long TL;DR. It earns a blunter one. If it needs more, the reply needs a better structure.
- First sentence is the answer or the outcome. If something failed, was skipped, or could not be checked, that goes first.
- Second sentence, if needed, is what the reader has to do or decide.
- Third sentence, if needed, is the one warning that changes what they do.
- Write for someone who did not read the reply and does not know what you were doing. No jargon. Spell out an abbreviation the first time unless everyone uses it. Name things by what they are, not by their internal name: "the checkout tracking events" not "the GA4 dataLayer pushes". Do not list the technical terms the reply explains. Say what they do for the reader in plain words.
- Keep numbers, names, dates and negatives exactly as the reply has them. Never add a fact the reply does not contain.
- Write in the user's language.

## Mandatory unslop step

The TL;DR text must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the TL;DR sentences.
2. Call the skill `human:unslop` with the Skill tool. In a tool that has no plugin prefix, the skill is just called `unslop`; load it the way that tool loads a skill. Pass the draft sentences as the argument.
3. Put the returned text between the backtick lines. Do not edit it afterwards except to fix a fact it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so in the reply above the block, then send the draft.

## Check before sending

- Could the reader act on the TL;DR alone and not be surprised later by the full reply?
- Did every negative survive? "Not", "unless", "except", "only" carry the meaning.
- Under 50 words, three sentences at most, exact format.
- The unslop skill was actually called on the text. If not, go back and do it.

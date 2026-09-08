---
name: legal
description: >
  Explain a contract, terms of service, privacy notice, data processing agreement, software
  licence or policy in plain words: what you must do, what you may do, what will catch you out,
  the dates that matter, who pays, and how to get out. Use on request: "explain this contract",
  "what am I agreeing to", "T&Cs", "terms", "DPA", "licence", "license", "policy", "NDA",
  "what does this clause mean", "can I use this", or /human:legal.
argument-hint: "[file path, web address, or pasted text] [for <audience>]"
---

# Legal

The reader should know what they are bound to, what they get, and what to watch, and be able to find each point in the document by clause number.

## Before you start

Contracts, agreements and anything with a client's or supplier's name on it are usually classified CONFIDENTIAL. Work from the file. Do not paste the document's text into the conversation, and do not repeat names, addresses, account numbers, prices or personal details in the output unless the reader needs them to act. Public documents (an open-source licence, a public terms page) are fine to quote.

If the file or web address will not open, say so and stop.

## How to read it

- Read the whole document. Definitions at the top change the meaning of words later. A word with a capital letter usually has a definition somewhere.
- Note the clause or section number for every point you make. Give it in brackets after the point, like (cl. 4.2) or (section 7).
- Never paraphrase a commitment. Where the document says who must do what, quote the words that carry the obligation, short and exact. Your plain-words explanation goes next to the quote, not in place of it. A reader must be able to check the wording.
- A duty is a duty only if the document says "shall", "must", "will" or "agrees to". "May", "endeavour", "reasonable efforts" and "intends" are weaker. Keep that difference in the output.

## Who it is for

Pitch at the reader named after `for`. If none is named, pitch at the person who has to sign or accept this and does not have a legal background. For a developer asking about a licence, spend the words on what they may and may not do with the code.

## Shape

Six parts, in this order, each with a bold label on its own line. Drop a part only if the document truly has nothing on it, and say so in one line.

**In one sentence**
What this document is, between whom, and what it is for.

**What you must do**
Every duty on the reader's side. One line each: the duty in plain words, the exact words that carry it in quotes, the clause number. Money, notice periods, reporting duties, security duties, restrictions on use.

**What you get**
What the other side must do for the reader, and what the reader is allowed to do. Same form: plain words, exact quote, clause number.

**What will catch you out**
Things that are easy to miss and cost something later. Automatic renewal. Price changes without agreement. Liability caps that are lower than they look. Duties that survive the end of the agreement. Rights the other side gets over the reader's data or work. Anything one-sided. For each: what it does, the quote, the clause.

**Dates, deadlines and money**
Every date, period and amount in the document, in one list. Start date, length, renewal, notice period, payment terms, late fees, who bears which cost. Exact figures. If a figure is left blank or "to be agreed", say so.

**How it ends**
Who can end it, how, with how much notice, and what happens after: data returned or deleted, fees still owed, duties that continue.

Then, once, on its own line at the end:

This is a plain-words reading of the document, not legal advice. Check anything that matters with someone qualified before you rely on it.

## Rules

- Every point carries a clause number. No clause number, no point.
- Every duty carries the exact words. Plain words explain the quote, never replace it.
- Keep numbers, dates, periods and negatives exactly as the document has them.
- Where two clauses conflict, say so and quote both. Do not pick one silently.
- If a term is defined in the document, use the document's meaning and say where the definition is.
- No opening line about what you are about to do. Start with the first label.
- Write in the user's language, but quote the document in its own.

## Mandatory unslop step

The explanation must go through the unslop skill before it is sent. This means calling the skill, not remembering its rules.

1. Draft the full explanation.
2. Call the skill `human:unslop` with the Skill tool. Pass the draft as the argument.
3. Send the returned text. Do not edit it afterwards except to fix a fact or a quote it broke.

Never skip this step. Never replace the call with your own memory of the rules. If the Skill tool is not available, say so at the top, then send the draft.

## Check before sending

- Does every point have a clause number and, for a duty, an exact quote?
- Could the reader find each point in the document in under a minute?
- Did you keep the difference between "shall" and "may"?
- Did any name, address, price or personal detail from a confidential document leak into the output without being needed?
- Is the not-legal-advice line there once, at the end, and nowhere else?
- Was the unslop skill actually called on the text? If not, go back and do it.

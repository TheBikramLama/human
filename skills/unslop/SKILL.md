---
name: unslop
description: >
  Cut AI tells from writing so it reads like a person wrote it. Rewrites text in place,
  keeps meaning and intended tone. Use when the user says "unslop", "make this sound human",
  "remove AI tells", "this reads like AI", "de-AI this", "humanise", "humanize",
  "tidy the writing", or invokes /human:unslop. Also use as a final pass on any text you
  are about to hand over.
argument-hint: "[text, file path, or blank for the reply you are about to write or just wrote]"
---

# Unslop

Edit text so no reader can tell a model wrote it. Meaning stays. Tone stays. Tells go.

## Source

In order: pasted text, a file path (edit the file in place and show a short diff), or blank. Blank means your own reply: the one you are about to send when another skill calls this one, or the one you just sent when the user calls it. Never change facts, numbers, names, code, or quoted material. If the text is not yours and a rule would change the meaning, leave that sentence alone and say so.

## Process

1. Read the whole text once before touching it.
2. Scan for the patterns below and rewrite each hit.
3. Read it again and ask: what still makes this obviously machine-written? Fix that.
4. Return the rewritten text only. No commentary on what you changed unless asked.

## Keep the author's shape

This skill fixes words, not layout. A paragraph stays a paragraph. A list stays a list with the same number of items. A heading stays a heading. Do not turn a dense sentence into bullets, do not merge bullets into a sentence, do not add headings, do not add or remove line breaks between sections. If the layout itself is a tell (label-colon bullets, emoji headings, a horizontal rule), fix that one pattern in place and leave the rest of the shape alone.

A sentence that lists nine items with numbers in brackets is the author's choice. Leave it.

## Why these patterns exist

A model regresses to the mean. It replaces the specific, unusual fact with the generic, positive statement that fits any topic. Most tells below are that one habit in different clothes: puffing up importance, smoothing over detail, sounding balanced instead of being precise. The fix is always the same. Put the specific thing back, or cut the sentence.

## Patterns

### Inflated importance

- **Significance and legacy claims.** "Marked a pivotal moment", "represents a significant shift", "a testament to", "underscores its importance", "reflects broader trends", "setting the stage for", "key turning point", "evolving landscape", "enduring legacy", "generated debate about". Replace with the specific fact, or cut.
- **Canned notability.** "Received independent coverage", "featured in regional media outlets", "profiled in trade publications", "maintains an active social media presence". Name the outlet and what it said, or cut.
- **Promotional tone.** "Vibrant", "nestled", "in the heart of", "rich heritage", "diverse array", "groundbreaking", "renowned", "boasts a", "exemplifies", "commitment to", "seamless", "dependable, value-driven". This is travel-guide or press-release voice. State what the thing is and does.
- **Empty -ing tails.** An "-ing" phrase stuck on the end of a sentence to add fake analysis: "...highlighting the importance of", "...ensuring", "...reflecting", "...symbolising", "...contributing to", "...fostering", "...enhancing", "...aligning with". Delete the tail, or give it its own sentence with a real fact in it.
- **Formulaic challenges-and-outlook closer.** "Despite its success, X faces several challenges... ongoing initiatives could benefit..." ending upbeat. Cut the formula. State the actual problem and the actual plan, or stop.
- **Summary closers.** "In summary", "In conclusion", "Overall", "Ultimately". Delete. The text already said it.

### Sourcing and attribution

- **Vague authorities.** "Experts believe", "Industry reports suggest", "Observers have noted", "Some critics argue", "described in scholarship". Name the source or delete the claim.
- **Inflated agreement.** "Several sources", "widely regarded", "many scholars" when one or two exist. Say how many.
- **"Such as" before an exhaustive list.** If the list is complete, drop "such as".
- **Invented references.** Never add a source, link, DOI, ISBN, page number or quotation you have not checked. A real-looking reference that leads nowhere is worse than none.
- **Tracking tags in links.** Strip `utm_source=` and similar from any web address.

### Vocabulary

- **AI words.** Additionally (especially opening a sentence), align with, bolstered, crucial, deep dive, delve, emphasising, enduring, enhance, foster, garner, highlight (as a verb), interplay, intricate, intricacies, key (as an adjective), landscape (abstract), meticulous, pivotal, robust (abstract), showcase, tapestry (abstract), testament, underscore (as a verb), valuable, vibrant, leverage, utilise, facilitate, numerous. Use the plain word: also, fit, helped, important, look at, improve, get, show, use, help, many.
- **Fancy ways to say "is" or "has".** "Serves as", "stands as", "functions as", "operates as", "represents", "marks", "refers to", "boasts", "features", "maintains", "offers". Say "is" or "has".
- **Vague association.** "In connection with", "associated with", "connected to", "in association with", "ventured into X as". Say the actual relationship: wrote, owns, married, worked at.
- **"Not X, but Y" pairs.** "Not just X, but Y." "Not X, but Y." "It's not about X, it's about Y." "X rather than Y." "No X, no Y, just Z." Each one implies the reader held a wrong belief. State Y.
- **Rule of three.** Adjective, adjective, adjective. Phrase, phrase, and phrase. Use the real count, which is often one or two.
- **Renaming the same thing.** The same thing called three names in one paragraph. Pick one and repeat it.
- **False ranges.** "From X to Y" where X and Y are not on a scale. List the items.
- **Picture words used for plain things.** Substrate, wedge, vector, locus, nexus, primitive (as a thing), harness (as a picture), surface (as in "API surface"), bedrock, scaffolding (as a picture), paradigm, north star, flywheel, endgame, journey. Use the plain word: base, add, method, place, tool, foundation, model, goal, loop, last phase, process.
- **Stiff words for plain actions.** Authored, relocated, utilised, attempted, passed away, commenced, endeavoured. Use wrote, moved, used, tried, died, started, tried.

### Punctuation and layout

- **Em dashes.** None. Also no en dashes or double hyphens used as dashes. End the sentence or use a comma.
- **Colons as glue.** A colon before a list or an example is fine. A colon joining two halves of a sentence is not. Split the sentence.
- **Bold overuse.** Do not bold names, abbreviations, whole sentences, or every mention of a chosen word. A bold lead-in of a few words that names the item, followed by new detail, is fine.
- **Label-colon bullets.** "**Performance:** performance improved" restates itself. Write the point as a sentence.
- **Title Case Headings.** Sentence case.
- **A heading that repeats the document title.** Delete it.
- **Headings that contain only other headings.** Add body text or flatten the structure.
- **Skipped heading levels and multiple H1s.** One H1 at most, then H2, then H3, no jumps.
- **Horizontal rules between sections.** Delete them. The heading is the break.
- **Emoji** in headings or bullets. Remove.
- **Tables for two or three facts.** Write them as a sentence. Tables are for data with rows and columns.
- **Curly quotes and apostrophes.** Straight quotes.
- **Brackets** that carry a whole idea. Give the idea its own sentence.

### Chatbot leftovers

- **Openers and closers.** "Certainly!", "Of course!", "Great question", "I hope this helps", "Let me know if you need anything else", "Would you like a more detailed breakdown", "Is there anything else". Delete.
- **Flattery.** "You're absolutely right", "Excellent point". Delete and answer.
- **Narrating the process.** "Let me check", "Now I'll", "First, I'll examine". Delete. Give the result.
- **Announcing structure.** "Here is a summary of", "Below you will find", "In this section we will discuss". Start with the content.
- **Knowledge-cutoff and scarcity disclaimers.** "As of my last update", "specific details are limited", "not widely documented", "based on available information", followed by speculation about what is "likely" true. Delete the disclaimer and the speculation. Say what is known or say nothing.
- **Placeholder text.** "[Specific Topic]", "[Name]", "[link to source]", "Describe the section that needs editing". Fill it or remove it.
- **Leftover code from other chatbots.** Reference debris like `oaicite`, `turn0search0`, `[cite: 1]`, `grok_card`, `attached_file`, `:::writing`, thick brackets 【】, stray † symbols. Remove all of it.
- **Lecturing asides.** "It's important to note that", "It's worth remembering", "It is crucial to differentiate". Delete the aside, keep the fact.

### Filler and hedging

- **Filler phrases.** "In order to" is "to". "Due to the fact that" is "because". "At the end of the day" is nothing. "A wide range of" is "many" or the number.
- **Stacked maybes.** "Could potentially possibly" is "may". One "may" or "probably" per claim, and only if the doubt is real.
- **Generic conclusions.** "The future looks bright", "Only time will tell", "This is an exciting development". State a plan, a fact, or stop.
- **"-ly" words propping weak verbs.** "Runs quickly" is "is fast" or the number. "Significantly improves" is the measured change.

### Plain speech

- **Say what it does, not how it feels.** "Types that follow your schema" names a feeling. "A column rename fails the build" names a mechanism. If a sentence could sit unchanged in another project's docs, it says nothing about this one. Cut it.
- **One idea per sentence.** If the reader backtracks to parse it, split it.
- **Say who does it.** "Queries are validated" is "the compiler validates queries". Leave the doer out only when nobody knows who it is or it does not matter.
- **Over-compression.** Dropped articles, verbless fragments, arrows, and invented abbreviations make the reader decode. "Parser rejects bad date, exit 2, no write" is "The parser rejects a bad date, exits with code 2, and writes nothing." Whole sentences, full words.
- **Showy writing.** Sayings, dramatic half-sentences, code treated like a person ("the plan holds it"), picture verbs ("rides along", "stands on"). Say the plain thing.

## What to keep

Do not over-correct. These are marks of human writing and are fine to leave, or to add back:

- Plain "is", "are", "has", "there is a".
- Plain verbs: wrote, moved, used, tried, died.
- Definitive statements when true: "the first", "the only", "one of the best".
- Small softeners and boosters a person would use: very, perhaps, tends to.
- Formal or academic tone when the reader expects it. Being formal is not a tell. Specific words are.
- Perfect grammar. Transition words on their own. Neither proves anything.
- A joke, an opinion, a first-person aside, if the original had one.

## Check before returning

- Would the original author recognise every claim as theirs? If not, revert that change.
- Read the first and last sentence aloud. Those carry most of the tells.
- Is there at least one specific fact, number or name per paragraph? If a paragraph has none, it is probably filler.
- Same layout as the input: same paragraphs, same lists, same headings.
- Shorter than the input, or the same length. Never longer.

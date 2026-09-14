#!/usr/bin/env python3
"""Stop hook: make sure a long reply ends with a correctly formatted TL;DR block.

Claude Code hands us the finished reply in `last_assistant_message`. If the reply
is long enough to need a TL;DR and does not already end with a well-formed one,
we return additionalContext so Claude keeps the turn open and appends it.
"""
import json
import re
import sys

WORD_LIMIT = 150   # reply is "long" past this many prose words
LINE_LIMIT = 12    # ...or this many prose lines
BODY_WORDS = 50    # hard cap on the TL;DR text itself

# > **TL;DR**
# > ```
# the sentences
# ```
BLOCK = re.compile(
    r"^> \*\*TL;DR\*\*\n> ```\n(?P<body>(?:(?!```)[^\n]*\n)+)```[ \t]*$",
    re.MULTILINE,
)

FORMAT = """Your reply was long enough to need a TL;DR block and does not end with a valid one.

Invoke the `human:tldr` skill and follow it. The format is locked, four lines, \
copied exactly, as the last thing in the reply with nothing after it:

> **TL;DR**
> ```
Two or three plain sentences, under 50 words, no formatting marks inside.
```

Lines 1 and 2 both start with "> ". Lines 3 and 4 do not. Reply with only the \
block (and a blank line before it); do not repeat or rewrite the answer you \
just gave."""


def prose_only(text):
    """Drop fenced code and table rows; return (kept lines, fenced line count)."""
    kept, fenced, in_fence = [], 0, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            fenced += 1
            continue
        if in_fence:
            fenced += 1
        elif not line.lstrip().startswith("|"):
            kept.append(line)
    return kept, fenced


def needs_tldr(text):
    lines, fenced = prose_only(text)
    if fenced > len(text.splitlines()) / 2:
        return False  # mostly code, the skill says leave it alone
    words = len(" ".join(lines).split())
    return words > WORD_LIMIT or len([l for l in lines if l.strip()]) > LINE_LIMIT


def block_is_valid(text):
    match = BLOCK.search(text)
    if not match:
        return False
    if text[match.end():].strip():
        return False  # something after the block; the skill forbids it
    return len(match.group("body").split()) <= BODY_WORDS


def main():
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    if event.get("stop_hook_active"):
        return  # already continuing from a stop hook, do not loop
    reply = event.get("last_assistant_message") or ""
    if not needs_tldr(reply) or block_is_valid(reply):
        return
    json.dump({"hookSpecificOutput": {
        "hookEventName": "Stop",
        "additionalContext": FORMAT,
    }}, sys.stdout)


if __name__ == "__main__":
    main()

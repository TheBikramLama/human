#!/usr/bin/env python3
"""Self-check for tldr_stop.py. Run: python3 hooks/test_tldr_stop.py"""
from tldr_stop import block_is_valid, needs_tldr

LONG = "\n".join(f"Line {i} of a reply that is comfortably past the limit." for i in range(20))
GOOD = "\n\n> **TL;DR**\n> ```\nThe push went through. Nothing else needs doing.\n```"

# needs_tldr
assert needs_tldr(LONG)
assert not needs_tldr("Done.")
assert not needs_tldr("Yes, that works fine and here is a single short sentence about it.")
assert not needs_tldr("Here:\n```\n" + "\n".join(f"code line {i}" for i in range(40)) + "\n```")
assert not needs_tldr("Table:\n" + "\n".join(f"| col {i} | val {i} |" for i in range(20)))

# block_is_valid
assert block_is_valid(LONG + GOOD)
assert not block_is_valid(LONG)
assert not block_is_valid(LONG + "\n\n**TL;DR** - inline bold, the shape we keep getting wrong.")
assert not block_is_valid(LONG + GOOD + "\n\nSources: some link.")   # nothing may follow
assert not block_is_valid(LONG + "\n\n> **TL;DR**\n> ```\n" + "word " * 60 + "\n```")  # over 50 words
assert not block_is_valid(LONG + "\n\n**TL;DR**\n```\nMissing the quote markers.\n```")

print("ok")

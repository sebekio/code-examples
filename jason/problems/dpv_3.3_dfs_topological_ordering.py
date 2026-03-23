#!/usr/bin/env python3
# trace/ — fast capture, allowed to be messy and incomplete
# Promote to note/ only when cleaned and worth keeping.
# Run: Ctrl+Shift+B  or  F5  or  scripts/run-py.sh <this file>
# ===========================================================================

# ---------------------------------------------------------------------------
# Problem (paste or describe it here)
# ---------------------------------------------------------------------------
"""
**3.3.** Run the DFS-based topological ordering algorithm on the following graph. Whenever you have a choice of vertices to explore, always pick the one that is alphabetically first.

**Graph visualization:** ./dpv_3.3_graph.md

(a) Indicate the **pre** and **post** numbers of the nodes.
(b) What are the **sources** and **sinks** of the graph?
(c) What **topological ordering** is found by the algorithm?
(d) How many **topological orderings** does this graph have?

"""

# ---------------------------------------------------------------------------
# Pre-drill recall  (from memory only — no search, no docs)
# If you need to look something up, stop and create a blocker-learning.
# ---------------------------------------------------------------------------
"""
Recall:
  ...
"""

# ---------------------------------------------------------------------------
# Pseudocode
# ---------------------------------------------------------------------------
"""
1. ...
2. ...
"""

# ---------------------------------------------------------------------------
# Implementation
# ---------------------------------------------------------------------------

def solution(inp):
    pass


# ---------------------------------------------------------------------------
# Tests  — edit inputs/expected, then run the file to see PASS / FAIL
# ---------------------------------------------------------------------------
def _test(fn, inp, expected, label=""):
    """Pass inp as a tuple to unpack as multiple args, or a single value."""
    got = fn(*inp) if isinstance(inp, tuple) else fn(inp)
    status = "PASS" if got == expected else "FAIL"
    tag = f" [{label}]" if label else ""
    print(f"  {status}{tag}  got={got!r}  expected={expected!r}")


if __name__ == "__main__":
    _test(solution, "example_input", None, "basic")
    # Multi-arg example — pass inputs as a tuple:
    # _test(solution, ([1, 2, 3], 6), True, "basic")

# ---------------------------------------------------------------------------
# Attempt review
# ---------------------------------------------------------------------------
"""
What I got wrong:
  ...

Skill gap or follow-up learning:
  ...
"""



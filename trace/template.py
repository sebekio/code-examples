#!/usr/bin/env python3
# trace/ — fast capture, allowed to be messy and incomplete
# Promote to note/ only when cleaned and worth keeping.
# Run: Ctrl+Shift+B  or  F5  or  scripts/run-py.sh <this file>
# ===========================================================================

# ---------------------------------------------------------------------------
# Problem (paste or describe it here)
# ---------------------------------------------------------------------------
"""
Given ...

Returns ...

Constraints:
  ...
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



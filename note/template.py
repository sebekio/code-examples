#!/usr/bin/env python3
# note/ — cleaned, kept, understandable later
# Must be readable without context. Remove all trace-phase scaffolding.
# Run: Ctrl+Shift+B  or  F5  or  scripts/run-py.sh <this file>
# ===========================================================================

# ---------------------------------------------------------------------------
# Problem
# ---------------------------------------------------------------------------
"""
Given ...

Returns ...

Constraints:
  ...

Key insight:
  ...
"""

# ---------------------------------------------------------------------------
# Algorithm
# ---------------------------------------------------------------------------
"""
Approach: ...
Time:  O(?)
Space: O(?)
"""

# ---------------------------------------------------------------------------
# Implementation
# ---------------------------------------------------------------------------

def solution(inp):
    pass


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def _test(fn, inp, expected, label=""):
    """Pass inp as a tuple to unpack as multiple args, or a single value."""
    got = fn(*inp) if isinstance(inp, tuple) else fn(inp)
    status = "PASS" if got == expected else "FAIL"
    tag = f" [{label}]" if label else ""
    print(f"  {status}{tag}  got={got!r}  expected={expected!r}")


if __name__ == "__main__":
    _test(solution, "example_input", None, "basic")

# solution
# code-examples

A single-problem drill workspace. Fast capture in `trace/`, clean artifact in `note/`.

---

## Workflow

### 1 — Paste the problem

Copy a new trace file from the template:

```bash
cp trace/template.py trace/<topic>__<drill>__v1.py
```

Paste the problem statement into the `Problem` docstring at the top. Nothing else yet.

**Naming:** `{topic}__{drill}__vN.py` — e.g. `lis__dp1__v1.py`, `dijkstra__heap__v1.py`

---

### 2 — Work the problem

Fill in the file top-to-bottom:

1. **Pre-drill recall** — write what you remember about the approach. No searching, no docs. If you need to look something up, stop and create a blocker-learning instead.
2. **Pseudocode** — write the steps in plain words before touching `solution()`.
3. **Implementation** — fill in `solution()`. Keep it ugly if needed; this is `trace/`.

---

### 3 — Run the tests

Edit the `_test(...)` calls at the bottom with real inputs and expected outputs, then:

```
Ctrl+Shift+B        # run in terminal (default build task)
F5                  # run with debugger (set breakpoints freely)
```

Output is `PASS` or `FAIL` with `got=` / `expected=` on each line.

To add more cases:

```python
_test(solution, [1, 2, 3], 6, "basic")           # single arg
_test(solution, ([1, 2, 3], 6), True, "two args") # tuple unpacks as multiple args
```

Iterate until all cases pass.

---

### 4 — Call it done

When all tests pass, fill in the **Attempt review** block at the bottom:
- What you got wrong on the first try
- Any skill gap or follow-up learning to capture

The file stays in `trace/`. It is allowed to be messy. You are done.

---

### 5 — Polish and save as a note (optional)

If the problem is worth keeping as a clean reference:

```bash
cp trace/<file>.py note/<file>.py
```

Then clean `note/<file>.py`:
- Remove the pre-drill recall and pseudocode scaffolding
- Fill in **Algorithm**, **Time**, and **Space** clearly
- Keep only the final implementation and tests
- It must be readable without any context

If it's not worth keeping clean, leave it in `trace/` and move on.

---

## Python

Uses `/usr/bin/python3` (workspace container). No venv, no install step.

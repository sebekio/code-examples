# Goal

Understand data layout, function calls, loads, stores, and one bounds-style validity rule across C++, C, and RISC-V.

---

## Shared Concept

A cell stores one integer and a valid bit.

### Conceptual Explanation

A "cell" in this lab is a minimal stateful data structure. It models a single memory slot that can either be empty or hold one integer value. The "valid" bit tracks whether the stored value is meaningful (valid) or not (empty).

**Key systems concepts:**
- Memory layout: The cell struct shows how data and metadata (the valid bit) are packed together.
- State: The cell can be empty or full, and you must check the valid bit before reading.
- Invariants: You must never read the value unless valid is set.
- Interface: The cell exposes simple operations—init, set, get, clear—mirroring how real-world hardware or software registers work.

**Real-world analogy:**
Think of a hardware register or a cache line: it may contain a value, but you need a flag to know if the value is current/usable. This pattern appears in CPU caches, database cells, and network packet buffers.

**Check:** Can you describe what would go wrong if you ignored the valid bit and always read the value?

### Behavior

- Initialize empty
- Store one integer
- Read it back only if valid
- Clear it

---

## Why This is the Right First Lab

It is the smallest thing that still gives you state, memory layout, branches, and ABI exposure. It avoids allocation, growth, templates, iterators, and irrelevant noise.

---

## Files

- `cell.cpp` — C++ implementation (struct + free functions)
- `cell.c` — C implementation
- `cell_rv.s` — RISC-V hand-written assembly
- `test_cell.cpp` — C++ tests
- `test_cell.c` — C tests
- `test_cell_rv.c` — C harness that calls the RISC-V assembly functions
- `Makefile`

---

## Data Model

```c
struct Cell {
    int value;
    int valid;
};
```

---

## Operations in All Three Layers

- `init(Cell*)`
- `set(Cell*, int)`
- `get(const Cell*, int* out)` // return 1 on success, 0 if empty
- `clear(Cell*)`

---

## Exact Progression



### Step 1: C++

Write the cleanest, most idiomatic C++ version:
- Use references (`Cell&`, `const Cell&`) in all function signatures to express intent and safety.
- Use `const` wherever possible for read-only access.
- No classes, templates, or advanced C++ features—just a plain struct and free functions.
- Avoid heap allocation and keep all state explicit.

**Example signatures:**
```cpp
void init(Cell& c);
void set(Cell& c, int val);
int get(const Cell& c, int& out);
void clear(Cell& c);
```

#### Why?
This approach demonstrates how C++ can provide safer, clearer interfaces (via references and const-correctness) while still exposing the underlying machine model. It also makes the differences with C explicit.

#### What to Learn:
How the compiler lowers idiomatic C++ code using references, and how this differs from C pointer-based code. Observe how references are implemented under the hood (as pointers), but with added type safety and clarity.

---



### Step 2: C

Port the C++ code directly to C, preserving all behavior, but use idiomatic C signatures:
- Use pointers for all struct arguments and outputs (e.g., `Cell*`, `const Cell*`).
- No references or const-correctness on arguments (except via `const` pointer types).
- Keep the struct and function names identical for easy comparison.

**Example signatures:**
```c
void init(Cell* c);
void set(Cell* c, int val);
int get(const Cell* c, int* out);
void clear(Cell* c);
```

#### Why?
This highlights the differences in expressiveness and safety between C++ (references, const) and C (pointers only). It also makes the ABI and calling convention differences visible.

#### What to Compare:
Generated assembly for C++ (using references) vs C (using pointers) at `-O0` and `-O2`.
- For this lab, they should be very similar. That is the point.

---

### Step 3: RISC-V
Handwrite only these four functions in RISC-V assembly:
- `init`
- `set`
- `get`
- `clear`

#### Notes:
Do not handwrite the whole program. Use a tiny C test harness to call the assembly functions. That keeps the assembly task surgical.

#### What the RISC-V Code Must Force You to Understand:
- Struct field offsets
- Argument registers
- Return register
- Load/store instructions
- Conditional branch for valid check
- How a pointer argument is dereferenced

---

## Success Criteria
You can point to the exact instruction that:
- Writes `value`
- Writes `valid`
- Checks `valid`
- Writes output value
- Returns success or failure

---

## Test Cases
- `init` makes cell empty
- `get` after `init` fails
- `set` then `get` succeeds and returns stored value
- `clear` after `set` makes `get` fail
- `set` twice returns latest value

---

## Build Matrix
- **C++ Native**: Debug and optimized
- **C Native**: Debug and optimized
- **RISC-V**: Debug-ish and optimized enough to inspect

---

## Deliverables
One page of notes with:
- Struct offsets
- Calling convention used
- Assembly branch path for `get` success/failure
- Differences between C++ and C output
- What changed between compiler output and your handwritten RISC-V
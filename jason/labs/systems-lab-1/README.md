# Goal
Understand data layout, function calls, loads, stores, and one bounds-style validity rule across C++, C, and RISC-V.

---

## Shared Concept
A cell stores one integer and a valid bit.

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
- `cpp/cell.cpp`
- `c/cell.c`
- `asm/cell_rv.s`
- `tests/test_cell.cpp`
- `tests/test_cell.c`
- `tests/test_cell_rv.S` or a tiny C harness that calls the assembly
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
Write the cleanest possible C++ version.
- No classes.
- No templates.
- Just the same struct and free functions.

#### Why?
This prevents C++ features from hiding the machine model.

#### What to Learn:
How the compiler lowers simple procedural code from C++.

---

### Step 2: C
Port it directly to C with identical behavior and nearly identical signatures.

#### Why?
Now you see what C++ added or did not add.

#### What to Compare:
Generated assembly for C++ vs C at `-O0` and `-O2`.
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
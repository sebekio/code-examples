

1. docker volume use case
2. precise definition of docker volume instructions, os host, file systems stuff
3. how docker works on mac
4. why --mount option is preferred over -v in modern docker installations.
5. How to write a class in Cpp.
6. when do I need a header and when can I not use a header?
7. Why docker desktop needed an emulator on my linux machine.
8. how to clear integer value.
9. fact what does int val = {}; do
10. return by reference best practices
11. entire makefile must be valid before any target can be compiled.
12. Be able to fully explain this error /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/13/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
13. proper way to instantiate object in cpp
14. The proper way to instantiate an object in C++ depends on the desired object lifetime and memory management. The two primary methods are creating objects with automatic storage duration (on the stack) or dynamic storage duration (on the heap).
15. how to instantiate a struct

16. analyze these mistakes
init() — uses -> on a non-pointer local, returns a pointer to a local (undefined behavior), and sets valid=1 instead of 0 (init = empty)
get() — does out = 1 / out = 0 (assigns to the pointer itself, not through it); should be *out = value and return 1/0 based on valid
set() — takes const Cell* but mutates the struct; missing * on out assignments; wrong signature (spec: set(Cell*, int))
clear() — takes const Cell* but mutates; declares int return but has no return statement
main() — calls init() which no longer takes a pointer correctly


Pointer & dereference errors

Using -> on a non-pointer local — -> dereferences a pointer; if your variable is a plain Cell cell (not Cell* c), you must use . to access its members, not ->.

Returning a pointer to a local variable — a local variable lives on the stack and is destroyed when the function returns; any pointer to it becomes a dangling pointer, causing undefined behavior when dereferenced.

Assigning to a pointer instead of through it (out = 1 vs *out = 1) — out = 1 reseats the pointer itself (changes where it points); *out = 1 writes through the pointer to the memory it addresses, which is what callers expect.

const correctness

Marking a mutating pointer const Cell* — const Cell* means "pointer to a Cell you promise not to modify"; if your function writes to c->value or c->valid, the compiler will reject it; only use const Cell* for read-only operations like get.
Return type discipline

Declaring a non-void return type but omitting return — a function declared int clear(...) that falls off the end without a return statement compiles with a warning but produces undefined behavior at runtime; if you don't need a return value, declare it void.

Returning a raw value instead of a success/failure code — get should return 1 (success) or 0 (failure) as a status, not the stored integer value; the value is communicated through the output pointer *out, keeping the return channel reserved for status.

Memory model / lifetime

init() set valid = 1 instead of 0 — the invariant is that init makes the cell empty; valid=1 means "there is a value here," which is the opposite of the initial state; confusing initialized-memory with valid-data is a classic logic bug.

Stack vs heap confusion in a factory function — returning Cell cell (stack) from a function that the caller treats as a live object is wrong; either let the caller own the stack allocation and pass Cell* in, or allocate on the heap with new/malloc (and then manage lifetime explicitly).

Signature discipline

Adding extra parameters not in the spec (int* out on set and clear) — set and clear have no reason to return data to the caller; adding a spurious out parameter clutters the API and signals that you haven't reasoned about which functions are queries vs commands.

Calling init() with no arguments when it requires Cell* — every function that operates on the cell needs a pointer to which cell; forgetting &cell means the function has no target to operate on and the compiler will error on a type mismatch.


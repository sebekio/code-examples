#include "cell.h"

void init(Cell* c) {
    c->value = 0;
    c->valid = 0;
}

void set(Cell* c, int value) {
    c->value = value;
    c->valid = 1;
}

int get(const Cell* c, int* value) {
    if (!c->valid) {
        return 0;
    }
    *value = c->value;
    return 1;
}

void clear(Cell* c) {
    c->value = 0;
    c->valid = 0;
}

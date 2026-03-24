struct Cell {
    int value;
    int valid;
};

void init(Cell* c) {
    c->value = 0;
    c->valid = 0;
}

void set(Cell* c, int val) {
    c->value = val;
    c->valid = 1;
}


int get(const Cell* c, int* out) {
    if (!c->valid) {
        return 0;
    }
    *out = c->value;
    return 1;
}

void clear(Cell* c) {
    c->value = 0;
    c->valid = 0;
}

int main() {
    return 0;
}
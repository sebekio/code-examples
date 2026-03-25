struct Cell {
    int value;
    int valid;
};

void init(Cell& c);
void set(Cell& c, int val);
int get(const Cell& c, int& value);
void clear(Cell& c);

typedef struct {
    int valid;
    int value;
} Cell;


void init(Cell* c);
void set(Cell* c, int value);
int get(const Cell* c, int* value);
void clear(Cell* c);
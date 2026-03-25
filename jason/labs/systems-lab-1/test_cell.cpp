#include "cell.hpp"
#include <cassert>

void test_Cell_Is_Empty_After_Init(const Cell& c) {
    assert(c.valid == 0);
    assert(c.value == 0);
}

void test_Cell_Get_After_Init_Returns_Zero(const Cell& c) {
    int val;
    assert(get(c, val) == 0);
    assert(val == 0);
    assert(c.valid == 0);
}

void test_Cell_Set_Then_Get(Cell& c) {
    int expected = 33;
    set(c, expected);
    int actual;
    assert(get(c, actual) == 1);
    assert(actual == expected);
    assert(c.valid == 1);
}

void test_Cell_Set_Then_Clear_Then_Get_Returns_Zero(Cell& c) {
    set(c, 1337);
    clear(c);
    int clearedValue;
    assert(get(c, clearedValue) == 0);
    assert(c.valid == 0);
}

void test_Cell_Set_Twice_Then_Get_Matches_Second(Cell& c) {
    set(c, 1);
    int second = 2;
    set(c, second);
    assert(get(c, second) == 1);
    assert(second == 2);
    assert(c.valid == 1);
}

int main()
{
    Cell cell;
    init(cell);
    test_Cell_Is_Empty_After_Init(cell);
    test_Cell_Get_After_Init_Returns_Zero(cell);
    test_Cell_Set_Then_Get(cell);
    test_Cell_Set_Then_Clear_Then_Get_Returns_Zero(cell);
    test_Cell_Set_Twice_Then_Get_Matches_Second(cell);
}
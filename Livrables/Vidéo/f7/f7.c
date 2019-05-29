#include <stdio.h>

int foo(const int a, const int d) {
    int b = a + d;
    if (b > d) {
        return 10;
    }

    return b;
}

int main(void)
{
    return 0;
}
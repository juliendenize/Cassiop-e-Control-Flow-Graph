#include <stdio.h>
#include <stdlib.h>

int foo1 (int a) {
    return a % 2;
}

int foo2 () {
    return rand();
}

int main (int argc, char** argv) {
    int a;
    if (argc > 1) {
        a = (int) *argv[1];
    }

    a = 2 * a;

    printf("%d", a);
}
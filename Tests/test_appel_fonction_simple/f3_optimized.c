#include <stdio.h>

int foo1 (int a) {
    return a % 50;
}

int foo2 (int a) {
    return a % 10;
}

int main (int argc, char** argv) {
    int a;
    if (argc > 1) {
        a = (int) *argv[1];
    }

    a = foo1(a);

    printf("%d", a);
}
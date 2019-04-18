#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv) {
    int a;
    if (argc > 1) {
        a = (int) *argv[1];
    }

    a = 2 * a;

    int b = a % 2;

    int c = rand();

    printf("%d", a);
}
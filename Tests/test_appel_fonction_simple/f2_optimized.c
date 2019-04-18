#include <stdio.h>

int main (int argc, char** argv) {
    int a;
    if (argc > 1) {
        a = (int) *argv[1] % 2;
    }
    printf("%d", a);
}
#include <stdio.h>

int main (int argc, char** argv) {
    int a;
    if (argc > 1) {
        a = (int) *argv[1] % 2;
    }
    if (a >= 2) {
        while (a < 100) {
            a ++;
        }
    }
    printf("%d", a);
}
#include <stdio.h>

int foo () {
    int a = 1;
    if (a == 1) {
        a ++;
    }
    return a;
}

int main (int argc, char** argv) {
    int a;
    a = foo();
    printf("%d", a);
}
#include <stdio.h>

int foo(int a) {
    if (a > 0) return -a;
    return a;
}

int yolo(int c) {
    return c;
}

int main(int argc, char *argv[]) {
    int b = 3;
    if (foo(yolo(b)) > 3) {
        printf("Large\n");
    }
    else {
        printf("Small\n");
    }
    return 0;
}
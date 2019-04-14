#include <stdio.h>

int foo(int a) {
    if (a > 0) return -a;
    return a;
}

int main(int argc, char *argv[]) {
    int b = 3;
    while(b == 3) {
        if(b == 3) {
            continue;
        }
        if( b == 4) {
            printf("hey\n");
        }
        b = 6;
    }
    if (foo(b) > 3) {
        printf("Large\n");
    }
    else {
        printf("Small\n");
    }
    return 0;
}
#include <stdio.h>
#define N 1
int f (int a) {
    return a;
}

int main() {
    int a = 0;
    if( a == 3) {
        if(a == 1) {
            if (a == 2) {
                a = 3;
            }
        }
        a = 4;
    }
    if(a == 0) {
        if(a == 1 & a == 2) {
            a = 3;
        }
        a = 4;
    }
    if(N) {
        a = 3;
    }
    return 1;
    a++;
    return 0;
}
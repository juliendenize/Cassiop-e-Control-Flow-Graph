#include <stdio.h>

int foo (int a) {
    return 100;
}

int main() {
    int a = 50;
    int b = 90;
    printf("je suis la fonction main");
    printf("%d", (a + b));    
    return 0;
}
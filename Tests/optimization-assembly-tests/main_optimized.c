#include <stdio.h>

int foo(int a) {
    return a+1;
}

int main() {
    int a = 0;
    scanf("%d", &a);
    if(a == 20) {
        printf("%d", a);
    }    
    printf("%d", a);
    return 0;
}
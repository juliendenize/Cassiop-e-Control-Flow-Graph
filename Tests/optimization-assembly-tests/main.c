#include <stdio.h>

int foo(int a) {
    return 0;
}

int main() {
    int a = 0;
    scanf("%d", &a);
    if(a > 15) {
        if(a < 30) {
            if (a == 20) {
                printf("%d", a);
            }
        }
    }
    
    printf("%d", a);
    return 0;
}
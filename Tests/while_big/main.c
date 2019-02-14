#include <stdio.h>

int main() {
    int a = 0;
    
    while(a < 1000) {
        if(a % 2 == 0) {
            a++;
        }
        else {
            a+=2;
        }
    }

    return 0;
}
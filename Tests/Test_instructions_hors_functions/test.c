#include <stdio.h>

int s = 4;

/* while(s != 3) {
    printf("bonjour");
    s = 2;
}

while(s == 5) {
    printf("au revoir");
} */


int foo(int a) {
    if (a > 0) return -a;
    return a;
}

int yolo(int c) {
    return c;
}

int main(int argc, char *argv[]) {
    int b = s;
    if (foo(yolo(b)) > 3) {
        printf("Large\n");
    }
    else {
        printf("Small\n");
    }
    return 0;
}
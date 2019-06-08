/**int foo2(const int* a, const unsigned int d) {
    int* b = malloc(sizeof(int));

    if (b == a) {
        int d = 5;
        d = a + d;
        return 11;
    }

    return b;
}**/

int foo(const int a, const unsigned int d) {
    int b = 0;
    int w = a + 10;

    b = a + 6;
    if (b < a + 10) {
        printf("hello world");
        if (d < 10) {
            w += a;
        } else {
            printf("yolo");
        }
        b = 6;
    } else if (d > 10) {
        b = 92;
    } else {
        w = 6;
        b = a - 10;
    }

    return b;
}

int main(void)
{
    return 0;
}
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
    if (a + 4 < b) {
        w = 0;
        if (d < 10) {
            w += a;
        } else {
            w = 1;
        }
        if(a + 7 < b) {
            w = 3;
        }
        b = 6;
    } else if (d > 10) {
        b = 92;
    } else {
        w = 6;
        b = a - 10;
    }
    b = 90;

    return b;
}

int main(void)
{
    return 0;
}
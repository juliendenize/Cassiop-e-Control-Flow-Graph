int foo2(const int* a, const unsigned int d) {
    int* b = malloc(sizeof(int));

    if (b == a) {
        int d = 5;
        d = a + d;
        return 11;
    }

    return b;
}

int foo(const int a, const unsigned int d) {
    int b = a + d;

    if (b < a) {
        return 11;
    }

    return b;
}

int main(void)
{
    return 0;
}
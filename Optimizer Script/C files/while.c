int foo2(const int* a, const unsigned int d) {
    for(int b = a + d; b < a; b++) {
        if (b < a + 10) {
            return 11;
        }
        else if (b > a) {
            return 10;
        } else {
            return 9;
        }
    }

    return 0;
}

int foo(const int a, const int d) {
    int b = a + d;

    while(b < a) {
        if (b < a + 10) {
            return 11;
        }
        return 10;
    }

    return b;
}

int main(void)
{
    return 0;
}
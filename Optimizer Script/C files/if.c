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
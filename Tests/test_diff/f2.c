int foo(const int a) {
    int b = a;

    if (b > 0 && b < 100 && b % 11 == 0)
    {
        return 11;
    }
    return 0;
}

int main(void)
{
        int x;
        if (x > 0 && x < 100 && x % 11 == 0)
        {
            return 11;

        }
        return 0;
}
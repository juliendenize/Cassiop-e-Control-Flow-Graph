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
    int x;
    if (x > 0)
    {
        if(x < 100)
        {
            if (x % 11 == 0)
            {
                    return 11;
            }
        }
    }
    return 0;
}
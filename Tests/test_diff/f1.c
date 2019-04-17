int foo(const int a) {
    int b = a;

    if (b > 0)
    {
        if(b < 100)
        {
            if (b % 11 == 0)
            {
                    return 11;
            }
        }
    }
    return 0;
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
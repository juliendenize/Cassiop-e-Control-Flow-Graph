# 1 "./C files/while.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 31 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 32 "<command-line>" 2
# 1 "./C files/while.c"
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

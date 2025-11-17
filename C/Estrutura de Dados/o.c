#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 10;
    int *xptr = &x;
    *xptr = 20;
    printf("Value of x: %d\n", x);
    return 0;
}
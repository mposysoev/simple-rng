#include "stdio.h"

int main()
{
    int x = 5;
    int* y = &x;
    printf("%f \n", (double)(int)y / (double)2147483647);
    return 0;
}

#include <stdio.h>
int max(int x, int y)
{
    if (x > y)
    {
        return x;
    }
    else
    {
        return y;
    }
}
int knapSac(int W, int profit[], int wt[], int n)
{
    int i, w;
    int l[100];
    int table[n + 1][W + 1];
    for (i = 0; i < n; i++)
    {
        printf("Object %d has %2d weight and %d profit\n", i + 1, wt[i], profit[i]);
    }
    printf("\noutput is:\n");
    printf("\ni/w|");
    // printf("_");
    for (w = 0; w <= W; w++)
    {
        printf("%2d |", w);
    }
    printf("\n   -");
    for (w = 0; w <= W; w++)
    {
        printf("----");
    }
    printf("\n");
    for (i = 0; i <= n; i++)
    {
        printf("%2d |", i);
        for (w = 0; w <= W; w++)
        {

            if (i == 0 || w == 0)
            {

                table[i][w] = 0;
                printf("%2d |", table[i][w]);
            }
            else if (w >= wt[i - 1])
            {
                table[i][w] = max(table[i - 1][w], (table[i - 1][w - wt[i - 1]]) + profit[i - 1]);
                printf("%2d |", table[i][w]);
            }
            else
            {
                table[i][w] = table[i - 1][w];
                printf("%2d |", table[i][w]);
            }
        }
        printf("\n");
    }
    printf("\nFinal result is :%d\n", table[n][W]);
    printf("It Takes Weights:\n");
    for (i = n - 1; i >= 0; i--)
    {
        for (w = 0; w <= W; w++)
        {
            if (table[n][W] == table[i][w])
            {
                /* code */ break;
            }
            if (w == W)
            {
                table[n][W] -= profit[i];
                printf("Object %d is selected\n", i + 1);
                /* code */
            }
        }
    }

    printf("\n");
    // return table[i][w];
}
int main()
{
    int W = 10;
    int profit[] = {1, 2, 3, 6, 7};
    int wt[] = {2, 3, 4, 5, 8};
    int n = sizeof(wt) / sizeof(wt[0]);

    knapSac(W, profit, wt, n);
    // printf("%d",res);
}

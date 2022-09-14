#include<stdio.h>
#include<conio.h>
int maxi(int x,int y)
{
    return (x>y)?x:y;
}
void main()
{
    int weight=8;
    int p[]={1,2,5,6};
    int wt[]={2,3,4,5};
    int n=sizeof(wt)/sizeof(wt[0]);
    int i,w;
    int t[n+1][weight+1];
    for(i=0;i<=n;i++)
    {
        for(w=0;w<=weight;w++)
        {
            if(i==0 || w==0)
            {
                t[i][w]=0;
            }
            else if(w>=wt[i-1])
            {
                t[i][w]=maxi(t[i-1][w],t[i-1][w-wt[i-1]]+p[i-1]);
            }
            else
            {
                t[i][w]=t[i-1][w];
            }
        }
    }
    for(i=0;i<=n;i++)
    {
        for(w=0;w<=weight;w++)
        {
            printf(" %d ",t[i][w]);
        }
        printf("\n");
    }
}
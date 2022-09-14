#include<stdio.h>
#include<stdlib.h>

int main(){
    int a[100],min,i,n,swap;
    printf("enter how many numbers you want to enter:");
    scanf("%d",&n);
    srand(time(0));
    printf("That %d Random Numbers are:\n",n);
    for (i = 0; i < n; i++)
    {
       // printf("%d",rand());
        a[i]=rand();
        printf("%d\n",a[i]);
        
    }
    for ( i = 0; i < n-1; i++)
    {
        min=i;
        for (int j = i+1; j< n; j++)
        {
            if(a[min]>a[j]){
                min=j;
                
            }
        
        }
        if(min!=i){
                swap=a[i];
                a[i]=a[min];
                a[min]=swap;
            }
            
        
        }
        printf("Sorted Array is:\n");
    for ( i = 0; i < n; i++)
    {
    printf("%d\n",a[i]);
    }
    
    
}

#include<stdio.h>
#include<stdlib.h>
int bs(int x,int n,int b[]){
    int low,high;
    low=0;
    high=n-1;
int mid=(low+high)/2;
//printf("%d",mid);

    /* code */


if (x==b[mid])
{
    printf("Elemenet is present at %d position",mid);
    return 0;
    /* code */
}
else if (x>b[mid])
{
    for ( low = mid+1; low <= high; low++)
    {
    
    if (x==b[low])
    {
        /* code */printf("Elemenet is present at %d position",low);
        return 0;
        break;
    }
    }
    
}
else if (x<b[mid])
{
    for ( high = mid-1; high >= low; high--)
    {
    
    if (x==b[high])
    {
        /* code */printf("Elemenet is present at %d position",high);
        return 0;
        break;

    }
    
}

}    
return -1;
    
}

int main(){
    int b[100],min,i,n,swap,x,res;
    printf("enter how many numbers you want to enter:");
    scanf("%d",&n);
    printf("Enter that numbers:");
    for ( i = 0; i < n; i++)
    {
        scanf("%d",&b[i]);
        
    }

for ( i = 0; i < n-1; i++)
    {
        min=i;
        for (int j = i+1; j< n; j++)
        {
            if(b[min]>b[j]){
                min=j;
                
            }
        
        }
        if(min!=i){
                swap=b[i];
                b[i]=b[min];
                b[min]=swap;
            }
            
        
        }
     printf("Sorted Array is:\n");
    for ( i = 0; i < n; i++)
    {
    printf("%d\n",b[i]);
    }   
   printf("Enter the number to search:");    
    scanf("%d",&x);
res=bs(x,n,b);

if (res==-1){
printf("element is not present");
}

}
    
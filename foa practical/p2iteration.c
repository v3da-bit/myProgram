#include<stdio.h> 
#include <time.h>

int f1(int n)    
{    
 int i,fact=1;    
    for(i=1;i<=n;i++){    
      fact=fact*i;    
  }    
  return fact;
}   
int main(){
      
 clock_t t;
    int n,result;
    	t = clock();
    printf("Enter a number: ");    
    scanf("%d",&n);  
	result=f1(n);
	t = clock() - t;
	double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("factorial is: %d",result);

	printf("\nfun() took %f milli seconds to execute \n", time_taken*1000);
	return 0;
}
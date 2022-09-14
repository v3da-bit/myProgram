#include<stdio.h>
#include<time.h>
#include<ctype.h>

long long int f1(long long int n){
    long long int sum;
    /*for (int i = 0; i < 100; i++)
    {
        printf("hello");
         code 
    }*/
    
    if(n==1){
        return 1;
    }
    else{
        sum = n*f1(n-1);
    }
return sum;

}   
 
long long int main(){
    
    clock_t t;
    long long int sum,n,result;
    printf("enter the number:");
    scanf("%lld",&n);
	t = clock();
	result=f1(n);
	t = clock() - t;
	double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("factorial is: %lld",result);
    	printf("\nfun() took %f milli seconds to execute \n", time_taken*100);
        printf("%lld",n);
        //printf("length %d",strlen((char)sum));
        return 0;
}

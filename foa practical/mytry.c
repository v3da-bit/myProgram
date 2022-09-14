#include<stdio.h>
int fun(int l){
if (l==1)
{
 
    return 0;
}
return 1;
}
void main(){
    int a,l=0;
    a=fun(l);
    printf("%d",a);
}
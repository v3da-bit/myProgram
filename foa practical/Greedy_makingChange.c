#include<stdio.h>
int main(){
int d[]={2,4,13};
int s[100]={0};
int target;
printf("enter target:");
scanf("%d",&target);
int i=(sizeof(d)/sizeof(d[0]))-1;
//printf("%d",i);
int j=0;
 while(target>0){
        while(d[i]<=target && i>=0){
            target-=d[i];
            s[j]=d[i];
            j++;
        }
        if(target==0 || d[0]>target){
            break;
        }
        else if(target<d[i] && i>=0)
            i--;
    }
    //printf("%d",j);
printf("Simplified Denominators are:\n");
for(j=0;j<(sizeof(s)/sizeof(s[0]))-1;j++){
    if(s[j]!=0){
printf("%d ",s[j]);
    }
}
printf("\nthe target becomes 0 or less than the lowest denominator in the array so it can't be further simplified");
          


}
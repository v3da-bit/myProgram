#include<stdio.h>

int mergeSort(int a[100],int temp[100],int lb,int ub)
{
    if(lb>=ub){return 0;}
    int mid=(lb+ub)/2;
    mergeSort(a,temp,lb,mid);
    mergeSort(a,temp,mid+1,ub);
    merge(a,temp,lb,mid,ub);


}
int merge(int a[100],int temp[100],int lb,int mid,int ub){
    int i;
    int j;
    int k;

for(i=lb,j=mid+1,k=lb;i<=mid && j<=ub;k++){
if(a[i]>a[j]){
temp[k]=a[j];
j++;
}
else if(a[i]<a[j]){
    temp[k]=a[i];
    i++;
}
}
while(i<=mid){
    temp[k]=a[i];
    i++;
    k++;
}
while(j<=ub){
    temp[k]=a[j];
    j++;
    k++;
}
for(i=lb;i<=ub;i++ )
    a[i]=temp[i];
}

int main(){
int a[]={20,10,5,6,4,11,15};
int lb=0;int ub=(sizeof(a)/sizeof(a[0]))-1;int temp[100];
mergeSort(a,temp,lb,ub);

printf("Sorted array is:");
for(int i=lb;i<=ub;i++)
printf("%d  ",a[i]);
}

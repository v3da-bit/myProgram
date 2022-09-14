import math
'''n=5
l=int(n*(n+1)/2)
print("Sum is:",l)
'''

'''
n=int(input("enter how many numbers:"))
sum=0
for i in range(n):
    i=int(input("enter that numbers"))
    sum=sum+i
print("sum is :",sum)
'''

'''
n=5
fac=1
for i in range(1,n+1):
    fac=fac*i
print("factorial is:",fac)    
'''

'''
n=int(input("enter range :"))
f1=0
f2=1

print(f1)
print(f2)
    
for i in range(n-1):
    t=f1+f2
    f1=f2
    f2=t
    print(f2)
    '''

'''
n=input("enter number:")
print(type(n))
print(int(n[ : :-1]))
'''

'''
   
n=int(input("enter number:"))
o="prime"
m="not prime"
l=str()
if n>2:
    for i in range(2,n):
        print(i)
        if n%i==0 :
            l=m
            break
        else:
            l=o
elif n==2:
    l=o
else:
    l=m
        
if l==m:
    print(l)
elif l==o:
    print(l)
'''

'''
n=int(input("enter range:"))
b=[]
for i in range(0,n):
    a=int(input("enter that number:"))
    if a%6==0:
        b.append(a)
print("divisible by 6 and even are:",b)
'''

'''
a=input("enter the number")
temp=0
for i in a:
    temp=temp+(int(i)**3)
if temp==int(a):
    print("armstrong") 
else:
    print("not armstrong")
'''

'''a=input("enter number:")

b=a[::-1]
if int(b)==int(a):
    print("pelindrome")
else:
    print("Not pelindrome")'''


'''a=5
for i in range(0,a):
    #print(i)
    for j in range(1,i+2):
        print(j,end=" ")
    print("")
'''

'''
a=5
for i in range(0,a):
    #print(i)
    for j in range(i,a):
        print("*",end=" ")
    print("")
   '''

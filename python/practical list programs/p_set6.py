
'''
l=[1,2,3,5,6,7,8,9,11,13,15]
def prime(n):
    if n==1 or n==0:
        return False
    elif n==2:
        return True
    elif n>2:
        flag=0
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False
result=filter(prime,l)
print("Prime numbers are:")
for i in result:
    print(i)
'''




'''
def prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
    else:
        return 1
print(list(filter(prime,range(3,12))))'''

# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools
from itertools import count

# importing operator for operator functions
import operator
from queue import PriorityQueue
import re
import rlcompleter
from tkinter import N

# initializing list
list = [1, 3, 5, 6, 2, 1]

print("Sum of elements are:",functools.reduce(operator.add,list))       
 

'''
list=[2,3,8,4,6]
def max(a,b):
    
    if a>b:
        return a
    else:
        return b
    
print("maximum is:",functools.reduce(max,list))
'''

'''
def fun(n):
    while n>0:
        r=n%10
        sum=sum+(r*r*r)
        r=n//10
    return sum
   
num=[153]
res=map(fun,num)
print(list(res))
'''

# Python program to demonstrate working
# of map.

# Return double of n
'''def fun(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+(r*r*r)
        n=n//10
    return sum
# We double all numbers using map()
nums = [153]
temp=nums
result = map(fun, temp)
if list(result) ==nums:
    print("armstrong")
else:
    print("not armstrong")
'''

'''
def square(n):
    return n*n
def cube(n):
    return n*n*n 
a=[2,3,4]
flag=0
if flag==0:
   res=map(square,a)
   print(list(res))
   flag=1
if flag==1:
    res=map(cube,a)
    print(list(res))
'''

'''
#1
def cube(n):
    return n*n*n
l1=[2,3,4]
res=map(cube,l1)
l2= list(res)
print(l2)

x=lambda a:a*a*a
l1=[1,2,3]
res=map(x,l1)
print(list(res))

l1=[1,2,3]
newlist = [x*x*x for x in l1]
print(newlist)

#2
def degToF(n):
    f=(n * (9/5)) + 32
    return f
n=[10,21]
res=map(degToF,n)
print("Fahrenheat values are:",list(res))

x=lambda a:(a * (9/5)) + 32
n1=[10,11]
res=map(x,n1)
print("Fahrenheat values are:",list(res))

n2=[11,12]
new=[(x*(9/2)+32) for x in n2] 
print("Fahrenheat values are:",new)

#3
l=[-1,0,1,2]
def pos(n):
    l1=[]
    if n>0:
        l1.append(n)
    return l1
res=map(pos,l)
print(list(res))

li=[-1,0,1,2]
l1=[]
x=lambda x:x if(x>0) else []
res1=map(x,li)
print(list(res1))

list=[-2,0,2,3]
l1=[]
res=[x for x in list if x>0 ]
print(res)

#4
l=[1,'a','b',2]
l1=[]
def alpha(n):
    if type(n)==type(str()):
       return n
    else:
        return []
res=map(alpha,l)
print(list(res))

x=lambda x:x if type(x)==type(str()) else []
res1=map(x,l)
print(list(res1))

res=[x for x in l if type(x)==type(str())]
print(list(res))
'''


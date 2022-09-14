'''
a=["a","b","c","d"]
b=[1,2,3,4,5,6]
a.append(b)
print(a)
print(len(a))
print(a.pop(0))
a.remove(b)
print(a)
'''

'''
a=["a","b","c","d"]
a.append("z")
print(a)
'''


'''a=[]
b=[]
n=int(input("Enter How many elements you want to enter:"))

for i in range(0,n):
    c=int(input("enter values:"))
    a.append(c)
print(a)
b=a[::-1]
print(b)
if a==b:
    print("pelindrome")
else:
    print("Not pelindrome")
'''

'''a=[]
n=int(input("Enter How many strings you want to enter:"))

for i in range(0,n):
    c=input("enter strings:")
    a.append(c)
print(a)
'''

'''
from itertools import count
from re import I


a=[2]

n=int(input("enter the range:"))
m="prime"
o="not prime"
l=str()  
for i in range(2,n):
    #print(i)
    for x in range(2,i):
        #print(x)
            if i%x==0:
                l=o
                break
            else:
                l=m
    if l==m:
        if a.count(i)<1:
            a.append(i)
    elif n%i!=0:
        if a.count(n)<1:
           a.append(n)
        
    

print(a)
'''

'''a=["ved","aba","a","aaa","b","abcda","bcdab"]
b=[]
#print(type(a[0]))
#print(a[0][len(a[0])-1:len(a[0])-2:-1])
#print(len(a[2]))
for i in range(len(a)):
    if len(a[i])>=2:
        if a[i][0:1:1]==a[i][len(a[i])-1:len(a[i])-2:-1]:
                b.append(a[i])
print(len(b))
   '''

'''a=[1,1,2,"a","a","b"]
print(set(a))'''


        

         



    

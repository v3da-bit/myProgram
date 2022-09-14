#practical set-2
'''a=int(input("enter the number:"))
if a%2==0 :
    print(a," is even")
else:
    print(a," is odd")'''

'''a=int(input("enter the number:"))
if a<0:
    print("negative")
elif a>0:
    print("positive")
else:
    print("zero")'''

'''a=int(input("enter 1st root"))
b=int(input("enter 2nd root"))
c=int(input("enter 3rd root"))


r=b*b-(4*a*c)

if r>=0:
    print(a,b,c,"are real roots")
else:
    
    print(a,b,c,"are not real")'''

'''l=['a','e','i','o','u']
e=str(input("enter the alphabet:"))
if e in l:
    print(e,"is vowel")
else:
    print(e,"is consonent")'''

'''a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
c=int(input("enter 3rd no:"))

if a>b:
    if a>c:
        print(a,"is max")
    elif c>a:
        print(c,"is max")
elif b>a:
    if b>c:
        print(b,"is max")
    elif c>b:
        print(c,"is max")'''

'''d=input("enter the degree:")
e=int(input("enter experience in years:"))
a=["B.E.","M.E."]
s=[30000,40000,50000,60000]
if d == a[0] :
    if e < 5 and e>=0:
        print("salary is",s[0])
    else:
        print("salary is",s[1])
elif d == a[1] :
    if e<5 and e>=0:
        print("salary is",s[2])
    else:
        print("salary is",s[3])
else:
    print("Invalid Degree")'''






'''a=input("Enter Input:")
if a.isdigit():
    a=int()
    print(type(a))
elif a.isalpha():
    
    print("a is character")
else:
    print("a is special symbol")'''
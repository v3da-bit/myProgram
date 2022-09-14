x=input("enter the string:")
a=input("enter the first char:")
b=input("enter second char:")
y=x.rfind(a)
z=x.rfind(b)
'''for a,b in x:
    print(y,z)'''
def f1():
    print("true")
def f2():
    print("false")

if a and b in x:
        if y < z:
            f1()
        else:
            f2()
else:
    print("not in it")
        
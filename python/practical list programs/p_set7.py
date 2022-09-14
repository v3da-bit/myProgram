'''
f=open("D:\my programs\python\practical list programs\hello.txt","r")
print(f.read())
f1=open("D:\my programs\python\practical list programs\hello.txt","r")
print(f1.readline())
f2=open("D:\my programs\python\practical list programs\hello.txt","r")
print(f2.readlines())'''

#f=open("D:\my programs\python\practical list programs\hello.txt","a")
#print(len(f.readlines()))
#f.write("this is new line")
#f.close()

'''
f=open("D:\my programs\python\practical list programs/num.txt","r")
f1=open("D:\my programs\python\practical list programs/cube.txt","w")
f1.write("Number Imported are:")
for i in f:
    f1.write(i)
    #print(i)
f1.close()
f.close()
f1=open("D:\my programs\python\practical list programs/cube.txt","a")
f1.write("addition of 2 paired numbers are:")
#print("addition of 2 paired numbers are:")
f=open("D:\my programs\python\practical list programs/num.txt","r")

for i in f:
    sum=0
    a=int(i)
    while a>0:
        r=a%10
        sum=sum+r
        
        a=a//10
        
    f1.write(str(sum)+"\n")
f1.close()
f.close()
f=open("D:\my programs\python\practical list programs/num.txt","r")
f1=open("D:\my programs\python\practical list programs/cube.txt","a")
f1.write("Multiplication of that numbers are:")
#print("Multiplication of that numbers are:")
for i in f:
    mul=1
    a=int(i)
    while a>0:
        r=a%10
        mul=mul*r
        print(mul)
        a=a//10
        
    f1.write(str(mul)+"\n")

    
        
f1.close()
f.close()
f=open("D:\my programs\python\practical list programs/cube.txt","r")
for i in f:
    print(i)
f.close()'''

#f1=open("D:\my programs\python\practical list programs/cube.txt","r")
#print(f1.read())
#f1.close()
#f1=open("D:\my programs\python\practical list programs/cube.txt","r")
#print(f1.read())




'''

f=open("D:\my programs\python\practical list programs\set7_p3_try.txt",'r')
l=[]
a=len(l)
for i in f.readlines():
    if "#" in i:
        continue
    elif i=='\n':
        continue
    elif a==0:
        a=a+1
    else:
        l.append(i)
print(l)
'''


'''
f=open("D:\my programs\python\practical list programs/num.txt",'r')
l=[]
for i in f.readlines():
    l.append(int(i))
print(l)
print("Minimum number in file is:",min(l))
'''

'''
f=open("D:\my programs\python\practical list programs/hyphenNum.txt",'r')
l=[]
l1=[]
for i in f:
    l.append(i)
    if "-" in i:
        continue
    else:
        l1.append(int(i))
print("Without removing Missing values:",l)
print("After removing missing values:",l1)
print("minimum Number is :",min(l1))
'''


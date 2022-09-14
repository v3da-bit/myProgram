
x=input("enter the string:")
if len(x) >= 3:
    if "ing" in x:
        print(x.replace("ing","ly"))
    else:
        print(x+"ing")
else:
    print(x)

    #print(x+"ing")

    

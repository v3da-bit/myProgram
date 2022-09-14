from operator import length_hint


x="hello not bad world"
if "not bad" in x:
    y=x.find("not bad")
    a=x[0:y]
    b="good"
    c=x[-y:]
    print(a+b+c)

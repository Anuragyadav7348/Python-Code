x =float(input("enter first number\n"))
y = float(input("enter the second number\n"))
z= float(input("enter the operator{+,-,*,/,//}/n"))
if z =="+":
    print("the sum of two number", x+y)
elif z == "-":
    print("subtraction of x-y number",x-y)
elif z== "*":
    print("multiplication of two number",x*Y)
elif z=="/":
    print("division of x/y",x/y)
elif z== "??":       
    print(("floor division of x//y",x//y))
else:    
    print("enter the wrong")
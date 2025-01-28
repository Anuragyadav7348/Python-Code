import math
def isperfectsqare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return isperfectsqare(5*n*n + 4) or isperfectsqare(5*n*n - 4)
i = int(input("enter the number"))
if (isFibonacci(i) == True):
    print(i,"is a Fibonacci Number")
else:
    print(i,"is a not Fibonacci Number")





        
x = int(input("enter the year\n"))
if x % 400 ==0:
    print(x,"is leap year")
elif x % 100==0:
    print(x,"is not leap year")
elif x % 4==0:
    print(x,"is leap year")
else:
    print(x,"is not leap year")
n = int(input("enter n digit number\n"))
num = n 
rev = 0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("reverse",rev)
if rev==num:
    print("palindrome")
else:
    print("thi is not palindrome")
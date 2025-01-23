nterms = int(input("How many terms?"))
n1,n2 = 0 ,1 
count = 0
if nterms <= 0:
    print("please enter a postive integer")
elif nterms  == 1:
    print(n1)
else:
   print("Fobonacci sequence")
   print(n1,n2)
   for i in range (3,nterms+1):
       nth = n1 + n2
       print(nth)
       n1  =  n2
       n2  =  nth
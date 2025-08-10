n=int(input("enter the number:"))
sum=0
while n>9:
    sum=0
    while n>0:
        r=n%10
        n=n//10
        sum=sum+r**2
    n=sum    
if n==1:
    print("happy number")
else:
    print("not a happy number")    
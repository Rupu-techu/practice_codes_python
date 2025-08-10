n=int(input("enter the number:"))
sum=0
pdt=n**2
while pdt>0:
    r=pdt%10
    pdt=pdt//10
    sum+=r
if sum==n:
    print("neon number")    
else:
    print("not a neon number")
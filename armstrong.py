n=int(input("enter a number:"))
p=len(str(n))
sum,u=0,n
while n>0:
    y=n%10
    n=n//10
    sum+=y**p
if u==sum:
    print("armstrong")
else:
    print("not armstrong")    
    
    


n=int(input("enter the number:"))
s,t,f=0,n,1
while n>0:
    r=n%10
    n=n//10
    for i in range(1,r+1):
        f*=i
    s+=f
    f=1
if t==s:
    print("krishnamurthy")        

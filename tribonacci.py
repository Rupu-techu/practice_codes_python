n=int(input("enter the range:"))
a,b,c,d=0,1,1,0
print(a,b,c,end="")
for i in range (4,n+1):
    d=a+b+c
    a=b
    b=c
    c=d
    print(" ",d,end="")
n=int(input("entyer the number: "))
a,b,c=0,1,0
print(a,b,end="")
for i in range (3,n+1):
    c=a+b
    a=b
    b=c
    print(c,end="")
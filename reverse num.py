n=int(input("enter the number:"))
s=0
while n>0:
    r=n%10
    n=n//10
    s=s*10+r
print ("the reverse of the number is :",s)    
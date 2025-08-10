n=int(input("enter the number:"))
while n>0:#n=0 hobe na cause n=0 hole loop abar cholbe jeta chalaor dorkar nei
    r=n%10
    n=n//10
    if r==0:
        c=1 #taking 1 like it can be any variable
        break
if c==1:
    print("the number is a duck number")
else:
    print("not a duck number")            

        
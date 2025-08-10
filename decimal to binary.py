n=int(input("enter a number"))#5
s=""#null value
while n>0:
    r=n%2 #1,0,1
    n=n//2 #4,2,1
    s=str(r)+s#1+null,'0'+1=01,'1'+'01'=101
print(s)

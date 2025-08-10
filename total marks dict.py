n=int(input("enter the number of students :"))
d={}
for i in range (0,n):
    r=int(input("enter the rolls:"))
    m=int(input("enter the marks:"))
    d[r]=m
print(d)
s=0
for i in d:
    s=s+d[i]
print("the totals marks:",s)    

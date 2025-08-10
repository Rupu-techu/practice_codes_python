r={}
n=int(input("enter num of students:"))
i=1
while i<=n:
    name=input("enter the name:")
    marks=input("enter the marks")
    r[name]=marks
    i+=1
    print(r)
s=input("enter name for search")
m=r.get(s)
if m is not None:
    print("{}:{}".format(s,m))
else:
    print("no")    

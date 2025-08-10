n=(int)(input("enter the numbe rof records:"))
d={}
for i in range (0,n):
    name=input("enter the nmae of the students:")
    m1=(int)(input("ener the marks of 1st sub:"))
    m2=(int)(input("enterbthe marks of the 2nd sub "))
    d[name]=[m1,m2]
m=0
for i in d:
    avg=(d[i][0]+d[i][1])/2
    if avg>m:
        m=avg
for i in d:
    avg=(d[i][0]+d[i][1])/2
    if m==avg:
        print("name=",i)            

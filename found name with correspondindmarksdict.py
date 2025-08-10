n=int(input("enter the number of students :"))
d={}
for i in range (0,n):
    r=input("enter the name:")
    m=int(input("enter the marks:"))
    d[r]=m
print(d)
n=input("enter name of student for marks:")
for i in d:
    if n==i:
        print("the marks is:",d[i])
        break
else:
    print("key is absent")    


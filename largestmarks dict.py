n=int(input("enter the number of students :"))
d={}
for i in range (0,n):
    r=input("enter the name:")
    m=int(input("enter the marks:"))
    d[r]=m
    n=0
    for i in d:
        if d[i]>n:
            n=d[i]
            t=i#if not then only the last name will beshiwn every time
print("highest marks:",n)
print("name:",t)            
l={}
i=1
n=int(input("enter the num of inputs"))
while i<=n:
    y=int(input('enter the keys'))
    v=int(input('enter the values'))
    l[y]=v
    i+=1
print(l)
print(max(l.values()))





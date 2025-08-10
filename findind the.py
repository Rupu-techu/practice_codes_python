f=open("student.txt","r")
s=f.read()
v="theTHE"
c=0
l=len(s)
for i in  s:
    if i in v:
     c+=1
print("the number of the is:",c)
f.close()


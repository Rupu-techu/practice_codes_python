f=open("student.txt","r")
s=f.read()
n=s.split()
p=input("enter the word:")
if p == n:
  print("word found")
else:
  print("no word found") 
f.close()       

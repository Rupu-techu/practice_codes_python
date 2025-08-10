n=int(input("enter a number:"))#1**1+3**2+5**3
sum=0
t=n #intitialising since compairing sum==nand n's value is chancging
while t>0:
    length=len(str(t)) #length=3,2(n=13),1(1)
    r=t%10   #r=5,3,1
    sum=sum+r**length#0+5**3=125,125+3**2=134,135+1=135
    t=t//10 #13,1
if sum==n:
    print("the number",n,"is weakram number")
else:
    print("not weakram")    
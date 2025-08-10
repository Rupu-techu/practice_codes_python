n=int(input("enter the electricity amount:"))
c=150
if n<=100:
    print("the bill is:",c)
elif n>100 and n<=200:
    print("the bill is:",(c+(n-100)*1.5))
elif n>200 and n<=350:
    print("the bill is:",(c+100*1.5+(n-200)*1.75))    
else:
    print("the bill is:",(150+(100*1.5)+(1.75*150)+(n-350)*2))    

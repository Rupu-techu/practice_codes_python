l=eval(input("enter a list :"))
s=0
e=0
for i in l:
    if i%2==0 :
        s+=i
    elif  i%2!=0:
        e+=i    
print("the sum of even numbers:",s)
print("the sum of odd number:",e)
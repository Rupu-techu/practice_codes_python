n=input("enter the str")
e=str(n)
u=0
l=0
d=0
s=0
for i in range (len(e)):
    if n[i].isupper():
        u+=1
    elif n[i].islower():
        l+=1
    elif n[i].isdigit():
        d+=1
    else:
        s+=1
print("uppercase:",u)    
print("lower case:",l)  
print("digit",d) 
print("special:",s)             
            
        
        
        

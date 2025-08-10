n=int(input("enter the number:"))#sum of the numbers of even numbers(not count)
sum=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        sum+=r      
print("the sum of the even numbers is:",sum)    #print otside the loop    

n=int(input("enter the sales amount:"))
if n<10000:
    print("5 percent discount")
    c=n-n*5/100
    print("the selling price is:",c)
elif n>=10000:
    print("9 percent discount")  
    d=n-n*9/100
    print("the selling price is:",d)
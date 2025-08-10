Str="GeeksForGeeks"
lower=0
upper=0
for i in Str:
    if(i.islower()):
        lower+=1
    elif (i.isupper):
        upper+=1
        print(upper)     #counting lower and upper case words
        print(lower)
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))#bujte prchi n
nterms =int(input("enter ythe series:"))
print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i))

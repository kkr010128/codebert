n = int(input())
fib = []
for i in range (n+1) :
    if i <= 1 :
        fib.append(1)
    else :
        fib.append(fib[i-2]+fib[i-1])
print(fib[n])


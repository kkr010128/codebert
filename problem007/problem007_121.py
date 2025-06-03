fib = [1]*100

for i in range(2,100):
    fib[i] = fib[i-1] + fib[i-2]
    
print(fib[int(input())])

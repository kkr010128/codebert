n = int(input())
fib = []
fib.append(1)
fib.append(1)
for _ in range(n - 1):
    fib.append(fib[-2] + fib[-1])
print(fib[-1])

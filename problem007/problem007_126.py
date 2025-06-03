#!/usr/bin/python3

# main
n = int(input()) - 1
fib = [1, 2]
for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[n])
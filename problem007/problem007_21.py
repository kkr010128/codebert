def fibonacci(f, n):
    if n == 0 or n == 1:
        f[n] = 1
        return f[n]
    if f[n]:
        return f[n]
    f[n] = fibonacci(f, n - 2) + fibonacci(f, n - 1)
    return f[n]

n = int(input())
f = [None for i in range(n + 1)]
print(fibonacci(f, n))
def fibonacci(n):
    if n == 0 or n == 1:
        F[n] = 1
        return F[n]
    if F[n] is not None:
        return F[n]
    F[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return F[n]


n = int(input())
F = [None]*(n + 1)
print(fibonacci(n))
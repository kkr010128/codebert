_fib = [0] * 45

def fib(n):
    if n < 2:
        return 1
    if _fib[n] > 0:
        return _fib[n]
    _fib[n] = fib(n-1) + fib(n-2)
    return _fib[n]

n = int(input())
print(fib(n))


def fib(n):
    if ft[n] != 0:
        return ft[n]
    else:
        ft[n] = fib(n - 1) + fib(n - 2)
        return ft[n]

ft = [0] * 45
ft[0] = ft[1] = 1
print fib(int(input()))
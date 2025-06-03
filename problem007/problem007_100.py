from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input())
ans = fib(n)

print(ans)
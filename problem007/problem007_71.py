from functools import lru_cache
@lru_cache(maxsize=None)

def Fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
n=int(input())
print(Fib(n))

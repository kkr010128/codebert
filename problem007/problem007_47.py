from functools import lru_cache

@lru_cache(maxsize=1024)

def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(int(input())))
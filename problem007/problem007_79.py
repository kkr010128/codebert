from functools import lru_cache
counter = 0
@lru_cache(maxsize=1024)

def fib(n):
    global counter
    counter += 1
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(int(input())))
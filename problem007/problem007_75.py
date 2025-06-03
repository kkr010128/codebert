N = int(input())

def memorize(f) :
    cache = {}
    def helper(*args) :
        if args not in cache :
            cache[args] = f(*args)
        return cache[args]
    return helper

@memorize
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    res = fibonacci(n - 2) + fibonacci(n - 1)
    return res

print(fibonacci(N))

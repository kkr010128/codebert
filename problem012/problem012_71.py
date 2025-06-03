from math import sqrt

def f(n):
    if n == 2:
        return 1

    if n % 2 == 0:
        return 0

    for i in range(3, round(sqrt(n)+1), 2):
        if n % i == 0:
            return 0
    else:
        return 1

def g(n):
    d = {}
    for _ in range(n):
        i = int(input())
        if not (i in d):
            d[i] = f(i)
        yield d[i]

n = int(input())
print(sum(g(n)))
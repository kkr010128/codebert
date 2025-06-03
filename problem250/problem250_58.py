
# 素因数分解
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

from itertools import count

X = int(input())

for x in count(X):
    if len(tuple(prime_factors(x))) == 1:
        print(x)
        break
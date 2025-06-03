import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
A = list(map(int, input().split()))

if gcd_list(A) != 1:
    print('not coprime')
    exit()

primes = set()
for a in A:
    len_primes = len(primes)
    divs = set(prime_factorize(a))
    primes |= divs

    if len(primes) != len_primes + len(divs):
        print('setwise coprime')
        exit()

print('pairwise coprime')

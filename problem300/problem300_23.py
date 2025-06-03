#!/usr/bin/env python3

import sys
from math import gcd, sqrt
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


A, B = map(int, input().split())
g = gcd(A, B)


def prime_factorize(n):
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a


primes = prime_factorize(g)
print(len(primes)+1)


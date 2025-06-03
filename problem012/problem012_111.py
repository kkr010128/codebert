#!/usr/bin/env python3
from itertools import count, takewhile


def prime():
    prime = []

    def _isPrime(n):
        for d in takewhile(lambda x: x * x <= n, prime):
            if n % d == 0:
                return False
        return True
    for i in count(2):
        if _isPrime(i):
            prime.append(i)
            yield(i)


def is_prime(primes, i):
    for p in takewhile(lambda x: x * x <= i, sorted(primes)):
        if i % p == 0:
            return False
    return True

primes = list(takewhile(lambda x: x < 10000, prime()))

n = int(input())
c = 0
for _ in range(n):
    i = int(input())
    if is_prime(primes, i):
        c += 1
print(c)
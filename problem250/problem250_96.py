# -*- coding: utf-8 -*-
# Next Prime

import sys


TEST_INPUT = \
"""

100000

"""

TEST_OUTPUT = \
"""

100003

"""


def primes(n):
    if n == 0 or n == 1: return []
    
    ps = [2]
    for odd in range(3, n + 1, 2):
        for p in ps:
            if odd % p == 0:
                break
            if p ** 2 > odd:
                ps.append(odd)
                break
    return ps


def isprime(n):
    if n == 0 or n == 1: return False
    
    last = int(n**.5)
    for m in primes(last):
        if n % m == 0:
            return False
    return True


def nextprime(n):
    if n in primes(n):
        return n
    else:
        i = n
        while not isprime(i):
            i += 1
        return i


def main(stdin):
    n = int(stdin)
    print(nextprime(n))


if __name__ == "__main__":
    main(sys.stdin.read().strip())
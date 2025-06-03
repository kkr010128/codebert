#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# E - Sum of gcd of Tuples (Hard)

n, k = map(int, input().split())

modulus = 10 ** 9 + 7

def expt(x, k):
    """(x ** k) % modulus"""
    p = 1
    for b in (bin(k))[2:]:
        p = p * p % modulus
        if b == '1':
            p = p * x % modulus
    return p

# iの倍数をn個並べた列の個数
nseq = [expt((k // i), n) if i > 0 else None for i in range(k + 1)]

for i in range(k, 0, -1):
    # iの2倍以上の倍数からなる列の個数を引く
    s = sum(nseq[m] for m in range(2 * i, k + 1, i))
    nseq[i] = (nseq[i] - s % modulus + modulus) % modulus

# nseq[i]はgcd==iになる列の個数
ans = sum(i * nseq[i] % modulus for i in range(1, k + 1))
print(ans % modulus)

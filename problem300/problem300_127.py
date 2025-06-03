#!/usr/bin/env python3
# 1. 素因数分解して公約数を作成(A,B共に)
# 2. 

from collections import Counter # N : 素因数分解


def calc_prime_factor(N):
    prime_factor = []
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            prime_factor.append(i)
            N /= i
    if N > 1:
        prime_factor.append(N)
    return prime_factor


A, B = [int(s) for s in input().split()]

prime_A = calc_prime_factor(A)
prime_B = calc_prime_factor(B)

print(len(list(set(Counter(prime_A).keys()) & set(Counter(prime_B).keys()))) + 1)
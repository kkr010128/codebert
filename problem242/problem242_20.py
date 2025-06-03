# coding: utf-8

import math

N, K = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
A.sort()

p = 10**9 + 7
facts = [1, 1]
for i in range(2, N+1):
	facts.append((facts[i-1] * i) % p)

invs = [1 for i in range(N+1)]
invs[N] = pow(facts[N], p-2, p)
for i in range(N, 1, -1):
	invs[i-1] = invs[i] * i % p

sum_max_s = 0
for i in range(K, N+1):
	sum_max_s += A[i-1] * (facts[i-1] * invs[K-1] * invs[i-K] % p) % p

sum_min_s = 0
for i in range(1, N-K+2):
	sum_min_s += A[i-1] * (facts[N-i] * invs[K-1] * invs[N-i-K+1] % p) % p

print(str(int(sum_max_s - sum_min_s) % p))
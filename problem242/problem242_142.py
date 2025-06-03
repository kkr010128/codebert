import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10


		
#階乗#
lim = 10**5   #必要そうな階乗の限界を入力
fact = [1] * (lim+1)
for n in range(1, lim+1):
	fact[n] = n * fact[n-1] % mod

#階乗の逆元#
fact_inv = [1]*(lim+1)
fact_inv[lim] = pow(fact[lim], mod-2, mod)
for n in range(lim, 0, -1):
	fact_inv[n-1] = n*fact_inv[n]%mod

def C(n, r):
	if n < r:
		return 0
	else:
		return (fact[n]*fact_inv[r]%mod)*fact_inv[n-r]%mod

N, K = MAP()
A = LIST()
A.sort()

A_cnt = Counter(A)

P = list(A_cnt.keys())
p = list(A_cnt.values())

#print("P={}".format(P))
#print("p={}".format(p))

p_acc = list(accumulate(p))
p_acc_rev = list(accumulate(p[::-1]))

#print("p_acc={}".format(p_acc))
#print("p_acc_rev={}".format(p_acc_rev))

n = len(p)
T = [[0]*4 for _ in range(n)]

for i in range(n):
	T[i][0] = p_acc[i]

for i in range(1, n):
	T[i][1] = p_acc[i-1]

for i in range(n):
	T[(-i-1)][3] = p_acc_rev[i]

for i in range(1, n):
	T[(-i-1)][2] = p_acc_rev[i-1]

#for i in range(n):
#	print(T[i])

t = [0]*n

for idx, x in enumerate(T):
	t[idx] = (C(x[0], K) - C(x[1], K) + C(x[2], K) - C(x[3], K))%mod

ans = 0
for i in range(n):
	ans = (ans + P[i]*t[i]%mod)%mod

print(ans)


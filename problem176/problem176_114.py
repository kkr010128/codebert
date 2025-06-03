#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

N, K = map(int, input().split())

d = [0]*(K+1)
for i in range(1, K+1):
    val = K//i
    d[i] = pow(val, N, MOD)

# print(d)

for i in range(K, 0, -1):
    # print('i', i)
    for j in range(K//i, 1, -1):
        # print(' j', j)
        # print(i, i*j)
        d[i] -= d[i*j]
    # print(d)

res = 0
for i, v in enu(d):
    res += i*v
    res %= MOD
print(res)

import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = []
T = []
for a in A:
    if a < 0:
        T.append(a)
    else:
        S.append(a)

ls = len(S)
lt = len(T)
ok = False

if ls > 0:
    if N == K:
        ok = lt % 2 == 0
    else:
        ok = True
else:
    ok = K % 2 == 0

ans = 1
if not ok:
    A = sorted(A, key=lambda x: abs(x))
    for a in A[:K]:
        ans *= a
        ans %= MOD
else:
    S = sorted(S)
    T = sorted(T, reverse=True)
    if K % 2 == 1: # if K is odd, the answer has at least one positive number.
        ans *= S.pop()
        ans %= MOD
    p = []
    # the num of negatives must be even, so positives must do the same
    # thus, we can pop 2 items at one time.
    while len(S) >= 2:
        x = S.pop()  
        y = S.pop()
        p.append(x * y)
    while len(T) >= 2:
        x = T.pop()  
        y = T.pop()
        p.append(x * y)
    p = sorted(p, reverse=True)
    for i in range(K // 2):
        ans *= p[i]
        ans %= MOD
print(ans % MOD)
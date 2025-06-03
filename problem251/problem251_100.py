import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

def get_point(x):
    if x == 'r':
        return P
    if x == 's':
        return R
    if x == 'p':
        return S

# think each mod K
ans = 0
for i in range(K):
    dp = [0] * 2
    pre = ''
    for j in range(i, N, K):
        dp2 = dp[:]
        dp2[0] = max(dp)
        if pre == T[j]:
            dp2[1] = dp[0] + get_point(T[j])
        else:
            dp2[1] = max(dp) + get_point(T[j])
        pre = T[j]
        dp = dp2
    ans += max(dp)

print(ans)
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

N, M = map(int, input().split())
A = list(sorted(map(int, input().split())))
S = sum(A)
acc = [0] * (N + 1)
for i in range(1, N + 1):
    acc[i] = acc[i - 1] + A[i - 1]

def check(x):
    total = 0
    cnt = 0
    for a in A:
        l = -1
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] + a >= x:
                r = m
            else:
                l = m
        cnt += N - r
        total += acc[N] - acc[r]
        total += a * (N - r)
    return (total, cnt)

left = 0
right = 10 ** 6
while right - left > 1:
    mid = (left + right) // 2
    res = check(mid)
    if res[1] >= M:
        left = mid
    else:
        right = mid
res = check(left)
ans = res[0]
print(ans - (res[1] - M) * left)

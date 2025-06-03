import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)

n, k, c = map(int, input().split())
s = input()
left = [-1]*k
right = [-1]*k

d = w = 0
while w < k:
    if s[d] == "o":
        left[w] = d
        w += 1
        d += c+1
    else:
        d += 1

d, w = n-1, k-1
while w >= 0:
    if s[d] == "o":
        right[w] = d
        w -= 1
        d -= c+1
    else:
        d -= 1

# print(left, right)
for i in range(k):
    if left[i] == right[i]:
        print(left[i]+1)

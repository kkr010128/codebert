from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
from fractions import gcd
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
EPS = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

n = int(input())
l_list = list(map(int, input().split()))
l_combo = itertools.combinations(l_list, 3)
ans = 0
for i in l_combo:
    if i[0] + i[1] > i[2] and i[1]+i[2] > i[0] and i[0] + i[2] > i[1] and i[0] != i[1] and i[1] != i[2] and i[0] != i[2]:
        ans += 1

print(ans)

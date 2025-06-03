import sys
import math,bisect
sys.setrecursionlimit(10 ** 5)
from itertools import groupby,accumulate
from heapq import heapify,heappop,heappush
from collections import deque,Counter,defaultdict
def I(): return int(sys.stdin.readline())
def neo(): return map(int, sys.stdin.readline().split())
def Neo(): return list(map(int, sys.stdin.readline().split()))
def dfs(t):
    vis[t] = 1
    for i in G[t]:
        if not vis[i]:
            dfs(i)
N,M = neo()
G = defaultdict(list)
vis = [0]*(N+1)
for i in range(M):
    x,y = neo()
    G[x] += [y]
    G[y] += [x]
c = 0
for i in range(1,N+1):
    if not vis[i]:
        dfs(i)
        c += 1
print(c-1)

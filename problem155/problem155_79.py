from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
h = inpl()
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = inpl()
    a,b = a-1,b-1
    g[a].append(b)
    g[b].append(a)
res = 0
for i in range(n):
    for j in g[i]:
        if h[j] >= h[i]:
            break
    else:
        res += 1
print(res)
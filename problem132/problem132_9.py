from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
now = inpl()
now.append(0)
for _ in range(k):
    pre = now[::]
    now = [0] * (n+1)
    for j in range(n):
        a = max(0,j-pre[j])
        b = min(n,j+pre[j]+1)
        now[a] += 1
        now[b] -= 1
    x = 0
    mi = INF
    for j in range(n):
        x += now[j]
        mi = min(mi,x)
        now[j] = x
    if mi == n:
        break
print(*now[:n])
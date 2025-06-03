from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,t = inpl()
wv = [None] * n
for i in range(n):
    a,b = inpl()
    wv[i] = (a,b)
rwv = wv[::-1]
udp = [[0] * t for _ in range(n)]
ddp = [[0] * t for _ in range(n)]

for i in range(n-1):
    w,v = wv[i]
    for j in range(t):
        if j < w:
            udp[i+1][j] = udp[i][j]
        else:
            udp[i+1][j] = max(udp[i][j], udp[i][j-w] + v)
res = udp[n-1][t-1] + wv[n-1][1]

for i in range(n-1):
    w,v = rwv[i]
    for j in range(t):
        if j < w:
            ddp[i+1][j] = ddp[i][j]
        else:
            ddp[i+1][j] = max(ddp[i][j], ddp[i][j-w] + v)
    res = max(res,ddp[n-1][t-1] + wv[0][1])
# print(res)
for i in range(1,n-1):
    u = i; d = n-i-1
    mx = 0
    for j in range(t):
        tmp = udp[u][j] + ddp[d][t-1-j]
        mx = max(mx, tmp)
    res = max(res, mx + wv[i][1])
print(res)
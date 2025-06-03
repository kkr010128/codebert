from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
now = inpl()
for _ in range(k):
    pre = now[::]
    cnt = [0] * (n+1)
    for i in range(n):
        l = max(0, i - pre[i])
        r = min(n, i + pre[i] + 1)
        cnt[l] += 1
        cnt[r] -= 1
    # print(cnt)
    now = [0] * n
    now[0] = cnt[0]
    for i in range(1,n):
        now[i] = now[i-1] + cnt[i]
    if min(now) == n:
        break
print(*now)
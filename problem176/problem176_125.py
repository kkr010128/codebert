from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n,k = inpl()
res = 0
cnt = [0] * (k+5)
for i in reversed(range(1,k+1)):
    tmp = pow(k//i,n,mod)
    cnt[i] = tmp
    now = i
    while True:
        now += i
        if now > k:
            break
        cnt[i] -= cnt[now]
    res += cnt[i] * i
    res %= mod
print(res)
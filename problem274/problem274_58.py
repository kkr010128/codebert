from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
s = list(input())[::-1]
res = []
now = 0
while now != n:
    nex = min(now + m, n)
    while s[nex] == '1':
        nex -= 1
        if nex == now:
            print(-1)
            quit()
    res += [nex - now]
    now = nex
print(*res[::-1])
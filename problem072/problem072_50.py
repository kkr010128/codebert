from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [inpl() for _ in range(n)]
a = [x == y for x,y in a]
res = False
for i in range(n-2):
    if sum(a[i:i+3]) == 3:
        res = True
print('Yes' if res else 'No')
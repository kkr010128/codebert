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
res = [0]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j > n: break
        res[i*j] += 1
print(sum(i*x for i,x in enumerate(res)))
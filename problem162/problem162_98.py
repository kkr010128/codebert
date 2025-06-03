from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
ge = []
l = 1
r = n-1
for i in range(m):
    if i%2:
        ge.append(l)
    else:
        ge.append(r)
    l += 1; r -= 1
ge.sort(reverse = True)
for i in range(m):
    print(i+1,i+1+ge[i])

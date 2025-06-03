from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,d,A = inpl()
d *= 2
xh = [inpl() for _ in range(n)]
xh.sort()
ln = 1
f = [0]
a = [0]
for i in range(n):
    x,h = xh[i]
    r = bisect_left(f,x+d)
    l = bisect_left(f,x)
    tmp = a[r-1] - a[l-1]
    # print(i,l,r)
    h -= tmp * A
    if h > 0:
        ind = x + d
        att = (h+A-1)//A
        f.append(ind)
        a.append(a[-1] + att)
        ln += 1
# print(f,a)
print(a[-1])

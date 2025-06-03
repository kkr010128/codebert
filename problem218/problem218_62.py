from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
d = []
s = set()
dd = {}
ind = 0
for i in range(n):
    x = input()
    if x in s:
        d[dd[x]][1] += 1
    else:
        dd[x] = ind
        d.append([x,1])
        ind += 1
        s.add(x)
d.sort(key = lambda x:x[1], reverse = True)
# print(d)
res = []
for key,va in d:
    if va < d[0][1]:
        break
    res.append(key)
res.sort()
for x in res:
    print(x)
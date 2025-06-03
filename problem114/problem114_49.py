from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

d = inp()
c = inpl()
s = [inpl() for _ in range(d)]
res = 0
last = [0]* 26
for day in range(d):
    t = inp(); t -= 1
    res += s[day][t]
    for i in range(26):
        last[i] += 1
        if i == t:
            last[t] = 0
        res -= c[i] * last[i]
    print(res)
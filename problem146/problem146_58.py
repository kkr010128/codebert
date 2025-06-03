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
z = 0
d = defaultdict(int)
for _ in range(n):
    a,b = inpl()
    if a == 0 and b == 0:
        z += 1
        continue
    if a == 0: b = 1
    if b == 0: a = 1
    if b < 0: a,b = -a,-b
    g = math.gcd(a,b)
    a //= g; b //= g
    d[(a,b)] += 1
res = 1
seen = set()
for k in list(d):
    a,b = k
    if k in seen: continue
    if a < 0: x,y = b,-a
    else: x,y = -b,a
    if a == 0: x,y = 1,0
    if b == 0: x,y = 0,1
    res *= pow(2,d[(a,b)],mod) + pow(2,d[(x,y)],mod) -1
    res %= mod
    # print(res)
    seen.add(k); seen.add((x,y))
res += z - 1
print(res%mod)
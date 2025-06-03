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
a = inpl()
ln = len(bin(max(a))) -2
cnt = [0] * ln
for x in a:
    for shift in range(ln):
        cnt[shift] += (x>>shift)%2
# print(cnt)
res = 0
for i in range(ln):
    now = cnt[i] * (n-cnt[i])
    res += now*pow(2,i)
    res %= mod
print(res)  


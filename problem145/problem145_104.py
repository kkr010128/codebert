import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

n, m = l()
g = [[] for i in range(n)]
for i in range(m):
    a, b = l()
    g[a-1].append(b-1)
    g[b-1].append(a-1)
q = deque([0])
d = [-1] * n
d[0] = 0
while q:
    v = q.popleft()
    for w in g[v]:
        if d[w] != -1:
            continue
        d[w] = v
        q.append(w)
if -1 in d:
    print("No")
else:
    print("Yes")
    for di in d[1:]:
        print(di+1)

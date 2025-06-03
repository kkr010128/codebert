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
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

D = i()
c = l()
C = sorted(c)
C.reverse()
rank = [0]*26
ans = [0]*D
for i in range(D):
    s = l()
    ans[i] = s.index(max(s))+1
for i in range(26):
    rank[i] = C.index(c[i])+1
for i in range(10):
    d = D//rank[i]
    for j in range(i,D,2**d+20):
        ans[j] = i+1
for i in ans:
    print(i)
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def s(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 1
ans = 0
inf = float("inf")

s = s()
k = k()

if s[0]*len(s) == s:
    print(len(s)*k // 2)
    sys.exit()

res = [1]

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        res[-1] += 1
    else:
        res.append(1)

for i in res:
    ans += (i//2)*k
if s[0] == s[-1]:
    diff = (res[0]+res[-1])//2 - (res[0]//2 + res[-1]//2)
    ans += diff*(k-1)
print(ans)

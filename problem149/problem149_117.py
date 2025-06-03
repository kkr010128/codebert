import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")

n,m,x = I()
book = [l() for i in range(n)]
money = []

for i in range(2**n):
    ccc = 0
    bag = [0]*(m+1)
    for j in range(n):
        for k in range(m+1):
            if ((i>>j)&1):
                bag[k] += book[j][k]
    for p in range(1,m+1):
        if bag[p] >= x:
            ccc += 1
    if ccc == m:
        money.append(bag[0])

if len(money) == 0:
    print(-1)
else:
    print(min(money))
    

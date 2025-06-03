import re
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
cnt = 0
ans = 0
inf = float("inf")

n,k=I()
p = l()
x = list(itertools.accumulate(p))

if n==1:
    print((p[0]+1)/2)
    sys.exit()

if n==k:
    print((x[-1]+k)/2)
    sys.exit()

for i in range(1,n-k+1):
    ans = max(ans,x[i+k-1]-x[i-1])

print((ans+k)/2)

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
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

N = i()
table = [[0]*9 for _ in range(9)]
for i in range(N):
    s = str(i+1)
    a,b = int(s[0]),int(s[-1])
    if b == 0:
        continue
    table[a-1][b-1] += 1
ans = 0
for i in range(9):
    for j in range(9):
        ans += table[i][j]*table[j][i]
print(ans)
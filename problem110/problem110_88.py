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

h, w, k = map(int, input().split())
C = []
for _ in range(h): C.append(input())
from itertools import *
ans = 0
for bit in range(1<<(h+w)):
    c = 0
    for i, j in product(range(w, h+w), range(w)):
        if bit>>i & 1 and bit>>j & 1: c += C[i-w][j] == '#'
    if c == k: ans += 1
print(ans)

import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

import networkx as nx
n,x,y = inpm()
x -= 1
y -= 1
if x > y:
    x,y = y,x

d = np.zeros((n,n),int)
ans = np.zeros(n,int)
for i in range(n):
    for j in range(i+1,n):
        a = j - i
        b = abs(x - i) + abs(j - y) + 1
        ans[min(a,b)] += 1

for i in range(1,n):
    print(ans[i])
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

a = inpll(3)
n = inp()
B = inplm(n)

tmp = np.zeros((3,3),dtype=np.int)

for b in B:
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                tmp[i][j] = 1

ans = 'No'
if np.any(np.all(tmp == 1,axis=0) == True) or np.any(np.all(tmp == 1,axis=1) == True) or (tmp[0][0] == 1 and tmp[1][1] == 1 and tmp[2][2] == 1) or (tmp[0][2] == 1 and tmp[1][1] == 1 and tmp[2][0] == 1):
    ans = 'Yes'

print(ans)
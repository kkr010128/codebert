import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
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

n,k = inpm()
r,s,p = inpm()
T = input()

cnt_r = T.count('r')
cnt_s = T.count('s')
cnt_p = T.count('p')
ans = cnt_r * p + cnt_s * r + cnt_p * s

tmp = [0]*n
for i in range(k,n):
    if tmp[i-k] == 1:
        continue
    if T[i] == T[i-k]:
        tmp[i] = 1
        if T[i] == 'r':
            ans -= p
        elif T[i] == 's':
            ans -= r
        elif T[i] == 'p':
            ans -= s
print(ans)
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

n,m = inpm()

P = []
S = []
for i in range(m):
    tmp = input().split()
    P.append(int(tmp[0]))
    S.append(tmp[1])

AC = [0]*100001
WA = [0]*100001

for i in range(m):
    if S[i] == 'AC':
        AC[P[i]] = 1
    elif S[i] == 'WA' and AC[P[i]] != 1:
        WA[P[i]] += 1

cnt_ac = 0
cnt_wa = 0
for i in range(1,n+1):
    if AC[i] == 1:
        cnt_ac += 1
        cnt_wa += WA[i]

print(cnt_ac,cnt_wa)
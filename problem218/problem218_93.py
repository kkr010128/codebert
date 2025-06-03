import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
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

n = inp()
s = sorted(inplL(n))

tmp = ''
ans = []
anscnt = -1
for i in range(n):
    if tmp == s[i]:
        ans[anscnt][1] += 1
    else:
        ans.append([s[i],1])
        anscnt += 1
    tmp = s[i]

ans.sort(key=lambda x: x[1],reverse=True)

tmp = 0
ret = []
for i in range(len(ans)):
    if i == 0 or tmp == ans[i][1]:
        ret.append(''.join(ans[i][0]))
        tmp = ans[i][1]
    elif tmp != ans[i][1] :
        break

ret.sort()
for i in range(len(ret)):
    print(ret[i])
import sys, bisect, math, itertools, string, queue, copy
#import numpy as np
#import scipy
from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# from fractions import gcd
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
# mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

s = input()
q = int(input())
ql = [input().split() for i in range(q)]

ans = deque(s)
isrev=False
for i in range(q):
  if ql[i][0] == '1':
    isrev = not isrev
    continue
  if (ql[i][1] == '2') == isrev:
    ans.appendleft(ql[i][2])
  else:
    ans.append(ql[i][2])

if isrev:
  ans.reverse()

s = ''.join(ans)

print(s)

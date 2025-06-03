import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# # input = sys.stdin.readline
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

n = inp()
S = input()

s1 = set()
s2 = set()
s3 = set()

for s in S:
    for ss2 in s2:
        s3.add(ss2+s)
    for ss1 in s1:
        s2.add(ss1+s)
    s1.add(s)

print(len(s3))
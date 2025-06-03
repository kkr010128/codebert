import sys, io, os, re
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor, ceil
from copy import copy, deepcopy
from collections import deque, defaultdict
from fractions import gcd
from functools import reduce
from itertools import groupby, combinations
from heapq import heapify, heappush, heappop

# sys.setrecursionlimit(5000)

n1 = lambda: int(sys.stdin.readline().strip())
nn = lambda: list(map(int, sys.stdin.readline().strip().split()))
f1 = lambda: float(sys.stdin.readline().strip())
fn = lambda: list(map(float, sys.stdin.readline().strip().split()))
s1 = lambda: sys.stdin.readline().strip()
sn = lambda: list(sys.stdin.readline().strip().split())
nl = lambda n: [n1() for _ in range(n)]
fl = lambda n: [f1() for _ in range(n)]
sl = lambda n: [s1() for _ in range(n)]
nm = lambda n: [nn() for _ in range(n)]
fm = lambda n: [fn() for _ in range(n)]
sm = lambda n: [sn() for _ in range(n)]

def array1(n, d=0): return [d] * n
def array2(n, m, d=0): return [[d] * m for x in range(n)]
def array3(n, m, l, d=0): return [[[d] * l for y in xrange(m)] for x in xrange(n)]
def linc(A, d=1): return list(map(lambda x: x + d, A))
def ldec(A, d=1): return list(map(lambda x: x - d, A))

N = n1()
A = nn()

#MAX = 10**6
MAX = max(A)
dp = defaultdict(list)

p = 2
while p <= MAX:
    i = p
    while i <= MAX:
        dp[i].append(p)
        i += p

    p += 1
    while len(dp[p]) >= 1:
        p += 1

if max(A) == 1:
    print("pairwise coprime")
    exit(0)

dic = defaultdict(list)

for ai in A:
    fact = dp[ai]
    for x in fact:
        dic[x].append(ai)

maxlen = 0
for k, v in dic.items():
    maxlen = max(len(v), maxlen)

if maxlen == 1:
    print("pairwise coprime")
elif maxlen == N:
    print("not coprime")
else:
    print("setwise coprime")
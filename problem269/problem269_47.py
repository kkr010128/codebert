import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

T1, T2 = MAP()
A1, A2 = MAP()
B1, B2 = MAP()

if T1*A1+T2*A2 == T1*B1+T2*B2:
    print("infinity")
    exit()
if (A1 < B1 and A2 < B2) or (B1 < A1 and B2 < A2):
    print(0)
    exit()

if A1 > B1:
    A1, B1 = B1, A1
    A2, B2 = B2, A2

if A1*T1+A2*T2 < B1*T1+B2*T2:
    print(0)
    exit()

F = A1*T1-B1*T1
L = A2*T2-B2*T2

S, T = divmod(-F, F+L)

if T == 0:
    print(2*S)
else:
    print(2*S+1)

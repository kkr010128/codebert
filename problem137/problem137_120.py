import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
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
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10


N = INT()
AB = [LIST() for _ in range(N)]

A, B = zip(*AB)
A = list(A)
B = list(B)

A.sort()
B.sort()

if N%2:
	a = A[N//2]
	b = B[N//2]
	print(b-a+1)
else:
	a = (A[N//2-1]+A[N//2])/2
	b = (B[N//2-1]+B[N//2])/2
	print(int((b-a)*2+1))

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
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

H, W, K = MAP()

s = [input() for _ in range(H)]

tmp = 1
ans = [[0]*W for _ in range(H)]

for i in range(H):
	if not "#" in s[i]:
		if i != 0:
			ans[i] = ans[i-1]
			continue
		else:
			continue

	is_first = True
	for j in range(W):
		if s[i][j] == "#":
			if is_first:
				is_first = False
			else:
				tmp += 1
		ans[i][j] = tmp
	tmp += 1

for i in range(H-2, -1, -1):
	if 0 in ans[i]:
		ans[i] = ans[i+1]

for i in range(H):
	print(*ans[i])

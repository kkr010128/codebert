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
	
X, Y, A, B, C = MAP()
p = deque(sorted(LIST(), reverse=True))
q = deque(sorted(LIST(), reverse=True))
r = deque(sorted(LIST(), reverse=True) + [0])

x = 0
y = 0
z = 0
ans = 0
while x+y+z < X+Y:
	compare = (p[0], q[0], r[0])

	if p[0] == max(compare):
		x += 1
		ans += p.popleft()
		if x == X:
			p = [0]
	elif q[0] == max(compare):
		y += 1
		ans += q.popleft()
		if y == Y:
			q = [0]
	else:
		z += 1
		ans += r.popleft()

print(ans)

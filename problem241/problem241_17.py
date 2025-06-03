import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
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
mod = 10**9 + 7
#from decimal import *

H, W = MAP()
S = [input() for _ in range(H)]
dy = (1, 0, -1, 0)
dx = (0, -1, 0, 1)

def diff_max(start_y, start_x):
	check = [[-1]*W for _ in range(H)]
	check[start_y][start_x] = 0
	q = deque([(start_y, start_x)])

	while q:
		y, x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if 0 <= ny < H and 0 <= nx < W:
				if check[ny][nx] == -1 and S[ny][nx] == ".":
					check[ny][nx] = check[y][x] + 1
					q.append((ny, nx))

	return max([max(x) for x in check])



ans = -INF
for i in range(H):
	for j in range(W):
		if S[i][j] == ".":
			ans = max(ans, diff_max(i, j))

print(ans)

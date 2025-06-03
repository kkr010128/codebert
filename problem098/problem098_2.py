import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mat = lambda x, y, v: [[v]*y for _ in range(x)]
ten = lambda x, y, z, v: [mat(y, z, v) for _ in range(x)]
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()
C = rs()

l, r = 0, N-1
ans = 0
while l < r:
	while C[l] == 'R' and l < N-1:
		l += 1
	while C[r] == 'W' and r > 0:
		r -= 1
	if l >= r: break
	l += 1
	r -= 1
	ans += 1
print(ans)
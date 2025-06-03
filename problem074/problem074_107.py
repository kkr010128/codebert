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

mod = 998244353

N, K = rl()
lr = []
for i in range(K):
	l, r = rl()
	lr.append((l,r))
lr.sort()

dp = [0] * (N+1)
dp[1] = 1
dp[2] = -1

ans = 0
s = 0
flags = [1] * K
for i in range(1, N+1):
	s += dp[i]
	s %= mod
	for k in range(K):
		if flags[k] == 0:
			break
		l, r = lr[k]
		if i+l <= N:
			dp[i+l] += s
			if i+r+1 <= N:
				dp[i+r+1] -= s
			else:
				ans += s
				ans %= mod
				break
		else:
			flags[k] = 0
			break
print(ans)


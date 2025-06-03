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
mod = 1000000007
sys.setrecursionlimit(1000000)
 
R, C, K = rl()
I = [[0]*(C+2) for _ in range(R+2)]
for i in range(K):
	r, c, v = rl()
	I[r][c] = v
 
dp = [[0]*4 for _ in range(C+2)]
dp2 = [[0]*4 for _ in range(C+2)]
 
for i in range(R+1):
	for j in range(C+1):
		for m in range(4):
			ni, nj = i, j+1
			dp[nj][m] = max(dp[nj][m], dp[j][m])
			if m < 3:
				dp[nj][m+1] = max(dp[nj][m+1], dp[j][m]+I[ni][nj])
			ni, nj = i+1, j
			dp2[nj][0] = max(dp2[nj][0], dp[j][m])
			dp2[nj][1] = max(dp2[nj][1], dp[j][m]+I[ni][nj])
	dp = dp2
	dp2 = [[0]*4 for _ in range(C+2)]
ans = 0
for m in range(4):
	ans = max(ans, dp[C][m])
print(ans)

from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from functools import lru_cache
import math

# setrecursionlimit(10**7)
rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')
MOD = 10**9 + 7

def main():
	n = int(rl())

	dp = [[[0 for k in range(2)] for j in range(2)] for i in range(n+1)]
	dp[0][0][0] = 1

	for i in range(n):
		for j in range(2):
			for k in range(2):
				for d in range(10):
					nj = j or d == 0
					nk = k or d == 9
					dp[i+1][nj][nk] += dp[i][j][k]
					dp[i+1][nj][nk] %= MOD 

	ans = dp[n][1][1]
	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()
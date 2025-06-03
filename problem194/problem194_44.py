import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
H, W = map(int, input().split())

I = [list(map(str, input())) for _ in range(H)]

dp = [[0] * W for _ in range(H)]

for i in range(H):
	for j in range(W):
		if i == 0 and j == 0:
			continue
		if i == 0:
			dp[i][j] = dp[i][j-1] if I[i][j] == I[i][j-1] else dp[i][j-1] + 1
			continue
		if j == 0:
			dp[i][j] = dp[i-1][j] if I[i][j] == I[i-1][j] else dp[i-1][j] + 1
			continue

		dp[i][j] = dp[i][j-1] if I[i][j] == I[i][j-1] else dp[i][j-1] + 1
		if I[i][j] == I[i-1][j]:
			dp[i][j] = min(dp[i][j], dp[i-1][j])
		else:
			dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)	

t = dp[-1][-1]
if I[0][0] == "#":
	t += 1
ans = -(-t//2)

print(ans)
		

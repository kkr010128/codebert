import sys
input = sys.stdin.readline
read = sys.stdin.read

n, t = map(int, input().split())
m = map(int, read().split())
AB = sorted(zip(m, m))
A, B = zip(*AB)
dp = [[0]*t for _ in range(n+1)]
for i, a in enumerate(A[:-1]):
  for j in range(t):
    if j < a:
      dp[i+1][j] = dp[i][j]
    else:
      dp[i+1][j] = max(dp[i][j-a]+B[i], dp[i][j])
ans = 0
maxB = [B[-1]]*n
for i in range(n-2, 0, -1):
  maxB[i] = max(B[i], maxB[i+1])
for i in range(n-1):
  ans = max(ans, dp[i+1][-1] + maxB[i+1])
print(ans)
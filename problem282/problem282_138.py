import sys
input = sys.stdin.readline
N, T = map(int, input().split())
a = []
for _ in range(N):
  w, v = map(int, input().split())
  a.append((w, v))
a.sort()
dp = [[0] * (T + 1) for _ in range(N + 1)]
for i in range(N):
  w, v = a[i]
  for j in range(T):
    if j + w >= T:
      dp[i + 1][T] = max(dp[i + 1][T], dp[i][j] + v)
    else:
      dp[i + 1][j + w] = max(dp[i + 1][j + w], dp[i][j] + v)
    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
  dp[i + 1][T] = max(dp[i + 1][T], dp[i][T])
print(max(dp[-1]))
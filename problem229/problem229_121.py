H, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
limit = H + max(A[i][0] for i in range(N))
dp = [int(1e18) for _ in range(limit+1)]
dp[0] = 0
for i in range(1, limit+1):
  for j in range(N):
    if A[j][0] > i:
      dp[i] = min(dp[i], A[j][1])
    else:
      dp[i] = min(dp[i], dp[i-A[j][0]]+A[j][1])
M = min(dp[i] for i in range(H, limit+1))
print(dp[H])

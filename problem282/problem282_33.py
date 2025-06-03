def solve():
  ans = 0
  N, T = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(N)]
  A.sort()
  dp = [[0]*(T+A[-1][0]) for _ in range(N+1)]
  for i in range(1,N+1):
    for t in range(1,T+A[-1][0]):
      if t<A[i-1][0] or t>=T+A[i-1][0]:
        dp[i][t] = max(dp[i-1][t],dp[i][t-1])
      else:
        dp[i][t] = max([dp[i-1][t],dp[i][t-1],dp[i-1][t-A[i-1][0]]+A[i-1][1]])
  ans = max(dp[-1])
  return ans
print(solve())
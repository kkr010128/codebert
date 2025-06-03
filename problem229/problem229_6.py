H, N = map(int, input().split())
AB = []
INF = 10**8 + 1

dp = [INF]*(H+1)
dp[0] = 0

for _ in range(N):
  a, b = map(int, input().split())
  AB.append((a, b))

for i in range(1, H+1):
  for j in range(N):
    dp[i] = min(dp[i], dp[max(0, i - AB[j][0])] + AB[j][1])

print(dp[-1])
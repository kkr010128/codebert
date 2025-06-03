H,N = map(int,input().split())
INF = 10 ** 10
dp = [INF] * (H + 1)
dp[0] = 0

for i in range(N):
  attack,magic = map(int,input().split())
  for j in range(len(dp)):
    if dp[j] == INF:
      continue
    target = j + attack
    if j + attack > H:
      target = H
    if dp[target] > dp[j] + magic:
      dp[target] = dp[j] + magic
      
print(dp[-1])
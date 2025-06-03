N, M, L = map(int, input().split())
INF = 10**12
dp = [[INF]*N for i in range(N)]
fp = [[INF]*N for i in range(N)]
for i in range(N):
  dp[i][i]=0
  fp[i][i]=0
k = [[0]*N for i in range(N)]
for i in range(M):
  a, b, c = map(int, input().split())
  dp[a-1][b-1] = c
  dp[b-1][a-1] = c

for i in range(N):
  for j in range(N):
    for h in range(N):
      dp[j][h] = min(dp[j][h], dp[j][i]+dp[i][h])

for j in range(N):
  for h in range(N):
    if dp[j][h]<=L:
      fp[j][h] = 1
for i in range(N):
  for j in range(N):
    for h in range(N):
      fp[j][h] = min(fp[j][h], fp[j][i]+fp[i][h])
Q = int(input())
for i in range(Q):
  s, t = map(int, input().split())
  s = s-1
  t = t-1
  if fp[s][t]==INF:
    print(-1)
  else:
    print(fp[s][t]-1)


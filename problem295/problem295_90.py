n, m, l = map(int, input().split())
x = [[] for _ in range(n)]
dp = [[n*10**9 for _ in range(n)] for _ in range(n)]
for _ in range(m):
  a, b, c = map(int, input().split())
  if c <= l:
    x[a-1].append(b-1)
    x[b-1].append(a-1)
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
q = int(input())
st = []
for _ in range(q):
  st.append(list(map(int, input().split())))
dp[0][0] = 0
for i in range(1,n):
  dp[i][i] = 0
  for j in range(i):
    for a in x[i]:
      dp[i][j] = min(dp[i][j],dp[i][a]+dp[a][j])
    dp[j][i] = dp[i][j]
  for j in range(i):
    for k in range(i):
      dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])
dp2 = [[n for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if dp[i][j] <= l:
      dp2[i][j] = 1
for i in range(1,n):
  for j in range(i):
    for k in range(i):
      dp2[i][j] = min(dp2[i][j],dp2[i][k]+dp2[k][j])
    dp2[j][i] = dp2[i][j]
  for j in range(i):
    for k in range(i):
      dp2[j][k] = min(dp2[j][k],dp2[j][i]+dp2[i][k])
for u in st:
  ans = dp2[u[0]-1][u[1]-1]
  if ans >= n:
    print(-1)
  else:
    print(ans-1)
N, T = map(int, input().split())
# 1-index
A = [0]
B = [0]
for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

# dp1[i][j] 1 ~ i の料理で j 分以内に完食できる美味しさの合計の最大値
# dp2[i][j] i ~ N の料理で j 分以内に〃
# max(DP1[i − 1][j] + DP2[i + 1][T − 1 − j]) i番目以外で T - 1 以内

dp1 = [[0] * T for _ in range(N+2)]
dp2 = [[0] * T for _ in range(N+2)]
for i in range(1, N+1):
  for j in range(T):
    dp1[i][j] = dp1[i-1][j]
    if j - A[i] >= 0:
      dp1[i][j] = max(dp1[i][j], dp1[i-1][j - A[i]] + B[i])

for i in range(N, 0, -1):
  for j in range(T):
    dp2[i][j] = dp2[i+1][j]
    if j - A[i] >= 0:
      dp2[i][j] = max(dp2[i][j], dp2[i+1][j - A[i]] + B[i])      

ans = 0
for i in range(1, N+1):
  for j in range(T):
    ans = max(ans, dp1[i-1][j] + B[i] + dp2[i+1][T - 1 - j])

print(ans)
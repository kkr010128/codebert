n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

max = max(m)

dp = [[0 for _ in range(max + 1)] for __ in range(n + 1)]
dp[0][0] = 1#[1 for _ in range(max + 1)]
for j in range(n):
  for k in range(max + 1):
    if k >= A[j] and dp[j][k - A[j]]:
      dp[j + 1][k] = 1
    elif dp[j][k]:
      dp[j + 1][k] = 1
for i in range(q):
  if dp[n][m[i]]:
     print("yes")
  else:
    print("no")

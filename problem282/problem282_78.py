def ints():
  return [int(x) for x in input().split()]
def ii():
  return int(input())

N, T = ints()
dp = [[0]*T for j in range(N+1)]
F = sorted([ints() for i in range(N)])

for i in range(N):
  a, b = F[i]

  for t in range(T):
    dp[i+1][t] = max(dp[i+1][t], dp[i][t])
    nt = t+a
    if nt<T:
      dp[i+1][nt] = max(dp[i+1][nt], dp[i][t]+b)

w = max([F[i][1] + dp[i][T-1] for i in range(1, N)])
print(w)

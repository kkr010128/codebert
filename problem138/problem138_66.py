N, S = map(int, input().split())
As = list(map(int, input().split()))

P = 998244353

memo = [[0 for _ in range(N+1)] for _ in range(S+1)]

for i in range(N+1):
  memo[0][i] = (2**i) % P

for i, a in enumerate(As):
  for j in range(S+1):
    if j - a < 0:
      memo[j][i+1] = memo[j][i]*2 % P
    else:
      memo[j][i+1] = (memo[j][i]*2 + memo[j-a][i]) % P

print(memo[S][N])
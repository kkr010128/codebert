import sys
readline = sys.stdin.readline

DIV = 998244353
N,S = map(int,readline().split())
A = list(map(int,readline().split()))

# ある数の取り得る状態は以下
# (1)部分集合Pに含まれない
# (2)部分集合Pに含まれ、和に使われている
# (3)部分集合Pに含まれ、和に使われていない

# dp[j][k] = 部分集合Pに含まれ(j)、総和がkになっている場合の数
dp = [[0] * (S + 1) for j in range(2)]
dp[0][0] = 1

for i in range(N):
  nextline = [[0] * (S + 1) for j in range(2)]
  for k in range(S, -1, -1):
    # (1)部分集合Pに含まれない
    nextline[0][k] += dp[0][k]
    nextline[0][k] += dp[1][k]
    nextline[0][k] %= DIV

    # (2)部分集合Pに含まれ、和に使われている
    if k + A[i] <= S:
      nextline[1][k + A[i]] += dp[0][k]
      nextline[1][k + A[i]] += dp[1][k]
      nextline[1][k + A[i]] %= DIV

    # (3)部分集合Pに含まれ、和に使われていない
    nextline[1][k] += dp[0][k]
    nextline[1][k] += dp[1][k]
    nextline[1][k] %= DIV
    
  dp = nextline

print((dp[0][-1] + dp[1][-1]) % DIV)

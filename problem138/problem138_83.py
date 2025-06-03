import sys
readline = sys.stdin.readline

DIV = 998244353
N,S = map(int,readline().split())
A = list(map(int,readline().split()))

# ある数の取り得る状態は以下
# (1)部分集合Pに含まれない
# (2)部分集合Pに含まれ、和に使われている
# (3)部分集合Pに含まれ、和に使われていない

# dp[k] = 総和がkになっている場合の数
dp = [0] * (S + 1)
dp[0] = 1

for i in range(N):
  nextline = [0] * (S + 1)
  for k in range(S, -1, -1):
    # (1)部分集合Pに含まれない
    # (3)部分集合Pに含まれ、和に使われていない
    nextline[k] += dp[k] * 2
    nextline[k] %= DIV

    # (2)部分集合Pに含まれ、和に使われている
    if k + A[i] <= S:
      nextline[k + A[i]] += dp[k]
      nextline[k + A[i]] %= DIV
    
  dp = nextline

print(dp[-1])

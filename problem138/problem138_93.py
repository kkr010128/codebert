# 解説AC
# Tの部分集合をUとすると
# A[i]番目の項目について、
# (1)Tに選ばれない
# (2)Uに選ばれない
# (3)Uに選ばれる
# の3通りの遷移がある
# (1)(2)の場合も含めて数え上げていく（その場合、和は変わらない）

import sys
readline = sys.stdin.readline

N,S = map(int, readline().split())
A = list(map(int,readline().split()))
DIV = 998244353

dp = [0] * (S + 1)
dp[0] = 1
for i in range(N):
  newline = [0] * (S + 1)
  for j in range(len(dp)):
    # 選択肢(1)(2)の場合
    newline[j] += dp[j] * 2
    newline[j] %= DIV
    # 選択肢(3)の場合
    if j + A[i] <= S:
      newline[j + A[i]] += dp[j]
      newline[j + A[i]] %= DIV
  dp = newline

print(dp[S])
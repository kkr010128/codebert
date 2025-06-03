# コード整理

import sys
from operator import itemgetter

input = sys.stdin.readline

#################
# 定数
#################
TIME = 0
VAL = 1

##################
# 入力処理
##################
N, T = [int(a) for a in input().split()]
time_value = [(-1, -1)] + [tuple(int(a) for a in input().split()) for _ in range(N)]

# Sort the array in the increasing order of value
time_value.sort(key = itemgetter(VAL))

###########################
# 動的計画法（Knapsack problem）のテーブル埋め
# 時間の最大値は T - 1
##########################
dp = [[-1] * T for _ in range(N + 1)] # (N+1)行 x T列 2次元リスト

for t in range(0, T):
    dp[0][t] = 0

for n in range(1, N + 1):
    dp[n][0] = 0
    for t in range(1, T):
        if time_value[n][TIME] > t:
            dp[n][t] = dp[n - 1][t]
        else:
            dp[n][t] = max(dp[n - 1][t],
                             time_value[n][VAL] + dp[n - 1][t - time_value[n][TIME]])

##########################
# DPテーブルを用いて問題を解く
##########################

# t = T - 1に食べ始める料理が N, N-1, N-2, ..., 2, 1それぞれの場合で
# 美味しさの最大値を出し、更にその最大値を取る

# 最後に食べる料理がNの場合
val_acum = time_value[N][VAL]
t = T - 1  # N以外の料理を食べるのに使える時間
max_val = val_acum + dp[N - 1][t]

for n in range(N - 1, 0, -1):  # 最後に食べる料理が n = N-1, N-2, ..., 2, 1の場合
    val_acum += time_value[n][VAL] # 料理 N, N-1, ..., nの美味しさ合計
    t -= time_value[n + 1][TIME] # その他の料理 1, 2, ..., n-1を食べるのに使える時間
    if t < 0:
        break
    else:
        max_val = max(max_val, val_acum + dp[n - 1][t])

print(max_val)

MOD = 998244353
N, S = map(int, input().split())
A = list(map(int, input().split()))
DP = [[0] * (1 + S) for _ in range(1 + N)]  # DP[i][j] はi番目までみた時に総和がjと成る組み合わせの総和
# 初期化
DP[0][0] = 1
# 漸化式　DP[i][j] = DP[i-1][j]*2 + DP[i-1][j-A[i]]
for i in range(1, N + 1):
    for j in range(S + 1):
        if j >= A[i - 1]:
            DP[i][j] = DP[i - 1][j] * 2 + DP[i - 1][j - A[i - 1]]
        else:
            DP[i][j] = DP[i - 1][j] * 2
        DP[i][j] %= MOD
print(DP[N][S])

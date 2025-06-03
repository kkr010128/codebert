# 解説AC
import sys
input = sys.stdin.buffer.readline

n = int(input())
A = list(map(int, input().split()))
B = []
for i, e in enumerate(A):
    B.append((e, i + 1))
B.sort(reverse=True)
# dp[i][j]: Aiまで入れた時、左にj個決めた時の最大値
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(i + 1):  # 左の個数
        k = i - j  # 右の個数
        ni = i + 1
        val, idx = B[i]
        dp[ni][j] = max(dp[ni][j], dp[i][j] + abs(n - k - idx) * val)
        dp[ni][j + 1] = max(dp[ni][j + 1], dp[i][j] + abs(idx - (j + 1)) * val)
ans = 0
for i in range(n + 1):
    ans = max(ans, dp[n][i])
print(ans)

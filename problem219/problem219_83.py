import sys
input = sys.stdin.readline

N = [int(x) for x in input().rstrip()][::-1] + [0]
L = len(N)

dp = [[10 ** 18, 10 ** 18] for _ in range(L + 1)]
dp[0] = [0, 0]
dp[1] = [N[0], 10 - N[0]]

for i in range(2, L + 1):
    n = N[i - 1]
    dp[i][0] = min(dp[i - 1][0] + n, dp[i - 1][1] + (n + 1))
    dp[i][1] = min(dp[i - 1][0] + (10 - n), dp[i - 1][1] + (10 - (n + 1)))

print(dp[-1][0])

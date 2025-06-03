N = '0' + input()
INF = float('inf')
dp = [[INF] * 2 for _ in range(len(N) + 1)]
dp[0][0] = 0

for i in range(len(N)):
    n = int(N[len(N) - 1 - i])
    for j in range(2):
        for a in range(10):
            ni = i + 1
            nj = 0
            b = a - n - j
            if b < 0:
                b += 10
                nj = 1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + a + b)
            a == b

print(dp[len(N)][0])

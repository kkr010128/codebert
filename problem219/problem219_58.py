N = input()
INF = 10 ** 9
N = N[::-1] + '0'
dp = [[INF for _ in range(2)] for _ in range(len(N) + 1)]
dp[0][0] = 0

for i in range(len(N)):
    for j in range(2):
        x = int(N[i])
        x += j
        for k in range(10):
            nexti = i + 1
            nextj = 0
            b = k - x
            if b < 0:
                nextj = 1
                b += 10
            dp[nexti][nextj] = min(dp[nexti][nextj], dp[i][j] + k + b)
print(dp[len(N)][0])
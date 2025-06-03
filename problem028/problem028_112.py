if __name__ == "__main__":
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    c = sorted(c)

    dp = [[0] * (n + 1)] * m

    for i in range(n + 1):
        dp[0][i] = i
    
    for i in range(1, m):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
            if j - c[i] >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - c[i]] + 1)
    print(dp[m-1][n])
        

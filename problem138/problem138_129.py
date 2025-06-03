def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [[0]*(s+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n+1):
        ai = a[i-1]
        for j in range(s+1):
            dp[i][j] += dp[i-1][j]*2
            if j >= ai:
                dp[i][j] += dp[i-1][j-ai]
            dp[i][j] %= mod
    print(dp[n][s])
            

if __name__ == "__main__":
    main()
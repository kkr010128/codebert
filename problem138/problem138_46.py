def main():
    N, S = map(int, input().split())
    A = tuple(map(int, input().split()))

    MOD = 998244353

    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    # morau
    for i, a in enumerate(A):
        dp[i][0] = pow(2, i, MOD)
            
        for j in range(S+1):
            if j >= a:
                dp[i+1][j] = 2 * dp[i][j]
                dp[i+1][j] %= MOD
                dp[i+1][j] += dp[i][j-a]
                dp[i+1][j] %= MOD
            else:
                dp[i+1][j] = 2 * dp[i][j]
                dp[i+1][j] %= MOD
                

    print(dp[N][S])
if __name__ == "__main__":
    main()
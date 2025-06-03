def main():
    MOD = 998244353
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i, a in enumerate(A):
        n = i + 1
        for s in range(S + 1):
            dp[n][s] += 2 * dp[n - 1][s]
            if s - a >= 0:
                dp[n][s] += dp[n - 1][s - a]
            dp[n][s] %= MOD
    print(dp[N][S])


if __name__ == '__main__':
    main()

def main():
    N, K = map(int, input().split())

    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353

    dp = [0]*(N+1)
    S = [0]*(N+1)
    dp[1] = 1
    S[1] = 1

    for i in range(2, N+1):
        for l, r in LR:
            if i-l < 0:
                continue
            else:
                dp[i] += S[i-l] - S[max(i-r-1, 0)]
        dp[i] %= MOD
        S[i] = S[i-1] + dp[i]
    print(dp[-1]%MOD)

if __name__ == '__main__':
    main()

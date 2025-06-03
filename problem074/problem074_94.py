MOD = 998244353


def main():
    # もらうdp + 累積和
    N, K = (int(i) for i in input().split())
    LR = [[int(i) for i in input().split()] for j in range(K)]

    dp = [0] * (N+2)
    dpsum = [0] * (N+1)
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2, N+1):
        for le, ri in LR:
            L = max(0, i - ri - 1)
            R = i - le
            if R < 1:
                continue
            dp[i] += dpsum[R] - dpsum[L]
            dp[i] %= MOD
        dpsum[i] += dpsum[i-1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])
    # print(dpsum)


if __name__ == '__main__':
    main()

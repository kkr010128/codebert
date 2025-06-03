def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    dp = [0] * (n + 1)
    dp[1] = 1
    dpsum = [0] * (n + 1)
    dpsum[1] = 1
    mod = 998244353

    for i in range(2, n + 1):
        for j in range(k):
            li = max(i - lr[j][1], 1)
            ri = i - lr[j][0]
            if ri < 0:
                continue
            dp[i] = (dp[i] + dpsum[ri] - dpsum[li - 1]) % mod
        dpsum[i] = dpsum[i - 1] + dp[i]

    print(dp[-1] % mod)


if __name__ == "__main__":
    main()

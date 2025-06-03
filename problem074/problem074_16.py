def resolve():
    n, k = map(int, input().split())
    S = []
    L, R = [], []
    for _ in range(k):
        l1, r1 = map(int, input().split())
        L.append(l1)
        R.append(r1)

    dp = [0 for i in range(n + 1)]
    dpsum = [0 for i in range(n + 1)]
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            Li = i - R[j]
            Ri = i - L[j]
            if Ri < 0:
                continue
            Li = max(1, Li)
            dp[i] += dpsum[Ri] - dpsum[Li - 1]  # dp[Li] ~ dp[Ri]
            dp[i] %=  998244353

        dpsum[i] = (dpsum[i - 1] + dp[i]) % 998244353

    print(dp[n])

resolve()
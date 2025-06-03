def resolve():
    X = int(input())
    dp = [0 for _ in range(X + 110)]
    dp[0] = 1
    for i in range(X + 1):
        if dp[i] == 0:
            continue
        dp[i + 100] = 1
        dp[i + 101] = 1
        dp[i + 102] = 1
        dp[i + 103] = 1
        dp[i + 104] = 1
        dp[i + 105] = 1
    print(dp[X])


resolve()

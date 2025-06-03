S = int(input())
if S == 1 or S == 2:
    print(0)

elif S == 3:
    print(1)

else:
    mod = 10 ** 9 + 7
    dp = [0 for _ in range(S)]
    dp[0] = dp[1] = 0
    dp[2] = dp[3] = 1

    for i in range(3, S):
        dp[i] = (dp[i - 3] + dp[i - 1]) % mod

    print(dp[-1])
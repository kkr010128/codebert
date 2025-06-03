def main():
    s = int(input())
    mod = 10**9 + 7

    dp = [0] * (s+1)
    dp[0] = 1
#    for i in range(1, s+1):
#        for j in range(0, (i-3)+1):
#            dp[i] += dp[j]
#            dp[i] %= mod
    for i in range(1, s+1):
        if i < 3:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-3]
            dp[i] %= mod

    print(dp[-1])


if __name__ == "__main__":
    main()

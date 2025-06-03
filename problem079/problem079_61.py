def main():
    MOD = 1000000007
    s = int(input())
    dp = [0] * (s + 1)
    dp[0] = 1
    tot = 0
    for i in range(1, s + 1):
        if i >= 3:
            tot += dp[i - 3]
            tot %= MOD
        dp[i] = tot
    print(dp[s])

if __name__ == '__main__':
    main()
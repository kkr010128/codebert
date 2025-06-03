MOD = int(1e9+7)


def main():
    S = int(input())
    dp = [[0] * (S+1) for _ in range(S//3+2)]
    for i in range(3, S+1):
        dp[1][i] = 1
    for i in range(2, S//3+2):
        sm = sum(dp[i-1]) % MOD
        sm = (sm - sum(dp[i-1][S-2:S+1])) % MOD
        for j in range(3*i, S+1)[::-1]:
            dp[i][j] = sm
            sm = (sm - dp[i-1][j-3]) % MOD
    ans = 0
    for i in range(S//3+2):
        ans = (ans + dp[i][S]) % MOD
    print(ans)


if __name__ == "__main__":
    main()

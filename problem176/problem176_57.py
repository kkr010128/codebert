MOD = int(1e9+7)


def main():
    N, K = map(int, input().split())
    dp = [0] * (K+1)
    ans = 0
    for i in range(1, K+1)[::-1]:
        tmp = pow(K//i, N, MOD)
        for j in range(i*2, K+1, i):
            tmp = (tmp - dp[j]) % MOD
        dp[i] = tmp
        ans = (ans + tmp * i) % MOD
    print(ans)


if __name__ == "__main__":
    main()

#!python3

LI = lambda: list(map(int, input().split()))

# input
N, S = LI()
A = LI()

MOD = 998244353


def main():
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(N):
        dp, l = [0] * (S + 1), dp
        for j in range(S + 1):
            dp[j] = (dp[j] + 2 * l[j]) % MOD
            if A[i] + j <= S:
                dp[A[i] + j] = (dp[A[i] + j] + l[j]) % MOD
    
    ans = dp[-1]
    print(ans)


if __name__ == "__main__":
    main()

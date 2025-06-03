import sys


def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    L = [0] * 10
    R = [0] * 10
    for i in range(K):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        L[i], R[i] = l, r

    dp = [0] * (N + 1)
    up = [0] * (N + 1)
    up[0] = 1
    up[1] = -1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + up[i - 1]
        for j in range(K):
            if i + (L[j] - 1) < N + 1:
                up[i + (L[j] - 1)] += dp[i]
            if i + R[j] < N + 1:
                up[i + R[j]] -= dp[i]
        dp[i] %= 998244353

    print(dp[N])


main()

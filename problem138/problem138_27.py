import sys
from functools import lru_cache

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    MOD = 998244353
    N, S, *A = map(int, read().split())

    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for s in range(S + 1):
            dp[i + 1][s] += 2 * dp[i][s]
            dp[i + 1][s] %= MOD
            if s - A[i] >= 0:
                dp[i + 1][s] += dp[i][s - A[i]]
                dp[i + 1][s] %= MOD

    print(dp[N][S])
    return


if __name__ == '__main__':
    main()

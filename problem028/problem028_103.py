# -*- coding:utf-8 -*-

def solve():
    import sys

    N, M = list(map(int, sys.stdin.readline().split()))
    Cs = list(map(int, sys.stdin.readline().split()))

    dp = [float("inf") for _ in range(N+1)]  # dp[i] := i円を作ることができるコインの最小枚数
    dp[0] = 0

    for c in Cs:
        for i in range(c, N+1):
            dp[i] = min(dp[i], dp[i-c]+1)
    print(dp[N])


if __name__ == "__main__":
    solve()


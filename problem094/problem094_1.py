import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    R, C, K = NMI()
    item = [[0] * (C + 1) for i in range(R + 1)]

    for i in range(K):
        r_, c_, v_, = NMI()
        item[r_ - 1][c_ - 1] = v_

    dp = [[[0 for _ in range(C + 2)] for _ in range(R + 2)] for _ in range(4)]

    for i in range(R + 1):
        for j in range(C + 1):
            for k in range(4):
                a = dp[k][i][j]
                v = item[i][j]

                if k == 3:
                    dp[0][i + 1][j] = max(a, dp[0][i + 1][j])
                    continue
                dp[0][i + 1][j] = max(a, a + v, dp[0][i + 1][j])
                dp[k][i][j + 1] = max(a, dp[k][i][j + 1])
                dp[k + 1][i][j + 1] = max(a + v, dp[k + 1][i][j + 1])

    print(max(dp[0][R][C], dp[1][R][C], dp[2][R][C], dp[3][R][C]))

if __name__ == "__main__":
    main()
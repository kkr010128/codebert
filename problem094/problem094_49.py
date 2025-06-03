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


def make_grid_int(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    R, C, K = NMI()
    grid = make_grid_int(R, C, 0)
    for i in range(K):
        r, c, v = NMI()
        grid[r-1][c-1] = v

    dp = [[[0 for _ in range(C+2)] for _ in range(R+2)] for _ in range(4)]

    for r in range(R+1):
        for c in range(C+1):
            for i in range(4):
                now = dp[i][r][c]
                try:
                    val = grid[r][c]
                except:
                    val = 0

                if i == 3:
                    # 取らずに下
                    dp[0][r + 1][c] = max(now, dp[0][r + 1][c])
                    continue

                # 取って下
                dp[0][r+1][c] = max(now + val, dp[0][r+1][c])
                # 取らずに下
                dp[0][r+1][c] = max(now, dp[0][r+1][c])
                # 取って横
                dp[i+1][r][c+1] = max(now + val, dp[i+1][r][c+1])
                # 取らずに横
                dp[i][r][c+1] = max(now, dp[i][r][c+1])

    print(max(dp[0][R][C], dp[1][R][C], dp[2][R][C], dp[3][R][C]))


if __name__ == "__main__":
    main()

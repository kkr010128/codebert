import numpy as np
import numba

@numba.njit("(i8,i8,i8,i8[:,:])", cache=True)
def solve(R, C, K, RCV):
    # dp[y][x][n]
    M = np.zeros((R+1, C+1), dtype=np.int64)
    for i in range(K):
        r, c, v = RCV[i]
        M[r, c] = v
    dp = np.zeros((R+1, C+1, 4), dtype=np.int64)
    for y in range(1, R+1):
        for x in range(1, C+1):
            for n in range(4):
                if n == 0:
                    dp[y, x, n] = max(
                        dp[y, x-1, 0],
                        dp[y-1, x, :].max()
                    )
                if n > 0:
                    dp[y, x, n] = max(
                        dp[y, x-1, n],
                        dp[y, x-1, n-1] + M[y, x],
                        dp[y-1, x, :].max() + M[y, x]
                    )
    ans = dp[R, C].max()
    print(ans)

import sys
def main():
    R, C, K = map(int, input().split())
    RCV = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(K, 3)
    solve(R, C, K, RCV)

main()

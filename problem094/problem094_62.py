import sys
import numpy as np
from numba import njit, void, i8
input = sys.stdin.buffer.readline

def main():
    R, C, K = map(int, input().split())
    cell = np.full((R+1, C+1), 0, dtype=np.int64)
    for i in range(K):
        x, y, c = map(int, input().split())
        cell[x-1, y-1] = c
    print(calc(cell, R, C))

@njit(i8(i8[:,:],i8,i8))
def calc(cell, R, C):
    L_INF = int(1e17)
    dp = np.full((R+1, C+1, 4), -L_INF, dtype=np.int64)
    dp[0, 1, 0] = dp[1, 0, 0] = 0
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            for k in range(4):
                dp[i, j, k] = max(dp[i, j, k], dp[i, j-1, k])
                if k > 0:
                    dp[i, j, k] = max(dp[i, j, k], dp[i, j, k-1])
                    dp[i, j, k] = max(dp[i, j, k], dp[i, j-1, k-1] + cell[i-1, j-1])
                if k == 1:
                    dp[i, j, 1] = max(dp[i, j, 1], dp[i-1, j, 3] + cell[i-1, j-1])
    return dp[R, C, 3]

if __name__ == "__main__":
    main()

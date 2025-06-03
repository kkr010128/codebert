import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], ), cache=True)
def main(S):
    N = len(S)
    L = np.empty(N, np.int64)
    R = np.empty(N, np.int64)

    x = y = 0
    n = 0
    for s in S:
        if s == 0:
            y += 1
        elif s == 1:
            if y:
                y -= 1
            else:
                x += 1
        else:
            L[n], R[n] = x, y
            n += 1
            x = y = 0

    L, R = L[:n], R[:n]
    L1, R1 = L[L > R], R[L > R]
    L2, R2 = L[L <= R], R[L <= R]

    ind = R1.argsort()
    L1, R1 = L1[ind], R1[ind]

    ind = L2.argsort()[::-1]
    L2, R2 = L2[ind], R2[ind]

    L = np.concatenate((L1, L2))
    R = np.concatenate((R1, R2))

    n = 0
    for i in range(len(L)):
        if n < R[i]:
            return False
        n += L[i] - R[i]
    return n == 0

N = int(readline())
S = np.array(list(read()), np.int64) - ord('(')

print('Yes' if main(S) else 'No')
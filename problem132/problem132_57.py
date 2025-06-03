import sys

from numba import njit

import numpy as np

readline = sys.stdin.buffer.readline


@njit('i8[:](i8, i8, i8[:])', cache=True)
def f(N, K, A):
    for i in range(min(K, 100)):
        C = np.zeros(N + 1, dtype=np.int64)

        for j, a in enumerate(A):
            l = max(0, j - a)
            r = min(j + a + 1, N)
            C[l] += 1
            C[r] -= 1

        A = np.cumsum(C)

    return A


def solver():
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    A = f(N, K, np.array(A))
    print(*A[:-1])


solver()

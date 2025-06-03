import numpy as np
from numba import njit


@njit('i8[:](i8,i8,i8[:])')
def solve(N, K, A):
    for _ in range(K):
        B = np.zeros(N + 1, dtype=np.int64)
        for i in range(N):
            a = A[i]
            B[max(0, i - a)] += 1
            B[min(N, i + a + 1)] -= 1
        A = np.cumsum(B)[:-1]
        if np.all(A == N):
            return A
    return A


N, K = map(int, input().split())
A = np.array(input().split(), dtype=int)
print(' '.join(map(str, solve(N, K, A))))
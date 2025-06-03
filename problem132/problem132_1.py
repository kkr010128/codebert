import sys
input = sys.stdin.readline
import numpy as np
from numba import njit


def read():
    N, K = map(int, input().strip().split())
    A = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
    return N, K, A


@njit
def solve(N, K, A):
    d = np.empty(N+1, dtype=np.int32)

    for k in range(K):
        for i in range(N):
            d[i] = 0
        
        for i in range(N):
            l = max(0, i-A[i])
            r = min(N, i+1+A[i])
            d[l] += 1
            d[r] -= 1
        
        terminate = True
        v = 0
        for i in range(N):
            v += d[i]
            A[i] = v
            if terminate and A[i] < N:
                terminate = False
        if terminate:
            break
    return A


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    print(*outputs)

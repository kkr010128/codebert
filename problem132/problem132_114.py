import numpy as np
from numba import njit

(N, K) = map(int, input().split())
A = np.array(list(map(int, input().split())))

@njit
def solve(N,K,A):
    for j in range(0, K):
        B = np.zeros(N, dtype=np.int64)

        for i in range(0,N):
            f = max(0, i - A[i])
            t = min(N-1, i + A[i])
            #for j in range(max(0, f), min(N, t)+1):
            #    B[j] += 1
            B[f] += 1
            if t+1 < N:
                B[t+1] -= 1
        A = np.cumsum(B)
        if np.all(A == N):
            return A
        i += 1
    return A
    

print(" ".join(map(str, solve(N,K,A))))
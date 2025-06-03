import numpy as np

from numba import njit


@njit("i8[:](i8, i8[:], i8[:])", cache=True)
def cumsum(K, A, cA):
    for i, a in enumerate(A):
        cA[i] += cA[i - 1] + A[i]
        if cA[i] > K:
            break

    cA = cA[cA != 0]
    cA = np.append(0, cA)
    return cA


@njit("i8(i8, i8[:], i8[:])", cache=True)
def solve(K, cA, cB):
    ans = np.searchsorted(cA, K - cB, side="right") - 1
    ans += np.arange(len(cB))
    return ans.max()


N, M, K = map(int, input().split())
A = np.array(input().split(), dtype=np.int64)
B = np.array(input().split(), dtype=np.int64)

cA = np.zeros(N, dtype=np.int64)
cB = np.zeros(M, dtype=np.int64)

# np.cumsumだとoverflowする
cA = cumsum(K, A, cA)
cB = cumsum(K, B, cB)

ans = solve(K, cA, cB)
print(ans)

import numpy as np

from numba import njit


@njit("i8[:](i8, i8[:], i8[:])", cache=True)
def cumsum(K, L, cL):
    for i, a in enumerate(L):
        cL[i] = cL[i - 1] + L[i]
        if cL[i] > K:
            cL[i] = 0
            break

    cL = cL[cL != 0]
    cL = np.append(0, cL)
    return cL


@njit("i8(i8, i8[:], i8[:])", cache=True)
def solve(K, A, cB):
    ans_max = 0
    for i, a in enumerate(A):
        ans = 0
        K -= a
        ind = np.searchsorted(cB, K, side="right") - 1
        ans = i + ind

        if ans > ans_max:
            ans_max = ans

        if ind == 0 or K < 0:
            break

    return ans_max


N, M, K = map(int, input().split())
A = np.array(input().split(), dtype=np.int64)
B = np.array(input().split(), dtype=np.int64)

cA = np.zeros(N, dtype=np.int64)
cB = np.zeros(M, dtype=np.int64)

# np.cumsumだとoverflowする
cA = cumsum(K, A, cA)
cB = cumsum(K, B, cB)

A = np.append(0, A)
ans = solve(K, A, cB)
print(max(ans, len(cA) - 1, len(cB) - 1))

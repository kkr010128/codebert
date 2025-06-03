import numpy as np
from numba import njit

@njit('i8,i8,i8[::1]',cache=True)
def solve(N,K,A):
    for i in range(K):
        br = np.zeros(N+1, dtype=np.int64)

        for ind, rux in enumerate(A):
            br[max(ind-rux,0)] += 1
            br[min(ind+rux+1,N)] -= 1
        A = br.cumsum()[:-1]

        if br[0] == N and br[-1] == -N:
            return A
    return A


if __name__ == "__main__":
    n,k = map(int, input().split())
    a = np.array(list(map(int, input().split())),dtype=np.int64)
    ans = solve(n,k,a)
    print(*ans)

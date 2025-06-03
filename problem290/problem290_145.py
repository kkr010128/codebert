import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8(i8,i8[:],i8[:])", cache=True)
def binary_search(K, A, F):
    """Meguru type binary search"""
    ng = -1
    ok = A[-1] * F[0]

    def is_ok(A, F, K, x):
        count = 0
        for a, f in zip(A, F):
            count += max(0, a - x // f)
        return count <= K

    while (ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(A, F, K, mid):
            ok = mid
        else:
            ng = mid

    return ok


def main():
    N, K = map(int, input().split())
    A = np.array(input().split(), dtype=np.int64)
    F = np.array(input().split(), dtype=np.int64)

    A.sort()
    F[::-1].sort()

    ans = binary_search(K, A, F)
    print(ans)


if __name__ == "__main__":
    main()

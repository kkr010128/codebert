import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8(i8[:], i8)", cache=True)
def binary_search(a, key):
    """Meguru type binary search"""
    ng = -1
    ok = len(a)

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] >= key:
            ok = mid
        else:
            ng = mid

    return ok


@nb.njit("i8(i8, i8[:])", cache=True)
def solve(N, L):
    L.sort()
    ans = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            c = binary_search(L, L[a] + L[b]) - 1
            ans += c - b
    return ans


def main():
    N = int(input())
    L = np.array(input().split(), dtype=np.int64)

    ans = solve(N, L)
    print(ans)


if __name__ == "__main__":
    main()

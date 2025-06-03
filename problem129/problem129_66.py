import sys
from collections import Counter

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8(i8[:],i8[:])", cache=True)
def solve(keys, values):
    MAX_A = 10 ** 6
    divisible = [False] * (MAX_A + 1)
    ans = 0
    for k, v in zip(keys, values):
        if v == 1 and not divisible[k]:
            ans += 1
        for i in range(k, MAX_A + 1, k):
            divisible[i] = True
    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    c = Counter(A)
    keys = np.array(tuple(c.keys()), dtype=np.int64)
    values = np.array(tuple(c.values()), dtype=np.int64)

    ans = solve(keys, values)
    print(ans)


if __name__ == "__main__":
    main()

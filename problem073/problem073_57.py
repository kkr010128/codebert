#!/usr/bin/env python3
import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

input = sys.stdin.readline


def I():
    return int(input())


@njit((i8,), cache=True)
def main(n):
    table = np.zeros(n, np.int64)

    for i in range(1, n):
        table[::i] += 1

    ans = 0
    for n in table[1:]:
        q, r = divmod(n, 2)
        ans += q * 2 + 1 * r

    return ans


N = I()

print(int(main(N)))

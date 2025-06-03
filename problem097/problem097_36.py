import sys
import numpy as np  # noqa
import numba  # noqa
from numba import njit, b1, i4, i8, f8  # noqa

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


@njit((i8, ), cache=True)
def main(K):
    for i in range(K):
        if i == 0:
            a = 7 % K
        else:
            a = (a * 10 + 7) % K
        if a == 0:
            return i + 1

    return -1


K = int(readline())

print(main(K))

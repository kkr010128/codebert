import numba
from numba import njit, b1, i4, i8, f8
import numpy as np  # noqa

N = int(input())
A = np.array([int(x) for x in input().split()], dtype=np.int32)


@njit((i4[:], ), cache=True)
def main(A):
    count = np.zeros(10**6 + 10, np.int32)
    for x in A:
        if count[x] > 1:
            continue
        count[::x] += 1
    ret = 0
    for x in A:
        ret += count[x] == 1
    return ret


print(main(A))

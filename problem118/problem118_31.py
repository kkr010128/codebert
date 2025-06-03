import numpy as np
from numba import njit


@njit('i8(i8)', cache=True)
def solve(x):
    count = np.zeros(x + 1, dtype=np.int64)
    for i in range(1, x + 1):
        for j in range(i, x + 1, i):
            count[j] += j
    return count.sum()


if __name__ == "__main__":
    x = int(input())
    print(solve(x))


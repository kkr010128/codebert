# coding: utf-8
import numpy as np
from numba import i8, njit


@njit(i8[:](i8, i8[:]), cache=True)
def f(k, A):
    n = len(A)
    cur = A
    for _ in range(k):
        prev = cur
        cur = np.zeros_like(A)
        for x, p in enumerate(prev):
            cur[max(0, x-p)] += 1
            if x+p+1 < n:
                cur[x+p+1] -= 1

        satulated = True
        for i in range(1, n):
            cur[i] += cur[i-1]
            satulated &= cur[i] == n
        if satulated:
            break
    return cur


def solve(*args: str) -> str:
    n, k = map(int, args[0].split())
    A = np.array(tuple(map(int, args[1].split())))
    return ' '.join(map(str, f(k, A)))


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))

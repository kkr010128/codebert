import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

uf_t = numba.types.UniTuple(i8[:], 2)


@njit((uf_t, i8), cache=True)
def find_root(uf, x):
    root = uf[0]
    while root[x] != x:
        root[x] = root[root[x]]
        x = root[x]
    return x


@njit((uf_t, i8, i8), cache=True)
def merge(uf, x, y):
    root, size = uf
    x, y = find_root(uf, x), find_root(uf, y)
    if x == y:
        return False
    if size[x] < size[y]:
        x, y = y, x
    size[x] += size[y]
    root[y] = root[x]
    return True

@njit((i8, i8, i8[:]), cache=True)
def main(N, M, AB):
    ans = N - 1
    root = np.arange(N + 1, dtype=np.int64)
    size = np.ones_like(root)
    uf = (root, size)

    for i in range(0, len(AB), 2):
        a, b = AB[i:i + 2]
        if merge(uf, a, b):
            ans -= 1
    return ans

N, M = map(int, readline().split())
AB = np.array(read().split(), np.int64)

print(main(N, M, AB))
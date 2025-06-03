import sys
input = sys.stdin.readline
import numpy as np
from numba import njit


def read():
    D = int(input().strip())
    C = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
    S = np.empty((D, 26), dtype=np.int32)
    for i in range(D):
        s = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
        S[i, :] = s[:]
    T = np.array([int(input().strip()) for i in range(D)], dtype=np.int32)
    return D, C, S, T


@njit
def satisfaction(d, C, S, T, last):
    v = 0
    v += S[d, T[d]-1]
    last[T[d]-1] = d+1
    for i in range(26):
        v -= C[i] * ((d+1) - last[i])
    return v


@njit
def solve(D, C, S, T):
    last = np.zeros(26, dtype=np.int32)
    cumsat = 0
    for i in range(D):
        sat = satisfaction(i, C, S, T, last)
        cumsat += sat
        print(cumsat)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))

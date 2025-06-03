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
    M = 10000
    RD = np.random.randint(D, size=(M, ), dtype=np.int32)
    RQ = np.random.randint(26, size=(M, ), dtype=np.int32)
    DQ = np.stack([RD, RQ]).T
    return D, C, S, M, DQ


@njit
def diff_satisfaction(C, S, d, p, last):
    """d日目にコンテストpを開催するときの、満足度の更新量を求める
    """
    v = 0
    for i in range(26):
        v -= C[i] * (d - last[i])
    v += C[p] * (d - last[p])
    v += S[d, p]
    return v


@njit
def evaluate(D, C, S, d, p, last, k=13):
    """d日目にコンテストpを開催し、その後d+k日目までコンテストが開催されないときの、満足度の更新差分を求める
    """
    v = diff_satisfaction(C, S, d, p, last)
    for e in range(d+1, min(d+k, D)):
        for i in range(26):
            v -= C[i] * (e - last[i])
        v += C[p] * (d - last[p])
    return v


@njit
def greedy_fine(D, C, S):
    T = np.zeros(D, dtype=np.int32)
    last = -np.ones(26, dtype=np.int32)
    cumsat = 0
    for d in range(D):
        
        max_p = 0
        max_e = -999999999

        # select contest greedily
        for p in range(26):
            e = evaluate(D, C, S, d, p, last, k=8)
            
            if e > max_e:
                max_p = p
                max_e = e
        
        # update schedule
        cumsat += diff_satisfaction(C, S, d, max_p, last)
        T[d] = max_p
        last[max_p] = d
    return cumsat, T


@njit
def solve(D, C, S, M, DQ):
    cumsat, T = greedy_fine(D, C, S)
    for t in T:
        print(t+1)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))

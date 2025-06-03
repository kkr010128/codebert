#!python3

from time import perf_counter
tick = perf_counter() + 1.92

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())
from random import randrange
from bisect import bisect

def resolve():
    G = 26
    it = map(int, sys.stdin.read().split())
    D = next(it)
    C = [next(it) for i in range(G)]
    S = [[next(it) for i in range(G)] for i in range(D)]
    L = [[-1] for i in range(G)]
    T = [0] * D

    def update(di, qi):

        score = 0
        t0 = T[di]
        score += S[di][qi]-S[di][t0]

        a1 = li = L[t0][:]
        ii = li.index(di)
        la = D if len(li)-1 == ii else li[ii+1]
        score -= C[t0] * (di-li[ii-1])*(la-di)
        li.pop(ii)

        a2 = li = L[qi][:]
        ii = bisect(li, di)
        li.insert(ii, di)
        la = D if len(li)-1 == ii else li[ii+1]
        score += C[qi] * (di-li[ii-1])*(la-di)

        return score, (a1, a2)

    U = 7
    def calc(i, j):
        score = S[i][j]
        for k in range(G):
            u = k - L[k][-1]
            score -= C[k] * (u + u + U) * U // 2
        score += C[k] * U * (i-L[j][-1])
        return score

    for di in range(D):
        i, score = 0, calc(di, 0)
        for qi in range(1, G):
            x = calc(di, qi)
            if x > score:
                i, score = qi, x
        T[di] = i
        L[i].append(di)

    while perf_counter() < tick:
        di, qi = randrange(0, D), randrange(0, G)
        diff, swap = update(di, qi)
        if diff > 0:
            score += diff
            q0, T[di] = T[di], qi
            L[q0], L[qi] = swap

    print(*(i+1 for i in T), sep="\n")

if __name__ == "__main__":
    resolve()

#!python3

from time import perf_counter
tick = perf_counter() + 1.92

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())
from random import randrange
from bisect import bisect

def resolve():
    it = map(int, sys.stdin.read().split())
    D = next(it)
    C = [next(it) for i in range(26)]
    S = [[next(it) for i in range(26)] for i in range(D)]
    L = [[-1]] * 26
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

    score = 0
    for i in range(D):
        score += S[i][0]
    L[0] = [i for i in range(-1, D)]

    x = (1+D)*D//2
    for i in range(1, 26):
        score -= C[i] * x

    for di in range(D):
        for qi in range(26):
            diff, swap = update(di, qi)
            if diff > 0:
                score += diff
                q0, T[di] = T[di], qi
                L[q0], L[qi] = swap

    while perf_counter() < tick:
        di, qi = randrange(0, D), randrange(0, 26)
        diff, swap = update(di, qi)
        if diff > 0:
            score += diff
            q0, T[di] = T[di], qi
            L[q0], L[qi] = swap

    print(*(i+1 for i in T), sep="\n")

if __name__ == "__main__":
    resolve()

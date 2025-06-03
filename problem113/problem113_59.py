#!python3

from time import perf_counter
limit = 1.92
tick = perf_counter()

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

    def dswap(di, dj):
        qi, qj = T[di], T[dj]
        swap0 = (L[qi], L[qj])

        score, swap1 = update(di, qj)
        T[di] = qj
        L[qi], L[qj] = swap1
        diff, swap2 = update(dj, qi)

        score += diff

        if score > 0:
            T[dj] = qi
            L[qj], L[qi] = swap2
        else:
            score = 0
            T[di], T[dj] = qi, qj
            L[qi], L[qj] = swap0
        return score

    def fullscore():
        score = 0
        last = [-1] * 26
        for i, ti in enumerate(T):
            score += S[i][ti]
            last[ti] = i
            for ci, la in zip(C, last):
                score -= ci * (i-la)
        return score

    for di in range(D):
        i, score = 0, calc(di, 0)
        for qi in range(1, G):
            x = calc(di, qi)
            if x > score:
                i, score = qi, x
        T[di] = i
        L[i].append(di)


    print(*(i+1 for i in T), sep="\n")



if __name__ == "__main__":
    resolve()

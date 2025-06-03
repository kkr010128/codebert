import bisect
import sys,io
import math
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.buffer.readline

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29

DIV = (10**9) + 7
#DIV = 998244353

def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


def CONV_TBL(max, mod=DIV):
    fac, finv, inv = [0]*max, [0]*max, [0]*max
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod % i] * (mod//i) % mod
        finv[i] = finv[i-1]*inv[i] % mod

    class CONV:
        def __init__(self):
            self.fac = fac
            self.finv = finv
            pass

        def ncr(self, n, k):
            if(n < k):
                return 0
            if(n < 0 or k < 0):
                return 0
            return fac[n]*(finv[k]*finv[n-k] % DIV) % DIV

    return CONV()


def cumsum(As):
    s = 0
    for a in As:
        s += a
        yield s


sys.setrecursionlimit(200005)


def dijkstra(G,start=0):
    heap = []
    cost = [INF]*len(G)
    heappush(heap,(0,start))
    while len(heap)!=0:
        c,n = heappop(heap)
        if cost[n] !=INF:
            continue
        cost[n]=c
        for e in G[n]:
            ec,v = e
            if cost[v]!=INF:
                continue
            heappush(heap,(ec+c,v))
    return cost


def main():
    R,C,K = isRaw()
    mas = [[0 for _ in range(C)]for _ in range(R)]
    for k in range(K):
        r,c,v = isRaw()
        mas[r-1][c-1]=v
    dp = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(3)]

    dp0 = dp[0]
    dp1 = dp[1]
    dp2 = dp[2]

    dp0[0][0]=mas[0][0]
    dp1[0][0]=mas[0][0]
    dp2[0][0]=mas[0][0]

    for r in range(R):
        for c in range(C):
            mrc = mas[r][c]
            
            dp0[r][c] = mrc
            dp1[r][c] = mrc
            dp2[r][c] = mrc

            if r>0:
                dp0[r][c] = max(dp0[r][c], dp2[r-1][c]+mrc)
                dp1[r][c] = max(dp1[r][c], dp2[r-1][c]+mrc)
                dp2[r][c] = max(dp2[r][c], dp2[r-1][c]+mrc)
            if c>0:
                dp0[r][c] = max(dp0[r][c], dp0[r][c-1], mrc)
                dp1[r][c] = max(dp1[r][c], dp1[r][c-1], dp0[r][c-1]+mrc)
                dp2[r][c] = max(dp2[r][c], dp2[r][c-1], dp1[r][c-1]+mrc)

    print(max([dp[ni][-1][-1] for ni in range(3)]))

main()

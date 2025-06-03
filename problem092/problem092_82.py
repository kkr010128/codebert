#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from bisect import bisect_left
from itertools import product
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def LF(): return list(map(float, input().split()))
def LC(): return [c for c in input().split()]
def LLI(n): return [LI() for _ in range(n)]
def NSTR(n): return [input() for _ in range(n)]

def array2d(N, M, initial=0):
    return [[initial]*M for _ in range(N)]

def copy2d(orig, N, M):
    ret = array2d(N, M)
    for i in range(N):
        for j in range(M):
            ret[i][j] = orig[i][j]
    return ret


INF = float("inf")
MOD = 10**9 + 7


def main():
    X, K, D = MAP()

    # 到達候補は0に近い正と負の二つの数
    d, m = divmod(X, D)
    cand = (m, m-D)

    if X >= 0:
        if K <= d:
            print(X-K*D)
            return
        else:
            rest = (K-d)
            if rest % 2 == 0:
                print(cand[0])
                return
            else:
                print(-cand[1])
                return
    else:
        if K <= -d-1:
            print(abs(X+K*D))
            return
        else:
            rest = K-(-d-1)
            if rest % 2 == 0:
                print(-cand[1])
                return
            else:
                print(cand[0])
                return
    return


if __name__ == '__main__':
    main()

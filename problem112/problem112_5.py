import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
import random
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


N, K = read_values()
def main():
    A = read_list()
    # A = [random.randint(-10 ** 9, 10 ** 9) for _ in range(N)]

    A.sort(reverse=True)
    if N == K or (A[0] < 0 and K % 2 == 1):
        res = 1
        for a in A[:K]:
            res *= a
            res %= mod
        print(res)
        return

    A.sort(key=lambda a: abs(a), reverse=True)

    P1 = list(filter(lambda a: a >= 0, A[:K]))
    P2 = list(filter(lambda a: a >= 0, A[K:]))
    N1 = list(filter(lambda a: a < 0, A[:K]))
    N2 = list(filter(lambda a: a < 0, A[K:]))

    if len(N1) % 2 == 1:
        # if N1[-1] * N2[0] : P1[-1] * P2[0]
        if len(P1) == 0 or len(N2) == 0:
            N1[-1] = P2[0]
        elif len(P2) == 0:
            P1[-1] = N2[0]
        else:
            if P1[-1] * P2[0] >= N1[-1] * N2[0]:
                N1[-1] = P2[0]
            else:
                P1[-1] = N2[0]
    
    res = 1
    for p in P1:
        res *= p
        res %= mod

    for n in N1:
        res *= n
        res %= mod
    
    print(res % mod)
        

if __name__ == "__main__":
    main()

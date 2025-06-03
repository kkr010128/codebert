import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
# from math import ceil, floor, log2
from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def solve():
    N, M = MI()
    E = [[] for _ in range(N)]
    for i in range(M):
        a, b = MI1()
        E[a].append(b)
        E[b].append(a)
    q = deque([0])
    used = [0] * N
    used[0] = 1
    ans = [0] * N
    ans[0] = 'Yes'
    while q:
        v = q.popleft()
        for nv in E[v]:
            if used[nv]: continue
            used[nv] = 1
            ans[nv] = v+1
            q.append(nv)
    printlist(ans, '\n')


if __name__ == '__main__':
    solve()

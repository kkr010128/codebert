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
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    H, W, K = MI()
    G = np.array(LLS(H))
    # print(G)

    ans = np.zeros((H, W), np.int)
    i = 0
    cnt = 0
    num = 1
    for h in range(H):
        g = G[h]
        if '#' in g:
            cnt += 1
        if cnt == 2:
            # print('tmp', i, h, cnt,)
            l = h-i
            c2 = 0
            for w in range(W):
                gw = G[i:h, w]
                # print(gw)
                if '#' in gw:
                    c2 += 1
                    if c2 == 2:
                        num += 1
                        c2 = 1
                for j in range(l):
                    ans[i+j, w] = num
            num += 1
            i = h
            cnt = 1
            tmp = []
    # print(i, h)
    # print('tmp', i, h, cnt, )
    c2 = 0
    for w in range(W):
        gw = G[i:h+1, w]
        # print(gw)
        if '#' in gw:
            c2 += 1
            if c2 == 2:
                num += 1
                c2 = 1
        for j in range(h+1-i):
            ans[i + j, w] = num
    
    for a in ans:
        print(*a)

if __name__ == '__main__':
    solve()

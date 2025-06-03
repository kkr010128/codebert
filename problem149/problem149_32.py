import bisect,collections,copy,heapq,itertools,math,string
from collections import defaultdict as D
from functools import reduce
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353    

N,M,X = LI()
# c=[]
# a=[]
# for i in range(n):
#     ca = LI()
#     c.append(ca[0])
#     a.append(ca[1:])
# print(c)
# print(a)

_ca = [LI() for _ in range(N)]
ca = np.array(_ca, np.int64)
# print(ca)
# ca = ca.reshape(n,-1)
C = ca[:,0]
A = ca[:,1:]
# print(c)
# print(a)

result = 10**7
# ビット全探索
for i in range(1 << N):
    t = [0] * M
    c = 0
    for j in range(N):
        # i を j回右にシフトして1との論理積を取り、1であればアイテムを購入しているとみなす
        # 購入していない場合
        if (i >> j) & 1 == 0:
            continue
        c += C[j]
        for k in range(M):
            t[k] += A[j][k]
    # 全てX以上であれば更新
    if all(x >= X for x in t):
            result = min(result, c)

if result == 10**7:
    print(-1)
else:
    print(result)
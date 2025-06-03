def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N, K = getNM()
P = [i - 1 for i in getList()]
C = getList()

ignore = [-1] * N
ans = -float('inf')
for i in range(N):
    if ignore[i] >= 0:
        continue
    ### ループ生成 ###
    ignore[i] = 1
    opt_l = [i]
    to = P[i]
    while ignore[to] == -1:
        opt_l.append(to)
        ignore[to] = 1
        to = P[to]
    ###
    ### 作成したループで得点リスト生成 ###
    n = len(opt_l)
    point = [0] * n
    for i in range(n):
        point[i] = C[opt_l[i]]
    ###
    ### 得点リスト内の連続する区間の総和のうちの最大値を累積和を使って求める ###
    sum_roop = sum(point)
    # ループの累積和作成
    imos = [0]
    point += point
    for i in range(len(point)):
        imos.append(imos[i] + point[i])
    #
    ran = min(n, K)
    for i in range(n):
        # 区間の大きさran以下についての総和を求める
        for j in range(1, ran + 1):
            if sum_roop >= 0:
                opt = imos[i + j] - imos[i] + ((K - j) // n) * sum_roop
            else:
                opt = imos[i + j] - imos[i]
            ans = max(ans, opt)
    ###
print(ans)
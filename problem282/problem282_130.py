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

N, A = getNM()
w = []
v = []
for i in range(N):
    a, b = getNM()
    w.append(a)
    v.append(b)
    
# limit回までコストカットできる
def knapsack_6(N, upper, limit, weight, value):
    dp = [[[0] * (upper + 1) for i in range(limit + 1)] for j in range(N + 1)]

    for i in range(N):
        # ボーナスでコスト１にするのを使ったか
        for j in range(limit + 1):
            for l in range(upper + 1):
                # コストカットできる時
                if j < limit:
                    dp[i + 1][j + 1][l] = dp[i][j + 1][l]
                    if l >= weight[i]:
                        dp[i + 1][j][l] = max(dp[i][j][l], dp[i][j][l - weight[i]] + value[i])
                        dp[i + 1][j + 1][l] = max(dp[i][j + 1][l], dp[i][j][l - 1] + value[i])
                    elif l >= 1:
                        dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])
                        dp[i + 1][j + 1][l] = max(dp[i + 1][j + 1][l], dp[i][j][l - 1] + value[i])
                    else:
                        dp[i + 1][j][l] = dp[i][j][l]
                # できない時
                else:
                    if l >= weight[i]:
                        dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l - weight[i]] + value[i])
    return dp[N][limit][upper]

print(knapsack_6(N, A, 1, w, v))
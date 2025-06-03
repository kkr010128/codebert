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
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N, U, V = getNM()
U -= 1
V -= 1
# 高橋君はできるだけ遅くゲームが終了するように移動し、青木君はできるだけ早くゲームが終了するように移動します。
# 高橋君は逃げ、青木君は追いかける
dist = [[] for i in range(N)]
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

taka_d = [-1] * N
aoki_d = [-1] * N

taka_d[U] = 0
pos = deque([[U, taka_d[U]]])
while len(pos) > 0:
    u, dis = pos.popleft()
    for i in dist[u]:
        if taka_d[i] == -1:
            taka_d[i] = dis + 1
            pos.append([i, taka_d[i]])

aoki_d[V] = 0
pos = deque([[V, aoki_d[V]]])
while len(pos) > 0:
    u, dis = pos.popleft()
    for i in dist[u]:
        if aoki_d[i] == -1:
            aoki_d[i] = dis + 1
            pos.append([i, aoki_d[i]])

ans = 0
for a, b in zip(taka_d, aoki_d):
    if a < b:
        ans = max(ans, b - 1)
print(ans)

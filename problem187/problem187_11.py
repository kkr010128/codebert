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

N, X, Y = getNM()

dist = [[] for i in range(N)]
for i in range(N - 1):
    dist[i].append(i + 1)
    dist[i + 1].append(i)

dist[X - 1].append(Y - 1)
dist[Y - 1].append(X - 1)

distance = [0] * N
def counter(sta):
    ignore = [0] * N
    ignore[sta] = 1
    pos = deque([[sta, 0]])

    while len(pos) > 0:
        u, dis = pos.popleft()
        for i in dist[u]:
            if ignore[i] == 0:
                ignore[i] = 1
                distance[dis + 1] += 1
                pos.append([i, dis + 1])
for i in range(N):
    counter(i)
for i in distance[1:]:
    print(i // 2)
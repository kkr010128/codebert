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

def segfunc(x, y):
    return min(x, y)

ide_ele = float('inf')

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

# 最短手数k回でクリアできるとすると、
# 1 ~ M　の内１つをk回選んで合計をNにする
N, M = getNM()
S = input()
trap = set()
for i in range(len(S)):
    if S[i] == '1':
        trap.add(i)

# これABC011 123引き算と同じでは

# 案1 dpを使う
# dp[i]: iマスに止まる時の最短手順
# dp[i]の時 dp[i + 1] ~ dp[i + M]についてmin(dp[i] + 1, dp[i + j])を見ていく
# 決まったらdpを前から見ていき最短手順がdp[i] - 1になるものを探す（辞書順）
# → M <= 10 ** 5より多分無理

# セグ木使えばいける？
# dp[i] = dp[i - M] ~ dp[i - 1]の最小値 + 1
# dp[i - M] ~ dp[i - 1]の最小値はlogNで求められるので全体でNlogN

dp = [float('inf')] * (N + 1)
dp[0] = 0
seg = SegTree([float('inf')] * (N + 1), segfunc, ide_ele)
seg.update(0, 0)

# dp[i]をレコード
for i in range(1, N + 1):
    # もしドボンマスなら飛ばす（float('inf')のまま）
    if i in trap:
        continue
    # dp[i - M] ~ dp[i - 1]の最小値をサーチ
    min_t = seg.query(max(0, i - M), i)
    seg.update(i, min_t + 1)
    dp[i] = min_t + 1

# goalに到達できないなら
if dp[-1] == float('inf'):
    print(-1)
    exit()

# 何回の試行で到達できるかをグルーピング
dis = [[] for i in range(dp[-1] + 1)]
for i in range(len(dp)):
    if dp[i] == float('inf'):
        continue
    dis[dp[i]].append(i)

# ゴールから巻き戻っていく
now = dp[-1]
now_index = N
ans = []
# 辞書順で1 4 4 < 3 3 3なので
# 一番前にできるだけ小さい数が来るようにする
for i in range(now, 0, -1):
    # dp[i] - 1回で到達できる
    # 現在地点からMマス以内
    # で最も現在地点から遠いところが１つ前のマス
    index = bisect_left(dis[i - 1], now_index - M)
    # サイコロの目を決める
    ans.append(now_index - dis[i - 1][index])
    # 現在地点更新
    now_index = dis[i - 1][index]

for i in ans[::-1]:
    print(i)
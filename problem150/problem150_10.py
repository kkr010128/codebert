#!/usr/bin/env python3
import bisect
import heapq
import itertools
import math
import numpy as np
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n,r,mod):
  bunshi=1
  bunbo=1
  for i in range(r):
    bunbo = bunbo*(i+1)%mod
    bunshi = bunshi*(n-i)%mod
  return (bunshi*pow(bunbo,mod-2,mod))%mod
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]



#いまいるところ,
#listとnが与えられたときn回テレポートしたところを出力する
def now_place(li,n):
    now = 1
    for i in range(n):
        now = li[now-1]
    return now

#p回のテレポートでたどってきた道筋のルートを返す

def root(li,p):
    ans = []
    now = 1
    for j in range(p):
        ans.append(now_place(li,j+1))
    return ans



n,k = MI()
a = LI()
#訪れたところのメモがtown
town = []
#訪れたかどうかを0と1で管理
visit=[0]*n
p = 1
while visit[p-1] == 0:
    town.append(p)
    visit[p-1] = 1
    p = a[p-1]
#香りだかい町がいつでてきたか→周期に入るまでのテレポート回数
#len(town[l:])は周期を表す
l = town.index(p)
if k <len(town):
    print(town[k])
else:
    print(town[l + (k-l)%(len(town[l:]))])

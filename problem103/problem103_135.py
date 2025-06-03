import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n = inp()
a = inpl()
sign = [-1]*n

pre = -1
for i in range(1,n):
    if a[i] > a[i - 1]:
        sign[i] = 1
        pre = 1
    elif a[i] < a[i - 1]:
        sign[i] = -1
        pre = -1
    else:
        sign[i] = pre

money = 1000
stock = 0
for i in range(n):
    if sign[i] == 0 or (i != n-1 and sign[i] == sign[i + 1]):
        continue

    if sign[i] == 1:
        #売る
        money += a[i] * stock
        stock = 0
    elif sign[i] == -1:
        flg = False
        if [j for j in sign[i:] if j == 1]:
            flg = True
        #買う
        if flg == True:
            buy =  money // a[i]
            stock += buy
            money -= a[i] * buy
print(money)
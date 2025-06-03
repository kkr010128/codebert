from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
x = [[0]*2 for i in range(n)]
for i in range(n):
    x[i][0], x[i][1] = MAP()

x.sort()
tmp = -inf
ans = n
for i in range(n):
    if tmp > x[i][0] - x[i][1]:
        ans -= 1
        tmp = min(tmp, x[i][0] + x[i][1])
    else:
        tmp = x[i][0] + x[i][1]
print(ans)
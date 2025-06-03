from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
p = LIST()
q = LIST()
count = 0
for x in permutations(range(1, n+1), n):
    count += 1
    if all( x[j] == p[j] for j in range(n)):
        a = count
    if all( x[j] == q[j] for j in range(n)):
        b = count
print(abs(a-b))
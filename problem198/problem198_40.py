from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
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

def dfs(s,d,i):
    for j in range(i+1):
        s[d] = chr(ord('a')+j)
        if d < len(s) - 1:
            dfs(s, d+1, max(j+1, i))
        else:
            a.add("".join(s))

n = INT()
s = ['a']*n
a = set()
dfs(s, 0, 0)
b = sorted(list(a))
for x in b:
    print(x)
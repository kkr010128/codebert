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

n, k = MAP()
R, S, P = MAP()
t = input()
s = ''

ans = 0
for i in range(len(t)):
    if t[i] == 'r':
        if i >= k and s[i-k] == 'p':
            s += 'x'
        else:
            ans += P
            s += 'p'
    elif t[i] == 's':
        if i >= k and s[i-k] == 'r':
            s += 'x'
        else:
            ans += R
            s += 'r'
    else:
        if i >= k and s[i-k] == 's':
            s += 'x'
        else:
            ans += S
            s += 's'
print(ans)
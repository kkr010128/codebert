from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

k = INT()
s = list('00000000000')

for i in range(k):
    for j in range(len(s)):
        if s[j] != '9' and ( int("".join(s[j+1:])) == 0 or int(s[j]) < int(s[j+1]) + 1 ):
            s[j] = str(int(s[j]) + 1)
        else:
            continue

        while j > 0:
            j -= 1
            s[j] = str(max(0, int(s[j+1])-1))
        break

ans = int("".join(reversed(s)))
print(ans)
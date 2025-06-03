import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n,d,a=map(int,input().split())
xh=[list(map(int,input().split())) for i in range(n)]
xh.sort()
r,tama=[],[0]

for i in range(n):
    x,h=xh[i]
    tmpr=bisect.bisect_left(r,x)
    h-=(tama[-1]-tama[tmpr])*a
    tmp=0
    if h>0:
        tmp=math.ceil(h/a)
    tama.append(tmp)
    tama[i+1]+=tama[i]
    r.append(x+2*d)

print(tama[-1])
# print(r)
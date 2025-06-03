import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

h,w=map(int,input().split())
s=[input() for i in range(h)]

d=deque([[0,0]])
itta=[[float('inf')]*w for i in range(h)]
if s[0][0]=="#":
    itta[0][0]=1
else:
    itta[0][0]=0

# print(itta)
ans=0
for i in range(h+w-2):
    # print(itta)
    for j in range(len(d)):
        now=d.popleft()
        nh,nw=now
        cnt=itta[nh][nw]
        if nh+1<h:
            tmp=cnt
            if s[nh][nw]=="." and s[nh+1][nw]=="#":
                tmp+=1
            if itta[nh+1][nw]==float('inf'):
                d.append([nh+1,nw])
            itta[nh+1][nw]=min(itta[nh+1][nw],tmp)
        if nw+1<w:
            tmp=cnt
            if s[nh][nw]=="." and s[nh][nw+1]=="#":
                tmp+=1
            if itta[nh][nw+1]==float('inf'):
                d.append([nh,nw+1])
            itta[nh][nw+1]=min(itta[nh][nw+1],tmp)

# print(itta)
# for i in range(len(d)):
print(itta[-1][-1])
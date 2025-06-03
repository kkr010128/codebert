import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
s=[input() for i in range(n)]
# lst=[[0]*2 for i in range(n)]

sei=[]
hu=[]

for i in range(n):
    l,r=0,0
    for j in range(len(s[i])):
        if s[i][j]==")":
            if r==0:
                l+=1
            else:
                r-=1
        if s[i][j]=="(":
            r+=1
    if r-l>0:
        sei.append([l,r-l])
    else:
        hu.append([r,l-r])

sei.sort(key=lambda x: x[0])
hu.sort(key=lambda x: x[0])

tmp=0

for i in range(len(sei)):
    if tmp-sei[i][0]<0:
        print("No")
        quit()
    tmp+=sei[i][1]

tmp2=0
for i in range(len(hu)):
    if tmp2-hu[i][0]<0:
        print("No")
        quit()
    tmp2+=hu[i][1]

if tmp==tmp2:
    print("Yes")
else:
    print("No")
#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
check=[-1]*n
finalans=-10**20
for i in range(n):
    if check[i]!=-1:
        continue
    loop=[i]
    now=i
    while p[now]!=i+1:
        check[now]=1
        loop.append(p[now]-1)
        now=p[now]-1
    L=len(loop)
    point=[0]*(L*2)
    point[0]=c[loop[0]]
    for j in range(1,L*2):
        if j<L:
            point[j]=point[j-1]+c[loop[j]]
        else:
            point[j]=point[j-1]+c[loop[j-L]]
    m=-10**20
    if point[L-1]>0:
        r=k%L
        if r==0:
            r=L
        for j in range(1,r+1):
            for t in range(j-1,j+L-1):
                cand=point[t]-point[t-j] if t-j>=0 else point[t]
                m=max(m,cand)
        ans=point[L-1]*(k//L)+m if r!=L else point[L-1]*((k//L)-1)+m
    else:
        for j in range(1,L+1):
            for t in range(j-1,j+L-1):
                cand=point[t]-point[t-j] if t-j>=0 else point[t]
                m=max(m,cand)
        ans=m
    finalans=max(ans,finalans)   
print(finalans)
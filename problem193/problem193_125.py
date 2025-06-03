import sys
#import numpy as np
#import math
#from fractions import Fraction
#import itertools
#import heapq

h,w,k=map(int,input().split())
s = [list(map(int, input())) for _ in range(h)]
res=0
ans=10**9
for i in range(2**(h-1)):
    p=1
    partation=[-1]*(h-1)

    for j in range(h-1):
        if i &(1<<j):
            partation[j]=1
            p+=1
    g=[0]*p
    res=0
    l=r=0
    f=False
    while r<w:
        m=0
        for j in range(h):
            g[m]+=s[j][r]
            if g[m]>k:
                res+=1
                g=[0]*p
                if l==r:
                  f=True
                l=r
                break
            if j<h-1 and partation[j]==1:
                m+=1
        else:
            r+=1
        if f:
          break
    else:
      res+=p-1
      if res<ans:
          ans=res
print(ans)
#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,t=map(int,input().split())
d1=[[0]*t for i in range(n+1)]
d2=[[0]*t for i in range(n+1)]

ab=[list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    a=ab[i-1][0]
    b=ab[i-1][1]
    for j in range(t):
        if j<a:
            d1[i][j]=d1[i-1][j]
        else:
            d1[i][j]=max(d1[i][j],d1[i-1][j],d1[i-1][j-a]+b)
    a,b=ab[n-i]
    for j in range(t):
        if j<a:
            d2[n-i][j]=d2[n-i+1][j]
        else:
            d2[n-i][j]=max(d2[n-i][j],d2[n-i+1][j],d2[n-i+1][j-a]+b)
ans=0
for i in range(1,n+1):
    b=ab[i-1][1]
    for j in range(t):
        ans=max(ans,b+d1[i-1][j]+d2[i][t-1-j])
print(ans)
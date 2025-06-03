#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
a=list(map(int,input().split()))
b_d=[[0,0] for _ in range(n+1)]
b_u=[[0,0] for _ in range(n+1)]
b_d[n]=[a[n],a[n]]
b_u[0]=[1,1]
for i in range(1,n+1):
    l=(1+b_d[n+1-i][0])//2+a[n-i]
    r=(b_d[n+1-i][1])+a[n-i]
    if l>r:
        print(-1)
        exit()
        break
    b_d[n-i]=[l,r]
    l=max(0,b_u[i-1][0]-a[i-1])
    r=2*(b_u[i-1][1]-a[i-1])
    if l>r:
        print(-1)
        exit()
        break
    b_u[i]=[l,r]
ans=0

for i in range(n+1):
    if b_d[i][0]>b_u[i][1] or b_u[i][0]>b_d[i][1]:
        print(-1)
        exit()
    else:
        ans+=min(b_u[i][1],b_d[i][1])
print(ans)
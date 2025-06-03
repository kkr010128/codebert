import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
#from collections import deque
#import heapq
#from fractions  import gcd
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
ans=1
d={x:0 for x in range(n)}
for i in range(n):
    if a[i]==0:
        d[0]+=1
    else:
        m=a[i]
        ans=(ans*(d[m-1]-d[m]))%mod
        if ans<=0:
          print(0)
          exit()
        d[m]+=1
    if d[a[i]]>3:
      print(0)
      exit()
if d[0]==1:
  print(ans*3%mod)
elif d[0]==2:
  print(ans*6%mod)
elif d[0]==3:
  print(ans*6%mod)
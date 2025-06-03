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
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ar=[0]*(n+1)
br=[0]*(m+1)
ans=0

for i in range(n):
    ar[i+1]=ar[i]+a[i]
for i in range(m):
    br[i+1]=br[i]+b[i]
for i in range(m+1):
    sup=k-br[i]
    if sup<0:
      break
    res=bisect.bisect_right(ar,sup)+i-1
    ans=max(res,ans)
print(ans)
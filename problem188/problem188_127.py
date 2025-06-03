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
x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
ansp=p[:x]
ansq=q[:y]
ans=sum(ansp)+sum(ansq)
ep=x-1
eq=y-1
for i in range(c):
    if ep<0 and eq<0:
        break
    if (ep>=0 and eq<0) or (ep>=0 and eq>=0 and ansp[ep]<ansq[eq]):
        if ansp[ep]<r[i]:
            ans=ans-ansp[ep]+r[i]
            ep-=1 
        else:
            break
    elif (eq>=0 and ep<0) or (ep>=0 and eq>=0 and ansq[eq]<=ansp[ep]):
        if ansq[eq]<r[i]:
            ans=ans-ansq[eq]+r[i]
            eq-=1
        else:
          break
print(ans)
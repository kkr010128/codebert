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
h,w,k=map(int,input().split())
a=1
res=[]
ans_r=[0]*h
x=0
for i in range(h):
    s=list(input())
    ans=[0]*w
    cnt=0
    if a==k+1:
      ans_r[i]=x-1
      continue
    for j in range(w):
        if s[j]=="#":
            if cnt==0:
                cnt+=1
            else:
                a+=1
            ans[j]=a
        else:
            ans[j]=a
    ans_r[i]=x
    if cnt!=0:
        res.append(ans)
        x+=1  
        a+=1
  
for i in range(h):
    j=ans_r[i]
    if j==-1:
        print(*res[-1])
    else:
        print(*res[j])
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
x=input()
p=0
for i in x:
    if i=="1":
        p+=1
rp=0
rq=0
for i in range(n):
    if x[i]=="1":
        rp+=pow(2,(n-1-i),p+1)
        rp%=p+1
        if p!=1:
          rq+=pow(2,(n-1-i),p-1)
          rq%=p-1
        else:
          rq=pow(2,(n-1-i))
def popcnt1(n):
    return bin(n).count("1")
res=[0]*n

for i in range(1,n+1):
    res[i-1]=i%popcnt1(i)

for i in range(n):
    ans=0
    if x[i]=="1":
        if p==1:
          print(0)
          continue
        q=rq-pow(2,(n-1-i),p-1)
        q%=p-1
        while True:
            if q==0:
                print(1+ans)
                break
            ans+=1
            q=res[q-1]
    else:
        q=rp+pow(2,(n-1-i),p+1)
        q%=p+1
        while True:
            if q==0:
                print(1+ans)
                break
            ans+=1
            q=res[q-1]
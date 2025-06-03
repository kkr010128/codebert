mod=10**9+7
import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
from itertools import combinations
import bisect
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()

a,b=mi()
if (a+b)%3!=0:
  print(0)
  sys.exit()
s=(a+b)//3
a-=s
b-=s
if a<0 or b<0:
  print(0)
  sys.exit()
fac=[1]*700000
for i in range(1,700000):
  fac[i]=(fac[i-1]*i)%mod
m=a+b
n=min(a,b)
c=1
for j in range(m,m-n,-1):
  c*=j
  c=c%mod
print((c*pow(fac[n],mod-2,mod))%mod)
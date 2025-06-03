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

s=int(input())
n=s//3

Mod=10**9+7
M=10**4 #書き換え
fac=[0]*M
finv=[0]*M
inv=[0]*M

#finvに逆元、facに階乗のmod
def COMinit():
  fac[0]=fac[1]=1
  finv[0]=finv[1]=1
  inv[1]=1
  for i in range(2,M):
    fac[i]=(fac[i-1]*i%Mod)%Mod
    inv[i]=Mod-inv[Mod%i]*(Mod//i) %Mod
    finv[i]=(finv[i-1]*inv[i]%Mod)%Mod
def COM(n,k):
  if n<k:
    return 0
  if n<0 or k<0:
    return 0
  return (fac[n]*(finv[k]*finv[n-k]%Mod)%Mod)%Mod

COMinit()
ans=0
for i in range(1,n+1):
    m=s-i*3
    ans+=COM(m+i-1,i-1)
    ans%=Mod
print(ans)
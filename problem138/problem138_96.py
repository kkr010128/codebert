from heapq import *
import sys
from collections import *
from itertools import *
from decimal import *
import copy
from bisect import *
import math
sys.setrecursionlimit(4100000)
def gcd(a,b):
    if(a%b==0):return(b)
    return (gcd(b,a%b))
input=lambda :sys.stdin.readline().rstrip()
N,S=map(int,input().split())
A=list(map(int,input().split()))
mod=998244353

gyaku=pow(2,mod-2,mod)
N2=pow(2,N-1,mod)
dp=[0 for n in range(3001)]
for n in range(N):
    a=A[n]
    for s in range(0,S+1)[::-1]:
        if s+a<=S:
            dp[s+a]+=dp[s]*gyaku%mod
            dp[s+a]%=mod
    dp[a]+=N2
    dp[a]%=mod

print(dp[S])

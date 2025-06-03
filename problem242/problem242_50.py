
import sys
import math
from heapq import *

stdin=sys.stdin

ns = lambda:stdin.readline().rstrip()
ni = lambda:int(stdin.readline().rstrip())
nm = lambda:map(int,stdin.readline().split())
nl = lambda:list(map(int,stdin.readline().split()))

N,K=nm()
A=nl()


A.sort()
ans_max=0
MOD=10**9+7


def comb(n,k):
    return (math.factorial(n)//math.factorial(n-k)*math.factorial(k))

#clc comb at high speed

p=MOD
fact=[1,1]
factinv=[1,1]
inv=[0,1]
for i in range(2,N+1):
    fact.append((fact[-1]*i)%p)
    inv.append((-inv[p%i]*(p//i))%p)
    factinv.append((factinv[-1]*inv[-1])%p)


def comb2(n,r,p):
    if(r<0) or (n<r):
        return 0
    r=min(r,n-r)
    return fact[n]*factinv[r]*factinv[n-r]%p 



for i in range(K-1,N):
    ans_max+=A[i]*comb2(i,K-1,p)
    ans_max=ans_max%MOD

A.sort(reverse=True)
ans_min=0
for i in range(K-1,N):
    ans_min+=A[i]*comb2(i,K-1,p)
    ans_min=ans_min%MOD

print((ans_max-ans_min)%MOD)

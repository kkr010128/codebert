from heapq import *
import sys
from collections import *
from itertools import *
from decimal import *
import copy
from bisect import *
import time
import math
def gcd(a,b):
    if(a%b==0):return(b)
    return (gcd(b,a%b))
N=int(input())
A=list(map(int,input().split()))
A=[[A[i],i] for i in range(N)]
A.sort(reverse=True)
dp=[[0 for i in range(N+1)] for _ in range(N+1)]
for n in range(N):
    a,p=A[n]
    for x in range(1,n+2):
        y=n+1-x
        dp[x][y]=max(dp[x][y],dp[x-1][y]+round(abs(x-1 - p))*a)
    for y in range(1,n+2):
        x=n+1-y
        dp[x][y]=max(dp[x][y],dp[x][y-1]+round(abs(N-y - p))*a)
    #print(dp)
print(max([dp[x][y] for x in range(N+1) for y in range(N+1) if x+y==N]))

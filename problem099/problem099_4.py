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



N,K=map(int,input().split())
A=list(map(int,input().split()))


def main(n):
    return(sum([max(i//n-(i%n==0)*1,0) for i in A])<=K)
#print(main(5))
ng=0
ok=10**18
while ok-ng>1:
    mid=(ok+ng)//2
    if main(mid):
        ok=mid
    else:
        ng=mid

print(ok)

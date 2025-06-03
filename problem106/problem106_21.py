#import sys
#input = sys.stdin.readline

import math
from collections import defaultdict,deque
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""
n=ii()
d=defaultdict(int)
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            w=i*i+j*j+k*k+i*j+i*k+j*k
            d[w]+=1
for i in range(1,n+1):
    print(d[i])
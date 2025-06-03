import sys
input=sys.stdin.readline
import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

t,k=ml()
n=ll()
ans=0
lol=0
for i in range(t):
    if(i>=k):
        lol+=((n[i]*(n[i]+1))//2)/n[i]
        lol-=((n[i-k]*(n[i-k]+1))//2)/n[i-k]
    else:
        lol+=((n[i]*(n[i]+1))//2)/n[i]
    ans=max(ans,lol)
print(ans)    
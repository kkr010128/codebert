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

t=1
for _ in range(t):
    l,r,d=ml()
    ans=0
    for i in range(l,r+1):
        if(i%d==0):
            ans+=1
    print(ans)        
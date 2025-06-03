# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
N,P=map(int, sys.stdin.readline().split())
S=sys.stdin.readline().strip()

if P in (2,5):
    ans=0
    for i,x in enumerate(S):
        if int(x)%P==0:
            ans+=i+1
    print ans
else:
    L=[int(S)%P]
    for i,x in enumerate(S):
        L.append((L[-1]-int(x)*pow(10,N-1-i,P))%P)
    ans=0
    D=defaultdict(lambda: 0)
    for i in range(N,-1,-1):
        x=L[i]
        ans+=D[x]
        D[x]+=1
    print ans

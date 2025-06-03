# -*- coding: utf-8 -*-
import sys
N,K,C=map(int, sys.stdin.readline().split())
S=sys.stdin.readline().strip()

#左から
L=[]
over=-1
L_cnt=0
for i,x in enumerate(S):
    if x=="o" and over<i:
        L.append(i)
        L_cnt+=1
        if L_cnt==K: break
        over=i+C

#右から
R=[]
over=-1
R_cnt=0
for i,x in enumerate(S[::-1]):
    if x=="o" and over<i:
        R.append(N-1-i)
        R_cnt+=1
        if R_cnt==K: break
        over=i+C

L.sort()
R.sort()

for x,y in zip(L,R):
    if x==y:
        print x+1
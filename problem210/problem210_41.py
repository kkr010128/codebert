# -*- coding: utf-8 -*-
import sys
N=input()
bit=[ [ 0 for _ in range(N+1) ] for __ in range(27) ] 

def add(i,a,w):
    while a<=N:
        bit[i][a]+=w
        a+=a&-a

def sum(i,a):
    ret=0
    while 0<a:
        ret+=bit[i][a]
        a-=a&-a
    return ret

S=sys.stdin.readline().strip()
S=[None]+list(S) #1-indexed
for j,x in enumerate(S):
    if j==0: continue
    i=ord(x)-96
    add(i,j,1)

Q=input()
for _ in range(Q):
    q1,q2,q3=sys.stdin.readline().split()
    if q1=="1":
        q1=int(q1)
        q2=int(q2)
        current_s=q3
        former_s=S[q2]
        former_s=ord(former_s)-96  #1-indexed
        S[q2]=current_s         #文字列で更新された1文字を置き換える
        current_s=ord(current_s)-96
        add(current_s,q2,1)
        add(former_s,q2,-1) 
    if q1=="2":
        q2=int(q2)
        q3=int(q3)
        begin,end=q2,q3
        cnt=0
        for i in range(1,27):
            if 0<sum(i,end)-sum(i,begin-1):
                cnt+=1
        print cnt
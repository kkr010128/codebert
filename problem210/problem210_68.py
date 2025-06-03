# -*- coding: utf-8 -*-
import sys

N=input()
S=["None"]+list(raw_input())
Q=input()
query=[ sys.stdin.readline().split() for _ in range(Q) ]

#BIT
bit=[ [ 0 for _ in range(N+1) ] for _ in range(27) ]  #1-indexed bit[1]:aのbit, bit[2]:bのbit ...

def add(idx,a,w):
    while a<=N:
        bit[idx][a]+=w
        a+=a&-a

def sum(idx,a):
    ret=0
    while 0<a:
        ret+=bit[idx][a]
        a-=a&-a
    return ret

for i,x in enumerate(S):
    if i==0: continue
    add(ord(x)-96,i,1)  #a~zのどのbit配列か,特定文字のbit配列の何番目,bitに代入する値


for q1,q2,q3 in query:
    q1=int(q1)
    q2=int(q2)
    if q1==1:
        before_q3=S[q2] #文字列Sの変更前の文字をbefore_q3に代入
        S[q2]=q3        #文字列Sの変更部分1文字を更新
        q3=ord(q3)-96                   #変更後の文字をアスキーコード10進数で表現
        before_q3=ord(before_q3)-96     #変更前の文字をアスキーコード10進数で表現
        add(q3,q2,1)                    #a~zのどのbit配列か,特定文字のbit配列の何番目,bitに代入する値
        add(before_q3,q2,-1)    #置き代えた文字は-1しなきゃいけない
    elif q1==2:
        q3=int(q3)
        cnt=0
        for i in range(1,27):
            if 0<sum(i,q3)-sum(i,q2-1):
                cnt+=1
        print cnt
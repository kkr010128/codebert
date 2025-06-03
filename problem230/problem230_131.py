# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left, bisect_right

N,D,A=map(int, sys.stdin.readline().split())
XH=[ map(int, sys.stdin.readline().split()) for _ in range(N) ]
XH.sort()

bit=[ 0 for _ in range(N+1) ]

#BIT 関数は全て1-indexed
def add(a,w):
    while a<=N:
        bit[a]+=w
        a+=a&-a

def sum(a):
    ret=0
    while 0<a:
        ret+=bit[a]
        a-=a&-a
    return ret

#区間[l,r]に一律wを加える
def range_add(l,r,w):
    add(l,w)
    add(r+1,w*-1)

#a番目のモンスターの体力を取得
def get_value(a):
    return sum(a)

X=[float("-inf")]
H=[float("-inf")]
for x,h in XH:
    X.append(x)
    H.append(h)

for i in range(1,N+1):
    if i==1:
        add(i,H[i])
    else:
        add(i,H[i]-H[i-1])  #区間に対する更新を行うため、値の差分をBITに持つ
    
ans=0

for i in range(1,N+1):
    h=get_value(i)
    if h<=0:    #モンスターの体力がゼロ以下だったら何もしない
        pass
    else:
        x=X[i]
        pos=bisect_right(X,x+2*D)-1 #攻撃範囲の一番右側を二分探索で決定
        if h%A==0:   #hがAで割り切れる場合
            cnt=h/A
            range_add(i,pos,A*cnt*-1)
        else:
            cnt=h/A+1   #hをAで割って余りが出る場合は攻撃回数を+１する
            range_add(i,pos,A*cnt*-1)
        ans+=cnt

print ans

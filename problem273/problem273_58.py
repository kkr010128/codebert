# -*- coding: utf-8 -*-
import sys

N,K=map(int, sys.stdin.readline().split())
A=map(int, sys.stdin.readline().split())
A=map(lambda a: (a-1)%K, A)

S=[0]
for a in A:
    S.append( (S[-1]+a)%K )   #累積和

d=dict()    #要素：要素の数を持つ

ans=0
for i in range(N+1):
    x=S[i]%K
    if i==0:
        d[x]=1
    else:
        if x in d:
            if 2<=K:    #K=1の時は自分の値も見てはいけない
                ans+=d[x]   #自分より前に同じ出現した、自分と同じ要素の数を答えに追加
            d[x]+=1
        else:
            d[x]=1      
        if 0<=i-K+1:
            x_head=S[i-K+1]%K  #長さK-1の範囲で配列Sを見るため、１つ進んだら一番先頭の要素を辞書から削除する
            d[x_head]-=1

print ans

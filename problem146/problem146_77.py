mod=10**9+7
n=int(input())
from collections import defaultdict
d=defaultdict(int)#各点の方向ベクトルを管理
z=0#原点にいる際は例外処理したいので別途数える
from math import gcd 
for i in range(n):
    x,y=map(int,input().split())
    if x==y==0:z+=1
    else:
        f=gcd(x,y)
        x//=f;y//=f#非本質な定数倍を削除
        if x<0:x*=-1;y*=-1#偏角は|theta|<=pi/2で十分
        if x==0 and y<0:y=-y
        d[(x,y)]+=1
ans=1
for (a,s) in d:
    if d[(a,s)]==0:continue#すでに数えた
    ng=0
    if (s,-a)in d:ng+=d[(s,-a)];d[(s,-a)]=0
    if (-s,a)in d:ng+=d[(-s,a)];d[(-s,a)]=0
    ans*=(pow(2,d[(a,s)],mod)-1 + pow(2,ng,mod)-1 +1)%mod
    #(a,s)を一本以上使う,ngを((a,s)と直交するもの)を一本以上使う,どちらも使わない
    ans%=mod
    d[(a,s)]=0
print((ans+z-1)%mod)#原点はそれ1つのみでしか使えない　+　1つも使わない例を除外

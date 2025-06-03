# imos解
n,d,a=map(int,input().split())
xh=[]
for i in range(n):
  xx,hh=map(int,input().split())
  xh.append([xx,hh])
xh.sort(key=lambda x:x[0])
xl=[x for x,h in xh]
# print(xh)
from math import ceil
from bisect import bisect_right

ans=0
damage=[0]*(n+1)

for i in range(n):
  x,h=xh[i]
  if damage[i]<h:
    need=ceil((h-damage[i])/a)
    right=x+2*d
    # 爆発に巻き込まれる範囲の右端のindexを取得する
    r_idx=bisect_right(xl,right)
    # imosしながら爆発させる
    damage[i]+=need*a
    damage[r_idx]-=need*a
    ans+=need
  # imosの累積和を取る
  damage[i+1]+=damage[i]
print(ans)

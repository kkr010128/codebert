# coding:utf-8
import math

N=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

manh_dist=0.0
for i in range(0,N):
    manh_dist=manh_dist+math.fabs(x[i]-y[i])

print('%.6f'%manh_dist)

eucl_dist=0.0
for i in range(0,N):
    eucl_dist=eucl_dist+(x[i]-y[i])**2
eucl_dist=math.sqrt(eucl_dist)

print('%.6f'%eucl_dist)

mink_dist=0.0
for i in range(0,N):
    mink_dist=mink_dist+math.fabs(x[i]-y[i])**3
mink_dist=math.pow(mink_dist,1.0/3)

print('%.6f'%mink_dist)

cheb_dist=0.0
for i in range(0,N):
    if cheb_dist<math.fabs(x[i]-y[i]):
        cheb_dist=math.fabs(x[i]-y[i])

print('%.6f'%cheb_dist)
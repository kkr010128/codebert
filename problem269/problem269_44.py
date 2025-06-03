#!/usr/bin python3
# -*- coding: utf-8 -*-

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
s1 = a1 - b1
s2 = a2 - b2

# a1 が先行にする
if s1<0:
    s1*=-1
    s2*=-1

d = s1*t1 + s2*t2
mxd = s1*t1

if d>0:
    print(0)
elif d==0:
    print('infinity')
else:
    if mxd%abs(d)==0:
        print(mxd//abs(d)*2)
    else:
        print(mxd//abs(d)*2+1)

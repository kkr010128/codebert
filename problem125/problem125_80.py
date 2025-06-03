# -*- coding: utf-8 -*-
x=int(input())
a=360
b=x
r=a%b
while r!=0:
  a=b
  b=r
  r=a%b
lcm=x*360/b
k=int(lcm/x)
print(k)
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:23:05 2020

@author: vivek
"""

n,d=[int(i) for i in input().strip().split(" ")]
ans=0
for _ in range(n):
  x,y=[int(i) for i in input().strip().split(" ")]
  if x*x+y*y<=d*d:
    ans+=1
print(ans)
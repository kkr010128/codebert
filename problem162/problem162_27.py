# -*- coding: utf-8 -*-

n, m=  [int(i) for i in input().split()]
for i in range(0,m):
  if n-2*i-1>n/2 or n%2==1:
    print(i+1,n-i)
  else:
    print(i+1,n-i-1)
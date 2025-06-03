#coding: utf-8
#ALDS1_1A
import sys

n=int(raw_input())
a=map(int,raw_input().split())

for i in xrange(n):
  print a[i],
print
for i in xrange(1,n):
 v=a[i]
 j=i-1
 while j>=0 and a[j]>v:
  a[j+1]=a[j]
  j-=1
 a[j+1]=v
 for k in xrange(n):
  print a[k],
 print
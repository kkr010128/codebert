#coding: utf-8
#ALDS1_1D
import sys

n=int(raw_input())
minv=float("inf")
maxv=float("-inf")
for i in xrange(1,n+1):
 r=int(raw_input())
 maxv=max(maxv,r-minv)
 minv=min(minv,r)

print maxv
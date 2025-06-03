# -*- coding: utf-8 -*-
#mitsui f
import sys
import math
import collections
#sys.setrecursionlimit(100000)

#n=int(input())

tmp = input().split()
t1,t2 = list(map(lambda a: int(a), tmp))
tmp = input().split()
a1,a2 = list(map(lambda a: int(a), tmp))
tmp = input().split()
b1,b2 = list(map(lambda a: int(a), tmp))

if(a1*t1+a2*t2==b1*t1+b2*t2):
	print("infinity")
	sys.exit()
diff=(a1*t1+a2*t2)-(b1*t1+b2*t2)


if(diff>0):
	c1=a1-b1
	c2=a2-b2
else:
	c1=b1-a1
	c2=b2-a2

if(c1>0):
	print("0")
	sys.exit()

diff=c1*t1+c2*t2
pitch=c1*t1*-1

ans=pitch//diff*2+1
if(pitch%diff==0):
	ans-=1
print(ans)

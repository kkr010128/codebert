from math import *

n=int(input())
a=[]
for i in range(n):
	s=input()
	a.append(s)

s=set(a)
print(len(s))
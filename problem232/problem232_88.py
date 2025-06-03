# coding: utf-8
# Your code here!
n,m=input().split()
a=n*int(m)
b=m*int(n)
nlist=[a,b]
nlist.sort()
print(nlist[0])
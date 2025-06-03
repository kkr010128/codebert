#coding: utf-8
#ALDS1_2A

def pnt(s):
 for i in xrange(len(s)):
  print s[i],
 print

n=int(raw_input())
a=map(int,raw_input().split())

sw=0
flag=True
while flag:
 flag=False
 for j in xrange(n-1,0,-1):
  if a[j]<a[j-1]:
   a[j],a[j-1]=a[j-1],a[j]
   flag=True
   sw+=1

pnt(a)
print sw
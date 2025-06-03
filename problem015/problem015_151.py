#coding: utf-8
#ALDS1_2B

def pnt(s):
 for i in xrange(len(s)):
  print s[i],
 print

n=int(raw_input())
a=map(int,raw_input().split())

cnt=0
for i in xrange(n):
 mini = i
 for j in xrange(i + 1, n):
  if a[j] < a[mini]:
   mini = j
 if i != mini:
  a[i], a[mini] = a[mini], a[i]
 if i!=mini:
  cnt+=1
pnt(a)
print cnt
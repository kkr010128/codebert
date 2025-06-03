import sys
import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
f.sort()
f.reverse()
if sum(a)<=k:
  print(0)
  sys.exit()
pointer=0
l=0
r=0
for i in range(n):
  r=max(r,a[i]*f[i])
while l+1<r:
  try1=(l+r)//2
  required=0
  for i in range(n):
    required+=(max(0,a[i]-try1//f[i]))
  if required>k:
    l=try1
  else:
    r=try1
required=0
for i in range(n):
  required+=(max(0,a[i]-l//f[i]))
if required>k:
  print(r)
else:
  print(l)

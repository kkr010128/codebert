from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from statistics import median

n=int(input())
l1=[]
l2=[]
for i in range(n):
  a,b=nii()
  l1.append(a)
  l2.append(b)

m1=median(l1)
m2=median(l2)
ans=m2-m1

if n%2==0:
  ans*=2

print(int(ans+1))
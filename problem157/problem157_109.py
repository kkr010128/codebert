from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import Counter

n=int(input())
a=lnii()

l1=[i+a[i] for i in range(n)]
l2=[i-a[i] for i in range(n)]

c1=Counter(l1)
c2=Counter(l2)

ans=0
for i in c1:
  ans+=c1[i]*c2[i]

print(ans)
from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import Counter

n=int(input())
l=lnii()

def eratosthenes(lim):
  num=[1 for i in range(lim)]
  for i in set(l):
    if num[i]:
      for j in range(i+i,lim,i):
        num[j]=0
  return num

lim=10**6+5
num=eratosthenes(lim)

count=Counter(l)

ans=0
for i in l:
  if num[i]==1 and count[i]==1:
    ans+=1

print(ans)
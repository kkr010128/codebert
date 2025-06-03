from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()

ans=[0 for i in range(n)]
for i in a:
  i-=1
  ans[i]+=1

for i in ans:
  print(i)
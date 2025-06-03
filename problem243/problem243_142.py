from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
l=[input().split() for i in range(n)]
x=input()

ans=0
c=False
for s,t in l:
  if c:
    ans+=int(t)
  if x==s:
    c=True

print(ans)
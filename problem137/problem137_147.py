from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
l1=[]
l2=[]
for i in range(n):
  a,b=nii()
  l1.append(a)
  l2.append(b)

l1.sort()
l2.sort()

if n%2==1:
  ans=l2[n//2]-l1[n//2]
else:
  m1=(l2[n//2]+l2[n//2-1])
  m2=(l1[n//2]+l1[n//2-1])
  ans=m1-m2

print(ans+1)
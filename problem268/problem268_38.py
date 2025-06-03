n=int(input())
a=list(map(int,input().split()))
p=[0,0,0]
mod=10**9+7
r=1
for i in range(n):
  c=0
  for j in range(3):
    if p[j]==a[i]:
      if c==0:
        p[j]+=1
      c+=1
  r=(r*c)%mod
print(r)
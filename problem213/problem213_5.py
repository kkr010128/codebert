a=int(input())
b=list(map(int,input().split()))
bmax=max(b)+1
bmin=min(b)
ans=1000000
for i in range(bmin,bmax,1):
  e=0
  for j in b:
    e+=(i-j)**2
  ans=min(ans,e)
print(ans)
n,k=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
ans=0
for i in ar:
  if(k==0):
    break
  ans+=i
  k-=1
print(ans)
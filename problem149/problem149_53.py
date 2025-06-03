n,m,x=map(int,input().split())
c=[list(map(int,input().split())) for _ in range(n)]

ans=float('inf')
for i in range(2**n):
  data=[0]*(m+1)
  for j in range(n):
    if i&(1<<j):
      for k in range(m+1):
        data[k]+=c[j][k]
    cnt=0
    for l in range(1,m+1):
      if data[l]>=x:
        cnt+=1
    if cnt==m:
      ans=min(ans,data[0])
if ans==float('inf'):
  print(-1)
  exit()
print(ans)
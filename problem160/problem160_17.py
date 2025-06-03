n,m,q=map(int,input().split())
e=[list(map(int,input().split())) for _ in range(q)]
ans=0
for i in range(1<<(m+n)):
  a=[1]
  for j in range(m+n):
    if (i>>j)&1:a[-1]+=1
    else:a+=[a[-1]]
    if a[-1]>m:
      flag=0
      break
    if len(a)>n:
      flag=1
      break
  else:flag=1
  if flag==0 or len(a)<n:continue
  cnt=0
  for s,t,u,v in e:
    if a[t-1]-a[s-1]==u:cnt+=v
  ans=max(ans,cnt)
print(ans)
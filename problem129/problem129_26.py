n,*a=map(int,open(0).read().split())
a.sort()
m=a[-1]+1
cnt=[0]*m
for ai in a:
  if cnt[ai]!=0:
    cnt[ai]+=1
    continue
  for i in range(ai,m,ai):
    cnt[i]+=1
ans=0
for ai in a:
  ans+=(cnt[ai]==1)
print(ans)
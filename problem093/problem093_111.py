n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
p=[x-1 for x in p]
mi=set(range(n))
g={}
# g[id]=[ary]
while mi:
  x0=mi.pop()
  ary=[c[x0]]
  x=x0
  while p[x]!=x0:
    x=p[x]
    mi.discard(x)
    ary.append(c[x])
  cnt=len(ary)
  tmp=0
  ary*=2
  cary=[tmp]
  for x in ary:
    tmp+=x
    cary.append(tmp)
  g[x0]=[cnt,cary]
ans=-float('inf')
for cnt,cary in g.values():
  x,y=divmod(k,cnt)
  tmp1=max(0,cary[cnt]*x)
  tmp2=-float('inf')
  for i in range(cnt):
    for j in range(y):
      tmp2=max(tmp2,cary[i+j+1]-cary[i])
  ans=max(ans,tmp1+tmp2)
  if x:
    tmp1=max(0,cary[cnt]*(x-1))
    tmp2=-float('inf')
    for i in range(cnt):
      for j in range(cnt):
        tmp2=max(tmp2,cary[i+j+1]-cary[i])
    ans=max(ans,tmp1+tmp2)
  

print(ans)

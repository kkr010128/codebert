n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
root=[]
mi=set(range(n))
while mi:
  v=mi.pop()
  r=[c[v]]
  while p[v]-1 in mi:
    r.append(c[p[v]-1])
    mi.discard(p[v]-1)
    v=p[v]-1
  root.append(r)
inf=float('inf')
ans=-inf
for r in root:
  ansr=-inf
  k1=k%len(r)
  k0=k//len(r)
  cr=[0]
  tmp=0
  for ri in r:
    tmp+=ri
    cr.append(tmp)
  sumr=cr[-1]
  for ri in r:
    tmp+=ri
    cr.append(tmp)
  for i in range(len(r)):
    for j in range(i,i+min(k,len(r))):
      ansr=max(ansr,cr[j+1]-cr[i])
  if sumr>0:
    ans=max(ans,ansr+sumr*(k0-1))
  else:
    ans=max(ans,ansr)
  if sumr>0:
    ansr=0
    for i in range(len(r)):
      for j in range(i,i+k1):
        ansr=max(ansr,cr[j+1]-cr[i])    
    ans=max(ans,ansr+sumr*k0)
print(ans)

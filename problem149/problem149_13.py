n,m,x=map(int,input().split())
ca=[]
ans=10**9
for i in range(n):
  tmp=list(map(int,input().split()))
  ca.append(tmp)
for p in range(2**n):
  i_bin = (bin(p)[2:]).zfill(n)
  fl=1
  for i in range(1,m+1):
    ttl=sum([int(i_bin[k])*ca[k][i] for k in range(n)])
    if ttl<x: fl=0
  ansc=sum([int(i_bin[k])*ca[k][0] for k in range(n)])
  if fl and ansc<ans:
    ans=ansc
if ans==10**9: print(-1)
else: print(ans)
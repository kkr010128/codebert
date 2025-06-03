N,M=map(int,input().split())
par=[i for i in range(N)]
size=[1 for i in range(N)]
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def union(a,b):
  x=find(a)
  y=find(b)
  if x!=y:
    if size[x]<size[y]:
      par[x]=par[y]
      size[y]+=size[x]
    else: 
      par[y]=par[x]
      size[x]+=size[y]
  else:
    return  

for i in range(M):
  a,b=map(int,input().split())
  union(a-1,b-1)
print(max(size))
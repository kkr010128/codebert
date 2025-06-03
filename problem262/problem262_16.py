def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

N=II()
ans=0
List=[[-1 for _ in range(N)] for _ in range(N)]
for j in range(N):
  A=II()
  for i in range(A):
    x,y=MI()
    x-=1
    List[j][x]=y
for i in range(1<<N):
  honests=[0]*N
  for j in range(N):
    if 1&(i>>j):
      honests[j]=1
  ok=True
  for j in range(N):
    if honests[j]:
      for k in range(N):
        if List[j][k]==-1:
          continue
        if List[j][k]!=honests[k]:
          ok=False
  if ok:
    ans=max(ans,honests.count(1))
print(ans)
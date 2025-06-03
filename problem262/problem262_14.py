def II(): return int(input())
def MI(): return map(int, input().split())
N=II()
a=[0]*N
x=[[0]*N for i in range(N)]
y=[[0]*N for i in range(N)]
for i in range(N):
  a[i]=II()
  for j in range(a[i]):
    x[i][j],y[i][j]=MI()
    x[i][j]-=1
def check(honest):
  for i in range(N):
    if not honest[i]:
      continue
    for j in range(a[i]):
      if y[i][j]==0 and honest[x[i][j]]:
        return False
      if y[i][j]==1 and not honest[x[i][j]]:
        return False
  return True
def dfs(honest):
  if len(honest)==N:
    if check(honest):
      return sum(honest)
    else:
      return 0
  return max(dfs(honest+[True]),dfs(honest+[False]))
print(dfs([]))
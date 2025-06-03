n=int(input())
l=[[-1 for i in range(n)] for j in range(n)]
for i in range(n):
  a=int(input())
  for j in range(a):
    x,y = map(int,input().split())
    l[i][x-1]=y

ans=0
for i in range(2**n):
  d=[0 for x in range(n)]
  for j in range(n):
    if i>>j & 1:
      d[j]=1

  flag=1

  for j in range(n):
    for s in range(n):
      if d[j]==1:
        if l[j][s]==-1:
          continue
        
        if l[j][s]!=d[s]:
          flag=0
          break
          
  if flag:
    ans=max(ans,sum(d))

print(ans)
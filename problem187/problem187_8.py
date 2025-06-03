n,x,y=map(int,input().split())
d=[[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
  for j in range(n):
    d[i][j]=abs(j-i)
for i in range(n):
  for j in range(n):
    d[i][j]=min(d[i][j],d[i][x-1]+d[y-1][j]+1)
ans=[0]*n
for i in range(n):
  for j in range(i+1,n):
    ans[d[i][j]]+=1
for i in ans[1:]:
  print(i)
N = int(input())
x = [0]*N
y = [0]*N
dist = [[0]*N]*N
ans = 0

for i in range(N):
  x[i],y[i]=map(int, input().split())

for i in range(N):
  for j in range(N):
    dist[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
    ans += dist[i][j]

print(ans/N)

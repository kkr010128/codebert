n,m,l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(m)]
c = [[0 for _ in range(l)] for __ in range(n)]
for i in range(n):
  for j in range(l):
    c[i][j] = sum([a[i][k]*b[k][j] for k in range(m)])
for ci in c:
  print(*ci)

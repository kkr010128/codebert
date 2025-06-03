n,m = map(int,input().split())
a = [1]*(n+1)
b = [0]*(n+1)
for i in range(m):
  x,y = map(int,input().split())
  u = x
  while a[u]==0:
    u = b[u]
  v = y
  while a[v]==0:
    v = b[v]
  if u!=v:
    b[v] = u
    b[y] = u
    b[x] = u
    a[u] += a[v]
    a[v] = 0
print(max(a))
n,m = map(int,input().split())
a = []
b = []
c = []
for i in range(n):
  a.append([int(j) for j in input().split()])
for k in range(m):
  b.append(int(input()))
for x in range(n):
  z = 0
  for y in range(m):
    z += a[x][y] * b[y]
  c.append(z)
for i in c:
  print(i)
 
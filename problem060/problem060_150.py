n, m, l = map(int, input().split())

a = []
for i in range(0, n):
  e = list(map(int, input().split()))
  a.append(e) 

b = []
for i in range(0, m):
  e = list(map(int, input().split()))
  b.append(e)

for i in range(0, n):
  e = []
  for j in range(0, l):
    ab = 0
    for k in range(0, m):
      ab += a[i][k] * b[k][j]
    e.append(ab)
  print(' '.join(map(str, e)))


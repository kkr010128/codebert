n, m = map(int,input().split())
count = 0
l = []

for i in range(n):
  for i2 in range(i,n):
    if i != i2:
      l.append([i,i2])

for i in range(m):
  for i2 in range(i,m):
    if i != i2:
      l.append([i,i2])
print(len(l))
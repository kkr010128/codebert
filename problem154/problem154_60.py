n = input()
n = n.split()
k = int(n[1])
n = int(n[0])
c = [0]
for f in range(n-1):
  c.append(0)
for b in range(k):
  d = int(input())
  a = input()
  a = a.split()
  for e in range(d):
    c[int(a[e])-1] = 1
h = 0
for g in range(n):
  if c[g] == 0:
    h = h + 1
print(h)
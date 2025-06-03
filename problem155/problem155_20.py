n, m = map(int, input().split())
h = list(map(int, input().split()))
d = [1] * n
for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  if h[a] > h[b]:
    d[b] = 0
  elif h[b] > h[a]:
    d[a] = 0
  else:
    d[a] = 0
    d[b] = 0
print(sum(d))
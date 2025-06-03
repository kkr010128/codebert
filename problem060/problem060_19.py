n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
for i in a:
  c = []
  for j in zip(*b):
    c.append(sum([k * l for k, l in zip(i, j)]))
  print(*c)

n, m = [int(_) for _ in input().split()]
a = []
for _ in range(n):
  a.append([int(_) for _ in input().split()])
b = []
for _ in range(m):
  b.append(int(input()))

for ai in a:
  print(sum([a_c * b_c for a_c, b_c in zip(ai, b)]))
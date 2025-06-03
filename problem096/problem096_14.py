n, d = map(int, input().split())
s = 0
for i in range(n):
  a, b = map(int, input().split())
  if (a ** 2 + b ** 2) ** 0.5 <= d:
    s += 1
print(s)
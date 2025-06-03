import math
n, d = map(int, input().split())
p = 0
for i in range(n):
  a, b = map(int, input().split())
  a = a ** 2
  b = b ** 2
  c = math.sqrt(a + b)
  if c <= d:
    p = p + 1
print(p)

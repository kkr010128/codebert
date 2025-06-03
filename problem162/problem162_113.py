n, m = map(int, input().split())

a = 1
b = m + 1
while a < b:
  print(a, b)
  a += 1
  b -= 1

a = m + 2
b = 2 * m + 1
while a < b:
  print(a, b)
  a += 1
  b -= 1
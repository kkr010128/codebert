h, a = map(int, input().split())
b = 0
while h-a > 0:
  h = h - a
  b += 1
print(b + 1)

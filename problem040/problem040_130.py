a, b, c = map(int, input().split())

d = 0
if a > b:
  d = a
  a = b
  b = d
else: pass

d = 0
if b > c:
  d = b
  b = c
  c = d
else: pass

d = 0
if a > b:
  d = a
  a = b
  b = d
else: pass

print(a, b, c)

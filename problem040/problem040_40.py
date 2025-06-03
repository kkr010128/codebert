a, b, c = map(int, input().split())
if a >= b:
  if b >= c:
    print(c, b, a)
  elif a <= c:
    print(b, a, c)
  else:
    print(b, c, a)
else:
  if a >= c:
    print(c, a, b)
  elif b >= c:
    print(a, c, b)
  else:
    print(a, b, c)
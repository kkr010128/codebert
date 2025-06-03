a, b, c, d = map(int, input().split())
if d < a:
  print(d)
  exit()
elif d < a + b:
  print(a)
  exit()
else:
  print(a+(-1)*(d-a-b))
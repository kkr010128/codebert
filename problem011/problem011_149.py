x, y = map(int,input().split())
while True:
  if x >= y:
    x %= y
  else:
    y %= x
  if x == 0 or y == 0:
    print(x+y)
    break
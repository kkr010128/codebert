while 1:
  x, y = map(int, input().split())
  if x == 0 and y == 0:
    break
  if x >= y:
    print("{0} {1}".format(y, x))
  else:
    print("{0} {1}".format(x, y))
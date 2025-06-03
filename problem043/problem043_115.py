while True:
  ab = [int(x) for x in input().split()]
  a, b = ab[0], ab[1]
  if a == 0 and b == 0:
    break
  if a > b:
    a, b = b, a
  print("{0} {1}".format(a, b))
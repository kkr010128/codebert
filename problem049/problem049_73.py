while True:
  a,b = map(int, input().split())
  if a == 0 and b == 0:
    break
  if a > 0 and b > 0:
    for i in range(a):
      for j in range(b):
        print("#", end="")
      print()
    print()

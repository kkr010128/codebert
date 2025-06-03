while True:
  a, b = map(int, input().split())
  if a == b == 0:
    break

  for i in range(a):
    if i == 0 or i == a - 1:
      print('#' * b)
      continue
    print('#', '.' * (b - 2), '#', sep = '')

  print()

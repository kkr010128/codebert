while True:
  H, W = map(int, input().split())
  if H == 0 and W == 0:
    break
  print('#' * W)
  for i in range(1,H-1):
    print('#', end='')
    for j in range(1,W-1):
      print('.', end='')
    print('#')
  print('#' * W)
  print()

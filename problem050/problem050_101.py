while True:
  hw = [int(x) for x in input().split()]
  h, w = hw[0], hw[1]

  if h == 0 and w == 0:
    break
  for hh in range(h):
    for ww in range(w):
      if hh == 0 or hh == h - 1 or ww == 0 or ww == w - 1:
        print('#', end = '')
      else:
        print('.', end = '')
    print('')
  print('')
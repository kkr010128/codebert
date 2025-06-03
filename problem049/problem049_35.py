while True:
  H, W = map(int, raw_input().split())
  if H == 0 and W == 0:
    break
  for i in range(H):
    width = ""
    for j in range(W):
      width += "#"
    print width
  print ""
while True:
    (H,W) = [int(x) for x in input().split()]
    if H == W == 0:
     break

    for h in range(0, H):
     for w in range(0, W):
      print("#", end="")
      if w == W - 1:
       print()
       break

    print()